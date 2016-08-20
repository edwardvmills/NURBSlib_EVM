#    NURBSLib_EVM
#    (c) Edward Mills 2016
#    edwardvmills@gmail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
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

####
#### SECTION 1: DIRECT FUNCTIONS - NO PARAMETRIC LINKING BETWEEN OBJECT - LEGACY
#### SECTION 2: PYTHON FEATURE CLASSES - PARAMETRIC LINKING BETWEEN OBJECT - IN PROGRESS (start around line 1150)
####


### SECTION 1: DIRECT FUNCTIONS - NO PARAMETRIC LINKING BETWEEN OBJECTS - LEGACY - will be kept in place until it is thouroughly picked over.
# Bottom up view:
# poles = 3D points with weights, as [[x,y,z],w], or [x,y,z] (these are leftovers waiting to receive weights). 
## These are the basic input data for all that follows. They are obtained from the FreeCAD functions .getPoles() and .getWeights()
## NOTE: Poles in FreeCAD, such as returned by .getPoles(), refer only to xyz coordinates of a control point, THROUGHOUT the following functions, pole means [[x,y,z],w]
## lists are probably not efficient, but until FreeCAD has fully integrated homogenous coordinates for all NURBS functions, this is easier for me :)
## right now, the computation of my scripts is ridiculously fast compared to the time taken to generate the surfaces using the FreeCAD Part.BSplineSurface() function

# Bezier_Cubic_curve([pole X 4]) -  pinned cubic rational B spline -  Part.BSplineCurve() in cubic bezier form

# NURBS_Cubic_6P_curve([pole X 6]) - pinned cubic rational Bspline - 6 control points, just enough to have independent endpoint curvature

# Cubic_Bezier_ddu(poles1, pole2) - cubic derivative at curve start (pole1) based on first two poles (no curve required). Weights not included yet

# Cubic_6P_ddu(poles1, pole2) - cubic derivative at curve start (pole1) based on first two poles (no curve required). Weights not included yet

# Cubic_Bezier_d2du2(poles1, pole2, pole3) - cubic second derivative at curve start (pole1) based on first three poles (no curve required). Weights not included yet

# Cubic_6P_d2du2(poles1, pole2, pole3) - cubic second derivative at curve start (pole1) based on first three poles (no curve required). Weights not included yet

# Cubic_Bezier_curvature(poles1, pole2, pole3) - curvature at curve start (pole1) based on the first three poles (no curve required). Weights not included yet

# Cubic_6P_curvature(poles1, pole2, pole3) - curvature at curve start (pole1) based on the first three poles (no curve required). Weights not included yet

# orient_a_to_b(polesa,polesb) - polesa and polesb are lists of poles that share one endpoint. if needed, this function reorders a so that a.end = b.start or b.end b is never modified

# grid_44_quad(c1,c2,c3,c4) - given four curves of 4 poles each that form a closed loop, prepare a 4*4 nurbs control grid

# grid_44_tri(c2,c2,c3) - given three curves of 4 poles each that form a closed loop, prepare 4 x 4 control grid. 
##this is a singular/degenerate pach. intersection of first and last curve is the singular point/edge

# grid_44_tri_alt(c2,c2,c3) - given three curves of 4 poles each that form a closed loop, prepare 4 x 4 control grid. 
##this is a singular/degenerate pach. intersection of first and last curve is the singular point/edge

# grid_66_quad(c1,c2,c3,c4) - given four curves of 6 poles each that form a closed loop, prepare a 6*6 nurbs control grid. Curve weights not assimilated yet

# grid_64_quad(c1,c2,c3,c4) - c1 and c3 are 6P curves, c2 and c4 are Bezier curves. Prepares 6*4 NURBS control grid

# poly_grid_44(grid_44) - given a 4 X 4 control patch, show the internal control mesh

# Bezier_Bicubic_surf(grid_44) - given a 4 x 4 control patch, build the bicubic bezier surface from a Part.BSplineSurface() !NOT! a Part.BezierSurface()

# NURBS_Cubic_66_surf(grid_66) - given a 6 x 6 control patch, build the bicubic bezier surface from a Part.BSplineSurface().

# isect_test(curve, surf, u)

# isect_curve_surf(curve, surf)

import Part
import FreeCAD
from FreeCAD import Base
from FreeCAD import Gui
import math

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


def Cubic_Bezier_ddu(pole1, pole2):   # first derivative with respect to parameter, returns value at first pole given. weights not inlcuded!
	P1=Base.Vector(pole1)
	P2=Base.Vector(pole2)
	Cubic_Bezier_ddu = (P2 - P1)*3
	return Cubic_Bezier_ddu

def Cubic_6P_ddu(pole1, pole2):   # first derivative with respect to parameter, returns value at first pole given. weights not inlcuded!
	P1=Base.Vector(pole1)
	P2=Base.Vector(pole2)
	Cubic_6P_ddu = (P2 - P1)*9
	return Cubic_6P_ddu

def Cubic_Bezier_d2du2(pole1, pole2, pole3): # second derivative with respect to parameter, returns value at first pole given. weights not inlcuded!
	P1=Base.Vector(pole1)
	P2=Base.Vector(pole2)
	P3=Base.Vector(pole3)	
	Cubic_Bezier_d2du2 = (P1- P2*2 + P3)*6
	return Cubic_Bezier_d2du2

def Cubic_6P_d2du2(pole1, pole2, pole3): # second derivative with respect to parameter, returns value at first pole given. weights not inlcuded!
	P1=Base.Vector(pole1)
	P2=Base.Vector(pole2)
	P3=Base.Vector(pole3)	
	Cubic_6P_d2du2 = (P1*2- P2*3 + P3)*27
	return Cubic_6P_d2du2

def Cubic_Bezier_curvature(pole1, pole2, pole3): # curvature, returns value at first pole given. weights not inlcuded!
	ddu = Cubic_Bezier_ddu(pole1, pole2)
	d2du2 = Cubic_Bezier_d2du2(pole1, pole2, pole3)
	Cubic_Bezier_curvature = ddu.cross(d2du2).Length/ddu.Length.__pow__(3)
	return Cubic_Bezier_curvature

def Cubic_6P_curvature(pole1, pole2, pole3): # curvature, returns value at first pole given. weights not inlcuded!
	ddu = Cubic_6P_ddu(pole1, pole2)
	d2du2 = Cubic_6P_d2du2(pole1, pole2, pole3)
	Cubic_6P_curvature = ddu.cross(d2du2).Length/ddu.Length.__pow__(3)
	return Cubic_6P_curvature

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


def grid_44_quad(c1,c2,c3,c4): # prepare 4 x 4 control point patch from four curves
	# extract curve poles
	poles1=c1.getPoles()
	poles2=c2.getPoles()
	poles3=c3.getPoles()
	poles4=c4.getPoles()

	weights1=c1.getWeights()
	weights2=c2.getWeights()
	weights3=c3.getWeights()
	weights4=c4.getWeights()

	# fix edge orientations, going counterclockwise from first curve (c1)
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

	grid_44_quad = [w00 ,w01, w02, w03,
				w10, w11, w12, w13,
				w20, w21, w22, w23,
				w30, w31, w32, w33]
	return grid_44_quad

def grid_44_tri(c1,c2,c3): 
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



	grid_44_tri =  [w00 ,w01, w02, w03,
				w10, w11, w12, w13,
				w20, w21, w22, w23,
				w30, w31, w32, w33]
	return grid_44_tri

def grid_44_tri_alt(c1,c2,c3): 
# prepare 4 x 4 control point patch from three curves. 
# this is a degenerate pach. 
# intersection of first and last curve is the singular point
# new strategy: let the inner control points at the degenerate corner coincide (p11 and p21), 
# cancel effect of 'doubling up' the control point by setting a reduced weight on
# the inner control points of the degenerate edge (p10 and p20).



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

	p_1_1 = p_0_1 +  (p_3_1 - p_0_0)   					# degenerate
	p_1_2 = p_0_3 + (p_0_2 - p_0_3) +  (p_1_3 - p_0_3)	# keep standard
	p_2_1 = p_3_1 + (p_0_1 - p_0_0)						# degenerate, identical to p_1_1, let them double up!
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

	w20 = [p_0_0, 0.5]	# correction for degenerate corner
	w10 = [p_0_0, 0.5]	# correction for degenerate corner

	# calculate inner weights
	# multiply neighbors across the grid? this makes a good cylinder, but bad tori and spheres...lets blame the inner control points!
	w11 = [p_1_1, weights1[1]*0.5]
	w12 = [p_1_2, weights1[2]*weights2[1]]
	w21 = [p_2_1, weights3[2]*0.5]
	w22 = [p_2_2, weights2[2]*weights3[1]]



	grid_44_tri_alt =  [w00 ,w01, w02, w03,
				w10, w11, w12, w13,
				w20, w21, w22, w23,
				w30, w31, w32, w33]
	return grid_44_tri_alt

def grid_66_quad_01(c1,c2,c3,c4): # prepare 6 x 6 control point patch from four curves
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

	# calculate edge inner control points. this blending gives preety good internal fairness, but curvature isn't readily controlled at the edges
	
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


	grid_66_quad = [p00, p01, p02, p03, p04, p05,
				p10, p11, p12, p13, p14, p15,
				p20, p21, p22, p23, p24, p25, 
				p30, p31, p32, p33, p34, p35,
				p40, p41, p42, p43, p44, p45,
				p50, p51, p52, p53, p54, p55]
	return grid_66_quad


def grid_66_quad(c1,c2,c3,c4): # prepare 6 x 6 control point patch from four curves.
	# all inner poles will now be tied to one corner of the patch. Trying to improve curvature matching along seams.

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
	p11 = p01 +  (p10 - p00) #
	p14 = p04 +  (p15 - p05) #
	p41 = p51 +  (p40 - p50) #
	p44 = p45 +  (p54 - p55) #

	# calculate edge inner control points
	
	p12 = p02 + (p10 - p00)
	p13 = p03 + (p15 - p05)
	
	p24 = p25 + (p04 - p05)
	p34 = p35 + (p54 - p55)
	
	p42 = p52 + (p40 - p50)
	p43 = p53 + (p45 - p55)

	p21 = p20 + (p01 - p00)
	p31 = p30 + (p51 - p50)


	# calculate inner control points

	p22 = p12 + (p20 - p10)
	p23 = p13 + (p25 - p15)

	p32 = p42 + (p30 - p40)
	p33 = p43 + (p35 - p45)

	grid_66_quad = [p00, p01, p02, p03, p04, p05,
				p10, p11, p12, p13, p14, p15,
				p20, p21, p22, p23, p24, p25, 
				p30, p31, p32, p33, p34, p35,
				p40, p41, p42, p43, p44, p45,
				p50, p51, p52, p53, p54, p55]
	return grid_66_quad

