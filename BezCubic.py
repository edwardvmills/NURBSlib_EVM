import Part
from FreeCAD import Base
from FreeCAD import Gui
import math



## Order >= 2
## Order:  2 = line, 3 = quadratic, 4 = cubic ...
## Degree = Order - 1
## Order = Degree +1
## nPoles >= Order
## nPoles >= Degree + 1
## nKnots = nPoles + Order
## nKnots = nPoles + degree + 1
## knot vector strictly ascending
## Pinned knot vector: k=Order, first k knots are equal, last k knots are equal


def BezCubic_curve(poles): 
#draws a degree 3 bspline from first to last point,
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
	for i in range(0,len(knot)-1):
	        if knot[i+1] > knot[i]:
	                bs.insertKnot(knot[i],id,0.0000001)
	i=0
	for ii in range(0,nPoles):
		bs.setPole(ii+1,poles[i][0],poles[i][1])
		i=i+1;
	return bs

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


def quad_patch(c1,c2,c3,c4):
	# extract curve poles
	poles1=c1.getPoles()
	poles2=c2.getPoles()
	poles3=c3.getPoles()
	poles4=c4.getPoles()

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
	p_1_1 =p_0_0 + (p_0_1 - p_0_0) +  (p_1_0 - p_0_0)
	p_1_2 =p_0_3 + (p_0_2 - p_0_3) +  (p_1_3 - p_0_3)
	p_2_1 =p_3_0 + (p_3_1 - p_3_0) +  (p_2_0 - p_3_0)
	p_2_2 = p_3_3 +(p_2_3 - p_3_3) +  (p_3_2 - p_3_3)

	quad_patch = [p_0_0,p_0_1,p_0_2,p_0_3,
				p_1_0,p_1_1,p_1_2,p_1_3,
				p_2_0,p_2_1,p_2_2,p_2_3,
				p_3_0,p_3_1,p_3_2,p_3_3]
	return quad_patch

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
	for i in range(0,len(knot_u)-1):
		if knot_u[i+1] > knot_u[i]:
			nurbs_quad_16.insertUKnot(knot_u[i],id,0.0000001)
	id=1
	for i in range(0,len(knot_v)-1):
		if knot_v[i+1] > knot_v[i]:
			nurbs_quad_16.insertVKnot(knot_v[i],id,0.0000001)
	i=0
	for jj in range(0,nNodes_v):
		for ii in range(0,nNodes_u):
			nurbs_quad_16.setPole(ii+1,jj+1,quad_patch[i],1);
			i=i+1;
	return nurbs_quad_16




