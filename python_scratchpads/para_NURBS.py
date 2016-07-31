from __future__ import division # allows floating point division from integers
import FreeCAD, Part, math
from FreeCAD import Base
from FreeCAD import Gui
import NURBSlib_EVM as Nl
 
"""
# first prototype parametric NURBS cubic bezier curve
# works only for single sketch containing three lines (the lines SHOULD be connected end to end, but this is NOT enforced)
class cubicBezier:
	def __init__(self, obj , sketch):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\ncubicBezier class Init\n")
		obj.addProperty("App::PropertyLink","Sketch","cubicBezier","reference Sketch").Sketch = sketch
		obj.Proxy = self

	def execute(self, fp):
		'''Print a short message when doing a recomputation, this method is mandatory'''
		p00=fp.Sketch.Geometry[0].StartPoint
		p01=fp.Sketch.Geometry[0].EndPoint
		p10=fp.Sketch.Geometry[1].StartPoint
		p11=fp.Sketch.Geometry[1].EndPoint
		p20=fp.Sketch.Geometry[2].StartPoint
		p21=fp.Sketch.Geometry[2].EndPoint
		poles = [[p00,1],[p10,1],[p20,1],[p21,1]]
		fp.Shape = Nl.Bezier_Cubic_curve(poles).toShape()
"""

# first prototype NURBS curve control polygon object.
# works only for single sketch containing three lines (the lines SHOULD be connected end to end, but this is NOT enforced)
class Poly_3L:
	def __init__(self, obj , sketch):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nPoly_3L class Init\n")
		obj.addProperty("App::PropertyLink","Sketch","Poly_3L","reference Sketch").Sketch = sketch
		obj.addProperty("Part::PropertyGeometryList","Legs","Poly_3L","reference Sketch").Legs

		obj.Proxy = self

	def execute(self, fp):
		'''Print a short message when doing a recomputation, this method is mandatory'''
		p00=fp.Sketch.Geometry[0].StartPoint
		p01=fp.Sketch.Geometry[0].EndPoint
		p10=fp.Sketch.Geometry[1].StartPoint
		p11=fp.Sketch.Geometry[1].EndPoint
		p20=fp.Sketch.Geometry[2].StartPoint
		p21=fp.Sketch.Geometry[2].EndPoint
		Leg0=Part.Line(p00,p01)
		Leg1=Part.Line(p10,p11)
		Leg2=Part.Line(p20,p21)
		#if (p01==p10) and (p11==p20):
		fp.Legs=[Leg0, Leg1, Leg2]
		fp.Shape = Part.Shape(fp.Legs)

# second prototype NURBS curve control polygon object.
# GOAL: receive 2 node sketches as input, and for each sketch: 
# identify the circle > get the center (poly end point)
# identify the line > get the point that does not match the center (poly inner point)
# form the control polygon as [center1, inner1, inner2, center 2]
class Poly_2N:
	def __init__(self, obj , sketch0, sketch1):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nPoly_2N class Init\n")
		obj.addProperty("App::PropertyLink","Sketch0","Poly_2N","reference Sketch").Sketch0 = sketch0
		obj.addProperty("App::PropertyLink","Sketch1","Poly_2N","reference Sketch").Sketch1 = sketch1
		obj.addProperty("Part::PropertyGeometryList","Legs","Poly_2N","reference Sketch").Legs

		obj.Proxy = self

	def execute(self, fp):
		'''Print a short message when doing a recomputation, this method is mandatory'''
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
		p00=cir0.Center
		if lin0.StartPoint==p00:
			p01=lin0.EndPoint
		elif lin0.EndPoint==p00:
			p01=lin0.StartPoint
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
		p11=cir1.Center
		if lin1.StartPoint==p11:
			p10=lin1.EndPoint
		elif lin1.EndPoint==p11:
			p10=lin1.StartPoint
		# prepare the polygon
		Leg0=Part.Line(p00,p01)
		Leg1=Part.Line(p01,p10)
		Leg2=Part.Line(p10,p11)
		#set the polygon legs property
		fp.Legs=[Leg0, Leg1, Leg2]
		# define the shape
		fp.Shape = Part.Shape(fp.Legs)


# second prototype parametric NURBS cubic bezier curve
# link a Poly_3L or Poly_2N into the NURBS curve
class cubicBezier:
	def __init__(self, obj , poly):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\ncubicBezier class Init\n")
		obj.addProperty("App::PropertyLink","Poly","cubicBezier","control polygon").Poly = poly
		obj.Proxy = self

	def execute(self, fp):
		'''Print a short message when doing a recomputation, this method is mandatory'''
		p00=fp.Poly.Legs[0].StartPoint
		p01=fp.Poly.Legs[0].EndPoint
		p20=fp.Poly.Legs[2].StartPoint
		p21=fp.Poly.Legs[2].EndPoint
		poles = [[p00,1],[p01,1],[p20,1],[p21,1]]
		fp.Shape = Nl.Bezier_Cubic_curve(poles).toShape()

# first prototype parametric control grid
# link 4 control polys into one grid
class ControlPoly44:
	def __init__(self, obj , poly0, poly1, pol2, poly3):
		''' Add the properties '''
		FreeCAD.Console.PrintMessage("\nControlPoly44 class Init\n")
		obj.addProperty("App::PropertyLink","Poly0","cubicBezier","control polygon").Poly0 = poly0
		obj.addProperty("App::PropertyLink","Poly1","cubicBezier","control polygon").Poly1 = poly1
		obj.addProperty("App::PropertyLink","Poly2","cubicBezier","control polygon").Poly2 = poly2
		obj.addProperty("App::PropertyLink","Poly3","cubicBezier","control polygon").Poly3 = poly3
		obj.Proxy = self





