def grid_64_quad(c1,c2,c3,c4): # prepare 6 x 4 control point patch from four curves.
	# all inner poles will now be tied to one corner of the patch.

	# extract curve poles
	poles1=c1.getPoles() # a 6P cubic curve
	poles2=c2.getPoles() # a bezier cubic curve
	poles3=c3.getPoles() # a 6P cubic curve
	poles4=c4.getPoles() # a bezier cubic curve

	# fix edge orientation, going counterclockwise from first curve (c1)
	sext_1_2 = orient_a_to_b(poles1,poles2)
	quad_2_3 = orient_a_to_b(poles2,poles3)
	sext_3_4 = orient_a_to_b(poles3,poles4)
	quad_4_1 = orient_a_to_b(poles4,poles1)	

	# bottom edge, left to right
	p00 = sext_1_2[0]
	p01 = sext_1_2[1]
	p02 = sext_1_2[2]	
	p03 = sext_1_2[3]
	p04 = sext_1_2[4]
	p05 = sext_1_2[5]

	# right edge, bottom to top, SKIP starting corner
	p15 = quad_2_3[1]
	p25 = quad_2_3[2]
	p35 = quad_2_3[3]

	# top edge, right to left, SKIP starting corner
	p34 = sext_3_4[1]
	p33 = sext_3_4[2]
	p32 = sext_3_4[3]
	p31 = sext_3_4[4]
	p30 = sext_3_4[5]

	# left edge, top to bottom, SKIP both corners
	p20 = quad_4_1[1]
	p10 = quad_4_1[2]

	# calculate inner corner control points
	p11 = p01 +  (p10 - p00) #
	p14 = p04 +  (p15 - p05) #
	p21 = p31 +  (p20 - p30) #
	p24 = p34 +  (p25 - p35) #

	# calculate edge inner control points
	
	p12 = p02 + (p10 - p00)
	p13 = p03 + (p15 - p05)

	p22 = p32 + (p20 - p30)
	p23 = p33 + (p25 - p35)


	grid_64_quad = [p00, p01, p02, p03, p04, p05,
				p10, p11, p12, p13, p14, p15,
				p20, p21, p22, p23, p24, p25, 
				p30, p31, p32, p33, p34, p35]
	return grid_64_quad

def grid_64_tri(c1,c2,c3): # prepare 6 x 4 control point triangular patch from three curves.
	#corner of first and last curve is the degenerate corner.
	# all inner poles tied to one corner of the patch.

	# extract curve poles
	poles1=c1.getPoles() # a bezier cubic curve
	poles2=c2.getPoles() # a 6P cubic curve
	poles3=c3.getPoles() # a bezier cubic curve

	weights1=c1.getWeights()
	weights2=c2.getWeights()
	weights3=c3.getWeights()

	# fix edge orientation, going counterclockwise from first curve (c1)
	quad_1_2 = orient_a_to_b(poles1,poles2)
	sext_2_3 = orient_a_to_b(poles2,poles3)
	quad_3_1 = orient_a_to_b(poles3,poles1)


	# flip weights of flipped edges - maybe this should go into 'orient_a_to_b()'
	if quad_1_2[0]!=poles1[0] and quad_1_2[0]==poles1[-1]:
		weights1=weights1[::-1]
	if sext_2_3[0]!=poles2[0] and sext_2_3[0]==poles2[-1]:
		weights2=weights2[::-1]
	if quad_3_1[0]!=poles3[0] and quad_3_1[0]==poles3[-1]:
		weights3=weights3[::-1]

	# the curves are received as bezier>6P>bezier, but the grid is built as 6P>bezier/degen6P/bezier
	# so sext_2_3 is the bottom row, quad_3_1 is the right column, quad_1_2 is the left column

	# bottom edge, left to right
	p00 = sext_2_3[0]
	p01 = sext_2_3[1]
	p02 = sext_2_3[2]	
	p03 = sext_2_3[3]
	p04 = sext_2_3[4]
	p05 = sext_2_3[5]

	# right edge, bottom to top, SKIP starting corner
	p15 = quad_3_1[1]
	p25 = quad_3_1[2]
	p35 = quad_3_1[3]

	# top edge, degenerate
	p34 = p35
	p33 = p35
	p32 = p35
	p31 = p35
	p30 = p35

	# left edge, top to bottom, SKIP both corners
	p20 = quad_1_2[1]
	p10 = quad_1_2[2]

	# calculate inner corner control points
	p11 = p01 +  (p10 - p00) 
	p14 = p04 +  (p15 - p05) 
	p21 = p20 +  (p25 - p35) 
	p24 = p21 

	# calculate inner control points
	
	p12 = p11
	p13 = p14

	p22 = p21
	p23 = p21

	# set weights, assign to control points, final format is [[x,y,z],w]. The patch will be a 6x4 matrix arranged as a list of 24 of these control format.

	# patch edges
	w00 = [p00, weights2[0]] # bottom edge
	w01 = [p01, weights2[1]]
	w02 = [p02, weights2[2]]
	w03 = [p03, weights2[3]]
	w04 = [p04, weights2[4]]
	w05 = [p05, weights2[5]]

	w15 = [p15, weights3[1]] # right edge
	w25 = [p25, weights3[2]]
	w35 = [p35, weights3[3]] #this is the start of the collapsed edge

	w34 = [p34, 1.0] # collapsed edge
	w33 = [p33, 1.0]
	w32 = [p32, 1.0]
	w31 = [p31, 1.0]
	w30 = [p30, weights1[0]]

	w20 = [p20, weights1[1]]	# left edge
	w10 = [p10, weights1[2]]	

	# calculate inner weights

	w11 = [p11, w01[1]*w10[1]*0.5] # combines weight at 01 and 10. multiply by 0.5 because 11 repeats as 12
	w12 = [p12, weights2[2]*w11[1]] # combines weight at 02 and 11. this brings the 0.5 factor over from 11

	w14 = [p14, w04[1]*w15[1]*0.5] # combines weight at 04 and 15. multiply by 0.5 because 14 repeats as 13
	w13 = [p13, weights2[3]*w14[1]] # combines weight at 03 and 14. this brings the 0.5 factor over from 14


	w21 = [p21, w20[1]*w25[1]*0.25] # combines weight at 20 and 25. multiply by 0.25 because 21 repeats as 22, 23, and 24
	w22 = [p22, w21[1]]
	w23 = [p23, w21[1]]
	w24 = [p24, w21[1]]

	grid_64_tri = [w00, w01, w02, w03, w04, w05,
				w10, w11, w12, w13, w14, w15,
				w20, w21, w22, w23, w24, w25, 
				w30, w31, w32, w33, w34, w35]
	return grid_64_tri

def poly_grid_44(grid_44):
	# start around the perimeter
	l_00_01 = Part.Line(grid_44[0][0], grid_44[1][0])
	l_01_02 = Part.Line(grid_44[1][0], grid_44[2][0])
	l_02_03 = Part.Line(grid_44[2][0], grid_44[3][0])
	l_03_13 = Part.Line(grid_44[3][0], grid_44[7][0])
	l_13_23 = Part.Line(grid_44[7][0], grid_44[11][0])
	l_23_33 = Part.Line(grid_44[11][0], grid_44[15][0])
	l_33_32 = Part.Line(grid_44[15][0], grid_44[14][0])
	l_32_31 = Part.Line(grid_44[14][0], grid_44[13][0])
	l_31_30 = Part.Line(grid_44[13][0], grid_44[12][0])

	# check for triangular patches - collapsed fourth edge
	if grid_44[0] != grid_44[12]: #normal case, four sided patch
		l_00_10=Part.Line(grid_44[0][0], grid_44[4][0])
		l_10_20=Part.Line(grid_44[4][0], grid_44[8][0])
		l_20_30=Part.Line(grid_44[8][0], grid_44[12][0])
	else: # triangle case
		l_00_10=Part.Point(grid_44[0][0])
		l_10_20=Part.Point(grid_44[0][0])
		l_20_30=Part.Point(grid_44[0][0])

	# Internal controls

	# check for triangular patches with collapsed fourth edge AND collpapsed fourth corner.
	if grid_44[1] != grid_44[13]: #normal case, four sided patch, or unique tangents on triangle patch
		l_01_11=Part.Line(grid_44[1][0], grid_44[5][0])
		l_31_21=Part.Line(grid_44[13][0], grid_44[9][0])
	else: #triangle case, collapsed tangents
		l_01_11=Part.Point(grid_44[1][0])
		l_31_21=Part.Point(grid_44[13][0])


	## l_01_11 above
	l_10_11=Part.Line(grid_44[4][0], grid_44[5][0])
	l_02_12=Part.Line(grid_44[2][0], grid_44[6][0])
	l_13_12=Part.Line(grid_44[7][0], grid_44[6][0])
	l_23_22=Part.Line(grid_44[11][0], grid_44[10][0])
	l_32_22=Part.Line(grid_44[14][0], grid_44[10][0])
	## l_31_21
	l_20_21=Part.Line(grid_44[8][0], grid_44[9][0])

	l_11_12=Part.Line(grid_44[5][0], grid_44[6][0])
	l_12_22=Part.Line(grid_44[6][0], grid_44[10][0])
	l_21_22=Part.Line(grid_44[9][0], grid_44[10][0])

	if (grid_44[5][0]==grid_44[9][0]):
		l_11_21=Part.Point(grid_44[5][0])
	else:
		l_11_21=Part.Line(grid_44[5][0], grid_44[9][0])

	poly_grid_44=[l_00_01, l_01_02, l_02_03,
				l_03_13, l_13_23, l_23_33,
				l_33_32, l_32_31, l_31_30,
				l_20_30, l_10_20, l_00_10,
				l_01_11, l_10_11, l_02_12, l_13_12, 
				l_23_22, l_32_22, l_31_21, l_20_21,
				l_11_12, l_12_22, l_21_22, l_11_21]
	return poly_grid_44

