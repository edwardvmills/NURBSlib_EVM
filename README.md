# NURBSlib_EVM
My python scripts for creating surfaces in FreeCAD

jump to setup and usage section unless you want lots of TL;DR

#NURBS   
The ultimate goal is to implement a set of tools to specify points and tangents/normals to generate NURBS surfaces of high continuity. I have some ideas in regards to what constitutes an efficient and intuitive input/interface structure. This is very personal, and cannot address all individual preferences. Although there are many parallels, i am not trying to implement the 'classic' surfacing tools like sweep, loft, blend, trim, etc. FreeCAD already has some of these tools in the Part module and i believe the PartDesign module is slated to get improved versions soon.

Ideally, the user interaction with the points/normals would be analogous to manipulating a coarse mesh, like subdivision surfaces. The main difference with subdivision surface being that with full NURBS, we can have perfect conics, and the 'handles' <i>stay on the surface itself</i>. So when we dimension/constrain the handles, we are dimensioning the surface itself.

For now, my focus is on skinning sets of 3 or 4 curves in a loop. The skinning routing should be consistent, and the seams joining adjacent surfaces should always have the same level of continuity as the adjacent curves at the surface corners.

I am learning as i go, so i am trying to 'juice' the most out of the basic NURBS formulations before moving on to more complex forms. High degrees and complex knot vectors give great smoothness, but few of the control points correspond to actual surface points, so they are challenging to fit among other engineering forms and constrain correctly.

The cubic bezier form is the simplest form that can connect two points with specified tangents (G1), and i am exploring its limits. The weight control interface is incomplete, but arcs can be converted to rational Bezier and used in surfaces. I have a basic quadrilateral surface patch, and a rudimentary triangular suface patch (one collapsed edge/corner). It is theoretically possible to modify the inner control points and weights of a bezier to control the curvature across the seams (G2) in some cases, but this requires manipulating several control points at once, and maintaining tangent continuity is hard to begin with.

For now, the Bezier curves and surfaces are considered to be 'rough drafts' of the final surfaces. Easy to specify, cheap to render. Sometimes maybe even adequate to patch a hole in a shell.

In order to have isolated curvature at each curve endpoint, i have made a 6 control point cubic curve, which opens up the possibility of using the 3rd and 4th points to control start and end curvature respectively. This can be done without interfering with the use of the 2nd and 5th control points to set tangents. Right now the curvature matching must be done by hand, but for any particular value of curvature desired at a curve connection, there is a family of possible control points positions. These additional degrees of freedom will (i hope) allow the possibility of curvature flow

#In this repo:   
-a single .py with all the 'geometry' functions, where i try to use the most basic inputs.   
-individual .fcmacro files that tie the current GUI and selection behavior of FreeCAD to single modeling operations.   
-test model files. Here it gets incredibly messy because i use both git and horrible filenames to track different versions.  These model files are irrelevant to the script structure, in keep them in the repo for my ease of access.   

#the basic design structure is:  
-write a function in BezCubic.py   
-write a GUI wrapper as guioperationx.fcmacro that calls functions in BezCubic.py  
-make a toolbar button   

there are a few icons in the 'icons'folder.

##to use as intended (general description only, not a FreeCAD tutorial):

#setup   
-put BezCubic.py and all the .fcmacro files where FreeCAD can find them   
-link the fcmacro scripts to icons, give the macro a name you like, tooltip, etc.   
-put all those GUI macros in a tool bar.   
-add that toolbar to the PartDesign workbench. The raw material will be PartDesign sketches, so this is the logical place to put this toolbar.   
(see http://freecadweb.org/wiki/index.php?title=Macros for details regarding setting toolbars/macros in FreeCAD)   
I'm aware of the plugin loader tool that's available, and i wish i was smart/dedicated enough to use it, but i'm not :)

#usage   
-draw sketches of lines/circles (read the curve macros to see what inputs they want)   
-select those lines/circles in the order specified by the macro, then hit the macro button > curve is created.   
-select 3/4 curves in a loop counterclockwise (surface normal will then point towards you), hit the surface macro button > surface is created.   

The surfaces are 100% controlled by the curves, which are 100% controlled by the sketches. This can be very powerful, but requires following strict rules for the sketches to obtain good results.
