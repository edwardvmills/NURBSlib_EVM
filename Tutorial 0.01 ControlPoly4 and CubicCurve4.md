
# Tutorial 0.01
##ControlPoly4 and CubicCurve4 macros in NURBSlib_EVM

[return to main page](http://edwardvmills.github.io/NURBSlib_EVM/)

### Target audience for this specific tutorial / presentation
This 'tutorial' is meant to give a glimpse of the NURBSlib_EVM _library_ to knowledgable users of FreeCAD. No explanations of basic FreeCAD actions are provided at this time.

As a library, NURBSlib_EVM provides basic elements that _can_ be used to produce models, but are not streamlined. Some steps in this tutorial will feel repetitive. They can be automated, and they will be automated eventually, in the form of a workbench. At this time, priority is given to stability and versatility of the objects. The interface is minimal, Spartan even. This is not necessarily a bad thing.

### Requirements to follow this tutorial / presentation
* ability to set up a macro in [FreeCAD](http://www.freecadweb.org/) 0.17 is required (Part.Line vs Part.LineSegment deprecation warning is fatal in 0.16)
* ability to create sketches of lines and arcs in FreeCAD
* an understanding of the three basic planes in FreeCAD
* having at least a vague notion of NURBS or Bezier curves, such as found in Inkscape or Illustrator is very helpful

### Specific investment of time required:
* 15 minutes to read this page and get an idea of what you might get out of it
* download three files from this repository (5 files if you want icons)
* set up two FreeCAD macros
* 30 minutes to follow the tutorial, up to two hours to examine most variations

### Motivation? It will take a few tutorials, but here is the goal:
![target](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/development_FC_models/parametric/begin%20transition%20to%200.17/Bezier%20primary%20Surface%20Volume%2066-07.bmp.png?raw=true)
The specific element of interest in the picture above is the fairly smooth blending of three main surfaces at the front top corner. There is a large 'blending radius' between the top and narrow front surface, and a sharp 'blending radius' between the wide side surface and the first two. These radii are controlled parametrically, and the seams are 95% curvature continuous. There are some known flaws as well, but let's focus on the positive for now!


### Setup ControlPoly4 and CubicCurve4:
from [master](https://github.com/edwardvmills/NURBSlib_EVM) /NURBSlib_EVM_python, copy:
* NURBSlib_EVM.py
* ControlPoly4.FCMacro
* CubicCurve4.FCMacro

from [master](https://github.com/edwardvmills/NURBSlib_EVM) /

Optional: from [master](https://github.com/edwardvmills/NURBSlib_EVM) /icons, copy:
* ControlPoly4.svg
* CubicCurve4.svg

Place them in your FreCAD macro folder (and a suitable icon folder)

In FreeCAD, set up macros for ControlPoly4 and CubicCurve4. Wherever you do put them, add the Sketcher workbench 'Create a new sketch' button close by. All sketches in this tutorial must be from Sketcher workbench, not PartDesign workbench.

### Usage
####-1-



![01](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_01%20A%20sketch%20of%20three%20lines%20connected%20end%20to%20end.png?raw=true)
