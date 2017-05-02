
## Tutorial 0.02 ControlGrid44 and CubicSurface44 - page 07
[return to page 6](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2005.md)

[return to first page](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2001.md)
### Usage - continued

![50](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2050.png?raw=true)

![51](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2051.png?raw=true)

![52](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2052.png?raw=true)

![53](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2053.png?raw=true)

![54](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2054.png?raw=true)

![55](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2055.png?raw=true)

#### -32-

Now let's do a dramatic change: move the entire arc sketch downward by 200.
Select the sketch and under the data tab, edit its placement, -200 in z

![56](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2056.png?raw=true)

![57](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2057.png?raw=true)

What's going on? the left side node polygon in the picture below moved correctly and followed the arc, but the other side didn't! The ControlPoly44 object has a red flag and is not updating.

The node that is moving correctly was drawn on YZ, and then attached to the arc point.

The node that is not moving correctly was drawn on XY, and tied to the arc through a geomtry link. This only works  as long as the arc is also on XY! if not, the geometry link still works, but since it is projected onto the node sketch, this doesn;t actually tie the two points together.

The attachment editor is the correct way to connect sketches. Another advantage is we end up using the origin more in our sketches. This basically the first two contraints for free in every sketch.

#### -33-

select the disconnected node sketch, start the attachment editor, select the arc endpoint as a reference.

![58](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2058.png?raw=true)

The grid and surface disappear, but don't worry, they'll be right back. The node sketch is now tied to the arc point, but we need to edit the sketch drawing as well.

#### -34-

Edit the sketch. Place the circle of the node at the origin, which is now right at the end of the arc (make sure the line comes along as well). The polygon, grid and surface will snap right back.

[done for the day. i hope there aren't too many mistakes, as i tried to cover a lot of ground in one day. If something doesn't quite work, let me know and i'll fix it.

[post questions/comments in this thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=20632)...unless the mods get mad at me for using the FreeCAD forum this way, in which case i will remove this link.

![59](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2059.png?raw=true)

![60](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2060.png?raw=true)


[return to main page](http://edwardvmills.github.io/NURBSlib_EVM/)
