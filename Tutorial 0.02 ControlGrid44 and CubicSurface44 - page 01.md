# Tutorial 0.02
##ControlGrid44 and CubicSurface44 macros in NURBSlib_EVM

These are the objects that respectively control and exploit a rational bicubic bezier surface.

[return to main page](http://edwardvmills.github.io/NURBSlib_EVM/)

### Target audience for this specific tutorial
This 'tutorial' is meant to give a glimpse of the NURBSlib_EVM _library_ to knowledgable users of FreeCAD. No explanations of basic FreeCAD actions are provided at this time. I will spend a little extra effort on the amazing Attachment Editor of FreeCAD as it relates to sketches used for surface modeling. The actual grid and surface portion take less than one minute, but without good sketches they are uninteresting.

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

### Usage
####-1-
Open ControlGrid44 and CubicSurface44 bare bones.FCStd
![01](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2001.png?raw=true)

This model containes some starting point sketches:
* a folder containing a set of linked sketches that form a 3D pointer
* a 

![02](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2002.png?raw=true)

![03](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2003.png?raw=true)

![04](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2004.png?raw=true)

![05](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2005.png?raw=true)

![06](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2006.png?raw=true)

![07](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2007.png?raw=true)

![08](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2008.png?raw=true)

![09](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2009.png?raw=true)

![10](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2010.png?raw=true)

![11](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2011.png?raw=true)

![12](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2012.png?raw=true)

![13](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2013.png?raw=true)

![14](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2014.png?raw=true)

![15](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2015.png?raw=true)

![16](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2016.png?raw=true)

![17](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2017.png?raw=true)

![18](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2018.png?raw=true)

![19](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2019.png?raw=true)

![20](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2020.png?raw=true)

![21](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2021.png?raw=true)

![22](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2022.png?raw=true)

![23](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2023.png?raw=true)

![24](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2024.png?raw=true)

![25](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2025.png?raw=true)

![26](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2026.png?raw=true)

![27](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2027.png?raw=true)

![28](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2028.png?raw=true)

![29](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2029.png?raw=true)

![30](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2030.png?raw=true)

![31](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2031.png?raw=true)

![32](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2032.png?raw=true)

![33](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2033.png?raw=true)

![34](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2034.png?raw=true)

![35](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2035.png?raw=true)

![36](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2036.png?raw=true)

![37](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2037.png?raw=true)

![38](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2038.png?raw=true)

![39](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2039.png?raw=true)

![40](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2040.png?raw=true)

![4](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%204.png?raw=true)


