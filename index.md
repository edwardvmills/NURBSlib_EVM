## NURBSlib_EVM
My python scripts for creating surfaces in [FreeCAD](http://freecadweb.org/).   
Extremely early release. 

![Best example of current state]
(https://github.com/edwardvmills/NURBSlib_EVM/blob/b33835dcd1e7ab148f09706c385ce4218eaf73d5/development_FC_models/parametric/begin%20transition%20to%200.17/Bezier%20primary%20Surface%20Volume%2032-12.png?raw=true)  

![A semi decent G2 seam between two surfaces](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/development_FC_models/parametric/Bezier%20surface%20segment%20and%20blend/Bezier%20surface%20segment%20and%20blend%2021/Bezier%20surface%20segment%20and%20blend%2021.gif?raw=true)   

![manipulating model above]
(https://github.com/edwardvmills/NURBSlib_EVM/blob/master/development_FC_models/parametric/Bezier%20surface%20segment%20and%20blend/Bezier%20surface%20segment%20and%20blend%2018/1f7g55.gif?raw=true)  

THIS PAGE IS OUT OF DATE (01-15-2017) I don't have time to update user instructions until i finish the next big development phase. If interested, please refer directly to the repository.  

All scripts in this repository are offered under the terms of the 
[GPLv3](http://www.gnu.org/licenses/gpl-3.0.en.html)   
All models in this repository are offered under the terms of 
[CC-BY](http://creativecommons.org/licenses/by/2.0/)   

For the time being, this page is intended to give a quick explanation of each tool along with pictures. 
You can read more about the project [here](README.md)
###Setup
There is a release, or you can grab from master.

-from [NURBSlib_EVM_python](https://github.com/edwardvmills/NURBSlib_EVM/tree/master/NURBSlib_EVM_python), take NURBSlib_EVM.py, all *.fcmacro files   
-grab the [icons](https://github.com/edwardvmills/NURBSlib_EVM/tree/master/icons)   
-put them somewhere FreeCAD can find them   
-link the fcmacro scripts to icons, descriptions(use macro name), tooltips (use macro name), etc.   
-put all those GUI macros in toolbars.   
-add those toolbars to the PartDesign workbench. The raw material will be PartDesign sketches, so this is a good place to put the toolbars for the time being.   

Here is a picture of how i like to group them:
![toolbar setup](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/site_stuff/basic_usage/setting%20up%20the%20toolbars.png?raw=true)
###Usage
**Draw sketches of lines/circles** (check each curve macro to see what inputs it wants). 

In the picture below we see:  
-a sketcher arc   
-a sketch of three lines connected end to end   
-three 'node' sketches. A node is one circle + any number of lines that start at the circle center. I have big plans for these little nodes...curvature data...derivative of curvature data...topology data!
![sketches as inputs](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/site_stuff/basic_usage/_01%20sketches%20as%20inputs.png?raw=true)

Select those lines/circles _in the order specified by the macro_, then hit the macro button. A curve is created.
In the picture below:   

-select the arc, then hit   
![Arc_to_rational_bezier](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/icon_bitmaps/Arc_to_rational_bezier.png?raw=true)   
This converts a sketch arc to a **cubic** **rational** bezier curve, formulated from a full NURBS.   

-select the three lines from the single sketch in order, then hit   
![Bezier_Cubic_3_lines](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/icon_bitmaps/Bezier_Cubic_3_lines.png?raw=true)    
This creates a cubic bezier curve, formulated from a full NURBS. The weights are all 1, so it's not rational _in practice_, but the weights are there, and in the future, we may modify them.   

-from one node, select the circle, then the line end point, then _from another node_, select a line endpoint, then the circle. hit   
![Bezier_Cubic_2_nodes](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/icon_bitmaps/Bezier_Cubic_2_nodes.png?raw=true)   
Same type of curve as above.   

Why the funky selection order with nodes? The circles represent curve endpoints, and the lines radiating from them represent the tangents. The multiple lines give hints as to the intended topology. This is a 3D bezier control, and picking a circle is WAY easier than trying to explain to FreeCAD which point i want when there are many lines connecting at a point.   
[TODO, maybe: adapt the macro so the selection goes: circle>line>cirle>line, extract the line endpoints, and reorder automatically)
   
![curves from sketches](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/site_stuff/basic_usage/_02%20curves%20from%20sketches.png?raw=true)   
The new arc is right on top of the sketch arc, so it looks funny.

**IMPORTANT NOTE ABOUT NURBS:** the curves within a single surface 'patch' _cannot_ be aligned at the corners! The corners _must_ pinch at least a little bit. Otherwise, the surface may build, but the tangency controls will vanish. For my intentions, that makes the surface unusable.   
If you need to join two curves that are tangent where they meet, you need two surfaces. At least for now, for these scripts.

**Making surfaces from the curves**   
The surface macros need to be given 3 or 4 curves of the _same type_ (degree, number of poles, knot vector). This is why we had to convert the arc.  
 
There are two types of surface right now:   
-rational bezier (accepts 3 or 4 cubic rational bezier curves)   
-6 pole by 6 pole NURBS (accepts 4 NURBS curves with 6 control points and a specific knot vector)

First, lets stay with bezier (icons are mostly red)

Select 3/4 curves in a loop counterclockwise (surface normal will then point towards you), and hit   
![Bezier_cubic_4_sided_surface](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/icon_bitmaps/Bezier_cubic_4_sided_surface.png?raw=true)   
And then wait...     
This takes a while. Expect FreeCAD to lock up for a bit. Adjust your tesselation in Preferences>Part design> Shape view until you have a balance of speed and surface resolution. If a single surface by itself looks rough, you need finer tesselation. I have no control over this, it's all FreeCAD internals as far as i know.

This creates a rational bezier surface.   
![bezier surfaces from bezier curves](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/site_stuff/basic_usage/_04%20surfaces%20from%20curves.png?raw=true)  
![surface from curves, other side](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/site_stuff/basic_usage/_05%20surfaces%20from%20curves%2002.png?raw=true) 
Note that the arc edge is still a _true arc_, so we should be able to make good FreeCAD shells that join this surface type to other FreeCAD surfaces.  

If you're not sure the curves are correct and don't want to waste the time to generate the surface, you can preview the control grid. [warning, generates a bazillion lines in your object tree. So organize your model tree and stick these lines in their own folder!]   

-select the curves the way you would for a surface, then hit   
![Bezier_cubic_4_sided_grid](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/icons/icon_bitmaps/Bezier_cubic_4_sided_grid.png?raw=true)   
This generates the grid that will be used for the surface   

![control grid preview](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/site_stuff/basic_usage/_03%20control%20grid%20preview%20from%20curves.png?raw=true)   

So what does that grid tell us? How would we know if it's a bad grid from bad curves? It just takes a little practice. The biggest problem is if the grid crosses itself, then the surface could double back on itself. The next problem is if one part of the grid is stretched out and almost pinches into a point. This will make FreeCAD's nurbs tesselation routine go crazy, lock up the program for a long time, and produce an ugly surface, if it makes it at all.

In the picture, on the left, you can see that all the 'squares' are roughly the same size, and the angles between lines are never less than 70 degrees or so. This is a reasonable grid.

On the right side, for the three curve grid, you can see a sliver of a triangle, this is not very good. This was my first try at a NURBS triangle, and it is not ideal. I have a very good idea how to fix it, and now that i have incorporated the curve weights into the surfaces, i can implement it. Soon it will be much better. An imperfect triangle surface now is better than than a perfect triangle surface later, so i included it in the first release.   
--link placeholder to talk about degenerate NURBS patches

Many times, a surface will look good when created, but when we set the display to shaded and hide the edge, the seam between two surfaces looks just absolutely awful. Here is a very crappy 'loft with rails'    

![crappy loft with rails](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/site_stuff/current_state/loft%20with%20rails%20-%20very%20crude.png?raw=true)   
![G1 is not enough](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/site_stuff/current_state/lofting%20with%20rails%20-%20Bezier%20G1%20is%20not%20enough.png?raw=true)

This is why G1 (tangency matching) is not enough. Using bezier curves/surfaces, direct G2 matching is obtained at the expense of tangent control, so that's just useless.   
--link placeholder to talk about bezier and G2   

Here is what i mean: in the picture below, i have massaged bezier surfaces to obtain G2 (curvature continuity) to a flat plate, but now i can _only control the position of the bottom curved edge_. I can make touch another edge, but i can't match tangents.   

![G2 bezier](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/site_stuff/current_state/Bezier%20G2%20transition.png?raw=true)

Even maintaining G1 is way harder than it _seems_ it ought to be.   
--link placeholder to go over the rules for curve making to obtain G1 across seams.   

In theory, we could set up a nonlinear solver that plays around with tangents and weights to seek G2, but this may not work. Even if it did, we would never have local control. Any change in any part would mean modifying everything everywhere. 

So this is about as far as the bezier formulation of NURBS will get us. We can fill a few holes, and join a small number of surfaces if we are extremely careful. Time to break away from bezier! Let's keep the idea of control with endpoints and tangents, and toss away the rest.

### Tutorials on the way: 
  
-the 4 point bezier curve, for when the types of sketches shown above just aren't enough.   

-the 6 point cubic NURBS. Now we can match curvature, and more, independently at each curve endpoint.  

-working in bezier and converting to 6 point cubic NURBS   

-the surface made from groups of 6 point cubic NURBS.   
![G2 66 surfaces](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/site_stuff/current_state/G2%20join%2066%20surfaces%2009.png?raw=true)

-'growing' two surfaces on one side of a single surface: local refinement within a non singular NURBS topology   

-the sketch placer tool to put nodes wherever you want them.   

-the sketch based curvature prediction tool (very incomplete)

-query curve type
