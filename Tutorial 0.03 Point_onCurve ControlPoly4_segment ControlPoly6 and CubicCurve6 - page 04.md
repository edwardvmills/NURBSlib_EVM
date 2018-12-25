# Tutorial 0.03   - Page 04

[return to page 3](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2003.md)   
[return to first page](https://github.com/edwardvmills/NURBSlib_EVM/blob/gh-pages/Tutorial%200.03%20Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%20-%20page%2001.md)

### Usage - Continued
#### -5-

* select the two CubicCurve_4 objects that form the corner, hit ControlPoly6 ![ControlPoly6](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/ControlPoly6.png?raw=true)

![30](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2030.png?raw=true)

![31](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2031.png?raw=true)

This creates our first 6 point cubic NURBS control polygon, a ControlPoly6 of type ControlPoly6_FilletBezier. Once again, ControlPoly6 objects *can* be used to model directly, but they exist *for the purpose* of joining cubic bezier segment. The extra points on a ControlPoly6 give it flexibility, but also make it easy to make absolutely awfully ugly curves.

In the long term, the plan for this library is to introduce higher degree Bezier for main design flexibility (5 point Bezier is quartic, 6 points is quintic, etc), and to keep the NURBS *in the corners*, so to speak. Bezier curves have some *self smoothing* properties that keep them from kinking in the middle unexpectedly. A general NURBS can be very rough *within its own borders*.

In this case, the ControlPoly6 looks carefully at the two curves it is linked to, determines the curvature on one end, on the other end, and makes a guess on the remaining degrees of freedom in the NURBS to produce a reasonable control poly.

* Set the poly color to light blue
* set the poly point color to dark blue, size 4.0

### -6-

* select the ControlPoly6_FilletBezier object, hit CubicCurve_6 ![CubicCurve6](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/CubicCurve6.png?raw=true)

![32](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2032.png?raw=true)

This creates the actual curve associated with the ControlPoly6 object above.
* change color to dark orange

![33](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2033.png?raw=true)

* Part Extrude the CubicCurve_6 object
* check for duplicate surfaces/figure out where FreeCAD decided to put the curve (model tree or under the part extrude or both?)
* set diplay mode shaded, color light orange, same as the segment curve extrusions.

![34](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2034.png?raw=true)

Having no visible edge lines and the same color for all three new surface segments is critical. Having edges lines drawn where two surfaces join can give the illusion of a smooth join, but when you render or machine the model, there are no lines. All of a sudden the imperfections of the join will scream! Two surfaces side by side almost never look that bad, but when you patch many into a body, you really don't want to see all the seams making crosses everywhere.

In the pictures below we have curvature matching at the seams. This is a decent start. In the early phase of a design, while the main (Bezier) lines are changing, there is no need for the edge blends to be perfect. Being able to see the rough blends and adjust the setbacks is very useful to guide the main design.

![35](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2035.png?raw=true)

![36](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2036.png?raw=true)

![37](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/Tutorial%20Models/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6/Point_onCurve%20ControlPoly4_segment%20ControlPoly6%20and%20CubicCurve6%2037.png?raw=true)

The next tutorial will deal with using the objects already present in this model to inspect seam quality and change the parameters manually to reach G3, *change of curvature* matching!

[return to project main page](http://edwardvmills.github.io/NURBSlib_EVM/)

### Project has moved to [Silk Repository](http://edwardvmills.github.io/Silk/)

### Next tutorial can be found on [FreeCAD forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=23243&start=70#p188431) you can go back and read the erlier parts of the comment thread too, but the next logical point is where this link takes you to.
