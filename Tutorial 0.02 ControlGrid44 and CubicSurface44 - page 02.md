##Tutorial 0.02 ControlGrid44 and CubicSurface44 - page 02
[return to page 1](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2001.md)

### Usage
####-1-
Open ControlGrid44 and CubicSurface44 bare bones.FCStd
![01](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2001.png?raw=true)

This model containes some starting point sketches:
* a folder containing a set of linked sketches that form a 3D pointer
* a three line sketch on the zx plane

Select the _3D node controller blank - COPY-PASTE THIS FOLDER_ folder that contains the sketches, and hit CTRL-C (copy)

FreeCAD will ask if we wish to copy the object the folder depends on, select YES

![02](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2002.png?raw=true)

####-2-

Hit CTRL-V (paste). Rename the folder to _3D node controller - front left_

![03](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2003.png?raw=true)

Expand the folder and select _Anchor - xy001_ (mine has 001 added to the contents, because i copied/pasted once exactly. you do it over and over, you will get 002, 003, 004, etc added to your object names. Pay attention to the screenshots, because our object names will probably get out of sync. if you want, you can use the screenshots to se my object names and check yours)

Go to the Part workbench, under menu Part, select the _attachment..._ function. (i have added this function to a custom toolbar so i don't have to switch around the workbenches so much)

Select the left most point of the _front\_profile\_zx_ sketch. It must be the _point_ itself. Not the _line_. Slecting the line does a different awesome thing.

When you have selected the point, you can see the attachment editor reporting that the first reference is a vertex, _Sketch:Vertex1_

The _Attachment mode_ is automatically set to _Translate origin_. This is what we want. Hit OK (and then cancel to escape..i think?)

![04](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2004.png?raw=true)

![05](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2005.png?raw=true)

![06](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2006.png?raw=true)

![07](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2007.png?raw=true)

![08](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2008.png?raw=true)

![09](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2009.png?raw=true)

![10](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2010.png?raw=true)

##[go to page 3](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2003.md)
