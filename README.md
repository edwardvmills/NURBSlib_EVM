## NURBSlib_EVM
My python scripts for creating surfaces in [FreeCAD](http://freecadweb.org/).   

This is the rough workflow prototyping phase. most basic objects are now parametric. The workflow is based on sketches drawn in FreeCAD 0.17 or later. The sketches are used to comtrol NURBS curves and surfaces. 

![Best example of current state](https://github.com/edwardvmills/NURBSlib_EVM/blob/master/development_FC_models/parametric/begin%20transition%20to%200.17/Bezier%20primary%20Surface%20Volume%2041-07.bmp.png?raw=true)  

The ultimate goal is to implement a set of tools that require *very few points and tangents/normals* to generate NURBS surfaces of high continuity. I have some ideas as to what constitutes an efficient and intuitive input/interface structure. This is very personal, and cannot address all individual preferences. 

Ideally, the user interaction with the points/normals would be analogous to manipulating a coarse mesh, like subdivision surfaces. The main difference with subdivision surfaces being that with full NURBS, we can have perfect conics, no intrinsic continuity limits, and the 'handles' <i>stay on the surface itself</i>. So when we dimension/constrain the handles, we are dimensioning the surface itself.

What this means in practice is that eventually the user will not need to know *anything* about control points, knot vectors, or weights. At this stage however, a minimum understanding of control points is still necessary to use the tools.

**These are not the 'classic' surfacing tools like sweep, loft, blend, trim, etc**, although there are many parallels.    
FreeCAD already has some of these tools in the Part module and i believe the PartDesign module is slated to get improved versions soon. OpenCascade itself already has all of these functions built in, but c++ is beyond my skills right now, so i'll stick yo python. 

All scripts (file extension .py and .fcmacro) in this repository are offered under the terms of the [GPLv3](http://www.gnu.org/licenses/gpl-3.0.en.html)   
All models (file extension .fcstd). and icon files (file extension .svg) in this repository are offered under the terms of [CC-BY](http://creativecommons.org/licenses/by/2.0/)

Current state can be seen [here](http://forum.freecadweb.org/viewtopic.php?f=24&t=19736), in the FreeCAD forum


ALL INFO BELOW IS OUT OF DATE AS OF 2017 - 01 -20 (the specifics are incorrect but the general lines are still valid)

###In this repo:   
-a single .py with all the 'geometry' functions, where i try to use the most basic inputs.   
-individual .fcmacro files that tie the current GUI and selection behavior of FreeCAD to single modeling operations.   
-various utility .fcmacro functions to assist in creating sketches ('handles') to pass to the NURBS tools.   
-test FreeCAD model files. These model files are irrelevant to the scripts, i keep them in the repo for my ease of access. 
___
###Setup   
-from the top level of the repository, take NURBSlib_EVM.py, all  *.fcmacro files, and the icons folder
-put them somewhere FreeCAD can find them   
-link the fcmacro scripts to icons, descriptions, tooltips, etc. 
-put all those GUI macros in toolbars.   
-add that toolbar to the PartDesign workbench. The raw material will be PartDesign sketches, so this is a good place to put the toolbars for the time being.   

[instructions for toolbars/macros in FreeCAD](http://freecadweb.org/wiki/index.php?title=Macros) 

###Usage (basic knowledge of the FreeCAD PartDesign Sketcher is required)  
More details on usage will be made available [here](http://edwardvmills.github.io/NURBSlib_EVM/) as time permits.

-draw sketches of lines/circles (read the curve macros to see what inputs they want)   
-select those lines/circles in the order specified by the macro, then hit the macro button > curve is created.   
-select 3/4 curves in a loop counterclockwise (surface normal will then point towards you), hit the surface macro button > surface is created.

The surfaces are 100% controlled by the curves, which are 100% controlled by the sketches. This can be very powerful, but requires following strict rules for the sketches to obtain good results. Utilities to control the sketches and continuity are in various stages of planning/prototyping. I suspect much could already be done by using spreadsheets and expressions.
___
###NURBS in general, and what these scripts are trying to do   

For now, my focus is on skinning sets of 3 or 4 curves in a loop. 

The skinning routines should be   
-*repeatable*: produce the same result for the same inputs   
-*consistent*: produce a scaled result for a scaled input.   

The seams joining adjacent surfaces should always have the same level of continuity as the adjacent curves at the surface corners.

I am learning as i go, so i am trying to 'juice' the most out of the basic NURBS formulations before moving on to more complex forms. High degrees and complex knot vectors give great smoothness, but few of the control points correspond to actual surface points, so they are challenging to fit among other engineering forms and constrain correctly.

The cubic bezier form is the simplest form that can connect two points with specified tangents (G1), and i am exploring its limits. The weight control interface is incomplete, but curve weights are incorporated into the surfaces in a crude way. Arcs can be converted to rational Bezier and used in surfaces. I have a basic quadrilateral surface patch, and a rudimentary triangular suface patch (one collapsed edge/corner). It is theoretically possible to modify the inner control points and weights of a bezier to control the curvature (G2) across the seams in some cases, but this requires manipulating several control points at once, and maintaining tangent continuity is hard to begin with.

For now, the Bezier curves and surfaces are considered to be 'rough drafts' of the final surfaces. Easy to specify, cheap to tesselate. Sometimes they may even be adequate to patch a hole in a shell, if the surrounding surfaces are simple.

In order to have isolated curvature at each curve endpoint, i made a 6 control point cubic curve and associated 6X6 surface. This surface type does not have a triangle version yet. Included are utilites to convert cubic Bezier and arcs to this curve type.   

This will open up the possibility of using the 3rd and 4th points to control start and end curvature respectively. This can be done without interfering with the use of the 2nd and 5th control points to set tangents. Right now the curvature matching must be done by hand, but for any particular value of curvature desired at a curve connection, there are many possible control points positions. These additional degrees of freedom will (i hope) allow the possibility of controlling the derivative of curvature (highlight flow).

