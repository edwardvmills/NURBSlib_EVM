
## Tutorial 0.02 ControlGrid44 and CubicSurface44 - page 03
[return to page 2](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2002.md)

[return to first page](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2001.md)
### Usage - continued

We just edited **_Anchor - xy001_**, the light blue sketch. The **_zx001_** and **_merge001_** sketches have updated as well. We are about to see how they are connected in one moment.

![11](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2011.png?raw=true)

#### -8-

Begin editing the **_zx001_** sketch. Please only perform the indicated change the tfirst time around

![12](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2012.png?raw=true)

change the angle from 5 to -85 degrees

![13](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2013.png?raw=true)

Note that the rectangle with a diagonal drawn in does a lot more than change angle, it also considerably lengthens. This is because the corner of the rectangle opposite the center of the circle is linked to **_Anchor - xy001_**

Exit the sketch and rotate the model to inspect it.

![14](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2014.png?raw=true)

**_merge001_** is a single node sketch that can point in any direction in 3D space, where the position and xy of the tangent are located in **_Anchor - xy001_**, and the z component of the tangent is controlled by **_zx001_**. There are many other ways to structure the sketches to get the same result. We could use horizontal and vertical dimensions in the sketches insted of angles. this particular method controls the _length_ of the **_merge001_** node as projected on the xy plane.

#### -9-

Begin editing the **_front\_profile\_zx_** sketch

![15](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2015.png?raw=true)

#### -10-

Click+hold the left side line, then drag it left


![16](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2016.png?raw=true)

And drop

![17](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2017.png?raw=true)

Evertime we drag and drop an object in the sketch, the rest of the model updates on the drop.

#### -11-

Hide **_Anchor - xy001_** and **_zx001_**

![18](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2018.png?raw=true)

We have just spent quite some effort to make a single node. Most of the time, a full 3D controller is not necessary. At least not at first. We will make the rest of the curves in this tutorial much faster. We will acutally make one of them "wrong", and then fix it to show the modularity of the components.

#### -12-

Select the point on **_front\_profile\_zx_** that is completely opposite the red node we just made. 

![19](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2019.png?raw=true)

Create a sketch. Because we had an active selection when we created the sketch, the sketch attachment window pops up. The default is **translate**, and that is what we want. Hit OK.

![20](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2020.png?raw=true)

## [Go to page 4](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2004.md)
