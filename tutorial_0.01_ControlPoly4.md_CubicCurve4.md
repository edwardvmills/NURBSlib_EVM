
# Presentation 0.01
##ControlPoly4 and CubicCurve4 macros in NURBSlib_EVM

[return to main page](http://edwardvmills.github.io/NURBSlib_EVM/)

This 'tutorial' is meant to give a glimpse of the NURBSlib_EVM _library

### Requirements to follow this presentation:
* ability to set up a macro in [FreeCAD](http://www.freecadweb.org/)
* ability to create sketches of lines and arcs in FreeCAD
* an understanding of the three basic planes in FreeCAD

### Specific investment of time required:
* download three files from this repositiory
* set up two FreeCAD macros
* 5 minutes to read this pages


### ControlPoly4 and CubicCurve4:
from [master](https://github.com/edwardvmills/NURBSlib_EVM) /NURBSlib_EVM_python, copy:
* NURBSlib_EVM.py
* ControlPoly4.FCMacro
* CubicCurve4.FCMacro

Place them in your FreCAD macro folder

In FreeCAD. set up macros for ControlPoly4 and CubicCurve4.

right now the icon names do not match the macro names. Ignore the icons folder. Sorry. Only two macros are used in this presentation so i think we'll survive.

* In FreeCAd, open a new document. Draw a sketch with 3 lines connected end to end. 3 lines.
![01](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_01%20A%20sketch%20of%20three%20lines%20connected%20end%20to%20end.png?raw=true)

* Select the 3 line sketch and click the ControlPoly4 macro
![02](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_02%20run%20ControlPoly4%20macro%20on%20sketch%20of%20three%20lines.png?raw=true)

* This creates a cControlPoly4_3L object in the document
![03](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_03%20ControlPoly4_3L%20object.png?raw=true)