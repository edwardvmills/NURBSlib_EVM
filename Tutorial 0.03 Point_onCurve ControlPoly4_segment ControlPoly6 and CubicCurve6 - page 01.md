# Tutorial 0.03   - Page 01

## Blending the corner of two cubic Bezier curves

## Point_onCurve, ControlPoly4_segment, ControlPoly6, and CubicCurve6 macros in NURBSlib_EVM

The methods shown here to work with curves are almost identical to the methods used to work with surfaces.  Learning the curve method will tell you if you wish to learn to manipulate the grid version (same but more parameters to set).

Point_onCurve and ControlPoly4_segment respectively define points along a curve and sections of a curve (at those points).

ControlPoly6 and CubicCurve6 respectively control and exploit a cubic NURBS curve of 6 control points. 

[go to tutorial 0.01, ControlPoly4 and CubicCurve4](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.01%20ControlPoly4%20and%20CubicCurve4.md)    
[go to Tutorial 0.02, ControlGrid44 and CubicSurface44](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2001.md)    
[return to the main project page](http://edwardvmills.github.io/NURBSlib_EVM/)

## Motivation

![target](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2000.png?raw=true)

A straight line (zero curvature) blended into a true arc (constant curvature) by use of a blending curve. The curvature is continuous (this is not top grade surfacing yet, but it is an important step along the way).

Matching curvature at the ends of a Bezier curve is very challenging. It is possible in some cases, but the result is then often unsatisfactory from a design standpoint (the curvature matches, but the curves look _nothing_ like before). Since my goal is to design broad strokes with Bezier, i need a special curve/surface to cleanly join pairs of Bezier curves/surfaces. I want to so within *well cotrolled* region, and leave the curves *unchanged* outside of those regions. I want to be able to name the different sections as i wish in the model tree so i can find them and edit them in a logical manner. I *do NOT* want a single NURBS of degree 7, with 12 control points, and 20 knots in the knot vector. I want feature based surfacing!

This is where ControlPoly6 and CubicCurve6 come into play. These objects can be used to model in their own right, but they were specifically created for the task of blending Bezier objects.

The fact that there are 6 and not 4 control point while still limiting the degree to cubic takes us beyond Bezier objects to the first full NURBS of the library. The additional points allow us to set the curvature at each end of the curve independently. This is shown in the picture above. Given two Bezier curves that meet at a sharp corner, we can define arbitrary setbacks (red points), and blend the two curves between the setbacks and the corners.  

Limiting the NURBS to cubic keeps  the tesselation process and all other internal NURBS functions efficient. The ControlPoly6 of the blend above is shown *out of the box*. It gives curvature continuity (G2), and the default settings are ok for rough drafts. There are manually adjustable parameters that can get us to G3, or very close, with careful tuning. These adjustments are a topic onto themselves and will only be glanced at here.

### Target audience for this specific tutorial
This tutorial is meant to give a glimpse of the NURBSlib_EVM _library_ to knowledgable users of FreeCAD. No explanations of basic FreeCAD actions are provided at this time.

I have included a starting point model, and a final model for the lazy.

### Requirements to follow this tutorial
* [Tutorial 0.01](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.01%20ControlPoly4%20and%20CubicCurve4.md) completed (especially the setup portion)
* [Tutorial 0.02](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2001.md)   
* ability to set up a macro in [FreeCAD](http://www.freecadweb.org/) 0.17 is required (Part.Line vs Part.LineSegment deprecation warning is fatal in 0.16)
* ability to create sketches of lines and arcs in FreeCAD
* an understanding of the three basic planes in FreeCAD
* having at least a vague notion of NURBS or Bezier curves, such as found in Inkscape or Illustrator is very helpful

### Specific investment of time required:
* X minutes to read this page and get an idea of what you might get out of it
* download six files from this repository (10 files if you want icons)
* set up four FreeCAD macros
* Y minutes to follow the tutorial, up to Z hour to examine most variations

### Setup Point_onCurve, ControlPoly4_segment, ControlPoly6, and CubicCurve6:
from [master](https://github.com/edwardvmills/NURBSlib_EVM) /NURBSlib_EVM_python, copy:
* Point_onCurve.FCMacro
* ControlPoly4_segment.FCMacro
* ControlPoly6.FCMacro
* CubicCurve_6.FCMacro

from [master](https://github.com/edwardvmills/NURBSlib_EVM) Tutorial Models/Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6/, copy:
* Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 00 starting point.FCStd   
* Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 01 finish.FCStd   

Optional: from [master](https://github.com/edwardvmills/NURBSlib_EVM) /icons, copy:
* Point_onCurve.svg
* ControlPoly4_segment.svg
* ControlPoly6.svg
* CubicCurve_6.svg

Place them in your FreCAD macro folder (and a suitable icon folder)

In FreeCAD, set up macros for Point_onCurve, ControlPoly4_segment, ControlPoly6, and CubicCurve6.

All Sketches _must_ be Sketcher Workbench sketches, not  Part Design workbench. refer to [Tutorial 0.01](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.01%20ControlPoly4%20and%20CubicCurve4.md)




### Usage
#### -1-
Open **_Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 00 starting point.FCStd_**

I recommend you immediately save it as **_Point_onCurve ControlPoly4_segment ControlPoly6 and CubicCurve6 in progress.FCStd_** or some other name you like. This is to maintain a fresh copy of the starting point.

![01](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2001.png?raw=true)

This model contains a folder of starting elements:
* a sketch of a straight line
* a sketch of an arc connected to the straight line at one end
* ControlPoly4_Arc objects linked to the straight line sketch (refer to [tutorial 0.01](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.01%20ControlPoly4%20and%20CubicCurve4.md) if you're curious why both use the "Arc" type. it's just the quick and easy cheat for a a simple example)
* CubicCurve_4 objects linked to the control polys above
* extrusion surfaces linked to the CubicCurve_4 objects above (these are made using the Part workbench extrude command, not PartDesign). Extruding a curve allows us to see the highlights of the curves. Bad highlights will make two curves that looked just fine by themselves look  very artificial when used in a surface. If you have worked through tutorial 0.02, you will appreciate the ability to quickly generate a surface without dealing with grids!


#### -2-   
Hide the sketches and show the CubicCurve objects (select in tree and hit _spacebar_ to toggle visibility

![02](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2002.png?raw=true)

* click the arc CubicCurve_4 between its center and where the two curves meet (see picture below)
* hit the Point_onCurve macro ![Point_onCurve](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/Point_OnCurve.png?raw=true)

![03](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2003.png?raw=true)

* select the Point_onCurve object in the model tree
* go to the view tab
* set size to 5.0
* set color to red

![04](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2004.png?raw=true)

* with the Point_onCurve object still selected, go to the data tab
* note the link to the reference curve
* note that the object has a Position property (which is used by other objects)
* the last parameter, labeled u, is the parametric position along the curve
* change u to 0.60


![05](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2005.png?raw=true)

The point is created by default at the location of the mouse click. It is good to avoid clicking too close to the middle. By clicking much closer to one end of the curve or the other, the u value is always much closer to 0 or 1. This makes it easy to see which direction u  goes for the curve in question, and how to slide the point along the curve in the direction you wish.

Right now, clicking and adjusting manually are the only two ways to set the parameters (many more methods are planned eventually. They are not hard, just time consuming).

#### -2-  

Add more points on the curves as shown in the pictures below (and make them red and size 5.0 as well)
* Arc curve, very close to the corner of the two curve. Set u to 1.0, so it is in the corner itself

![06](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2006.png?raw=true)

![07](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2007.png?raw=true)

![08](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2008.png?raw=true)

Following the few next pictures: first create all the points, then select them all at once to change size and color, then adjust the u values (the details will be repeated along the way, this summary is to give an overview of what we are doing)
 
* Arc curve, very close to the far left end. Set u to 0.0 so it is on the far edge
* Line curve, towards the corner, but not too close. Set u to 0.22
* Line curve, towards the right end. Set u to 0.7

![09](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2009.png?raw=true)

This Tutorial is split into several pages so there are no more than 10 full size screenshots per page.

## [go to page 2](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2002.md)
