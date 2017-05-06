# Tutorial 0.03   - Page 03

[return to page 2](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2002.md)   
[return to first page](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2001.md)

### Usage - Continued
#### -3-

* Pick the first segment polygon, hit CubicCurve_4 ![CubicCurve4](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/CubicCurve4.png?raw=true)
* Set the curve color to dark orange
* repeat for second segment polygon

![20](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2020.png?raw=true)



![21](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2021.png?raw=true)



![22](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2022.png?raw=true)

![23](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2023.png?raw=true)

* Line curve, towards the left end. Set u to 0.22

![24](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2024.png?raw=true)

* Line curve, towards the right end. Set u to 0.7

![25](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2025.png?raw=true)

### -2-

We are going to cut the curve based on the points we just created. Remember to identify the objects you wish to select, and select in the model tree. Selection in the 3D view is unpredictable, especially if you need a Point_onCurve on top of a curve endpoint.

* select the CubicCurve_4 of the arc
* ctrl-select the first Point_onCurve (middle of the arc curve)
* ctrl-select the second Point_onCurve (the corner of the two curves)
* hit the ControlPoly4_segment macro ![Point_onCurve](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/ControlPoly4_segment.png?raw=true)

![26](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2026.png?raw=true)

![27](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2027.png?raw=true)

A ControlPoly4_segment object is created. Select it and go to the data tab. You can see a link to the underlying curve, and links to the two points.

As explained in the first tutorial, the default behavior of the library is to create a control polygon or a control grid first, instead of curves and surfaces directly.

Let's keep making segments!

* select the CubicCurve_4 of the arc
* ctrl-select the first Point_onCurve (middle of the arc curve)
* ctrl-select the third Point_onCurve (far end the arc curve, left in the pictures)
* hit the ControlPoly4_segment macro ![Point_onCurve](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/ControlPoly4_segment.png?raw=true)

![28](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2028.png?raw=true)

Once you have your second segment polygon, select them both, change the line to size 1.0 light blue, point to size 4.0 dark blue.

![29](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2029.png?raw=true)

This Tutorial is split into several pages so there are no more than 10 full size screenshots per page.

## [go to page 3](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2003.md)
