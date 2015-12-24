import Part
from FreeCAD import Base
from FreeCAD import Gui
import math


## Basic NURBS rules and terms
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

# Bottom up view:
# points, weights, as [[x,y,z],w] are the basic inputs. lists are probably not efficient, but until FreeCAD has fully integrated homogenous coordinates for all NURBS functions, this is easier for me :)
# Bezier_Cubic_curve -  pinned cubic rational B spline -  Part.BSplineCurve() in cubic bezier form
# NURBS_Cubic_6P_curve - pinned cubic rational Bspline - 6 control points, just enough to have independent endpoint curvature
# Cubic_ddu - cubic derivative with u at curve start based on first two control points (no curve required)
# Cubic_d2du2 - cubic second derivative with u at curve start based on first three control points (no curve required)
# Cubic_curvature - curvature at curve start based on the first three control points (no curve required)
# orient_a_to_b - a and b are lists of points that share one endpoint. if needed, this function reorders a so that a.end = b.start or b.end b is not modified
# quad_patch - given four curves that form a closed loop, prepare a 4*4 nurbs control mesh
# tri_quad_patch - prepare 4 x 4 control point patch from three curves. this is a degenerate pach. intersection of first and last curve is the singular point
# mid_edge_poly - given a control patch, show the internal control mesh
# BezCubic_patch - given a 4 x 4 control patch, build the bicubic bezier patch




def Bezier_Cubic_curve(poles): 
#draws a degree 3 rational bspline from first to last point,
# second and third act as tangents
# poles is a list: [[[x,y,z],w],[[x,y,z],w],[[x,y,z],w],[[x,y,z],w]]
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

def NURBS_Cubic_6P_curve(poles): 
# draws a degree 3 rational bspline from first to last point,
# second and third act as tangents
# poles is a list: [[[x,y,z],w],[[x,y,z],w],[[x,y,z],w],[[x,y,z],w],[[x,y,z],w],[[x,y,z],w]]
## nKnot = 6 + 3 +1 = 10
## Order = 3 + 1 = 4
	degree=3
	nPoles=6
	knot=[0,0,0,0,0.3333,0.6666,1,1,1,1]
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


def Cubic_ddu(pole1, pole2):   # first derivative with respect to parameter, returns value at first pole given
	P1=Base.Vector(pole1)
	P2=Base.Vector(pole2)
	Cubic_ddu = (P2 - P1)*3
	return Cubic_ddu

def Cubic_d2du2(pole1, pole2, pole3): # second derivative with respect to parameter, returns value at first pole given
	P1=Base.Vector(pole1)
	P2=Base.Vector(pole2)
	P3=Base.Vector(pole3)	
	Cubic_d2du2 = (P1- P2*2 + P3)*6
	return Cubic_d2du2