def poly_grid_64(grid_64):
	# start around the perimeter
	l_00_01 = Part.Line(grid_64[0], grid_64[1])
	l_01_02 = Part.Line(grid_64[1], grid_64[2])
	l_02_03 = Part.Line(grid_64[2], grid_64[3])
	l_03_04 = Part.Line(grid_64[3], grid_64[4])
	l_04_05 = Part.Line(grid_64[4], grid_64[5])

	l_05_15 = Part.Line(grid_64[5], grid_64[11])
	l_15_25 = Part.Line(grid_64[11], grid_64[17])
	l_25_35 = Part.Line(grid_64[17], grid_64[23])

	l_34_35 = Part.Line(grid_64[22], grid_64[23])
	l_33_34 = Part.Line(grid_64[21], grid_64[22])
	l_32_33 = Part.Line(grid_64[20], grid_64[21])
	l_31_32 = Part.Line(grid_64[19], grid_64[20])
	l_30_31 = Part.Line(grid_64[18], grid_64[19])

	l_20_30=Part.Line(grid_64[12], grid_64[18])
	l_10_20=Part.Line(grid_64[6], grid_64[12])
	l_00_10=Part.Line(grid_64[0], grid_64[6])

	# Internal controls - along the edges
	l_01_11 =Part.Line(grid_64[1], grid_64[7])
	l_02_12 =Part.Line(grid_64[2], grid_64[8])
	l_03_13 =Part.Line(grid_64[3], grid_64[9])
	l_04_14 =Part.Line(grid_64[4], grid_64[10])

	l_14_15 =Part.Line(grid_64[10], grid_64[11])
	l_24_25 =Part.Line(grid_64[16], grid_64[17])

	l_24_34 =Part.Line(grid_64[16], grid_64[22])
	l_23_33 =Part.Line(grid_64[15], grid_64[21])
	l_22_32 =Part.Line(grid_64[14], grid_64[20])
	l_21_31 =Part.Line(grid_64[13], grid_64[19])

	l_20_21 =Part.Line(grid_64[12], grid_64[13])
	l_10_11 =Part.Line(grid_64[6], grid_64[7])

	# Internal controls - the three innermost cells

	l_11_12 =Part.Line(grid_64[7], grid_64[8])
	l_12_13 =Part.Line(grid_64[8], grid_64[9])
	l_13_14 =Part.Line(grid_64[9], grid_64[10])

	l_14_24 =Part.Line(grid_64[10], grid_64[16])

	l_23_24 =Part.Line(grid_64[15], grid_64[16])
	l_22_23 =Part.Line(grid_64[14], grid_64[15])
	l_21_22 =Part.Line(grid_64[13], grid_64[14])

	l_11_21 =Part.Line(grid_64[7], grid_64[13])

	l_12_22 =Part.Line(grid_64[8], grid_64[14])
	l_13_23 =Part.Line(grid_64[9], grid_64[15])

	poly_grid_64=[l_00_01, l_01_02, l_02_03,l_03_04,l_04_05,
				l_00_10,l_01_11,l_02_12,l_03_13,l_04_14,l_05_15,
				l_10_11, l_11_12, l_12_13,l_13_14,l_14_15,
				l_10_20,l_11_21,l_12_22,l_13_23,l_14_24,l_15_25,
				l_20_21, l_21_22, l_22_23,l_23_24,l_24_25,
				l_20_30,l_21_31,l_22_32,l_23_33,l_24_34,l_25_35,
				l_30_31, l_31_32, l_32_33,l_33_34,l_34_35]
	return poly_grid_64

def poly_grid_64_tri(grid_64):
	## start around the perimeter
	l_00_01 = Part.Line(grid_64[0][0], grid_64[1][0])
	l_01_02 = Part.Line(grid_64[1][0], grid_64[2][0])
	l_02_03 = Part.Line(grid_64[2][0], grid_64[3][0])
	l_03_04 = Part.Line(grid_64[3][0], grid_64[4][0])
	l_04_05 = Part.Line(grid_64[4][0], grid_64[5][0])

	l_05_15 = Part.Line(grid_64[5][0], grid_64[11][0])
	l_15_25 = Part.Line(grid_64[11][0], grid_64[17][0])
	l_25_35 = Part.Line(grid_64[17][0], grid_64[23][0])

	# skip top edge

	l_20_30=Part.Line(grid_64[12][0], grid_64[18][0])
	l_10_20=Part.Line(grid_64[6][0], grid_64[12][0])
	l_00_10=Part.Line(grid_64[0][0], grid_64[6][0])

	## Internal controls - along the edges
	#bottom
	l_01_11 =Part.Line(grid_64[1][0], grid_64[7][0])
	l_02_12 =Part.Line(grid_64[2][0], grid_64[8][0])
	l_03_13 =Part.Line(grid_64[3][0], grid_64[9][0])
	l_04_14 =Part.Line(grid_64[4][0], grid_64[10][0])

	#right
	l_14_15 =Part.Line(grid_64[10][0], grid_64[11][0])
	l_24_25 =Part.Line(grid_64[16][0], grid_64[17][0])

	# skip anything connecting to top edge
	l_21_31 = Part.Line(grid_64[13][0], grid_64[23][0])  #this is not a real control leg. just a visual indication of the collapsed corner

	# left
	l_20_21 =Part.Line(grid_64[12][0], grid_64[13][0])
	l_10_11 =Part.Line(grid_64[6][0], grid_64[7][0])

	## Internal controls - the center triangle

	l_12_13 =Part.Line(grid_64[8][0], grid_64[9][0]) #

	l_14_24 =Part.Line(grid_64[10][0], grid_64[16][0]) #

	l_11_21 =Part.Line(grid_64[7][0], grid_64[13][0]) #

	poly_grid_64_tri=[l_00_01, l_01_02, l_02_03,l_03_04,l_04_05, #keep whole
				l_00_10,l_01_11,l_02_12,l_03_13,l_04_14,l_05_15, #keep whole
				l_10_11, l_12_13,l_14_15,  # two legs removed
				l_10_20,l_11_21,l_14_24,l_15_25, # two legs removed
				l_20_21,l_24_25, # three legs removed
				l_20_30,l_21_31,l_25_35, # three legs removed, 'fake'l21_31 added back
				] # all 5 top edge segments removed
	return poly_grid_64_tri


def BezBiCubic_surf(grid_44):	# obsolete - this was made to check against Bezier_Bicubic_surf(grid_44), and is not used for anything.
	surf=Part.BezierSurface()
	surf.increase(3,3)
	n=0
	for u in range(1,5):
		for v in range(1,5):
			surf.setPole(v,u,grid_44[n])
			n=n+1
	return surf

def  Bezier_Bicubic_surf(grid_44):
	# len(knot_u) := nNodes_u + degree_u + 1
	# len(knot_v) := nNodes_v + degree_v + 1
	degree_u=3
	degree_v=3
	nNodes_u=4
	nNodes_v=4
	knot_u=[0,0,0,0,1,1,1,1]
	knot_v=[0,0,0,0,1,1,1,1]
	Bezier_Bicubic_surf=Part.BSplineSurface()
	Bezier_Bicubic_surf.increaseDegree(degree_u,degree_v)
	id=1
	for i in range(0,len(knot_u)):    #-1):
		Bezier_Bicubic_surf.insertUKnot(knot_u[i],id,0.0000001)
	id=1
	for i in range(0,len(knot_v)):    #-1):
		Bezier_Bicubic_surf.insertVKnot(knot_v[i],id,0.0000001)
	i=0
	for jj in range(0,nNodes_v):
		for ii in range(0,nNodes_u):
			Bezier_Bicubic_surf.setPole(ii+1,jj+1,grid_44[i][0], grid_44[i][1]);
			i=i+1;
	return Bezier_Bicubic_surf

def NURBS_Cubic_66_surf(grid_66):
	# len(knot_u) := nNodes_u + degree_u + 1
	# len(knot_v) := nNodes_v + degree_v + 1
	degree_u=3
	degree_v=3
	nNodes_u=6
	nNodes_v=6
	knot_u=[0,0,0,0,0.3333,0.6666,1,1,1,1]
	knot_v=[0,0,0,0,0.3333,0.6666,1,1,1,1]
	NURBS_Cubic_66_surf=Part.BSplineSurface()
	NURBS_Cubic_66_surf.increaseDegree(degree_u,degree_v)
	id=1
	for i in range(0,len(knot_u)):    #-1):
		NURBS_Cubic_66_surf.insertUKnot(knot_u[i],id,0.0000001)
	id=1
	for i in range(0,len(knot_v)):    #-1):
		NURBS_Cubic_66_surf.insertVKnot(knot_v[i],id,0.0000001)
	i=0
	for jj in range(0,nNodes_v):
		for ii in range(0,nNodes_u):
			NURBS_Cubic_66_surf.setPole(ii+1,jj+1,grid_66[i][0],grid_66[i][1]);
			i=i+1;
	return  NURBS_Cubic_66_surf

def NURBS_Cubic_64_surf_no_weights(grid_64):
	# len(knot_u) := nNodes_u + degree_u + 1
	# len(knot_v) := nNodes_v + degree_v + 1
	degree_u=3
	degree_v=3
	nNodes_u=6
	nNodes_v=4
	knot_u=[0,0,0,0,0.3333,0.6666,1,1,1,1]
	knot_v=[0,0,0,0,1,1,1,1]
	NURBS_Cubic_64_surf=Part.BSplineSurface()
	NURBS_Cubic_64_surf.increaseDegree(degree_u,degree_v)
	id=1
	for i in range(0,len(knot_u)):    #-1):
		NURBS_Cubic_64_surf.insertUKnot(knot_u[i],id,0.0000001)
	id=1
	for i in range(0,len(knot_v)):    #-1):
		NURBS_Cubic_64_surf.insertVKnot(knot_v[i],id,0.0000001)
	i=0
	for jj in range(0,nNodes_v):
		for ii in range(0,nNodes_u):
			NURBS_Cubic_64_surf.setPole(ii+1,jj+1,grid_64[i],1);
			i=i+1;
	return  NURBS_Cubic_64_surf

def NURBS_Cubic_64_surf(grid_64):
	# len(knot_u) := nNodes_u + degree_u + 1
	# len(knot_v) := nNodes_v + degree_v + 1
	degree_u=3
	degree_v=3
	nNodes_u=6
	nNodes_v=4
	knot_u=[0,0,0,0,0.3333,0.6666,1,1,1,1]
	knot_v=[0,0,0,0,1,1,1,1]
	NURBS_Cubic_64_surf=Part.BSplineSurface()
	NURBS_Cubic_64_surf.increaseDegree(degree_u,degree_v)
	id=1
	for i in range(0,len(knot_u)):    #-1):
		NURBS_Cubic_64_surf.insertUKnot(knot_u[i],id,0.0000001)
	id=1
	for i in range(0,len(knot_v)):    #-1):
		NURBS_Cubic_64_surf.insertVKnot(knot_v[i],id,0.0000001)
	i=0
	for jj in range(0,nNodes_v):
		for ii in range(0,nNodes_u):
			NURBS_Cubic_64_surf.setPole(ii+1,jj+1,grid_64[i][0],grid_64[i][1]);
			i=i+1;
	return  NURBS_Cubic_64_surf


def isect_test(curve, surf, u):		# provides information about a curve point at parameter u as a surface intersection candidate.						
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

