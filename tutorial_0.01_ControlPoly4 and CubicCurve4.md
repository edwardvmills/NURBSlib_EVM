
# Tutorial 0.01
##ControlPoly4 and CubicCurve4 macros in NURBSlib_EVM

[return to main page](http://edwardvmills.github.io/NURBSlib_EVM/)

This 'tutorial' is meant to give a glimpse of the NURBSlib_EVM _library_. This is not a FreeCAD tutorial.

As a library, NURBSlib_EVM provides basic elements that _can_ be used to produce models, but are not streamlined. Some steps in this tutorial will feel repetitive. They _can_ be automated, and they _will_ be automated eventually, however, _at this time_, priority is given to stability and versatility of the objects

### Target audience for this specific tutorial
* Triplus 
* Microelly2
* Chris_G if he's curious
* anyone else who wants to, of course.

### Requirements to follow this presentation:
* ability to set up a macro in [FreeCAD](http://www.freecadweb.org/) 0.17 is required (Part.Line vs Part.LineSegment deprecation warning is fatal in 0.16)
* ability to create sketches of lines and arcs in FreeCAD
* an understanding of the three basic planes in FreeCAD

### Specific investment of time required:
* download three files from this repositiory (5 files if you want icons)
* set up two FreeCAD macros
* 5 minutes to read this page

### motivation? It will take a few tutorials, but here is the end result:
![target](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/development_FC_models/parametric/begin%20transition%20to%200.17/Bezier%20primary%20Surface%20Volume%2066-07.bmp.png?raw=true)


### Setup ControlPoly4 and CubicCurve4:
from [master](https://github.com/edwardvmills/NURBSlib_EVM) /NURBSlib_EVM_python, copy:
* NURBSlib_EVM.py
* ControlPoly4.FCMacro
* CubicCurve4.FCMacro

Optional: from [master](https://github.com/edwardvmills/NURBSlib_EVM) /icons, copy:
* ControlPoly4.svg
* CubicCurve4.svg

Place them in your FreCAD macro folder (and a suitable icon folder)

In FreeCAD, set up macros for ControlPoly4 and CubicCurve4.

### Usage

In FreeCAD, open a new document. Draw a sketch with 3 lines connected end to end. Nothing else should be in the sketch (for now)
![01](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_01%20A%20sketch%20of%20three%20lines%20connected%20end%20to%20end.png?raw=true)

Select the 3 line sketch and click the ControlPoly4 macro
![02](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/ControlPoly4.png?raw=true)

This creates a ControlPoly4_3L object in the document. Note the '_3L_' suffix. This is one of several different flavors of the ControlPoly4 category of objects
![03](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_03%20ControlPoly4_3L%20object.png?raw=true)

In the Data Tab, you can see two parameters:
* Sketch - this was the input selection, and it can be remapped to another sketch (also of exactly three lines end-to-end)
* Weights - we'll talk about this again in a moment

Select the ControlPoly_3L object and click the CubicCurve4 macro
![04](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/CubicCurve4.png?raw=true)

This creates a CubicCurve4 object in the document.
![05](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_05%20CubicCurve4%20object.png?raw=true)

In the Data Tab, you can see a single parameter:
* Poly = ControlPoly4_3L. this was the input selection, and it can be remapped to _any ControlPoly4_ object (of which there are 3 varieties at this time)

Why isn't the curve directly mapped to the sketch? The weights could just be a property of the curve object, couldn't they? In fact i used to have it set up in that way, but i chose to separate the _Control Polygons_ from the NURBS objects _as much as possible_.  
Here's why:
* Sometimes we need a polygon, but have no itention of calculating the NURBS curve.
* Many properties of the NURBS can be determined directly from the polygon. These can be used to build other polygons.
* Calculating curves and surfaces we don't need limits how much we can build before FreeCAD overloads and crashes.
* I could spend a long time learning to nest objects inside of each other, but FreeCAD is not completely consistent as it is, and i'm not sure i even know _yet_ what the best nesting strategy is (i am aware of several competing methods).
* in the meantime, i have complete freedom to name all the objects and organize them in folders as i like. It is actually really annoying when FreeCAD moves stuff around (for example when mirroring a surface)