def Cubic_curvature(pole1, pole2, pole3): # curvature, returns value at first pole given
	ddu = Cubic_ddu(pole1, pole2)
	d2du2 = Cubic_d2du2(pole1, pole2, pole3)
	BezCubic_curvature = ddu.cross(d2du2).Length/ddu.Length.__pow__(3)
	return Cubic_curvature


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

	# fix edge orientation, going counterclockwise from first curve (c1)
	quad_1_2 = orient_a_to_b(poles1,poles2)
	quad_2_3 = orient_a_to_b(poles2,poles3)
	quad_3_4 = orient_a_to_b(poles3,poles4)
	quad_4_1 = orient_a_to_b(poles4,poles1)	

	# flip weights of flipped edges - maybe this should go into 'orient_a_to_b()'
	if quad_1_2[0]!=poles1[0] and quad_1_2[0]==poles1[-1]:
		weights1=weights1[::-1]
	if quad_2_3[0]!=poles2[0] and quad_2_3[0]==poles2[-1]:
		weights2=weights2[::-1]
	if quad_3_4[0]!=poles3[0] and quad_3_4[0]==poles3[-1]:
		weights3=weights3[::-1]
	if quad_4_1[0]!=poles4[0] and quad_4_1[0]==poles4[-1]:
		weights4=weights4[::-1]

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

	# calculate inner control points. this method makes continuous patches, but all corner grids make parallelograms. need to improve.
	# needs to stay planar across the patch corners!
	p_1_1 = p_0_0 + (p_0_1 - p_0_0) +  (p_1_0 - p_0_0)
	p_1_2 = p_0_3 + (p_0_2 - p_0_3) +  (p_1_3 - p_0_3)
	p_2_1 = p_3_0 + (p_3_1 - p_3_0) +  (p_2_0 - p_3_0)
	p_2_2 = p_3_3 + (p_2_3 - p_3_3) +  (p_3_2 - p_3_3)

	# set weights, assign to control points, final format is [[x,y,z],w]. The patch will be a 4x4 matrix arranged as a list of 16 of these control format.
	# original edges
	w00 = [p_0_0, weights1[0]]
	w01 = [p_0_1, weights1[1]]
	w02 = [p_0_2, weights1[2]]
	w03 = [p_0_3, weights1[3]]

	w13 = [p_1_3, weights2[1]]
	w23 = [p_2_3, weights2[2]]
	w33 = [p_3_3, weights2[3]]

	w32 = [p_3_2, weights3[2]]
	w31 = [p_3_1, weights3[1]]
	w30 = [p_3_0, weights3[0]]

	w20 = [p_2_0, weights4[2]]
	w10 = [p_1_0, weights4[1]]

	# calculate inner weights
	# multiply neighbors across the grid? this makes a good cylinder, but bad tori and spheres...lets blame the inner control points!
	w11 = [p_1_1, weights1[1]*weights4[2]]
	w12 = [p_1_2, weights1[2]*weights2[1]]
	w21 = [p_2_1, weights3[2]*weights4[1]]
	w22 = [p_2_2, weights2[2]*weights3[1]]

	quad_patch = [w00 ,w01, w02, w03,
				w10, w11, w12, w13,
				w20, w21, w22, w23,
				w30, w31, w32, w33]
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


	# fix edge orientation, going counterclockwise from first curve (c1)
	quad_1_2 = orient_a_to_b(poles1,poles2)
	quad_2_3 = orient_a_to_b(poles2,poles3)
	quad_3_1 = orient_a_to_b(poles3,poles1)

	# flip weights of flipped edges - maybe this should go into 'orient_a_to_b()'
	if quad_1_2[0]!=poles1[0] and quad_1_2[0]==poles1[-1]:
		weights1=weights1[::-1]
	if quad_2_3[0]!=poles2[0] and quad_2_3[0]==poles2[-1]:
		weights2=weights2[::-1]
	if quad_3_1[0]!=poles3[0] and quad_3_1[0]==poles3[-1]:
		weights3=weights3[::-1]


	# make sure this is a degenerate quadrangle, i.e. a triangle
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
	p_3_0 = p_0_0

	# left edge, top to bottom, degenerate. SKIP both corners
	p_2_0 = p_0_0
	p_1_0 = p_0_0

	# calculate inner control points
	tan_inner_11 = (p_3_1 - p_0_0) # direction p_0_1 to p_1_1
	tan_inner_21 = (p_0_1 - p_0_0) # direction p_3_1 to p_2_1

	# degenerate inner control point scale factor
	# delt=2.0/3.0 
	theta = tan_inner_11.getAngle(tan_inner_21)
	delt = math.sin(theta) # 1 for a right angle corner, 0 for a collapsed corner

	p_1_1 = p_0_1 +  tan_inner_11.scale(delt,delt,delt)
	p_1_2 = p_0_3 + (p_0_2 - p_0_3) +  (p_1_3 - p_0_3)	# keep standard
	p_2_1 = p_3_1 +  tan_inner_21.scale(delt,delt,delt)
	p_2_2 = p_3_3 + (p_2_3 - p_3_3) +  (p_3_2 - p_3_3)	# keep standard

	# set weights, assign to control points, final format is [[x,y,z],w]. The patch will be a 4x4 matrix arranged as a list of 16 of these control format.
	# original edges
	w00 = [p_0_0, weights1[0]]
	w01 = [p_0_1, weights1[1]]
	w02 = [p_0_2, weights1[2]]
	w03 = [p_0_3, weights1[3]]

	w13 = [p_1_3, weights2[1]]
	w23 = [p_2_3, weights2[2]]
	w33 = [p_3_3, weights2[3]]

	w32 = [p_3_2, weights3[2]]
	w31 = [p_3_1, weights3[1]]
	w30 = [p_3_0, weights3[0]]

	w20 = w00
	w10 = w00

	# calculate inner weights
	# multiply neighbors across the grid? this makes a good cylinder, but bad tori and spheres...lets blame the inner control points!
	w11 = [p_1_1, weights1[1]*weights3[2]]
	w12 = [p_1_2, weights1[2]*weights2[1]]
	w21 = [p_2_1, weights3[2]*weights1[1]]
	w22 = [p_2_2, weights2[2]*weights3[1]]



	tri_quad_patch =  [w00 ,w01, w02, w03,
				w10, w11, w12, w13,
				w20, w21, w22, w23,
				w30, w31, w32, w33]
	return tri_quad_patch