def  isect_curve_surf(curve, surf):
	tol= 0.00000001
	# setup the parameter search span 
	test_span = [curve.FirstParameter, curve.LastParameter]
	# determine whether the curve grows from inside or outside the surface. this will govern how to split the search span
	test_u_direction =  isect_test(curve, surf, curve.FirstParameter) 	# project curve startpoint to determine if it is 'inside' or 'outside' the surface.
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
		test =  isect_test(curve, surf, test_u)			# project curve(u) onto surface
		error = test[2]							# set current intersection error
		if ((test[3]*direction) < 0):					# is the projection still coming from outside the surface?
			test_span = [test_u, test_span[1]]		# > use second half of current span for the next search
		if ((test[3]*direction) > 0):					# is the projection coming from inside the surface?
			test_span = [test_span[0], test_u]		# > use first half of current span for the next search
		loop_count=loop_count + 1
	print 'step ', loop_count, '  u ', test_u, '  error ', test[2]
	if error > tol:
		print 'no intersection found within ', tol
		isect_curve_surf = 'NONE'
	else:
		isect_curve_surf = [test[0], test_u, test[4]]
	return  isect_curve_surf

#################################################################################################
#################################################################################################

#### SECTION 2: PYTHON FEATURE CLASSES - PARAMETRIC LINKING BETWEEN OBJECTS - IN PROGRESS

# poles = 3D points with weights, as [[x,y,z],w], or [x,y,z] (these are leftovers waiting to receive weights). 
# need to make a class for this...but i'm hoping to have FreeCAD do it for me :)

#### new classes needed to implement linked parametric behavior:

### polyline of control points created from a variety of sketches.

## 4 points, for use in Bezier cubic curves.

# ControlPoly4_3L(sketch) 					# made from a single sketch containing 3 line objects
# ControlPoly4_2N(sketch0, sketch1)			# made from 2 node sketches. each node sketch contain one line (tangent), and one circle (endpoint) located at one end of the line.
# ControlPoly4_Arc(sketch)					# made from a single sketch containing 1 arc object

## 6 points, for use in 6 point NURBS cubic curves.

# ControlPoly6_5L(sketch) 					# made from a single sketch containing 5 line objects
# ControlPoly6_2N(sketch0, sketch1)			# made from 2 node sketches. each node sketch contain 2 lines, and one circle.
# ControlPoly6_Arc(sketch)					# made from a single sketch containing 1 arc object

### polyhedra of control points created from loops of CubicControlPolys.

## 4 points by 4 point grids, for use in BezierXBezier Bicubic surface patches.

# ControlGrid44_4(poly0, poly1, poly2, poly3)	# made from 4 CubicControlPoly4.
# ControlGrid44_3(poly0, poly1, poly2)			# made from 3 CubicControlPoly4. degenerate grid.

## 6 points by 4 point grids, for use in BezierX6P Bicubic surface patches.

# ControlGrid64_4(poly0, poly1, poly2, poly3)	# made from 2 CubicControlPoly6 and 2 CubicControlPoly4.
# ControlGrid64_3(poly0, poly1, poly2)			# made from 2 CubicControlPoly4 and 1 CubicControlPoly6. degenerate grid.

## 6 points by 6 point grids, for use in 6PX6P Bicubic surface patches.

# ControlGrid66_4(poly0, poly1, poly2, poly3)	# made from 4 CubicControlPoly6.
# ControlGrid66_3(poly0, poly1, poly2)			# made from 3 CubicControlPoly6. degenerate grid.

### cubic curves created from CubicControlPolys

# CubicCurve_4
# CubicCurve_6

### BiCubic surfaces created from CubicControlGrids

# CubicSurface_44
# CubicSurface_64
# CubicSurface_66

#### CLASS RECAP

# ControlPoly4_3L(sketch)									#tested-works 2016-08-04
# ControlPoly4_2N(sketch0, sketch1)							#tested-works 2016-08-04
# ControlPoly4_Arc(sketch)									#tested-works 2016-08-05
# ControlPoly6_5L(sketch)									#tested-works 2016-08-06
# ControlPoly6_2N(sketch0, sketch1)							#tested-works 2016-08-06
# ControlPoly6_Arc(sketch)									#tested-works 2016-08-17
# ControlGrid44_4(poly0, poly1, poly2, poly3)				#tested-works 2016-08-05
# ControlGrid44_3(poly0, poly1, poly2)			
# ControlGrid64_4(poly0, poly1, poly2, poly3)				#tested-works 2016-08-14
# ControlGrid64_3(poly0, poly1, poly2)
# ControlGrid66_4(poly0, poly1, poly2, poly3)				#tested-works 2016-08-06
# ControlGrid66_3(poly0, poly1, poly2)
# CubicCurve_4												#tested-works 2016-08-04
# CubicCurve_6												#tested-works 2016-08-06
# ControlPoly6_Bezier(CubicCurve4_0)						#tested-works 2016-08-17
# ControlPoly6_FilletBezier(CubicCurve4_0,CubicCurve4_1)
# CubicSurface_44											#tested-works 2016-08-04
# CubicSurface_64											#tested-works 2016-08-14
# CubicSurface_66											#tested-works 2016-08-06



#### used legacy functions:
#
# orient_a_to_b(lista,listb)
# Bezier_Cubic_curve(WeightedPoles)
# Bezier_Bicubic_surf(WeightedPoles)
# NURBS_Cubic_6P_curve(WeightedPoles)
# NURBS_Cubic_66_surf(WeightedPoles)
# NURBS_Cubic_64_surf(WeightedPoles)
#
#
#
#
#
#
#### let's get started!

#### control polygons

#### 4 points

class ControlPoly4_3L:
	def __init__(self, obj , sketch):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nControlPoly4_3L class Init\n")
		obj.addProperty("App::PropertyLink","Sketch","ControlPoly4_3L","reference Sketch").Sketch = sketch
		obj.addProperty("Part::PropertyGeometryList","Legs","ControlPoly4_3L","control segments").Legs
		obj.addProperty("App::PropertyVectorList","Poles","ControlPoly4_3L","Poles").Poles
		obj.addProperty("App::PropertyFloatList","Weights","ControlPoly4_3L","Weights").Weights = [1.0,1.0,1.0,1.0]
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		# get all points on first three lines...error check later
		p00s=fp.Sketch.Geometry[0].StartPoint
		p01s=fp.Sketch.Geometry[0].EndPoint
		p10s=fp.Sketch.Geometry[1].StartPoint
		p11s=fp.Sketch.Geometry[1].EndPoint
		p20s=fp.Sketch.Geometry[2].StartPoint
		p21s=fp.Sketch.Geometry[2].EndPoint
		# to world
		mat=fp.Sketch.Placement.toMatrix()
		p00=mat.multiply(p00s)
		p01=mat.multiply(p01s)
		p20=mat.multiply(p20s)
		p21=mat.multiply(p21s)
		#for now assume
		fp.Poles=[p00,p01,p20,p21]
		# prepare the lines to draw the polyline
		Leg0=Part.Line(p00,p01)
		Leg1=Part.Line(p01,p20)
		Leg2=Part.Line(p20,p21)
		#set the polygon legs property
		fp.Legs=[Leg0, Leg1, Leg2]
		# define the shape for visualization
		fp.Shape = Part.Shape(fp.Legs)


class ControlPoly4_2N:
	def __init__(self, obj , sketch0, sketch1):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nControlPoly4_2N class Init\n")
		obj.addProperty("App::PropertyLink","Sketch0","ControlPoly4_2N","reference Sketch").Sketch0 = sketch0
		obj.addProperty("App::PropertyLink","Sketch1","ControlPoly4_2N","reference Sketch").Sketch1 = sketch1
		obj.addProperty("Part::PropertyGeometryList","Legs","ControlPoly4_2N","control segments").Legs
		obj.addProperty("App::PropertyVectorList","Poles","ControlPoly4_2N","Poles").Poles
		obj.addProperty("App::PropertyFloatList","Weights","ControlPoly4_2N","Weights").Weights = [1.0,1.0,1.0,1.0]
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		# process Sketch0
		obj00=fp.Sketch0.Geometry[0]
		obj01=fp.Sketch0.Geometry[1]
		if obj00.__class__==Part.Circle:
			cir0=obj00
		if obj01.__class__==Part.Circle:
			cir0=obj01
		if obj00.__class__==Part.Line:
			lin0=obj00
		if obj01.__class__==Part.Line:
			lin0=obj01
		p00s=cir0.Center
		if lin0.StartPoint==p00s:
			p01s=lin0.EndPoint
		elif lin0.EndPoint==p00s:
			p01s=lin0.StartPoint
		# to world
		mat0=fp.Sketch0.Placement.toMatrix()
		p00=mat0.multiply(p00s)
		p01=mat0.multiply(p01s)
		# process Sketch1
		obj10=fp.Sketch1.Geometry[0]
		obj11=fp.Sketch1.Geometry[1]
		if obj10.__class__==Part.Circle:
			cir1=obj10
		if obj11.__class__==Part.Circle:
			cir1=obj11
		if obj10.__class__==Part.Line:
			lin1=obj10
		if obj11.__class__==Part.Line:
			lin1=obj11
		p11s=cir1.Center
		if lin1.StartPoint==p11s:
			p10s=lin1.EndPoint
		elif lin1.EndPoint==p11s:
			p10s=lin1.StartPoint
		# to world
		mat1=fp.Sketch1.Placement.toMatrix()
		p10=mat1.multiply(p10s)
		p11=mat1.multiply(p11s)
		# set the poles
		fp.Poles=[p00,p01,p10,p11]
		# prepare the polygon
		Leg0=Part.Line(p00,p01)
		Leg1=Part.Line(p01,p10)
		Leg2=Part.Line(p10,p11)
		#set the polygon legs property
		fp.Legs=[Leg0, Leg1, Leg2]
		# define the shape for visualization
		fp.Shape = Part.Shape(fp.Legs)

class ControlPoly4_Arc:
	def __init__(self, obj , sketch):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nControlPoly4_Arc class Init\n")
		obj.addProperty("App::PropertyLink","Sketch","ControlPoly4_Arc","reference Sketch").Sketch = sketch
		obj.addProperty("Part::PropertyGeometryList","Legs","ControlPoly4_Arc","control segments").Legs
		obj.addProperty("App::PropertyVectorList","Poles","ControlPoly4_Arc","Poles").Poles
		obj.addProperty("App::PropertyFloatList","Weights","ControlPoly4_Arc","Weights").Weights = [1.0,1.0,1.0,1.0]
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		# process the sketch arc...error check later
		ArcNurbs=fp.Sketch.Shape.Edges[0].toNurbs().Edge1.Curve
		ArcNurbs.increaseDegree(3)
		p0=ArcNurbs.getPole(1)
		p1=ArcNurbs.getPole(2)
		p2=ArcNurbs.getPole(3)
		p3=ArcNurbs.getPole(4)
		# already to world?
		#mat=fp.Sketch.Placement.toMatrix()
		#p0=mat.multiply(p0s)
		#p1=mat.multiply(p1s)
		#p2=mat.multiply(p2s)
		#p3=mat.multiply(p3s)
		fp.Poles=[p0,p1,p2,p3]
		# set the weights
		fp.Weights = ArcNurbs.getWeights()
		# prepare the lines to draw the polyline
		Leg0=Part.Line(p0,p1)
		Leg1=Part.Line(p1,p2)
		Leg2=Part.Line(p2,p3)
		#set the polygon legs property
		fp.Legs=[Leg0, Leg1, Leg2]
		# define the shape for visualization
		fp.Shape = Part.Shape(fp.Legs)

