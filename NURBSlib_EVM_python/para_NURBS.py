from __future__ import division # allows floating point division from integers
import FreeCAD, Part, math
from FreeCAD import Base
from FreeCAD import Gui
import NURBSlib_EVM as Nl
 
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