def quad66_patch(c1,c2,c3,c4): # prepare 6 x 6 control point patch from four curves
	# extract curve poles
	poles1=c1.getPoles()
	poles2=c2.getPoles()
	poles3=c3.getPoles()
	poles4=c4.getPoles()

	# fix edge orientation, going counterclockwise from first curve (c1)
	sext_1_2 = orient_a_to_b(poles1,poles2)
	sext_2_3 = orient_a_to_b(poles2,poles3)
	sext_3_4 = orient_a_to_b(poles3,poles4)
	sext_4_1 = orient_a_to_b(poles4,poles1)	

	# bottom edge, left to right
	p00 = sext_1_2[0]
	p01 = sext_1_2[1]
	p02 = sext_1_2[2]	
	p03 = sext_1_2[3]
	p04 = sext_1_2[4]
	p05 = sext_1_2[5]

	# right edge, bottom to top, SKIP starting corner
	p15 = sext_2_3[1]
	p25 = sext_2_3[2]
	p35 = sext_2_3[3]
	p45 = sext_2_3[4]
	p55 = sext_2_3[5]

	# top edge, right to left, SKIP starting corner
	p54 = sext_3_4[1]
	p53 = sext_3_4[2]
	p52 = sext_3_4[3]
	p51 = sext_3_4[4]
	p50 = sext_3_4[5]

	# left edge, top to bottom, SKIP both corners
	p40 = sext_4_1[1]
	p30 = sext_4_1[2]
	p20 = sext_4_1[3]
	p10 = sext_4_1[4]

	# calculate inner corner control points
	p11 = p00 + (p01 - p00) +  (p10 - p00) #
	p14 = p05 + (p04 - p05) +  (p15 - p05) #
	p41 = p50 + (p51 - p50) +  (p40 - p50) #
	p44 = p55 + (p45 - p55) +  (p54 - p55) #

	# calculate edge inner control points
	
	p12=p02+(p11-p01).multiply(2.0/3)+(p14-p04).multiply(1.0/3)
	p13=p03+(p11-p01).multiply(1.0/3)+(p14-p04).multiply(2.0/3)
	
	p24=p25+(p14-p15).multiply(2.0/3)+(p44-p45).multiply(1.0/3)
	p34=p35+(p14-p15).multiply(1.0/3)+(p44-p45).multiply(2.0/3)
	
	p42=p52+(p41-p51).multiply(2.0/3)+(p44-p54).multiply(1.0/3)
	p43=p53+(p41-p51).multiply(1.0/3)+(p44-p54).multiply(2.0/3)

	p21=p20+(p11-p10).multiply(2.0/3)+(p41-p40).multiply(1.0/3)
	p31=p30+(p11-p10).multiply(1.0/3)+(p41-p40).multiply(2.0/3)


	# calculate inner control points

	p22u= p12+(p21-p11).multiply(2.0/3)+(p24-p14).multiply(1.0/3)
	p23u= p13+(p21-p11).multiply(1.0/3)+(p24-p14).multiply(2.0/3)

	p32u= p42+(p31-p41).multiply(2.0/3)+(p34-p44).multiply(1.0/3)
	p33u= p43+(p31-p41).multiply(1.0/3)+(p34-p44).multiply(2.0/3)

	p22v= p21+(p12-p11).multiply(2.0/3)+(p42-p41).multiply(1.0/3)
	p32v= p31+(p12-p11).multiply(1.0/3)+(p42-p41).multiply(2.0/3)
	
	p23v= p24+(p13-p14).multiply(2.0/3)+(p43-p44).multiply(1.0/3)	
	p33v= p34+(p13-p14).multiply(1.0/3)+(p43-p44).multiply(2.0/3)

	p22=(p22u+p22v).multiply(0.5)
	p23=(p23u+p23v).multiply(0.5)
	p32=(p32u+p32v).multiply(0.5)
	p33=(p33u+p33v).multiply(0.5)


	quad66_patch = [p00, p01, p02, p03, p04, p05,
				p10, p11, p12, p13, p14, p15,
				p20, p21, p22, p23, p24, p25, 
				p30, p31, p32, p33, p34, p35,
				p40, p41, p42, p43, p44, p45,
				p50, p51, p52, p53, p54, p55]
	return quad66_patch





