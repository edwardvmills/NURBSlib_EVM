# Tutorial 0.02
##ControlGrid44 and CubicSurface44 macros in NURBSlib_EVM

[return to main page](http://edwardvmills.github.io/NURBSlib_EVM/)

### Target audience for this specific tutorial
This 'tutorial' is meant to give a glimpse of the NURBSlib_EVM _library_ to knowledgable users of FreeCAD. No explanations of basic FreeCAD actions are provided at this time. I will spend a little extra effort on the amazing Attachment Editor of FreeCAD as it relates to sketches used for surface modeling. 

### Requirements to follow this tutorial
* [Tutorial 0.01](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.01%20ControlPoly4%20and%20CubicCurve4.md) completed (especially the setup portion)
* ability to set up a macro in [FreeCAD](http://www.freecadweb.org/) 0.17 is required (Part.Line vs Part.LineSegment deprecation warning is fatal in 0.16)
* ability to create sketches of lines and arcs in FreeCAD
* an understanding of the three basic planes in FreeCAD
* having at least a vague notion of NURBS or Bezier curves, such as found in Inkscape or Illustrator is very helpful

### Specific investment of time required:
* 15 minutes to read this page and get an idea of what you might get out of it
* download three files from this repository (5 files if you want icons)
* set up two FreeCAD macros
* 10 minutes to follow the tutorial, up to one hour to examine most variations
* Hypnosis warning, 3D sketching is dangerously fun

### Setup ControlGrid44 and CubicSurface44:
from [master](https://github.com/edwardvmills/NURBSlib_EVM) /NURBSlib_EVM_python, copy:
* ControlGrid44.FCMacro
* CubicSurface44.FCMacro

from [master](https://github.com/edwardvmills/NURBSlib_EVM) /NURBSlib_EVM_python, copy:
* ControlGrid44.FCMacro
* CubicSurface44.FCMacro

Optional: from [master](https://github.com/edwardvmills/NURBSlib_EVM) /icons, copy:
* ControlGrid44.svg
* CubicSurface44.svg

Place them in your FreCAD macro folder (and a suitable icon folder)

In FreeCAD, set up macros for ControlGrid44 and ControlGrid44.

All Sketches _must_ be Sketcher Workbench sketches, not  Part Design workbench. refer to [Tutorial 0.01](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.01%20ControlPoly4%20and%20CubicCurve4.md)

### Usage
####-1-
In FreeCAD, open a new document. Draw a sketch with 3 lines connected end to end. Nothing else should be in the sketch (for now). 
![01](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_01%20A%20sketch%20of%20three%20lines%20connected%20end%20to%20end.png?raw=true)
####-2-
Select the 3 line sketch and click the ControlPoly4 macro
![02](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/ControlPoly4.png?raw=true)

This creates a ControlPoly4_3L object in the document. Note the '_3L_' suffix. This is one of several different flavors of the ControlPoly4 category of objects
![03](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_03%20ControlPoly4_3L%20object.png?raw=true)

In the case of the three line sketch, the ControlPoly4_3L object is hidden by the sketch itself. Hide the sketch to see it directly if you wish.

In the Data Tab, you can see two parameters:
* Sketch - this was the input selection, and it can be remapped to another sketch (also of exactly three lines end-to-end)
* Weights - we'll talk about this again in a moment      

It's not very interesting yet, so let's keep moving to next step!


