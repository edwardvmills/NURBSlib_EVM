# FreeCAD_Scripts_EVM
My python scripts for FreeCAD

#NURBS   
The ultimate goal is to implement a set of tools to specify points and tangents/normals to generate NURBS surfaces of high continuity. I have some ideas in regards to what constitutes an efficient and intuitive input/interface structure. This is very personal, and cannot address all individual pereferences.

I am learning as i go, so i am trying to 'juice' the most out of the basic NURBS formulations before moving on to more complex forms. The cubic bezier form is the simplest form that can connect two points with specified tangents, so i am currently exploring its limits. The weight control interface is incomplete.

#In this repo:   
-a single .py with all the 'geometry' functions, where i try to use the most basic inputs.   
-individual .fcmacro files that tie the current GUI and selection behavior of FreeCAD to single modeling operations.   
-test model files. Here it gets incredibly messy because i use both git and horrible filenames to track different versions. These model files are irrelevant to the script structure, in keep them in the repo for my ease of access.   

#the basic flow for the scripts is:  
-write a function in BezCubic.py   
-write a GUI wrapper   
-make a toolbar button   

i don't have any premade toolbars or icons yet.

I'm aware of the plugin loader tool that's available, and i wish i was smart/dedicated enough to use it, but i'm not :)
