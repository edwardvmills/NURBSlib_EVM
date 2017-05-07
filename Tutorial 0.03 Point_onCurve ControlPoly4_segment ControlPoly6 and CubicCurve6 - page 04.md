# Tutorial 0.03   - Page 04

[return to page 4](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2003.md)   
[return to first page](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2001.md)

### Usage - Continued
#### -5-

* select the two CubicCurve_4 objects that form the corner, hit ControlPoly6 ![CubicCurve4](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/ControlPoly6.png?raw=true)

![30](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2030.png?raw=true)

This creates our first 6 point cubic NURBS, a ControlPoly6 of type ControlPoly6_FilletBezier. Once again, ControlPoly6 objects *can* be used to model directly, but they exist *for the purpose* of joining cubic bezier segment. The extra points on a ControlPoly6 give it flexibility, but also make it easy to make absolutely awfully ugly curves.

In the long term, the plan for this library is to introduce higher degree Bezier for main design flexibility (5 point Bezier is quartic, 6 points is quintic, etc), and to keep the NURBS *in the corners*, so to speak. Bezier curves have some *self smoothing* properties that keep it from kinking in the middle unexpectedly.

* Set the poly color to light blue
* set the poly point color to dark blue, size 4.0

![31](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2031.png?raw=true)

![32](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2032.png?raw=true)

![33](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2033.png?raw=true)

![34](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2034.png?raw=true)

![35](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2035.png?raw=true)

![36](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2036.png?raw=true)

![37](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2037.png?raw=true)


This is the last tutorial for the library right now. [return to project main page](http://edwardvmills.github.io/NURBSlib_EVM/)
