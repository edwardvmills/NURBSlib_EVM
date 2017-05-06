# Tutorial 0.03   - Page 02

[return to page 1](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2001.md)

### Usage - Continued
#### -1- Continued

![10](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2010.png?raw=true)

* create a new folder in the model tree and put all the Point_onCurve objets in it

![11](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2011.png?raw=true)

* Arc curve, very close to the far left end. Set u to 0.0 so it is on the far edge

![12](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2012.png?raw=true)

![13](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2013.png?raw=true)

* Line curve, towards the left end. Set u to 0.22

![14](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2014.png?raw=true)

* Line curve, towards the right end. Set u to 0.7

![15](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2015.png?raw=true)

### -2-

We are going to cut the curve based on the points we just created. Remember to identify the objects you wish to select, and select in the model tree. Selection in the 3D view is unpredictable, especially if you need a Point_onCurve on top of a curve endpoint.

* select the CubicCurve_4 of the arc
* ctrl-select the first Point_onCurve (middle of the arc curve)
* ctrl-select the second Point_onCurve (the corner of the two curves)
* hit the ControlPoly4_segment macro ![Point_onCurve](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/ControlPoly4_segment.png?raw=true)

![16](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2016.png?raw=true)

A ControlPoly4_segment object is created. Select it and go to the data tab. You can see a link to the underlying curve, and links to the two points.

As explained in the first tutorial, the default behavior of the library is to create a control polygon or a control grid first, instead of curves and surfaces directly.

![17](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2017.png?raw=true)

Let's keep making segments!

* select the CubicCurve_4 of the arc
* ctrl-select the first Point_onCurve (middle of the arc curve)
* ctrl-select the third Point_onCurve (far end the arc curve, left in the pictures)
* hit the ControlPoly4_segment macro ![Point_onCurve](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/ControlPoly4_segment.png?raw=true)

![18](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2018.png?raw=true)

![19](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2019.png?raw=true)

* hit the Point_onCurve macro ![Point_onCurve](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/Point_OnCurve.png?raw=true)

This Tutorial is split into several pages so there are no more than 10 full size screenshots per page.

## [go to page 3](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2003.md)
