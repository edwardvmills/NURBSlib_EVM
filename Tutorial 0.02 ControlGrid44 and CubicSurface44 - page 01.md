# Tutorial 0.02
##ControlGrid44 and CubicSurface44 macros in NURBSlib_EVM

These are the objects that respectively control and exploit a rational bicubic bezier surface.

[go to tutorial 0.01, ControlPoly4 and CubicCurve4 macros in NURBSlib_EVM](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.01%20ControlPoly4%20and%20CubicCurve4.md)
[return to main page](http://edwardvmills.github.io/NURBSlib_EVM/)

### Target audience for this specific tutorial
This 'tutorial' is meant to give a glimpse of the NURBSlib_EVM _library_ to knowledgable users of FreeCAD. No explanations of basic FreeCAD actions are provided at this time. I will spend a little extra effort on the amazing Attachment Editor of FreeCAD as it relates to sketches used for surface modeling. FreeCAD's 2D sketcher, when combined with the Part Workbench attachment editor and unlimited external references, is the best 3D sketching system i have ever seen (my experience is limited to Solidworks and Autodesk Inventor).

The actual grid and surface portion take less than one minute, but without good sketches they are uninteresting.

I have included a starting point model, and a final model for the lazy.

### Requirements to follow this tutorial
* [Tutorial 0.01](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.01%20ControlPoly4%20and%20CubicCurve4.md) completed (especially the setup portion)
* ability to set up a macro in [FreeCAD](http://www.freecadweb.org/) 0.17 is required (Part.Line vs Part.LineSegment deprecation warning is fatal in 0.16)
* ability to create sketches of lines and arcs in FreeCAD
* an understanding of the three basic planes in FreeCAD
* having at least a vague notion of NURBS or Bezier curves, such as found in Inkscape or Illustrator is very helpful

### Specific investment of time required:
* X minutes to read this page and get an idea of what you might get out of it
* download three files from this repository (5 files if you want icons)
* set up two FreeCAD macros
* Y minutes to follow the tutorial, up to Z hour to examine most variations
* Hypnosis warning, 3D sketching is dangerously fun

### Setup ControlGrid44 and CubicSurface44:
from [master](https://github.com/edwardvmills/NURBSlib_EVM) /NURBSlib_EVM_python, copy:
* ControlGrid44.FCMacro
* CubicSurface44.FCMacro

from [master](https://github.com/edwardvmills/NURBSlib_EVM) /Tutorial Models/ControlGridd44 and CubicSurface44/, copy:
* ControlGrid44 and CubicSurface44 bare bones.FCStd
* ControlGrid44 and CubicSurface44 Complete.FCStd

Optional: from [master](https://github.com/edwardvmills/NURBSlib_EVM) /icons, copy:
* ControlGrid44.svg
* CubicSurface44.svg

Place them in your FreCAD macro folder (and a suitable icon folder)

In FreeCAD, set up macros for ControlGrid44 and ControlGrid44.

All Sketches _must_ be Sketcher Workbench sketches, not  Part Design workbench. refer to [Tutorial 0.01](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.01%20ControlPoly4%20and%20CubicCurve4.md)

This Tutorial is split up so there are no more than 10 images per page. These are full size screenshots.

[go to page 2](https://github.com/edwardvmills/NURBSlib_EVM/edit/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2002.md)