#### 6 points

class ControlPoly6_5L:
	def __init__(self, obj , sketch):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nControlPoly6_5L class Init\n")
		obj.addProperty("App::PropertyLink","Sketch","ControlPoly4_3L","reference Sketch").Sketch = sketch
		obj.addProperty("Part::PropertyGeometryList","Legs","ControlPoly4_3L","control segments").Legs
		obj.addProperty("App::PropertyVectorList","Poles","ControlPoly4_3L","Poles").Poles
		obj.addProperty("App::PropertyFloatList","Weights","ControlPoly4_3L","Weights").Weights = [1.0,1.0,1.0,1.0,1.0,1.0]
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		# get all points on first three lines...error check later
		p00s=fp.Sketch.Geometry[0].StartPoint
		p01s=fp.Sketch.Geometry[0].EndPoint
		p10s=fp.Sketch.Geometry[1].StartPoint
		p11s=fp.Sketch.Geometry[1].EndPoint
		p20s=fp.Sketch.Geometry[2].StartPoint
		p21s=fp.Sketch.Geometry[2].EndPoint
		p30s=fp.Sketch.Geometry[3].StartPoint
		p31s=fp.Sketch.Geometry[3].EndPoint
		p40s=fp.Sketch.Geometry[4].StartPoint
		p41s=fp.Sketch.Geometry[4].EndPoint
		# to world
		mat=fp.Sketch.Placement.toMatrix()
		p00=mat.multiply(p00s)
		p01=mat.multiply(p01s)
		p20=mat.multiply(p20s)
		p21=mat.multiply(p21s)
		p40=mat.multiply(p40s)
		p41=mat.multiply(p41s)
		#for now assume
		fp.Poles=[p00,p01,p20,p21,p40,p41]
		# prepare the lines to draw the polyline
		Leg0=Part.Line(p00,p01)
		Leg1=Part.Line(p01,p20)
		Leg2=Part.Line(p20,p21)
		Leg4=Part.Line(p21,p40)
		Leg5=Part.Line(p40,p41)
		#set the polygon legs property
		fp.Legs=[Leg0, Leg1, Leg2, Leg4, Leg5]
		# define the shape for visualization
		fp.Shape = Part.Shape(fp.Legs)

class ControlPoly6_2N:
	def __init__(self, obj , sketch0, sketch1):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nControlPoly6_2N class Init\n")
		obj.addProperty("App::PropertyLink","Sketch0","ControlPoly6_2N","reference Sketch").Sketch0 = sketch0
		obj.addProperty("App::PropertyLink","Sketch1","ControlPoly6_2N","reference Sketch").Sketch1 = sketch1
		obj.addProperty("Part::PropertyGeometryList","Legs","ControlPoly6_2N","control segments").Legs
		obj.addProperty("App::PropertyVectorList","Poles","ControlPoly6_2N","Poles").Poles
		obj.addProperty("App::PropertyFloatList","Weights","ControlPoly6_2N","Weights").Weights = [1.0,1.0,1.0,1.0,1.0,1.0]
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		# process Sketch0
		obj00=fp.Sketch0.Geometry[0]
		obj01=fp.Sketch0.Geometry[1]
		obj02=fp.Sketch0.Geometry[2]
		# must draw the pieces in the correct order! improve later
		p00s=obj00.Center
		p01s=obj01.EndPoint
		p02s=obj02.EndPoint
		# to world
		mat0=fp.Sketch0.Placement.toMatrix()
		p00=mat0.multiply(p00s)
		p01=mat0.multiply(p01s)
		p02=mat0.multiply(p02s)
		# process Sketch1
		obj10=fp.Sketch1.Geometry[0]
		obj11=fp.Sketch1.Geometry[1]
		obj12=fp.Sketch1.Geometry[2]
		# must draw the pieces in the correct order! improve later
		p12s=obj10.Center
		p11s=obj11.EndPoint
		p10s=obj12.EndPoint
		# to world
		mat1=fp.Sketch1.Placement.toMatrix()
		p10=mat1.multiply(p10s)
		p11=mat1.multiply(p11s)
		p12=mat1.multiply(p12s)
		# set the poles
		fp.Poles=[p00,p01,p02,p10,p11, p12]
		# prepare the polygon
		Leg0=Part.Line(p00,p01)
		Leg1=Part.Line(p01,p02)
		Leg2=Part.Line(p02,p10)
		Leg3=Part.Line(p10,p11)
		Leg4=Part.Line(p11,p12)
		#set the polygon legs property
		fp.Legs=[Leg0, Leg1, Leg2, Leg3, Leg4]
		# define the shape for visualization
		fp.Shape = Part.Shape(fp.Legs)

class ControlPoly6_Arc:
	def __init__(self, obj , sketch):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nControlPoly6_Arc class Init\n")
		obj.addProperty("App::PropertyLink","Sketch","ControlPoly6_Arc","reference Sketch").Sketch = sketch
		obj.addProperty("Part::PropertyGeometryList","Legs","ControlPoly6_Arc","control segments").Legs
		obj.addProperty("App::PropertyVectorList","Poles","ControlPoly6_Arc","Poles").Poles
		obj.addProperty("App::PropertyFloatList","Weights","ControlPoly6_Arc","Weights").Weights = [1.0,1.0,1.0,1.0]
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		# process the sketch arc...error check later
		ArcNurbs=fp.Sketch.Shape.Edges[0].toNurbs().Edge1.Curve
		ArcNurbs.increaseDegree(3)
		start=ArcNurbs.FirstParameter
		end=ArcNurbs.LastParameter
		knot1=start+(end-start)/3.0
		knot2=end-(end-start)/3.0
		ArcNurbs.insertKnot(knot1)
		ArcNurbs.insertKnot(knot2)
		p0=ArcNurbs.getPole(1)
		p1=ArcNurbs.getPole(2)
		p2=ArcNurbs.getPole(3)
		p3=ArcNurbs.getPole(4)
		p4=ArcNurbs.getPole(5)
		p5=ArcNurbs.getPole(6)
		# already to world?
		#mat=fp.Sketch.Placement.toMatrix()
		#p0=mat.multiply(p0s)
		#p1=mat.multiply(p1s)
		#p2=mat.multiply(p2s)
		#p3=mat.multiply(p3s)
		fp.Poles=[p0,p1,p2,p3,p4,p5]
		# set the weights
		fp.Weights = ArcNurbs.getWeights()
		# prepare the lines to draw the polyline
		Leg0=Part.Line(p0,p1)
		Leg1=Part.Line(p1,p2)
		Leg2=Part.Line(p2,p3)
		Leg3=Part.Line(p3,p4)
		Leg4=Part.Line(p4,p5)
		#set the polygon legs property
		fp.Legs=[Leg0, Leg1, Leg2, Leg3, Leg4]
		# define the shape for visualization
		fp.Shape = Part.Shape(fp.Legs)


###################################################################################################

# ControlGrid44_4(poly0, poly1, poly2, poly3)
class ControlGrid44_4:
	def __init__(self, obj , poly0, poly1, poly2, poly3):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nControlGrid44_4 class Init\n")
		obj.addProperty("App::PropertyLink","Poly0","ControlGrid44_4","control polygon").Poly0 = poly0
		obj.addProperty("App::PropertyLink","Poly1","ControlGrid44_4","control polygon").Poly1 = poly1
		obj.addProperty("App::PropertyLink","Poly2","ControlGrid44_4","control polygon").Poly2 = poly2
		obj.addProperty("App::PropertyLink","Poly3","ControlGrid44_4","control polygon").Poly3 = poly3
		obj.addProperty("Part::PropertyGeometryList","Legs","ControlGrid44_4","control segments").Legs
		obj.addProperty("App::PropertyVectorList","Poles","ControlGrid44_4","Poles").Poles
		obj.addProperty("App::PropertyFloatList","Weights","ControlGrid44_4","Weights").Weights
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		poles1=fp.Poly0.Poles
		poles2=fp.Poly1.Poles
		poles3=fp.Poly2.Poles
		poles4=fp.Poly3.Poles	
		weights1=fp.Poly0.Weights
		weights2=fp.Poly1.Weights
		weights3=fp.Poly2.Weights
		weights4=fp.Poly3.Weights
		quad12 = orient_a_to_b(poles1,poles2)
		quad23 = orient_a_to_b(poles2,poles3)
		quad34 = orient_a_to_b(poles3,poles4)
		quad41 = orient_a_to_b(poles4,poles1)	
		if quad12[0]!=poles1[0] and quad12[0]==poles1[-1]:
			weights1=weights1[::-1]
		if quad23[0]!=poles2[0] and quad23[0]==poles2[-1]:
			weights2=weights2[::-1]
		if quad34[0]!=poles3[0] and quad34[0]==poles3[-1]:
			weights3=weights3[::-1]
		if quad41[0]!=poles4[0] and quad41[0]==poles4[-1]:
			weights4=weights4[::-1]
		p00 = quad12[0]
		p01 = quad12[1]
		p02 = quad12[2]	
		p03 = quad12[3]
		p13 = quad23[1]
		p23 = quad23[2]
		p33 = quad23[3]
		p32 = quad34[1]
		p31 = quad34[2]
		p30 = quad34[3]
		p20 = quad41[1]
		p10 = quad41[2]
		p11 = p00 + (p01 - p00) +  (p10 - p00)
		p12 = p03 + (p02 - p03) +  (p13 - p03)
		p21 = p30 + (p31 - p30) +  (p20 - p30)
		p22 = p33 + (p23 - p33) +  (p32 - p33)
		fp.Poles = [p00 ,p01, p02, p03,
					p10, p11, p12, p13,
					p20, p21, p22, p23,
					p30, p31, p32, p33]
		w00 = weights1[0]
		w01 = weights1[1]
		w02 = weights1[2]
		w03 = weights1[3]
		w13 = weights2[1]
		w23 = weights2[2]
		w33 = weights2[3]
		w32 = weights3[1]
		w31 = weights3[2]
		w30 = weights3[3]
		w20 = weights4[1]
		w10 = weights4[2]
		w11 = w01*w20
		w12 = w02*w13
		w21 = w32*w10
		w22 = w23*w31
		fp.Weights = [w00 ,w01, w02, w03,
					w10, w11, w12, w13,
					w20, w21, w22, w23,
					w30, w31, w32, w33]
		Legs=[0]*24
		for i in range(0,3):
			Legs[i]=Part.Line(fp.Poles[i],fp.Poles[i+1])
		for i in range(3,6):
			Legs[i]=Part.Line(fp.Poles[i+1],fp.Poles[i+2])
		for i in range(6,9):
			Legs[i]=Part.Line(fp.Poles[i+2],fp.Poles[i+3])
		for i in range(9,12):
			Legs[i]=Part.Line(fp.Poles[i+3],fp.Poles[i+4])
		for i in range(12,16):
			Legs[i]=Part.Line(fp.Poles[i-12],fp.Poles[i-8])
		for i in range(16,20):
			Legs[i]=Part.Line(fp.Poles[i-12],fp.Poles[i-8])
		for i in range(20,24):
			Legs[i]=Part.Line(fp.Poles[i-12],fp.Poles[i-8])
		fp.Legs=Legs
		fp.Shape = Part.Shape(fp.Legs)

