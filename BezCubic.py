import Part
from FreeCAD import Base
from FreeCAD import Gui
import math


# Bottom up view:
# points, weights
# BezCubic_curve -  pinned cubic rational B spline -  Part.BSplineCurve() in cubic bezier form
# BezCubic_ddu - derivative with u at curve start based on first two control points (no curve rquired)
# BezCubic_d2du2 - second derivative with u at curve start based on first three control points (no curve rquired)
# BezCubic_curvature - curvature at curve start based on the first three control points (no curve rquired)
# orient_a_to_b - a and b are lists of points share one endpoint. if needed, this function reorders a or b so that a.end = b.start
# quad_patch - given four curves that form a closed loop, prepare a 4*4 nurbs control mesh
# tri_quad_patch - prepare 4 x 4 control point patch from three curves. this is a degenerate pach. intersection of first and last curve is the singular point
# mid_edge_poly - given a control patch, show the internal control mesh
# BezCubic_patch - given a 4 x 4 control patch, build the bicubic bezier patch

## Order >= 2
## Order:  2 = line, 3 = quadratic, 4 = cubic ...
## Degree = Order - 1
## Order = Degree + 1
## nPoles >= Order
## nPoles >= Degree + 1
## nKnots = nPoles + Order
## nKnots = nPoles + degree + 1
## knot vector strictly ascending
## Pinned knot vector: k=Order, first k knots are equal, last k knots are equal


def BezCubic_curve(poles): 
#draws a degree 3 rational bspline from first to last point,
# second and third act as tangents
# quartet is a list: [[[x,y,z],w],[[x,y,z],w],[[x,y,z],w],[[x,y,z],w]]
## nKnot = 4 + 3 +1 = 8
## Order = 3 + 1 = 4
	degree=3
	nPoles=4
	knot=[0,0,0,0,1,1,1,1]
	bs=Part.BSplineCurve()
	bs.increaseDegree(degree)
	id=1
	for i in range(0,len(knot)):    #-1):
		bs.insertKnot(knot[i],id,0.0000001)
	i=0
	for ii in range(0,nPoles):
		bs.setPole(ii+1,poles[i][0],poles[i][1])
		i=i+1;
	return bs

def BezCubic_ddu(pole1, pole2):   # first derivative with respect to parameter, returns value at first pole given
	P1=Base.Vector(pole1)
	P2=Base.Vector(pole2)
	BezCubic_ddu = (P2 - P1)*3
	return BezCubic_ddu

def BezCubic_d2du2(pole1, pole2, pole3): # second derivative with respect to parameter, returns value at first pole given
	P1=Base.Vector(pole1)
	P2=Base.Vector(pole2)
	P3=Base.Vector(pole3)	
	BezCubic_d2du2 = (P1- P2*2 + P3)*6
	return BezCubic_d2du2

def BezCubic_curvature(pole1, pole2, pole3): # curvature, returns value at first pole given
	ddu = BezCubic_ddu(pole1, pole2)
	d2du2 = BezCubic_d2du2(pole1, pole2, pole3)
	BezCubic_curvature = ddu.cross(d2du2).Length/ddu.Length.__pow__(3)
	return BezCubic_curvature


def orient_a_to_b(polesa,polesb):

	if (polesa[-1]==polesb[0]):  # last point of first curve is first point of second curve
		# curve 1 is oriented properly
		return polesa
	elif (polesa[-1]==polesb[-1]):  # last point of first curve is last point of second curve
		# curve 1 is oriented properly
		return polesa
	elif (polesa[0]==polesb[0]):  # first point of first curve is first point of second curve
		# curve 1 is reversed
		return polesa[::-1]
	elif (polesa[0]==polesb[-1]):  # first point of first curve is last point of second curve
		# curve 1 is reversed
		return polesa[::-1]
	else:
		print 'curves do not share endpoints'
		return 0


def quad_patch(c1,c2,c3,c4): # prepare 4 x 4 control point patch from four curves
	# extract curve poles
	poles1=c1.getPoles()
	poles2=c2.getPoles()
	poles3=c3.getPoles()
	poles4=c4.getPoles()

	weights1=c1.getWeights()
	weights2=c2.getWeights()
	weights3=c3.getWeights()
	weights4=c4.getWeights()

	ctrls1=[poles1,weights1]
	ctrls2=[poles2,weights2]
	ctrls3=[poles3,weights3]
	ctrls4=[poles4,weights4]

	# fix edge orientation, going counterclockwise from first curve (c1)
	quad_1_2 = orient_a_to_b(poles1,poles2)
	quad_2_3 = orient_a_to_b(poles2,poles3)
	quad_3_4 = orient_a_to_b(poles3,poles4)
	quad_4_1 = orient_a_to_b(poles4,poles1)	

	# bottom edge, left to right
	p_0_0 = quad_1_2[0]
	p_0_1 = quad_1_2[1]
	p_0_2 = quad_1_2[2]	
	p_0_3 = quad_1_2[3]

	# right edge, bottom to top, SKIP starting corner
	p_1_3 = quad_2_3[1]
	p_2_3 = quad_2_3[2]
	p_3_3 = quad_2_3[3]

	# top edge, right to left, SKIP starting corner
	p_3_2 = quad_3_4[1]
	p_3_1 = quad_3_4[2]
	p_3_0 = quad_3_4[3]

	# left edge, top to bottom, SKIP both corners
	p_2_0 = quad_4_1[1]
	p_1_0 = quad_4_1[2]

	# calculate inner control points
	p_1_1 = p_0_0 + (p_0_1 - p_0_0) +  (p_1_0 - p_0_0)
	p_1_2 = p_0_3 + (p_0_2 - p_0_3) +  (p_1_3 - p_0_3)
	p_2_1 = p_3_0 + (p_3_1 - p_3_0) +  (p_2_0 - p_3_0)
	p_2_2 = p_3_3 + (p_2_3 - p_3_3) +  (p_3_2 - p_3_3)

	quad_patch = [p_0_0,p_0_1,p_0_2,p_0_3,
				p_1_0,p_1_1,p_1_2,p_1_3,
				p_2_0,p_2_1,p_2_2,p_2_3,
				p_3_0,p_3_1,p_3_2,p_3_3]
	return quad_patch

