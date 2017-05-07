
# Tutorial 0.01
## ControlPoly4 and CubicCurve4 macros in NURBSlib_EVM

These are the objects that respectively control and exploit a rational cubic bezier curve

[return to main project page](http://edwardvmills.github.io/NURBSlib_EVM/)

### Target audience for this specific tutorial / presentation
This tutorial is meant to give a glimpse of the NURBSlib_EVM _library_ to knowledgable users of FreeCAD. No explanations of basic FreeCAD actions are provided at this time.

As a library, NURBSlib_EVM provides basic elements that _can_ be used to produce models, but are not streamlined. Some steps in this tutorial will feel repetitive. They can be automated, and they will be automated eventually, in the form of a workbench. At this time, priority is given to stability and versatility of the objects. The interface is minimal, Spartan even. This is not necessarily a bad thing.

### Requirements to follow this tutorial / presentation
* ability to set up a macro in [FreeCAD](http://www.freecadweb.org/) 0.17 is required
* ability to create sketches of lines and arcs in FreeCAD
* an understanding of the three basic planes in FreeCAD
* having at least a vague notion of NURBS or Bezier curves, such as found in Inkscape or Illustrator is very helpful

### Specific investment of time required:
* 15 minutes to read this page and get an idea of what you might get out of it
* download three files from this repository (5 files if you want icons)
* set up two FreeCAD macros
* 30 minutes to follow the tutorial, up to two hours to examine most variations

### Motivation? It will take a few tutorials, but here is the goal:
![target](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/development_FC_models/parametric/FreeCAD%200.17.9528/Bezier%20primary%20Surface%20Volume%2066-07.bmp.png?raw=true)
The specific element of interest in the picture above is the fairly smooth blending of three main surfaces at the front top corner. There is a large 'blending radius' between the top and narrow front surface, and a sharp 'blending radius' between the wide side surface and the first two. These radii are controlled parametrically, and the seams are 95% curvature continuous. There are some known flaws as well, but let's focus on the positive for now!


### Setup ControlPoly4 and CubicCurve4:
from [master](https://github.com/edwardvmills/NURBSlib_EVM) /NURBSlib_EVM_python, copy:
* NURBSlib_EVM.py
* ControlPoly4.FCMacro
* CubicCurve4.FCMacro

Optional: from [master](https://github.com/edwardvmills/NURBSlib_EVM) /icons, copy:
* ControlPoly4.svg
* CubicCurve4.svg

Place them in your FreCAD macro folder (and a suitable icon folder)

In FreeCAD, set up macros for ControlPoly4 and CubicCurve4. Wherever you do put them, add the Sketcher workbench 'Create a new sketch' button close by. All sketches in this tutorial must be from Sketcher workbench, not PartDesign workbench.

### Usage
#### -1-
In FreeCAD, open a new document. Draw a sketch with 3 lines connected end to end. Nothing else should be in the sketch (for now). The Sketch _must_ be from the sketcher workbench, not the part design workbench.
![01](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_01%20A%20sketch%20of%20three%20lines%20connected%20end%20to%20end.png?raw=true)
#### -2-
Select the 3 line sketch and click the ControlPoly4 macro
![02](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/ControlPoly4.png?raw=true)

This creates a ControlPoly4_3L object in the document. Note the '_3L_' suffix. This is one of several different flavors of the ControlPoly4 category of objects
![03](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_03%20ControlPoly4_3L%20object.png?raw=true)

In the case of the three line sketch, the ControlPoly4_3L object is hidden by the sketch itself. Hide the sketch to see it directly if you wish.

In the Data Tab, you can see two parameters:
* Sketch - this was the input selection, and it can be remapped to another sketch (also of exactly three lines end-to-end)
* Weights - we'll talk about this again in a moment      

It's not very interesting yet, so let's keep moving to next step!

#### -3-
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
* in the meantime, i have complete freedom to name all the objects and organize them in folders as i like. It is actually really annoying when FreeCAD moves stuff around in the model tree (for example when mirroring a surface)   

#### -4-
Edit the original sketch. 'Drag' a line...the polygon and curve update very time you 'drop'

#### -5-
Now that we have a CubicCurve4 attached to the ControlPoly4, let's go back to the ControlPoly4 object and examine the weight controls.

In the data tab of the polygon, the weights are displayed as a list with default values [1,1,1,1]. Hitting the ... button on the right side of the list opens up a very simple list editor window. 
![06](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_06%20the%20weight%20list%20of%20all%20ControlPoly4%20objects.png?raw=true)

#### -6-
In this window, change one of the weights. Hit OK to close the editor window
![07](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_07%20editing%20a%20specific%20weight%20of%20the%20ControlPoly4%20object.png?raw=true)

#### -7-
Hit F5 to recompute the model. In the case shown in the picture, raising the weights from 1.0 to 4.0 for the second pole causes the curve to be drawn towards the second pole.
![08](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_08%20the%20CubicCurve4%20object%20updates%20to%20the%20modified%20ControlPoly4%20weight.png?raw=true)
The weights can be used to influence the model directly, but it is not recommended as a basic modeling strategy. The primary function of the weights is to allow exact conversion of arcs of circles (and ellipses and other conics). This is done automatically and generally shouldn't be messed with. The mechanism is exposed here to present the python object model.

#### -8-
Start a new sketch on the xy plane. Draw 1 circle and 1 line. The line must have one point (end point or start point) exactly on the circle center. Do not put anything else in the sketch. Place it so it doesn't overlap the first sketch. Odd angles are good, as they will show us more later. The Sketch _must_ be from the sketcher workbench, not the part design workbench.
![09](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_09%20a%20single%20Node%20sketch%20on%20xy.png?raw=true)
This type sketch is called a _Node_ sketch.

#### -9-
Start a new sketch on the yz plane. Draw another node sketch. Place it so it doesn't overlap the other sketches. Odd angles are good, as they will show us more later. The Sketch _must_ be from the sketcher workbench, not the part design workbench.
![10](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_10%20a%20single%20Node%20sketch%20on%20yz.png?raw=true)

#### -10-
Select both Node sketches and click the ControlPoly4 macro
![02](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/ControlPoly4.png?raw=true)
![11](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_11%20run%20ControlPoly4%20macro%20on%20two%20Node%20sketches.png?raw=true)
This creates a ControlPoly4_2N object in the document. Note the '_2N_' suffix. This is the second flavor of the ControlPoly4 category of objects
![12](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_12%20ControlPoly4_2N%20object.png?raw=true)

In the Data Tab, you can see three parameters:
* Sketch0 - this was the first input selection, and it can be remapped to another sketch (must also be a node sketch)
* Sketch1 - this was the second input selection, and it can be remapped to another sketch (must also be a node sketch)
* Weights - exactly the same as in ControlPoly_3L

At this stage, take a moment to hide/show the different objects by selecting them in the model tree. Turn the model around and inspect it. Note that the two nodes are in separate planes, and the ControlPoly4_2N joins them to form a non planar polygon.

#### -11-
Select the ControlPoly_2N object and click the CubicCurve4 macro
![04](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/CubicCurve4.png?raw=true)
![14](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_14%20non%20planar%20CubicCurve4%20object.png?raw=true)
This creates one more CubicCurve4 object in the document.
In the Data Tab, you can see a single parameter:
* Poly = ControlPoly4_2N. This was the input selection, and it can be remapped to _any ControlPoly4_ object (of which there are 3 varieties at this time)

Now we can see the different roles played by the Node sketches and their components. Back in ControlPoly4_2N:
* the Node passed to Sketch0 controls the start of the curve
* the Node passed to Sketch1 controls the end of the curve
* The center of the circle in each node determines the start(/end) point of the curve
* The line controls the start(/end) tangent of the curve

#### -12- (optional)
Repeat steps 5, 6,and 7 with ControlPoly4_2N to verify that the weight controls work. Edit the Node sketches and watch the curves updating.
![15](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_15%20non%20planar%20ControlPoly4%20weight%20edit.png?raw=true)

#### -13-
Start a new sketch on the zx plane. Draw an arc of cirle, SUBTENDING 90 degrees (less than a quarter of a circle). There are usually no problems up to 180 degrees, but 90 degrees is _rock solid_. I like to make models very stable, so i split my arcs as necessary. You can put whatever else you like in this sketch, but the arc _must_ be drawn first. The Sketch _must_ be from the sketcher workbench, not the part design workbench.
![16](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_16%20a%20sketch%20of%20an%20arc%20of%20circle%20SUBTENDING%2090%20degrees.png?raw=true)

#### -14-
Select the sketch with the arc, and click the ControlPoly4 macro
![02](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/ControlPoly4.png?raw=true)
This creates a ControlPoly4_Arc object in the document. Note the '_Arc_' suffix. This is the third flavor of the ControlPoly4 category of objects
![18](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_18%20ControlPoly4_Arc%20object.png?raw=true)
In the Data Tab, you can see two parameters:
* Sketch - this was the input selection, and it can be remapped to another sketch (also of arc)
* Weights = [1,0.8356,0.8356,1]

Note that this time, the weights are not the default [1,1,1,1]. The values generated automatically will give a true circular arc.

#### -15-
Select the ControlPoly4_Arc object, and click the CubicCurve4 macro
![04](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/CubicCurve4.png?raw=true)

![20](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_20%20CubicCurve4%20exact%20arc%20object.png?raw=true)
This creates one more CubicCurve4 object in the document.
In the Data Tab, you can see a single parameter:
* Poly = ControlPoly4_Arc. This was the input selection, and it can be remapped to _any ControlPoly4_ object (of which there are 3 varieties at this time)

What is the point  of steps 14 and 15 if just end up with the same arc?
* Sketcher arcs are quadratic NURBS
* the CubicCurve4 version of the arc is a cubic NURBS
* cubic NURBS are the simplest form that is generally considered suitable for free form modeling
* Once it is in ControlPoly4_arc or CubicCurve4 form, our sketcher arc can now be used alongside the other curves to make surfaces
* usually we only need the polygon, so we sketch the arc, make the polygon, and skip making a curve. There is little extra effort to get the conversion

Here is an example picture of blending a sketcher arc extrusion to a freeform surface with _exact_ matching at the seam. OUT OF SCOPE for this tutorial, i just want to show a concrete example.
![21](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/development_FC_models/parametric/FreeCAD%200.16/blend%20arc%20to%2066%20demo/live%2066%2002.PNG?raw=true)

#### -16- BONUS ROUND
For any single sketch, the ControlPoly4 macro uses Arc mode if there aren't exactly 3 sketch objects (3L mode). This always applies to the first geometry object in the sketch.
The net effect is 
* elliptic arcs are converted exactly.
* a line is automatically split into three (this is handy when you are too lazy to draw three lines, but a bad habit)
* parabola and hyperbola don't work yet, but it's just a matter of exposing startpoint and endpoint. I'm not worried about it at this time
![22](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlPoly4%20and%20CubicCurve4/_21%20freebie%20elliptic%20arc%20and%20line%20come%20for%20free.png?raw=true)

[post questions/comments in this thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=20632)...unless the mods get mad at me for using the FreeCAD forum this way, in which case i will remove this link.

## [go to Tutorial 0.02, ControlGrid44 and CubicSurface44](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2001.md)
