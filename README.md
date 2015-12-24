# FreeCAD_Scripts_EVM
My python scripts for FreeCAD

#NURBS   
The ultimate goal is to implement a set of tools to specify points and tangents/normals to generate NURBS surfaces of high continuity. I have some ideas in regards to what constitutes an efficient and intuitive input/interface structure. This is very personal, and cannot address all individual pereferences.

I am learning as i go, so i am trying to 'juice' the most out of the basic NURBS formulations before moving on to more complex forms. The cubic bezier form is the simplest form that can connect two points with specified tangents, so i am currently exploring its limits. The weight control interface is incomplete.

#In this repo:   
-a single .py with all the 'geometry' functions, where i try to use the most basic inputs.   
-individual .fcmacro files that tie the current GUI and selection behavior of FreeCAD to single modeling operations.   
-test model files. Here it gets incredibly messy because i use both git and horrible filenames to track different versions.  These model files are irrelevant to the script structure, in keep them in the repo for my ease of access.   

#the basic design structure is:  
-write a function in BezCubic.py   
-write a GUI wrapper as guioperationx.fcmacro that calls functions in BezCubic.py  
-make a toolbar button   

i don't have any premade toolbars or icons yet.

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
-select 3/4 curves in a loop counterclockwise (surface normal with then point towards you), hit the surface macro button > surface is created.   

The surfaces are 100% controlled by the curves, which are 100% controlled by the sketches. This is very powerful, but requires following strict rules for the sketches to obtain good results.