def tri_quad_patch(c1,c2,c3): 
# prepare 4 x 4 control point patch from three curves. 
# this is a degenerate pach. 
# intersection of first and last curve is the singular point
#
# extract curve poles
	poles1=c1.getPoles()
	poles2=c2.getPoles()
	poles3=c3.getPoles()

	weights1=c1.getWeights()
	weights2=c2.getWeights()
	weights3=c3.getWeights()

	ctrls1=[poles1,weights1]
	ctrls2=[poles2,weights2]
	ctrls3=[poles3,weights3]

	# fix edge orientation, going counterclockwise from first curve (c1)
	quad_1_2 = orient_a_to_b(poles1,poles2)
	quad_2_3 = orient_a_to_b(poles2,poles3)
	quad_3_1 = orient_a_to_b(poles3,poles1)

	# make sure this is a degenrate quadrangle, i.e. a triangle
	if (quad_3_1[3] != quad_1_2[0]):
		print 'edge loop does not form a triangle'
		return 0

	# bottom edge, left to right
	p_0_0 = quad_1_2[0]
	p_0_1 = quad_1_2[1]
	p_0_2 = quad_1_2[2]	
	p_0_3 = quad_1_2[3]

	# right edge, bottom to top, SKIP starting corner
	p_1_3 = quad_2_3[1]
	p_2_3 = quad_2_3[2]
	p_3_3 = quad_2_3[3]

	# top edge, right to left, SKIP starting corner
	p_3_2 = quad_3_1[1]
	p_3_1 = quad_3_1[2]
	p_3_0 = quad_3_1[3] # this is redundant already

	# left edge, top to bottom, degenerate
	p_2_0 = p_3_0
	p_1_0 = p_0_0

	# calculate inner control points
	s=2.0/3.0 # degenerate inner control point scale factor

	tan_inner_11 = (p_3_1 - p_3_0).scale(s,s,s)
	tan_inner_21 = (p_0_1 - p_0_0).scale(s,s,s)

	p_1_1 = p_0_1 +  tan_inner_11
	p_1_2 = p_0_3 + (p_0_2 - p_0_3) +  (p_1_3 - p_0_3)	# keep standard
	p_2_1 = p_3_1 +  tan_inner_21
	p_2_2 = p_3_3 + (p_2_3 - p_3_3) +  (p_3_2 - p_3_3)	# keep standard

	tri_quad_patch = [p_0_0,p_0_1,p_0_2,p_0_3,
				p_1_0,p_1_1,p_1_2,p_1_3,
				p_2_0,p_2_1,p_2_2,p_2_3,
				p_3_0,p_3_1,p_3_2,p_3_3]
	return tri_quad_patch

def mid_edge_poly(quad_patch):
	l_01_11=Part.Line(quad_patch[1], quad_patch[5])
	l_10_11=Part.Line(quad_patch[4], quad_patch[5])
	l_02_12=Part.Line(quad_patch[2], quad_patch[6])
	l_13_12=Part.Line(quad_patch[7], quad_patch[6])
	l_23_22=Part.Line(quad_patch[11], quad_patch[10])
	l_32_22=Part.Line(quad_patch[14], quad_patch[10])
	l_31_21=Part.Line(quad_patch[13], quad_patch[9])
	l_20_21=Part.Line(quad_patch[8], quad_patch[9])
	mid_edge_poly=[l_01_11, l_10_11, l_02_12, l_13_12, 
				l_23_22, l_32_22, l_31_21, l_20_21]
	return mid_edge_poly


def BezBiCubic_surf(quad_patch):
	surf=Part.BezierSurface()
	surf.increase(3,3)
	n=0
	for u in range(1,5):
		for v in range(1,5):
			surf.setPole(v,u,quad_patch[n])
			n=n+1
	return surf

def BezCubic_patch(quad_patch):
	# len(knot_u) := nNodes_u + degree_u + 1
	# len(knot_v) := nNodes_v + degree_v + 1
	degree_u=3
	degree_v=3
	nNodes_u=4
	nNodes_v=4
	knot_u=[0,0,0,0,1,1,1,1]
	knot_v=[0,0,0,0,1,1,1,1]
	nurbs_quad_16=Part.BSplineSurface()
	nurbs_quad_16.increaseDegree(degree_u,degree_v)
	id=1
	for i in range(0,len(knot_u)):    #-1):
		nurbs_quad_16.insertUKnot(knot_u[i],id,0.0000001)
	id=1
	for i in range(0,len(knot_v)):    #-1):
		nurbs_quad_16.insertVKnot(knot_v[i],id,0.0000001)
	i=0
	for jj in range(0,nNodes_v):
		for ii in range(0,nNodes_u):
			nurbs_quad_16.setPole(ii+1,jj+1,quad_patch[i],1);
			i=i+1;
	return nurbs_quad_16




