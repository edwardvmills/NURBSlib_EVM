# Tutorial 0.03   

## Point_onCurve, ControlPoly4_segment, ControlPoly6, and CubicCurve6 macros in NURBSlib_EVM

Point_onCurve and ControlPoly4_segment respectively define points along a curve and sections of a curve (at those points).

ControlPoly6 and CubicCurve6 respectively control and exploit a cubic NURBS curve of 6 control points. 

If the title above made no sense to you, please refer to the beginning of this tutorial series   
[go to tutorial 0.01, ControlPoly4 and CubicCurve4](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.01%20ControlPoly4%20and%20CubicCurve4.md)    
[go to Tutorial 0.02, ControlGrid44 and CubicSurface44](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2001.md)    
[return to main page](http://edwardvmills.github.io/NURBSlib_EVM/)

## Motivation

![target](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2000.png?raw=true)

Matching curvature at the ends of a Bezier curve is very challenging. It is possible in some cases, but the result is then often unsatisfactory from a design standpoint. Since my goal is to design braod strokes with Bezier, i need a special curve/surface to cleanly join pairs of Bezier curves/surfaces. This is where ControlPoly6 and CubicCurve6 come into play. These objects can be used to model in their own right, but they were specifically created for the task of blending Bezier objects.

The fact that there are 6 and not 4 control point while still limiting the degree to cubic take us beyond Bezier objects to the first full NURBS of the library. The additional points allow us to set the curvature at each end of the curve independently. This is shown in the picture above. Given two Bezier curves that meet at a sharp corner, we can define arbitrary setbacks (red points), and blend the two curves between the setbacks and the corners. In the picture above, the various curves are extruded using simple FreeCAD functions to allow us to quickly see the highlights of the curves. This is a handy way to examnine curves before building complex grids and surfaces

Limiting the NURBS to cubic keeps tesselation and all internal NURBS function efficient. The ControlPoly6 of the blend above is shown *out of the box*. It gives curvature continuity (G2), and the default settings are ok for rough drafts. There are manually adjustable parameters that can get us to G3, or very close, with careful tuning. These adjustments are a topic onto themselves and will only be glanced at here.

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
* set up two FreeCAD macros
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


This Tutorial is split into several pages so there are no more than 10 full size screenshots per page.

# UNDER CONSTRUCTION

## [go to page 2](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2002.md)
