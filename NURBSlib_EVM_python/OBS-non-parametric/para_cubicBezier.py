from __future__ import division # allows floating point division from integers
import FreeCAD, Part, math
from FreeCAD import Base
from FreeCAD import Gui
import NURBSlib_EVM as Nl
import para_NURBS as pN


poly=Gui.Selection.getSelection()[0]
a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","cubicBezier")
pN.cubicBezier(a,poly)
a.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
FreeCAD.ActiveDocument.recompute()