def mid_edge_poly(quad_patch):
	# start around the perimeter
	l_00_01 = Part.Line(quad_patch[0][0], quad_patch[1][0])
	l_01_02 = Part.Line(quad_patch[1][0], quad_patch[2][0])
	l_02_03 = Part.Line(quad_patch[2][0], quad_patch[3][0])
	l_03_13 = Part.Line(quad_patch[3][0], quad_patch[7][0])
	l_13_23 = Part.Line(quad_patch[7][0], quad_patch[11][0])
	l_23_33 = Part.Line(quad_patch[11][0], quad_patch[15][0])
	l_33_32 = Part.Line(quad_patch[15][0], quad_patch[14][0])
	l_32_31 = Part.Line(quad_patch[14][0], quad_patch[13][0])
	l_31_30 = Part.Line(quad_patch[13][0], quad_patch[12][0])

	# check for triangular patches - collapsed fourth edge
	if quad_patch[0] != quad_patch[12]: #normal case, four sided patch
		l_00_10=Part.Line(quad_patch[0][0], quad_patch[4][0])
		l_10_20=Part.Line(quad_patch[4][0], quad_patch[8][0])
		l_20_30=Part.Line(quad_patch[8][0], quad_patch[12][0])
	else: # triangle case
		l_00_10=Part.Point(quad_patch[0][0])
		l_10_20=Part.Point(quad_patch[0][0])
		l_20_30=Part.Point(quad_patch[0][0])

	# Internal controls

	# check for triangular patches with collapsed fourth edge AND collpapsed fourth corner.
	if quad_patch[1] != quad_patch[13]: #normal case, four sided patch, or unique tangents on triangle patch
		l_01_11=Part.Line(quad_patch[1][0], quad_patch[5][0])
		l_31_21=Part.Line(quad_patch[13][0], quad_patch[9][0])
	else: #triangle case, collapsed tangents
		l_01_11=Part.Point(quad_patch[1][0])
		l_31_21=Part.Point(quad_patch[13][0])


	## l_01_11 above
	l_10_11=Part.Line(quad_patch[4][0], quad_patch[5][0])
	l_02_12=Part.Line(quad_patch[2][0], quad_patch[6][0])
	l_13_12=Part.Line(quad_patch[7][0], quad_patch[6][0])
	l_23_22=Part.Line(quad_patch[11][0], quad_patch[10][0])
	l_32_22=Part.Line(quad_patch[14][0], quad_patch[10][0])
	## l_31_21
	l_20_21=Part.Line(quad_patch[8][0], quad_patch[9][0])

	l_11_12=Part.Line(quad_patch[5][0], quad_patch[6][0])
	l_12_22=Part.Line(quad_patch[6][0], quad_patch[10][0])
	l_21_22=Part.Line(quad_patch[9][0], quad_patch[10][0])
	l_11_21=Part.Line(quad_patch[5][0], quad_patch[9][0])

	mid_edge_poly=[l_00_01, l_01_02, l_02_03,
				l_03_13, l_13_23, l_23_33,
				l_33_32, l_32_31, l_31_30,
				l_20_30, l_10_20, l_00_10,
				l_01_11, l_10_11, l_02_12, l_13_12, 
				l_23_22, l_32_22, l_31_21, l_20_21,
				l_11_12, l_12_22, l_21_22, l_11_21]
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
			nurbs_quad_16.setPole(ii+1,jj+1,quad_patch[i][0], quad_patch[i][1]);
			i=i+1;
	return nurbs_quad_16