# ControlGrid66_4
class ControlGrid66_4:
	def __init__(self, obj , poly0, poly1, poly2, poly3):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nControlGrid66_4 class Init\n")
		obj.addProperty("App::PropertyLink","Poly0","ControlGrid66_4","control polygon").Poly0 = poly0
		obj.addProperty("App::PropertyLink","Poly1","ControlGrid66_4","control polygon").Poly1 = poly1
		obj.addProperty("App::PropertyLink","Poly2","ControlGrid66_4","control polygon").Poly2 = poly2
		obj.addProperty("App::PropertyLink","Poly3","ControlGrid66_4","control polygon").Poly3 = poly3
		obj.addProperty("Part::PropertyGeometryList","Legs","ControlGrid66_4","control segments").Legs
		obj.addProperty("App::PropertyVectorList","Poles","ControlGrid66_4","Poles").Poles
		obj.addProperty("App::PropertyFloatList","Weights","ControlGrid66_4","Weights").Weights
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		poles1=fp.Poly0.Poles
		poles2=fp.Poly1.Poles
		poles3=fp.Poly2.Poles
		poles4=fp.Poly3.Poles	
		weights1=fp.Poly0.Weights
		weights2=fp.Poly1.Weights
		weights3=fp.Poly2.Weights
		weights4=fp.Poly3.Weights
		sext12 = orient_a_to_b(poles1,poles2)
		sext23 = orient_a_to_b(poles2,poles3)
		sext34 = orient_a_to_b(poles3,poles4)
		sext41 = orient_a_to_b(poles4,poles1)	
		if sext12[0]!=poles1[0] and sext12[0]==poles1[-1]:
			weights1=weights1[::-1]
		if sext23[0]!=poles2[0] and sext23[0]==poles2[-1]:
			weights2=weights2[::-1]
		if sext34[0]!=poles3[0] and sext34[0]==poles3[-1]:
			weights3=weights3[::-1]
		if sext41[0]!=poles4[0] and sext41[0]==poles4[-1]:
			weights4=weights4[::-1]
		p00 = sext12[0]
		p01 = sext12[1]
		p02 = sext12[2]	
		p03 = sext12[3]
		p04 = sext12[4]
		p05 = sext12[5]
		p15 = sext23[1]
		p25 = sext23[2]
		p35 = sext23[3]
		p45 = sext23[4]
		p55 = sext23[5]
		p54 = sext34[1]
		p53 = sext34[2]
		p52 = sext34[3]
		p51 = sext34[4]
		p50 = sext34[5]
		p40 = sext41[1]
		p30 = sext41[2]
		p20 = sext41[3]
		p10 = sext41[4]
		p11 = p01 + (p10 - p00)
		p14 = p04 + (p15 - p05)
		p41 = p51 + (p40 - p50)
		p44 = p45 + (p54 - p55)
		p12 = p02 + (p10 - p00)
		p13 = p03 + (p15 - p05)	
		p24 = p25 + (p04 - p05)
		p34 = p35 + (p54 - p55)	
		p42 = p52 + (p40 - p50)
		p43 = p53 + (p45 - p55)
		p21 = p20 + (p01 - p00)
		p31 = p30 + (p51 - p50)
		p22 = p12 + (p20 - p10)
		p23 = p13 + (p25 - p15)
		p32 = p42 + (p30 - p40)
		p33 = p43 + (p35 - p45)
		fp.Poles = [p00, p01, p02, p03, p04, p05,
					p10, p11, p12, p13, p14, p15,
					p20, p21, p22, p23, p24, p25,
					p30, p31, p32, p33, p34, p35,
					p40, p41, p42, p43, p44, p45,
					p50, p51, p52, p53, p54, p55]
		w00 = weights1[0]
		w01 = weights1[1]
		w02 = weights1[2]
		w03 = weights1[3]
		w04 = weights1[4]
		w05 = weights1[5]
		w15 = weights2[1]
		w25 = weights2[2]
		w35 = weights2[3]
		w45 = weights2[4]
		w55 = weights2[5]
		w54 = weights3[1]
		w53 = weights3[2]
		w52 = weights3[3]
		w51 = weights3[4]
		w50 = weights3[5]
		w40 = weights4[1]
		w30 = weights4[2]		
		w20 = weights4[3]
		w10 = weights4[4]
		# maybe i should average instead of multiply? needs testing.
		# currently based on the idea all wights are between 0 and 1.
		# previous used cumulative neighbor mulitplication. this drives weights too low.
		# current method multiplies the two weights along isos to the closest edge
		w11 = w01*w10
		w12 = w02*w10 
		w21 = w01*w20
		w22 = w02*w20
		w14 = w04*w15
		w13 = w03*w15
		w24 = w04*w25
		w23 = w03*w25
		w44 = w45*w54
		w34 = w35*w54
		w43 = w54*w45
		w33 = w35*w53
		w41 = w40*w51
		w31 = w30*w51
		w42 = w52*w40
		w32 = w30*w52

		fp.Weights = [w00, w01, w02, w03, w04, w05,
					w10, w11, w12, w13, w14, w15,
					w20, w21, w22, w23, w24, w25,
					w30, w31, w32, w33, w34, w35,
					w40, w41, w42, w43, w44, w45,
					w50, w51, w52, w53, w54, w55]
		Legs=[0]*60
		for i in range(0,5):
			Legs[i]=Part.Line(fp.Poles[i],fp.Poles[i+1])
		for i in range(5,10):
			Legs[i]=Part.Line(fp.Poles[i+1],fp.Poles[i+2])
		for i in range(10,15):
			Legs[i]=Part.Line(fp.Poles[i+2],fp.Poles[i+3])
		for i in range(15,20):
			Legs[i]=Part.Line(fp.Poles[i+3],fp.Poles[i+4])
		for i in range(20,25):
			Legs[i]=Part.Line(fp.Poles[i+4],fp.Poles[i+5])
		for i in range(25,30):
			Legs[i]=Part.Line(fp.Poles[i+5],fp.Poles[i+6])
		for i in range(30,36):
			Legs[i]=Part.Line(fp.Poles[i-30],fp.Poles[i-24])
		for i in range(36,42):
			Legs[i]=Part.Line(fp.Poles[i-30],fp.Poles[i-24])
		for i in range(42,48):
			Legs[i]=Part.Line(fp.Poles[i-30],fp.Poles[i-24])
		for i in range(48,54):
			Legs[i]=Part.Line(fp.Poles[i-30],fp.Poles[i-24])
		for i in range(54,60):
			Legs[i]=Part.Line(fp.Poles[i-30],fp.Poles[i-24])

		fp.Legs=Legs
		fp.Shape = Part.Shape(fp.Legs)

# ControlGrid64_4(poly0, poly1, poly2, poly3)
class ControlGrid64_4:
	def __init__(self, obj , poly6_0, poly4_1, poly6_2, poly4_3):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nControlGrid64_4 class Init\n")
		obj.addProperty("App::PropertyLink","Poly6_0","ControlGrid64_4","control polygon").Poly6_0 = poly6_0
		obj.addProperty("App::PropertyLink","Poly4_1","ControlGrid64_4","control polygon").Poly4_1 = poly4_1
		obj.addProperty("App::PropertyLink","Poly6_2","ControlGrid64_4","control polygon").Poly6_2 = poly6_2
		obj.addProperty("App::PropertyLink","Poly4_3","ControlGrid64_4","control polygon").Poly4_3 = poly4_3
		obj.addProperty("Part::PropertyGeometryList","Legs","ControlGrid64_4","control segments").Legs
		obj.addProperty("App::PropertyVectorList","Poles","ControlGrid64_4","Poles").Poles
		obj.addProperty("App::PropertyFloatList","Weights","ControlGrid64_4","Weights").Weights
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		poles6_0=fp.Poly6_0.Poles
		poles4_1=fp.Poly4_1.Poles
		poles6_2=fp.Poly6_2.Poles
		poles4_3=fp.Poly4_3.Poles	
		weights6_0=fp.Poly6_0.Weights
		weights4_1=fp.Poly4_1.Weights
		weights6_2=fp.Poly6_2.Weights
		weights4_3=fp.Poly4_3.Weights
		sext12 = orient_a_to_b(poles6_0,poles4_1)
		quad23 = orient_a_to_b(poles4_1,poles6_2)
		sext34 = orient_a_to_b(poles6_2,poles4_3)
		quad41 = orient_a_to_b(poles4_3,poles6_0)	
		if sext12[0]!=poles6_0[0] and sext12[0]==poles6_0[-1]:
			weights6_0=weights6_0[::-1]
		if quad23[0]!=poles4_1[0] and quad23[0]==poles4_1[-1]:
			weights4_1=weights4_1[::-1]
		if sext34[0]!=poles6_2[0] and sext34[0]==poles6_2[-1]:
			weights6_2=weights6_2[::-1]
		if quad41[0]!=poles4_3[0] and quad41[0]==poles4_3[-1]:
			weights4_3=weights4_3[::-1]
		p00 = sext12[0]
		p01 = sext12[1]
		p02 = sext12[2]	
		p03 = sext12[3]
		p04 = sext12[4]
		p05 = sext12[5]
		p15 = quad23[1]
		p25 = quad23[2]
		p35 = quad23[3]
		p34 = sext34[1]
		p33 = sext34[2]
		p32 = sext34[3]
		p31 = sext34[4]
		p30 = sext34[5]
		p20 = quad41[1]
		p10 = quad41[2]
		p11 = p01 + (p10 - p00)
		p14 = p04 + (p15 - p05)
		p21 = p31 + (p20 - p30)
		p24 = p25 + (p34 - p35)
		p12 = p02 + (p10 - p00)
		p13 = p03 + (p15 - p05)	
		p22 = p32 + (p20 - p30)
		p23 = p33 + (p25 - p35)
		fp.Poles = [p00, p01, p02, p03, p04, p05,
					p10, p11, p12, p13, p14, p15,
					p20, p21, p22, p23, p24, p25,
					p30, p31, p32, p33, p34, p35]
		w00 = weights6_0[0]
		w01 = weights6_0[1]
		w02 = weights6_0[2]
		w03 = weights6_0[3]
		w04 = weights6_0[4]
		w05 = weights6_0[5]
		w15 = weights4_1[1]
		w25 = weights4_1[2]
		w35 = weights4_1[3]
		w34 = weights6_2[1]
		w33 = weights6_2[2]
		w32 = weights6_2[3]
		w31 = weights6_2[4]
		w30 = weights6_2[5]
		w20 = weights4_3[1]
		w10 = weights4_3[2]
		# maybe i should average instead of multiply? needs testing.
		# currently based on the idea all wights are between 0 and 1.
		# previous used cumulative neighbor mulitplication. this drives weights too low.
		# current method multiplies the two weights along isos to the closest edge
		w11 = w01*w10
		w12 = w02*w10
		w13 = w03*w15
		w14 = w04*w15
		w21 = w31*w20
		w22 = w32*w20		
		w23 = w33*w25		
		w24 = w34*w25
		fp.Weights = [w00, w01, w02, w03, w04, w05,
					w10, w11, w12, w13, w14, w15,
					w20, w21, w22, w23, w24, w25,
					w30, w31, w32, w33, w34, w35]
		Legs=[0]*38
		for i in range(0,5):
			Legs[i]=Part.Line(fp.Poles[i],fp.Poles[i+1])
		for i in range(5,10):
			Legs[i]=Part.Line(fp.Poles[i+1],fp.Poles[i+2])
		for i in range(10,15):
			Legs[i]=Part.Line(fp.Poles[i+2],fp.Poles[i+3])
		for i in range(15,20):
			Legs[i]=Part.Line(fp.Poles[i+3],fp.Poles[i+4])

		for i in range(20,26):
			Legs[i]=Part.Line(fp.Poles[i-20],fp.Poles[i-14])
		for i in range(26,32):
			Legs[i]=Part.Line(fp.Poles[i-20],fp.Poles[i-14])
		for i in range(32,38):
			Legs[i]=Part.Line(fp.Poles[i-20],fp.Poles[i-14])
		fp.Legs=Legs
		fp.Shape = Part.Shape(fp.Legs)


