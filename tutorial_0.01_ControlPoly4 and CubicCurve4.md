
# Tutorial 0.01
##ControlPoly4 and CubicCurve4 macros in NURBSlib_EVM

[return to main page](http://edwardvmills.github.io/NURBSlib_EVM/)

### Target audience for this specific tutorial / presentation
* Triplus 
* Microelly2
* Chris_G if he's curious
* anyone else who wants to, of course, but it'll be hard to follow without context.

This 'tutorial' is meant to give a glimpse of the NURBSlib_EVM _library_ to knoledgable users of FreeCAD. No explanations of basic FreeCAD actions is provided at this time.

As a library, NURBSlib_EVM provides basic elements that _can_ be used to produce models, but are not streamlined. Some steps in this tutorial will feel repetitive. They can be automated, and they will be automated eventually, in the form of a workbench. At this time, priority is given to stability and versatility of the objects. The interface is minimal, Spartan even.

### Requirements to follow this presentation:
* ability to set up a macro in [FreeCAD](http://www.freecadweb.org/) 0.17 is required (Part.Line vs Part.LineSegment deprecation warning is fatal in 0.16)
* ability to create sketches of lines and arcs in FreeCAD
* an understanding of the three basic planes in FreeCAD

### Specific investment of time required:
* 5 minutes to read the page
* download three files from this repositiory (5 files if you want icons)
* set up two FreeCAD macros
* 20 minutes to to follow the tutorial, up to two hours to examine most variations

### Motivation? It will take a few tutorials, but here is the goal:
![target](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/development_FC_models/parametric/begin%20transition%20to%200.17/Bezier%20primary%20Surface%20Volume%2066-07.bmp.png?raw=true)
The specific element of interest in the picture above is the fairly smooth blending of three main surfaces at the front top corner.


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

-hold here while editing- Below are the rest of the pictures for the tutorial, i will complete the step descriptions ASAP, thanks for reading!

Now that we have a CubicCurve4 attached to the ControlPoly4, let's go back to the ControlPoly4 object and examine the weight controls.

In the data tab of the polygon, the weights are displayed as a list with default values [1,1,1,1]. Hitting the ... button on the right side of the list opens up a very simple list editor window. 
![06](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_06%20the%20weight%20list%20of%20all%20ControlPoly4%20objects.png?raw=true)

In this window, change one of the weights. Hit OK to close the editor window
![07](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_07%20editing%20a%20specific%20weight%20of%20the%20ControlPoly4%20object.png?raw=true)

Hit F5 to recompute the model. In the case shown in the picture, raising the weights from 1.0 to 4.0 for the second pole causes the curve to be drawn towards the second pole.
![08](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_08%20the%20CubicCurve4%20object%20updates%20to%20the%20modified%20ControlPoly4%20weight.png?raw=true)
The weights can be used to influence the model directly, but it is not recommended as a basic modeling strategy. The primary function of the weights is to allow exact conversion of arcs of cricles (and ellipses and other conics). This is done automatically and generally shouldn't be messed with. The mechanism is exposed here to present the python object model.


Start a new sketch on the xy plane. Draw 1 circle and 1 line. The line must have one point (end point or start point) exactly on the circle center. Do not put anything else in the sketch.
![09](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_09%20a%20single%20Node%20sketch%20on%20xy.png?raw=true)
This type sketch is called a _Node_ sketch.

Start a new sketch on the yz plane. Draw another node sketch.
![10](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_10%20a%20single%20Node%20sketch%20on%20yz.png?raw=true)

Select both Node sketches click the ControlPoly4 macro
![02](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/ControlPoly4.png?raw=true)
![11](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_11%20run%20ControlPoly4%20macro%20on%20two%20Node%20sketches.png?raw=true)

This creates a ControlPoly4_2N object in the document. Note the '_3L_' suffix. This is second flavor of the ControlPoly4 category of objects
![12](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_12%20ControlPoly4_2N%20object.png?raw=true)

In the Data Tab, you can see three parameters:
* Sketch0 - this was the first input selection, and it can be remapped to another sketch (must also be a node sketch)
* Sketch1 - this was the second input selection, and it can be remapped to another sketch (must also be a node sketch)
* Weights - exactly the same as in ControlPoly_3L

At this stage, take a moment to hide/show the different objects by selecting them in the model tree

Select the ControlPoly_2N object and click the CubicCurve4 macro
![04](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/CubicCurve4.png?raw=true)
![14](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_14%20non%20planar%20CubicCurve4%20object.png?raw=true)

![15](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_15%20non%20planar%20ControlPoly4%20weight%20edit.png?raw=true)

![16](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_16%20a%20sketch%20of%20an%20arc%20of%20circle%20SUBTENDING%2090%20degrees.png?raw=true)

![17](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_17%20run%20ControlPoly4%20macro%20on%20sketch%20of%20arc%20of%20circle.png?raw=true)

![18](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_18%20ControlPoly4_Arc%20object.png?raw=true)

![19](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_19%20run%20CubicCurve4%20on%20ControlPoly4_Arc.png?raw=true)

![20](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_20%20CubicCurve4%20exact%20arc%20object.png?raw=true)

![21](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_21%20freebie%20elliptic%20arc%20and%20line%20come%20for%20free.png?raw=true)