def BezCubic66_patch(quad66_patch):
	# len(knot_u) := nNodes_u + degree_u + 1
	# len(knot_v) := nNodes_v + degree_v + 1
	degree_u=3
	degree_v=3
	nNodes_u=6
	nNodes_v=6
	knot_u=[0,0,0,0,0.3333,0.6666,1,1,1,1]
	knot_v=[0,0,0,0,0.3333,0.6666,1,1,1,1]
	nurbs_quad_36=Part.BSplineSurface()
	nurbs_quad_36.increaseDegree(degree_u,degree_v)
	id=1
	for i in range(0,len(knot_u)):    #-1):
		nurbs_quad_36.insertUKnot(knot_u[i],id,0.0000001)
	id=1
	for i in range(0,len(knot_v)):    #-1):
		nurbs_quad_36.insertVKnot(knot_v[i],id,0.0000001)
	i=0
	for jj in range(0,nNodes_v):
		for ii in range(0,nNodes_u):
			nurbs_quad_36.setPole(ii+1,jj+1,quad66_patch[i],1);
			i=i+1;
	return nurbs_quad_36


def test_isect(curve, surf, u):		# provides information about a curve point at parameter u as a surface intersection candidate.						
	test_point = curve.value(u)											# point on curve
	test_proj_param = surf.parameter(test_point)							# parameter of projection of curve point onto surface
	test_proj = surf.value(test_proj_param[0],test_proj_param[1])			# projection of curve point onto surface
	test_proj_tan = surf.tangent(test_proj_param[0],test_proj_param[1])		# tangents of surface at projection
	test_proj_n = test_proj_tan[0].cross(test_proj_tan[1])					# get surface normal from tangents
	test_error = test_proj - test_point									# error vector
	error = test_error.Length											# distance between curve point and its surface projection
	testdot = test_error.dot(test_proj_n)									# compare orientation of point and surface
	test_center = [test_point, test_error, error, testdot,test_proj_param]					# prepare list of results
	return test_center

def curve_surf_isect(curve, surf):
	tol= 0.00000001
	# setup the parameter search span 
	test_span = [curve.FirstParameter, curve.LastParameter]
	# determine whether the curve grows from inside or outside the surface. this will govern how to split the search span
	test_u_direction = test_isect(curve, surf, curve.FirstParameter) 	# project curve startpoint to determine if it is 'inside' or 'outside' the surface.
	if (test_u_direction[3] < 0):								# compare projection path to surface normal: dot product negative
		direction = 1											# > curve grows 'into' the surface
	elif (test_u_direction[3] > 0):								# compare projection path to surface normal: dot product positive
		direction = -1										# > curve grows 'out of' the surface
	# initialize error
	error = 1.0	
	# set up binary search loop
	loop_count = 0
	while (error > tol  and loop_count < 100):
		test_u = (test_span[1] + test_span[0]) / 2	# pick u in the center of the search span
		test = test_isect(curve, surf, test_u)			# project curve(u) onto surface
		error = test[2]							# set current intersection error
		if ((test[3]*direction) < 0):					# is the projection still coming from outside the surface?
			test_span = [test_u, test_span[1]]		# > use second half of current span for the next search
		if ((test[3]*direction) > 0):					# is the projection coming from inside the surface?
			test_span = [test_span[0], test_u]		# > use first half of current span for the next search
		loop_count=loop_count + 1
	print 'step ', loop_count, '  u ', test_u, '  error ', test[2]
	if error > tol:
		print 'no intersection found within ', tol
		curve_surf_isect = 'NONE'
	else:
		curve_surf_isect = [test[0], test_u, test[4]]
	return curve_surf_isect



