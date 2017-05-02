## Tutorial 0.02 ControlGrid44 and CubicSurface44 - page 06
[return to page 5](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2005.md)

[return to first page](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2001.md)
### Usage - continued

#### -26-

Change the color of the grid to light purple

![41](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2041.png?raw=true)

#### -27-

With the grid still selected, click the CubicSurface44 macro.
![00](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/CubicSurface44.png?raw=true)

![42](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2042.png?raw=true)

### -28-

Change the color of the surface to orange, and change the transparency to 40. The color and transparency are useful to process the depth of the image better. Maybe you prefer other colors, the point is that trying to decipher a bunch of black lines on a grey surface is hard on the brain, and contrast frees up your brain for other tasks.

![43](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2043.png?raw=true)

Rotate the model around and inspect. Note where the control lines go through the surface. try to figure out how the angles of the lines lead to the curves of the surface.

![44](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2044.png?raw=true)


#### -29-

Turn the sketches back on

![45](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2045.png?raw=true)

#### -30-

Edit the arc sketch as shown below. Change the vertical dimension controlling the arc center from 10 to 100.

![46](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2046.png?raw=true)

![47](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2047.png?raw=true)

When you hit enter on the dimension entry box, the model will update as fast as your computer can handle it. The arc sketch will _push_ to the node sketches connected to it, those nodes sketches will _push_ to the ControlPoly4s that depends on them, those will push to the ControlGrid44 that depends on them, and that will _push_ to the surface itself! On large models, you can see the update cascading through the model.

Entering a dimension updates immediately. Drag and drop updates every time you drop. **_CAUTION_** if the change in the sketch causes the grid to get all garbled, the resulting surface will be very hard to compute, and can cause FreeCAD to hang. This is a limitation of NURBS themselves, not FreeCAD. If you tell FreecAD to compute a pinched and folded NURBS, it will do its best, but the result will be ugly and cost a lot in processor time!

I general, a grid should not cross itself over too much, and the angles should be kept minimal. Only bend things as much as you really need to. There is no substitute for practice. You make models and have them crash/hang to know where the line is.

The amazing thing is that if you do spend any time doing this, you will find that very quickly, you only need to see the grid to know if you are on the right track. Then you can hide the surfaces, and basically 0 computing power is needed to work directly with the grids. I don't care how much computer power you have, locking up 99% of it will slow you down.

A good in between step is to hide the surfaces you aren't modifying, leave their grids on, and only display the surfaces you are focused on.

#### -31- 

Replicate the changes shown in the pictures below. (or skip to step 32 for the last important point of this tutorial)

![48](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2048.png?raw=true)

![49](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2049.png?raw=true)

![50](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2050.png?raw=true)

## [Go to page 7](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2007.md)

