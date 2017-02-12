##Tutorial 0.02 ControlGrid44 and CubicSurface44 - page 04
[return to page 3](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2003.md)

[return to first page](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2001.md)
### Usage - continued

Create a node sketch as shown below. The 100 degree angle is measured from the x axis of the sketch.

![21](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2021.png?raw=true)

Close the Sketch

####-13-

Go to TOP VIEW

Click into empty space to make sure nothing is selected.

Create a new sketch. since nothing is selected, the conventional plane chooser comes up. Select **XY-Plane**, and hit **OK**

![22](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2022.png?raw=true)

Draw an arc of circle as shown. the center is constrained to the y axis and there is a symmetry constraint between the endpoints of the arc and the y axis.

![23](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2023.png?raw=true)

Close the sketch

####-14-

Click into empty space to make sure nothing is selected.

Create a new sketch. since nothing is selected, the conventional plane chooser comes up. Select **XY-Plane**, and hit **OK**.

From the Sketcher toolbar, hit **Create an edge linked to an external geometry**, select the arc, escape the command

![24](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2024.png?raw=true)

Draw the node shown below. the circle is on the linked arc end point. This is the sketch that will work at first glance, but we will have to fix it later.

![25](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2025.png?raw=true)

####-15-

Click into empty space to make sure nothing is selected.

Create a new sketch. since nothing is selected, the conventional plane chooser comes up. Select **YZ-Plane**, and hit **OK**


![26](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2026.png?raw=true)


Draw the node shown below. the circle is on the origin.

![27](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2027.png?raw=true)


![28](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2028.png?raw=true)

####-16-

Select the last drawn sketch (on YZ) and activate the attachment editor. Select the right side endpoint of the arc sketch as a reference object.

![29](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2029.png?raw=true)

Once the arc enfpoint is selected, the node move over to the arc. **Attachment mode** should default to **Translate orign**. this is what we want. Hit **OK**.

####-17-

Spin the model around to get a feel for where we are, and how the sketch so far relate to each other and the base planes. Inspect the DAG view in the next picture:
* there are 3 independent groups
* first is the _blank_ 3D controller, we can ignore that
* the second group is the front profile, _and everything attached to it_
* the third group is the arc,  _and everything attached to it_


![30](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/ControlGridd44%20and%20CubicSurface44/ControlGrid44%20and%20CubicSurface44%2030.png?raw=true)

##[Go to page 5](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.02%20ControlGrid44%20and%20CubicSurface44%20-%20page%2005.md)