###################################################################################################
# CubicCurve_4
class CubicCurve_4:
	def __init__(self, obj , poly):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nCubicCurve_4 class Init\n")
		obj.addProperty("App::PropertyLink","Poly","CubicCurve_4","control polygon").Poly = poly
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		# get the poles list from the poly. legacy shape function wants 'homogeneous' coords as [[x,y,z],w]
		WeightedPoles=[[fp.Poly.Poles[0],fp.Poly.Weights[0]],
				[fp.Poly.Poles[1],fp.Poly.Weights[1]],
				[fp.Poly.Poles[2],fp.Poly.Weights[2]],
				[fp.Poly.Poles[3],fp.Poly.Weights[3]]]
		# the legacy function below sets the degree and knot vector
		fp.Shape = Bezier_Cubic_curve(WeightedPoles).toShape()

# CubicCurve_6
class CubicCurve_6:
	def __init__(self, obj , poly):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nCubicCurve_6 class Init\n")
		obj.addProperty("App::PropertyLink","Poly","CubicCurve_6","control polygon").Poly = poly
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		# get the poles list from the poly. legacy shape function wants 'homogeneous' coords as [[x,y,z],w]
		WeightedPoles=[[fp.Poly.Poles[0],fp.Poly.Weights[0]],
				[fp.Poly.Poles[1],fp.Poly.Weights[1]],
				[fp.Poly.Poles[2],fp.Poly.Weights[2]],
				[fp.Poly.Poles[3],fp.Poly.Weights[3]],
				[fp.Poly.Poles[4],fp.Poly.Weights[4]],
				[fp.Poly.Poles[5],fp.Poly.Weights[5]]]
		# the legacy function below sets the degree and knot vector
		fp.Shape = NURBS_Cubic_6P_curve(WeightedPoles).toShape()

###########################     Curve linked / derived control polygons   ###########################
# ControlPoly6_Bezier
class ControlPoly6_Bezier:
	def __init__(self, obj , cubiccurve4_0):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nControlPoly6_Bezier class Init\n")
		obj.addProperty("App::PropertyLink","Sketch","ControlPoly6_Bezier","reference Bezier Curve").CubicCurve4_0 = cubiccurve4_0
		obj.addProperty("Part::PropertyGeometryList","Legs","ControlPoly6_Bezier","control segments").Legs
		obj.addProperty("App::PropertyVectorList","Poles","ControlPoly6_Bezier","Poles").Poles
		obj.addProperty("App::PropertyFloatList","Weights","ControlPoly6_Bezier","Weights").Weights = [1.0,1.0,1.0,1.0]
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		# process the sketch arc...error check later
		curve=fp.fp.CubicCurve4_0.Shape
		curve.increaseDegree(3)
		start=curve.FirstParameter
		end=curve.LastParameter
		knot1=start+(end-start)/3.0
		knot2=end-(end-start)/3.0
		curve.insertKnot(knot1)
		curve.insertKnot(knot2)
		p0=curve.getPole(1)
		p1=curve.getPole(2)
		p2=curve.getPole(3)
		p3=curve.getPole(4)
		p4=curve.getPole(5)
		p5=curve.getPole(6)
		fp.Poles=[p0,p1,p2,p3,p4,p5]
		# set the weights
		fp.Weights = curve.getWeights()
		# prepare the lines to draw the polyline
		Leg0=Part.Line(p0,p1)
		Leg1=Part.Line(p1,p2)
		Leg2=Part.Line(p2,p3)
		Leg3=Part.Line(p3,p4)
		Leg4=Part.Line(p4,p5)
		#set the polygon legs property
		fp.Legs=[Leg0, Leg1, Leg2, Leg3, Leg4]
		# define the shape for visualization
		fp.Shape = Part.Shape(fp.Legs)

# ControlPoly6_FilletBezier(CubicCurve4_0,CubicCurve4_1)
class ControlPoly6_FilletBezier:
	def __init__(self, obj , cubiccurve4_0, cibiccurve4_1):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nControlPoly6_FilletBezier class Init\n")
		obj.addProperty("App::PropertyLink","Sketch","ControlPoly6_FilletBezier","First reference Bezier Curve").CubicCurve4_0 = cubiccurve4_0
		obj.addProperty("App::PropertyLink","Sketch","ControlPoly6_FilletBezier","Second reference Bezier Curve").CubicCurve4_1 = cubiccurve4_1
		obj.addProperty("App::PropertyFloat","Scale_0","ControlPoly6_FilletBezier","First curve tangent scaling").Scale_1 = 2.0
		obj.addProperty("App::PropertyFloat","Scale_4","ControlPoly6_FilletBezier","Second curve tangent scaling").Scale_4 = 2.0
		obj.addProperty("App::PropertyFloat","Scale_1","ControlPoly6_FilletBezier","First curve inner scaling").Scale_2 = 2.0
		obj.addProperty("App::PropertyFloat","Scale_1","ControlPoly6_FilletBezier","Second curve inner scaling").Scale_3 = 2.0
		obj.addProperty("Part::PropertyGeometryList","Legs","ControlPoly6_FilletBezier","control segments").Legs
		obj.addProperty("App::PropertyVectorList","Poles","ControlPoly6_FilletBezier","Poles").Poles
		obj.addProperty("App::PropertyFloatList","Weights","ControlPoly6_FilletBezier","Weights").Weights = [1.0,1.0,1.0,1.0]
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		cubiccurve6_0=cubiccurve4_0.copy() # make copy to keep original selection intact
		cubiccurve6_0.insertKnot(1.0/3.0) # add knots to convert bezier to 6P
		cubiccurve6_0.insertKnot(2.0/3.0)

		cubiccurve6_1=cubiccurve4_1.copy() # make copy to keep original selection intact
		cubiccurve6_1.insertKnot(1.0/3.0) # add knots to convert bezier to 6P
		cubiccurve6_1.insertKnot(2.0/3.0)

		# get all poles and weights
		poles_0=NURBS_6P_0.getPoles()
		weights_0=NURBS_6P_0.getWeights()
		poles_1=NURBS_6P_1.getPoles()
		weights_1=NURBS_6P_1.getWeights()

		# get all start/end points of the curves to determine how they are connected. 
		p00 = curve_0.StartPoint
		p01 = curve_0.EndPoint
		p10 = curve_1.StartPoint
		p11 = curve_1.EndPoint

		# reorder so control points flow from first curve into second curve. this is analogous to orient_a_to_b()
		# the 'fillet' CubicCurve6 will be built based on the first three control points of the first curve, 
		# and the last three control points of the second curve (after they are oriented correctly). 
		# This allows start and end curvature control.

		corner='none'
		if p00==p10: 
			p0=[poles_0[5],weights_0[5]]
			p1=[poles_0[4],weights_0[4]]
			p2=[poles_0[3],weights_0[3]]
			p3=[poles_1[3],weights_0[3]]
			p4=[poles_1[4],weights_0[4]]
			p5=[poles_1[5],weights_0[5]]
			corner=p00p10
		
		if p00==p11:
			p0=[poles_0[5],weights_0[5]]
			p1=[poles_0[4],weights_0[4]]
			p2=[poles_0[3],weights_0[3]]
			p3=[poles_1[2],weights_0[2]]
			p4=[poles_1[1],weights_0[1]]
			p5=[poles_1[0],weights_0[0]]
			corner=p00p11
		
		if p01==p10:
			p0=[poles_0[0],weights_0[0]]
			p1=[poles_0[1],weights_0[1]]
			p2=[poles_0[2],weights_0[2]]
			p3=[poles_1[3],weights_0[3]]
			p4=[poles_1[4],weights_0[4]]
			p5=[poles_1[5],weights_0[5]]
			corner=p01p10
		
		if p01==p11:
			p0=[poles_0[0],weights_0[0]]
			p1=[poles_0[1],weights_0[1]]
			p2=[poles_0[2],weights_0[2]]
			p3=[poles_1[2],weights_0[2]]
			p4=[poles_1[1],weights_0[1]]
			p5=[poles_1[0],weights_0[0]]
			corner=p01p11

		# print warning if input curves do not join at a 'corner'		
		if corner=='none':
			print 'bezier blend/fillet only works if the curves are connected end to end'
		#no further error handling is implemented

		# at this stage, these poles are clustered around the curve start and end of the final curve.
		# They need to get 'spread out' a bit
		
		#### find start/end curvatures, scale start and end tangents, then reposition innermost control points to maintain curvature. 
		#### set the height to the tangent, but leave the length along the tangent as numeric input. what to use for a start value?
		
		############## rewrite checkpoint
		
		### calculate curvature components
		## start point
		l0 = p1[0]-p0[0]					# first control leg
		tan0=Base.Vector(l0)				# make clean copy
		tan0.normalize()					# unit tangent direction
		l1=Base.Vector(tan0)				# make clean copy
		l1.multiply(tan0.dot(p2[0]-p1[0])) 	# scalar projection of second control leg along unit tangent
		h1=(p2[0]-p1[0])-l1					# height of second control leg orthogonal to tangent
		## end point
		l4 = p4[0]-p5[0]					# last control leg
		tan4=Base.Vector(l4)				# make clean copy
		tan4.normalize()					# unit tangent direction
		l3=Base.Vector(tan4)				# make clean copy
		l3.multiply(tan4.dot(p3[0]-p4[0])) 	# scalar projection of second to last control leg along unit tangent
		h3=(p3[0]-p4[0])-l3					# height of second control leg orthogonal to tangent
		
		### scale first and last control legs
		L0=Base.Vector(l0)					# make clean copy
		L0.multiply(Scale_1)				# apply tangent scale
		p1_scl = [p0[0] + L0, p1[1]]		# reposition second control point
		
		L4=Base.Vector(l4)					# make clean copy
		L4.multiply(Scale_4)				# apply tangent scale
		p4_scl = [p5[0] + L4, p4[1]]		# reposition fifth control point
		
		### calc new heights for inner control legs
		H1 = Base.Vector(h1)				# make clean copy
		H1.multiply(Scale_1.__pow__(2))		# apply height scale
		
		H3 = Base.Vector(h3)				# make clean copy
		H3.multiply(Scale_4.__pow__(2))		# apply height scale
		
		L1 = Base.Vector(l1) 				# make clean copy
		L1 = L1.multiply(Scale_2)			# apply inner tangent scale
		p2_scl = [p1[0] + H1 + L1, p2[1]]	# reposition third control point
				
		L3 = Base.Vector(l3) 				# make clean copy
		L3 = L3.multiply(Scale_3)			# apply inner tangent scale
		p3_scl = [p4[0] + H3 + L3, p3[1]]	# reposition third control point
		
		
		fp.Poles=[p0[0], p1_scl, p2_scl, p3_scl, p4_scl, p5[0]]
		# set the weights. No scaling at this point. No idea what happens if one of the input curve is an arc.
		# it would probably be a mess, since the curvature formulas above do not incorporate weights yet.
		fp.Weights = [p0[1], p1[1], p2[1], p3[1], p4[1], p5[1]]
		# prepare the lines to draw the polyline
		Leg0=Part.Line(p0,p1_scl)
		Leg1=Part.Line(p1_scl,p2_scl)
		Leg2=Part.Line(p2_scl,p3_scl)
		Leg3=Part.Line(p3_scl,p4_scl)
		Leg4=Part.Line(p4_scl,p5_scl)
		#set the polygon legs property
		fp.Legs=[Leg0, Leg1, Leg2, Leg3, Leg4]
		# define the shape for visualization
		fp.Shape = Part.Shape(fp.Legs)



###################################################################################################

# CubicSurface_44

class CubicSurface_44:
	def __init__(self, obj , grid):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nCubicSurface_44 class Init\n")
		obj.addProperty("App::PropertyLink","Grid","CubicSurface_44","control grid").Grid = grid
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		# get the poles list from the poly. legacy shape function wants 'homogeneous' coords as [[x,y,z],w]
		WeightedPoles=[
			[fp.Grid.Poles[0],fp.Grid.Weights[0]],
			[fp.Grid.Poles[1],fp.Grid.Weights[1]],
			[fp.Grid.Poles[2],fp.Grid.Weights[2]],
			[fp.Grid.Poles[3],fp.Grid.Weights[3]],
			[fp.Grid.Poles[4],fp.Grid.Weights[4]],
			[fp.Grid.Poles[5],fp.Grid.Weights[5]],
			[fp.Grid.Poles[6],fp.Grid.Weights[6]],
			[fp.Grid.Poles[7],fp.Grid.Weights[7]],
			[fp.Grid.Poles[8],fp.Grid.Weights[8]],
			[fp.Grid.Poles[9],fp.Grid.Weights[9]],
			[fp.Grid.Poles[10],fp.Grid.Weights[10]],
			[fp.Grid.Poles[11],fp.Grid.Weights[11]],
			[fp.Grid.Poles[12],fp.Grid.Weights[12]],
			[fp.Grid.Poles[13],fp.Grid.Weights[13]],
			[fp.Grid.Poles[14],fp.Grid.Weights[14]],
			[fp.Grid.Poles[15],fp.Grid.Weights[15]]]
		# the legacy function below sets the degree and knot vector
		fp.Shape = Bezier_Bicubic_surf(WeightedPoles).toShape()


class CubicSurface_66:
	def __init__(self, obj , grid):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nCubicSurface_66 class Init\n")
		obj.addProperty("App::PropertyLink","Grid","CubicSurface_66","control grid").Grid = grid
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		# get the poles list from the poly. legacy shape function wants 'homogeneous' coords as [[x,y,z],w]
		WeightedPoles=[
			[fp.Grid.Poles[0],fp.Grid.Weights[0]],
			[fp.Grid.Poles[1],fp.Grid.Weights[1]],
			[fp.Grid.Poles[2],fp.Grid.Weights[2]],
			[fp.Grid.Poles[3],fp.Grid.Weights[3]],
			[fp.Grid.Poles[4],fp.Grid.Weights[4]],
			[fp.Grid.Poles[5],fp.Grid.Weights[5]],
			[fp.Grid.Poles[6],fp.Grid.Weights[6]],
			[fp.Grid.Poles[7],fp.Grid.Weights[7]],
			[fp.Grid.Poles[8],fp.Grid.Weights[8]],
			[fp.Grid.Poles[9],fp.Grid.Weights[9]],
			[fp.Grid.Poles[10],fp.Grid.Weights[10]],
			[fp.Grid.Poles[11],fp.Grid.Weights[11]],
			[fp.Grid.Poles[12],fp.Grid.Weights[12]],
			[fp.Grid.Poles[13],fp.Grid.Weights[13]],
			[fp.Grid.Poles[14],fp.Grid.Weights[14]],
			[fp.Grid.Poles[15],fp.Grid.Weights[15]],
			[fp.Grid.Poles[16],fp.Grid.Weights[16]],
			[fp.Grid.Poles[17],fp.Grid.Weights[17]],
			[fp.Grid.Poles[18],fp.Grid.Weights[18]],
			[fp.Grid.Poles[19],fp.Grid.Weights[19]],
			[fp.Grid.Poles[20],fp.Grid.Weights[20]],
			[fp.Grid.Poles[21],fp.Grid.Weights[21]],
			[fp.Grid.Poles[22],fp.Grid.Weights[22]],
			[fp.Grid.Poles[23],fp.Grid.Weights[23]],
			[fp.Grid.Poles[24],fp.Grid.Weights[24]],
			[fp.Grid.Poles[25],fp.Grid.Weights[25]],
			[fp.Grid.Poles[26],fp.Grid.Weights[26]],
			[fp.Grid.Poles[27],fp.Grid.Weights[27]],
			[fp.Grid.Poles[28],fp.Grid.Weights[28]],
			[fp.Grid.Poles[29],fp.Grid.Weights[29]],
			[fp.Grid.Poles[30],fp.Grid.Weights[30]],
			[fp.Grid.Poles[31],fp.Grid.Weights[31]],
			[fp.Grid.Poles[32],fp.Grid.Weights[32]],
			[fp.Grid.Poles[33],fp.Grid.Weights[33]],
			[fp.Grid.Poles[34],fp.Grid.Weights[34]],
			[fp.Grid.Poles[35],fp.Grid.Weights[35]]]
		# the legacy function below sets the degree and knot vector
		fp.Shape = NURBS_Cubic_66_surf(WeightedPoles).toShape()

class CubicSurface_64:
	def __init__(self, obj , grid):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nCubicSurface_64 class Init\n")
		obj.addProperty("App::PropertyLink","Grid","CubicSurface_64","control grid").Grid = grid
		obj.Proxy = self

	def execute(self, fp):
		'''Do something when doing a recomputation, this method is mandatory'''
		# get the poles list from the poly. legacy shape function wants 'homogeneous' coords as [[x,y,z],w]
		WeightedPoles=[
			[fp.Grid.Poles[0],fp.Grid.Weights[0]],
			[fp.Grid.Poles[1],fp.Grid.Weights[1]],
			[fp.Grid.Poles[2],fp.Grid.Weights[2]],
			[fp.Grid.Poles[3],fp.Grid.Weights[3]],
			[fp.Grid.Poles[4],fp.Grid.Weights[4]],
			[fp.Grid.Poles[5],fp.Grid.Weights[5]],
			[fp.Grid.Poles[6],fp.Grid.Weights[6]],
			[fp.Grid.Poles[7],fp.Grid.Weights[7]],
			[fp.Grid.Poles[8],fp.Grid.Weights[8]],
			[fp.Grid.Poles[9],fp.Grid.Weights[9]],
			[fp.Grid.Poles[10],fp.Grid.Weights[10]],
			[fp.Grid.Poles[11],fp.Grid.Weights[11]],
			[fp.Grid.Poles[12],fp.Grid.Weights[12]],
			[fp.Grid.Poles[13],fp.Grid.Weights[13]],
			[fp.Grid.Poles[14],fp.Grid.Weights[14]],
			[fp.Grid.Poles[15],fp.Grid.Weights[15]],
			[fp.Grid.Poles[16],fp.Grid.Weights[16]],
			[fp.Grid.Poles[17],fp.Grid.Weights[17]],
			[fp.Grid.Poles[18],fp.Grid.Weights[18]],
			[fp.Grid.Poles[19],fp.Grid.Weights[19]],
			[fp.Grid.Poles[20],fp.Grid.Weights[20]],
			[fp.Grid.Poles[21],fp.Grid.Weights[21]],
			[fp.Grid.Poles[22],fp.Grid.Weights[22]],
			[fp.Grid.Poles[23],fp.Grid.Weights[23]]]
		# the legacy function below sets the degree and knot vector
		fp.Shape = NURBS_Cubic_64_surf(WeightedPoles).toShape()

