"""
Domemaster3D Camera Setup Script V1.4 B10
Created by Andrew Hazelden  andrew@andrewhazelden.com
Based upon the Softimage scripting work of Max Crow

This script makes it easy to start creating fulldome stereoscopic content in Autodesk Softimage.


Version History

Version 1.4 B10
---------------------------
Feb 23, 2014

8.47am rig with names
8.57am cleaning up the script with vars
9.45am adding functions

10am rob lookup background added
10.38am working on python button scripts and import commands
11.52am working on texture connections
12.01pm used vars for nodes and named the connections
12.26pm adding a camera rig variable
12.58pm testing code improvements
1.05pm added 4mm focal length to base camera
1.37pm Added the latlong camera function
4.52pm added starglobe, rob lookup camera, wiki weblink, resolution buttons
5.31pm Worked on pass names

##todo 
In scene anaglyph preview
  set regular camera fov to 4 mm
  set camera separation based upon domeAFL_FOV_Stereo shader
  toggle stereo mode between pre and post roll script

"""



"""
Change the render resolution
"""

def setRenderRes512():
  Application.SetValue("preferences.output_format.preset", 0, "")
  Application.SetValue("preferences.output_format.ir_xres", 512, "")
  Application.SetValue("preferences.output_format.picture_ratio", 1, "")

def setRenderRes1K():
  Application.SetValue("preferences.output_format.preset", 0, "")
  Application.SetValue("preferences.output_format.ir_xres", 1024, "")
  Application.SetValue("preferences.output_format.picture_ratio", 1, "")

def setRenderRes2K():
  Application.SetValue("preferences.output_format.preset", 0, "")
  Application.SetValue("preferences.output_format.ir_xres", 2048, "")
  Application.SetValue("preferences.output_format.picture_ratio", 1, "")

def setRenderRes4K():
  Application.SetValue("preferences.output_format.preset", 0, "")
  Application.SetValue("preferences.output_format.ir_xres", 4096, "")
  Application.SetValue("preferences.output_format.picture_ratio", 1, "")

def setRenderRes8K():
  Application.SetValue("preferences.output_format.preset", 0, "")
  Application.SetValue("preferences.output_format.ir_xres", 8192, "")
  Application.SetValue("preferences.output_format.picture_ratio", 1, "")

def openDomemasterWiki():
  import webbrowser

  # Domemaster Stereo Shader - Wiki Page
  url = 'https://code.google.com/p/domemaster-stereo-shader/w/list'

  # Open URL in new window, raising the window if possible.
  webbrowser.open_new(url)


"""
Find out the path to the sourceimages folder
----------------------
A python function to check the operating system platform and the source images folder. 

"""
def getSourceImagesPath(imageFileName):

  # ---------------------------------------------------------------------
  #Setup the base folder path for the Domemaster3D control maps
  # ---------------------------------------------------------------------

  #Check OS platform for Windows/Mac/Linux Paths
  import platform


  # Find the Domemaster3D Addon folder
  import os
  xsiUserFolder = os.getenv( "XSI_USERHOME" )
  # C:\Users\hazelden\Autodesk\Softimage_2014_SP1

  #This is the base path for the images folder
  baseImagesFolder = ""

  if platform.system()=='Windows':
    #Check if the program is running on Windows 
    # C:\Users\hazelden\Autodesk\Softimage_2014_SP1\Addons\domemaster3D\Application\bitmaps\
    baseImagesFolder =  xsiUserFolder + "\\Addons\\domemaster3D\\Application\\bitmaps\\"
  elif platform.system()== 'win32':
    #Check if the program is running on Windows 32
    baseImagesFolder =  xsiUserFolder + "\\Addons\\domemaster3D\\Application\\bitmaps\\"
  elif platform.system()== 'Linux':
    #Check if the program is running on Linux
    baseImagesFolder =  xsiUserFolder + "/Addons/domemaster3D/Application/bitmaps/"
  elif platform.system()== 'Linux2':
    #Check if the program is running on Linux
    baseImagesFolder =  xsiUserFolder + "/Addons/domemaster3D/Application/bitmaps/"
  else:
    # Create the empty variable as a fallback mode
    baseImagesFolder = ""

  combinedFileAndImagePath = baseImagesFolder + imageFileName

  print "[Domemaster3D is running on a " + platform.system() + " System]"
  print "[Requesting the image file]: " + combinedFileAndImagePath

  return combinedFileAndImagePath


"""
Domemaster3D Fulldome Stereo Rig
--------------------------------
A python function to create a fulldome stereo rig in Softimage.
"""

def createFulldomeStereoRig():

  # Deselect the objects in the scene
  Application.DeselectAll() 

  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------

  #Setup the base folder path for the Domemaster3D control maps
  #Variables
  #separationMapFileTexture = "C:\\Program Files\\Domemaster3D\\sourceimages\\separation_map.png"
  separationMapFileTexture = getSourceImagesPath("separation_map.png")
  turnMapFileTexture = getSourceImagesPath("turn_map.png")

  # Add a stereo camera named "DomeStereoCamera"
  rigName = "DomeStereoCamera"

  rig = str(Application.GetPrimStereoCamera(rigName))
  #  DomeStereoCamera_Root1
  baseRig = rig.replace("_Root", "");
  #  DomeStereoCamera1
  leftRig = rig.replace("_Root", "_Left");
  #  DomeStereoCamera_Left1
  rightRig = rig.replace("_Root", "_Right");
  #  DomeStereoCamera_Right1
  interestRig = rig.replace("_Root", "_Interest");
  #  DomeStereoCamera_Interest1
  print("Stereo Camera Rig:" + rig + " Left: " + leftRig + " Right: " + rightRig + " Interest: " + interestRig )

  # Variable to hold the rig controls name
  rigControls = rig+".Domemaster_camera_controls"
  # DomeStereoCamera_Root1.Domemaster_camera_controls

  # Rotate the camera rig upright
  Application.SetValue(baseRig+ ".kine.global.rotx", 90, "")
  Application.SetValue(baseRig+ ".kine.global.roty", 0, "")
  Application.SetValue(baseRig+ ".kine.global.rotz", 0, "")

  # Snap the rig to the origin
  Application.SetValue(baseRig+ ".kine.global.posx", 0, "")
  Application.SetValue(baseRig+ ".kine.global.posy", 0, "")
  Application.SetValue(baseRig+ ".kine.global.posz", 0, "")

  # Set the camera to use a 4 mm focal length
  Application.SetValue(baseRig+".camera.fov", 154.94, "")

  # Move the center of interest upwards above the origin
  Application.Translate(interestRig, 0, 10, 0, "siAbsolute", "siPivot", "siObj", "siY", "", "", "", "", "", "", "", "", "", 0, "")
  #Application.Translate("DomeStereoCamera_Interest", 0, 10, 0, "siAbsolute", "siPivot", "siObj", "siY", "", "", "", "", "", "", "", "", "", 0, "")

  # Turn off the default Softimage stereo controls
  Application.SetValue(rig+".Stereo.StereoType", 0, "")

  # Add the domeAFL_FOV_Stereo lens shader to the camera rig
  Application.SIAddArrayElement(leftRig+".camera.lensshader")
  Application.SIApplyShaderToCnxPoint2("Softimage.domeAFL_FOV_Stereo.1.0", leftRig+".camera.Item", "", "")
  Application.SetValue(leftRig+".camera.domeAFL_FOV_Stereo.Camera", 1, "")

  Application.SIAddArrayElement(rightRig+".camera.lensshader")
  Application.SIApplyShaderToCnxPoint2("Softimage.domeAFL_FOV_Stereo.1.0", rightRig+".camera.Item", "", "")
  Application.SetValue(rightRig+".camera.domeAFL_FOV_Stereo.Camera", 2, "")

  # Create the user interface controls
  Application.SelectObj(rig, "", "")
  Application.AddProp("Custom_parameter_list", "", "", "Domemaster camera controls", "")
  Application.SelectObj(rigControls, "", "")

  Application.SIAddCustomParameter(rigControls, "Separation", "siDouble", 6, "", 1000000, "", 2053, "", 1000000, "", "")

  Application.SIAddCustomParameter(rigControls, "Field of View", "siDouble", 180, "", 360, "", 2053, "", 360, "", "")

  Application.SIAddCustomParameter(rigControls, "Dome Radius", "siDouble", 360, 1, 1000000, "", 2053, 1, 1000000, "", "")

  Application.SIAddCustomParameter(rigControls, "Dome Tilt", "siDouble", 0, "", 90, "", 2053, "", 90, "", "")

  Application.SIAddCustomParameter(rigControls, "Tilt Compensation", "siDouble", 0, "", 100, "", 2053, "", 100, "", "")

  Application.SIAddCustomParameter(rigControls, "Vertical Mode", "siDouble", 0, "", 100, "", 2053, "", 100, "", "")

  Application.SIAddCustomParameter(rigControls, "Separation Multiplier", "siDouble", 1, "", "", "", 2053, "", 1, "", "")

  Application.SIAddCustomParameter(rigControls, "Turn Multiplier", "siDouble", 1, "", "", "", 2053, "", 1, "", "")

  Application.SIAddCustomParameter(rigControls, "Head Tilt", "siDouble", 0.5, "", "", "", 2053, "", 1, "", "")

  # Link the stereo user interface elements
  Application.CopyPaste(rigControls+".Separation", "", leftRig+".camera.domeAFL_FOV_Stereo.Cameras_Separation", 1)
  Application.CopyPaste(rigControls+".Separation", "", rightRig+".camera.domeAFL_FOV_Stereo.Cameras_Separation", 1)

  Application.CopyPaste(rigControls+".Field_of_View", "", leftRig+".camera.domeAFL_FOV_Stereo.FOV_Angle", 1)
  Application.CopyPaste(rigControls+".Field_of_View", "", rightRig+".camera.domeAFL_FOV_Stereo.FOV_Angle", 1)

  Application.CopyPaste(rigControls+".Dome_Radius", "", leftRig+".camera.domeAFL_FOV_Stereo.Dome_Radius", 1)
  Application.CopyPaste(rigControls+".Dome_Radius", "", rightRig+".camera.domeAFL_FOV_Stereo.Dome_Radius", 1)

  Application.CopyPaste(rigControls+".Dome_Tilt", "", leftRig+".camera.domeAFL_FOV_Stereo.Dome_Tilt", 1)
  Application.CopyPaste(rigControls+".Dome_Tilt", "", rightRig+".camera.domeAFL_FOV_Stereo.Dome_Tilt", 1)

  Application.CopyPaste(rigControls+".Tilt_Compensation", "", leftRig+".camera.domeAFL_FOV_Stereo.Dome_Tilt_Compensation", 1)
  Application.CopyPaste(rigControls+".Tilt_Compensation", "", rightRig+".camera.domeAFL_FOV_Stereo.Dome_Tilt_Compensation", 1)

  Application.CopyPaste(rigControls+".Vertical_Mode", "", leftRig+".camera.domeAFL_FOV_Stereo.Vertical_Mode", 1)
  Application.CopyPaste(rigControls+".Vertical_Mode", "", rightRig+".camera.domeAFL_FOV_Stereo.Vertical_Mode", 1)

  Application.CopyPaste(rigControls+".Separation_Multiplier", "", leftRig+".camera.domeAFL_FOV_Stereo.Cameras_Separation_Map", 1)
  Application.CopyPaste(rigControls+".Separation_Multiplier", "", rightRig+".camera.domeAFL_FOV_Stereo.Cameras_Separation_Map", 1)

  Application.CopyPaste(rigControls+".Turn_Multiplier", "", leftRig+".camera.domeAFL_FOV_Stereo.Head_Turn_Map", 1)
  Application.CopyPaste(rigControls+".Turn_Multiplier", "", rightRig+".camera.domeAFL_FOV_Stereo.Head_Turn_Map", 1)

  Application.CopyPaste(rigControls+".Head_Tilt", "", leftRig+".camera.domeAFL_FOV_Stereo.Head_Tilt_Map", 1)
  Application.CopyPaste(rigControls+".Head_Tilt", "", rightRig+".camera.domeAFL_FOV_Stereo.Head_Tilt_Map", 1)

  # -----------------------------------------------

  # Create the DomeAFL_FOV_Stereo control texture maps
  #baseRig = "DomeStereoCamera"

  # Add the separation map to the left and right cameras
  right_separation_map_color_to_scalar_node  = str(Application.SIApplyShaderToCnxPoint("Conversion\\Color_to_Scalar",  rightRig+".camera.domeAFL_FOV_Stereo.Cameras_Separation_Map", "right_separation_map_color_to_scalar", ""))
  left_separation_map_color_to_scalar_node  =  str(Application.SIApplyShaderToCnxPoint("Conversion\\Color_to_Scalar",  leftRig+".camera.domeAFL_FOV_Stereo.Cameras_Separation_Map", "left_separation_map_color_to_scalar", ""))

  separation_mib_texture_filter_lookup_node = str(Application.CreateShaderFromProgID("mentalray.mib_texture_filter_lookup.1.0", rightRig+".camera", "separation_mib_texture_filter_lookup"))
  Application.SIConnectShaderToCnxPoint(separation_mib_texture_filter_lookup_node+".out", right_separation_map_color_to_scalar_node+".input", False)
  Application.SIConnectShaderToCnxPoint(separation_mib_texture_filter_lookup_node+".out", left_separation_map_color_to_scalar_node+".input", False)
  separationMapFileTexture_node = str(Application.SICreateImageClip(separationMapFileTexture, "", ""))
  Application.SIConnectShaderToCnxPoint("Clips.separation_map_png", separation_mib_texture_filter_lookup_node+".tex", False)
  separation_mib_texture_vector_node  = str(Application.CreateShaderFromProgID("mentalray.mib_texture_vector.1.0", rightRig+".camera", "separation_mib_texture_vector"))
  separation_mib_texture_remap_node  = str(Application.CreateShaderFromProgID("mentalray.mib_texture_remap.1.0", rightRig+".camera", "separation_mib_texture_remap"))
  Application.SetValue(separation_mib_texture_vector_node+".selspace", 4, "")
  Application.SIConnectShaderToCnxPoint(separation_mib_texture_vector_node+".out", separation_mib_texture_remap_node+".input", False)
  Application.SIConnectShaderToCnxPoint(separation_mib_texture_remap_node+".out", separation_mib_texture_filter_lookup_node+".coord", False)

  # -----------------------------------------------

  # Add the turn map to the left and right cameras
  right_turn_map_color_to_scalar_node = str(Application.SIApplyShaderToCnxPoint("Conversion\\Color_to_Scalar", rightRig+".camera.domeAFL_FOV_Stereo.Head_Turn_Map", "right_turn_map_color_to_scalar", ""))
  left_turn_map_color_to_scalar_node = str(Application.SIApplyShaderToCnxPoint("Conversion\\Color_to_Scalar", leftRig+".camera.domeAFL_FOV_Stereo.Head_Turn_Map", "left_turn_map_color_to_scalar", ""))

  #baseRig = "DomeStereoCamera"
  turn_mib_texture_filter_lookup_node = str(Application.CreateShaderFromProgID("mentalray.mib_texture_filter_lookup.1.0", rightRig+".camera", "turn_mib_texture_filter_lookup"))
  Application.SIConnectShaderToCnxPoint(turn_mib_texture_filter_lookup_node+".out", right_turn_map_color_to_scalar_node+".input", False)
  Application.SIConnectShaderToCnxPoint(turn_mib_texture_filter_lookup_node+".out", left_turn_map_color_to_scalar_node+".input", False)
  turnMapFileTexture_node = str(Application.SICreateImageClip(turnMapFileTexture, "", ""))
  Application.SIConnectShaderToCnxPoint("Clips.turn_map_png", turn_mib_texture_filter_lookup_node+".tex", False)
  turn_mib_texture_vector_node  = str(Application.CreateShaderFromProgID("mentalray.mib_texture_vector.1.0", rightRig+".camera", "turn_mib_texture_vector"))
  turn_mib_texture_remap_node  = str(Application.CreateShaderFromProgID("mentalray.mib_texture_remap.1.0", rightRig+".camera", "turn_mib_texture_remap"))
  Application.SetValue(turn_mib_texture_vector_node+".selspace", 4, "")
  Application.SIConnectShaderToCnxPoint(turn_mib_texture_vector_node+".out", turn_mib_texture_remap_node+".input", False)
  Application.SIConnectShaderToCnxPoint(turn_mib_texture_remap_node+".out", turn_mib_texture_filter_lookup_node+".coord", False)

 # -----------------------------------------------

  # Create and assign render passes for the left and right cameras
  Application.CreatePass("", "", "")
  Application.SetValue("Passes.Pass.Name", leftRig, "")
  Application.SetValue("Passes."+leftRig+".Camera", leftRig, "")
  Application.SetValue("Passes."+leftRig+".Main.Filename", "DomeLeftCam\\[Pass]_[Framebuffer]", "")

  Application.CreatePass("", "", "")
  Application.SetValue("Passes.Pass.Name", rightRig, "")
  Application.SetValue("Passes."+rightRig+".Camera", rightRig, "")
  Application.SetValue("Passes."+rightRig+".Main.Filename", "DomeRightCam\\[Pass]_[Framebuffer]", "")



"""
Domemaster3D createDomeAFL_FOV_Camera
----------------------
A python function to create a domeAFL_FOV lens shader and attach it to a camera.
"""	
def createDomeAFL_FOV_Camera():

 # Deselect the objects in the scene
  Application.DeselectAll() 

  # Add a camera named "domeAFL_FOV_Camera"
  rigName = "domeAFL_FOV_Camera"
  rig = str(Application.GetPrimCamera("", rigName, "", "", "", ""))
  #  domeAFL_FOV_Camera_Root1
  baseRig = rig.replace("_Root", "");
  #  domeAFL_FOV_Camera1
  interestRig = rig.replace("_Root", "_Interest");
  #  domeAFL_FOV_Camera_Interest1
  print("Fulldome Camera Rig Name: " + rig)

  # Rotate the camera rig upright
  Application.SetValue(baseRig+ ".kine.global.rotx", 90, "")
  Application.SetValue(baseRig+ ".kine.global.roty", 0, "")
  Application.SetValue(baseRig+ ".kine.global.rotz", 0, "")

  # Set the camera to use a 4 mm focal length
  Application.SetValue(baseRig+".camera.fov", 154.94, "")

  # Move the center of interest upwards above the origin
  Application.Translate(interestRig, 0, 10, 0, "siAbsolute", "siPivot", "siObj", "siY", "", "", "", "", "", "", "", "", "", 0, "")

  # Add the domeAFL_FOV_Stereo lens shader to the camera
  Application.SIAddArrayElement(baseRig+".camera.lensshader")
  #Application.SIApplyShaderToCnxPoint2("Softimage.domeAFL_FOV.1.0", baseRig+".camera.Item", "", "")
  Application.SIApplyShaderToCnxPoint2("Softimage.domeAFL_FOV_Stereo.1.0", baseRig+".camera.Item", "", "")

  #Make sure the fisheye view is set to center
  Application.SetValue( baseRig+".camera.domeAFL_FOV_Stereo.Camera", 0, "")

  # Create and assign render passes for the camera
  Application.CreatePass("", "", "")
  Application.SetValue("Passes.Pass.Name", baseRig, "")
  Application.SetValue("Passes."+baseRig+".Camera",  baseRig, "")
  Application.SetValue("Passes."+baseRig+".Main.Filename", "DomeFOVCam\\[Pass]_[Framebuffer]", "")


"""
Domemaster3D createDomeAFL_WxH_Camera
----------------------
A python function to create a domeAFL_WxH lens shader and attach it to a camera.
"""	
def createDomeAFL_WxH_Camera():

 # Deselect the objects in the scene
  Application.DeselectAll() 

  # Add a camera named "domeAFL_WxH_Camera"
  rigName = "domeAFL_WxH_Camera"
  rig = str(Application.GetPrimCamera("", rigName, "", "", "", ""))
  #  DomeStereoCamera_Root1
  baseRig = rig.replace("_Root", "");
  #  DomeStereoCamera1
  interestRig = rig.replace("_Root", "_Interest");
  #  DomeStereoCamera_Interest1
  print("Fulldome Camera Rig Name: " + rig)

  # Rotate the camera rig upright
  Application.SetValue(baseRig+ ".kine.global.rotx", 90, "")
  Application.SetValue(baseRig+ ".kine.global.roty", 0, "")
  Application.SetValue(baseRig+ ".kine.global.rotz", 0, "")

  # Set the camera to use a 4 mm focal length
  Application.SetValue(baseRig+".camera.fov", 154.94, "")

  # Move the center of interest upwards above the origin
  Application.Translate(interestRig, 0, 10, 0, "siAbsolute", "siPivot", "siObj", "siY", "", "", "", "", "", "", "", "", "", 0, "")

  # Add the domeAFL_FOV_Stereo lens shader to the camera
  Application.SIAddArrayElement(baseRig+".camera.lensshader")
  Application.SIApplyShaderToCnxPoint2("Softimage.domeAFL_WxH.1.0", baseRig+".camera.Item", "", "")

  # Create and assign render passes for the camera
  Application.CreatePass("", "", "")
  Application.SetValue("Passes.Pass.Name", baseRig, "")
  Application.SetValue("Passes."+baseRig+".Camera",  baseRig, "")
  Application.SetValue("Passes."+baseRig+".Main.Filename", "DomeWxHCam\\[Pass]_[Framebuffer]", "")


"""
Domemaster3D createLatLong_Camera
----------------------
A python function to create a latitude longitude lens shader and attach it to a camera.
"""	
def createLatLong_Camera():

 # Deselect the objects in the scene
  Application.DeselectAll() 

  # Add a camera named "latlong_lens"
  rigName = "LatLong_Camera"
  rig = str(Application.GetPrimCamera("", rigName, "", "", "", ""))
  #  DomeStereoCamera_Root1
  baseRig = rig.replace("_Root", "");
  #  DomeStereoCamera1
  interestRig = rig.replace("_Root", "_Interest");
  #  DomeStereoCamera_Interest1
  print("Fulldome Camera Rig Name: " + rig)

  # Rotate the camera rig upright
  Application.SetValue(baseRig+ ".kine.global.rotx", 0, "")
  Application.SetValue(baseRig+ ".kine.global.roty", 0, "")
  Application.SetValue(baseRig+ ".kine.global.rotz", 0, "")

  # Set the camera to use a 4 mm focal length
  Application.SetValue(baseRig+".camera.fov", 154.94, "")

  # Move the center of interest upwards above the origin
  Application.Translate(interestRig, 0, 10, 0, "siAbsolute", "siPivot", "siObj", "siY", "", "", "", "", "", "", "", "", "", 0, "")

  # Add the latlong_lens lens shader to the camera
  Application.SIAddArrayElement(baseRig+".camera.lensshader")
  Application.SIApplyShaderToCnxPoint2("Softimage.latlong_lens.1.0", baseRig+".camera.Item", "", "")

  # Create and assign render passes for the camera
  Application.CreatePass("", "", "")
  Application.SetValue("Passes.Pass.Name", baseRig, "")
  Application.SetValue("Passes."+baseRig+".Camera",  baseRig, "")
  Application.SetValue("Passes."+baseRig+".Main.Filename", "LatLongCam\\[Pass]_[Framebuffer]", "")


"""
Domemaster3D createRobLookup
----------------------
A python function to create a mental ray screen space texture 
and connect it to a robLookupBackground lens shader. 
"""

def createRobLookup():
    
  #Setup the base folder path for the Domemaster3D control maps
  #Variables
  #separationMapFileTexture = "C:\\Program Files\\Domemaster3D\\sourceimages\\separation_map.png"
  separationMapFileTexture = getSourceImagesPath("separation_map.png")
  print "[Loading Separation Map]: " + separationMapFileTexture 

 # Deselect the objects in the scene
  Application.DeselectAll() 

  # Add a camera named "robLookupCamera"
  rigName = "robLookupCamera"
  rig = str(Application.GetPrimCamera("", rigName, "", "", "", ""))
  #  DomeStereoCamera_Root1
  baseRig = rig.replace("_Root", "");
  #  DomeStereoCamera1
  interestRig = rig.replace("_Root", "_Interest");
  #  DomeStereoCamera_Interest1
  print("Fulldome Camera Rig Name: " + rig)

  # Rotate the camera rig upright
  Application.SetValue(baseRig+ ".kine.global.rotx", 90, "")
  Application.SetValue(baseRig+ ".kine.global.roty", 0, "")
  Application.SetValue(baseRig+ ".kine.global.rotz", 0, "")

  # Set the camera to use a 4 mm focal length
  Application.SetValue(baseRig+".camera.fov", 154.94, "")

  # Move the center of interest upwards above the origin
  Application.Translate(interestRig, 0, 10, 0, "siAbsolute", "siPivot", "siObj", "siY", "", "", "", "", "", "", "", "", "", 0, "")

  # Add the rob_lookup_background lens shader to the camera
  Application.SIAddArrayElement(baseRig+".camera.lensshader")
  Application.SIApplyShaderToCnxPoint2("Softimage.rob_lookup_background.1.0", baseRig+".camera.Item", "", "")

  # Add a screen space separation map to the robLookupCamera
  Application.SIApplyShaderToCnxPoint("Conversion\\Color_to_Scalar",  baseRig+".camera.rob_lookup_background.tex", "", "")
  separation_map_color_to_scalar_node  = str(Application.SIApplyShaderToCnxPoint("Conversion\\Color_to_Scalar",  baseRig+".camera.rob_lookup_background.tex", "separation_map_color_to_scalar", ""))

  separation_mib_texture_filter_lookup_node = str(Application.CreateShaderFromProgID("mentalray.mib_texture_filter_lookup.1.0", baseRig+".camera", "separation_mib_texture_filter_lookup"))
  Application.SIConnectShaderToCnxPoint(separation_mib_texture_filter_lookup_node+".out", separation_map_color_to_scalar_node+".input", False)
  Application.SIConnectShaderToCnxPoint(separation_mib_texture_filter_lookup_node+".out", separation_map_color_to_scalar_node+".input", False)
  separationMapFileTexture_node = str(Application.SICreateImageClip(separationMapFileTexture, "", ""))
  Application.SIConnectShaderToCnxPoint("Clips.separation_map_png", separation_mib_texture_filter_lookup_node+".tex", False)
  separation_mib_texture_vector_node  = str(Application.CreateShaderFromProgID("mentalray.mib_texture_vector.1.0", baseRig+".camera", "separation_mib_texture_vector"))
  separation_mib_texture_remap_node  = str(Application.CreateShaderFromProgID("mentalray.mib_texture_remap.1.0", baseRig+".camera", "separation_mib_texture_remap"))
  Application.SetValue(separation_mib_texture_vector_node+".selspace", 4, "")
  Application.SIConnectShaderToCnxPoint(separation_mib_texture_vector_node+".out", separation_mib_texture_remap_node+".input", False)
  Application.SIConnectShaderToCnxPoint(separation_mib_texture_remap_node+".out", separation_mib_texture_filter_lookup_node+".coord", False)


  # Create and assign render passes for the camera
  Application.CreatePass("", "", "")
  Application.SetValue("Passes.Pass.Name", baseRig, "")
  Application.SetValue("Passes."+baseRig+".Camera",  baseRig, "")
  Application.SetValue("Passes."+baseRig+".Main.Filename", "robLookupCamera\\[Pass]_[Framebuffer]", "")



"""
Find out the path to the models folder
----------------------
A python function to check the operating system platform and the models folder. 

"""
def getModelsPath(modelFileName):
  # ---------------------------------------------------------------------
  #Set up the base folder path for the Domemaster3D models
  # ---------------------------------------------------------------------

  #Check OS platform for Windows/Mac/Linux Paths
  import platform

  # Find the Domemaster3D Addon folder
  import os
  xsiUserFolder = os.getenv( "XSI_USERHOME" )
  # C:\Users\hazelden\Autodesk\Softimage_2014_SP1

  #This is the base path for the images folder
  baseModelsFolder = ""

  if platform.system()=='Windows':
    #Check if the program is running on Windows 
    # C:\Users\hazelden\Autodesk\Softimage_2014_SP1\Addons\domemaster3D\Data\
    baseModelsFolder = xsiUserFolder + "\\Addons\\domemaster3D\\Data\\"
  elif platform.system()== 'win32':
    #Check if the program is running on Windows 32
    baseModelsFolder = xsiUserFolder + "\\Addons\\domemaster3D\\Data\\"
  elif platform.system()== 'Linux':
    #Check if the program is running on Linux
    baseModelsFolder = xsiUserFolder + "/Addons/domemaster3D/Data/"
  elif platform.system()== 'Linux2':
    #Check if the program is running on Linux
    baseModelsFolder = xsiUserFolder + "/Addons/domemaster3D/Data/"
  else:
    # Create the empty variable as a fallback mode
    baseModelsFolder = ""

  combinedFileAndModelPath = baseModelsFolder + modelFileName

  print "[Domemaster3D is running on a " + platform.system() + " System]"
  print "[Requesting the model file]: " + combinedFileAndModelPath

  return combinedFileAndModelPath


"""
Create a starglobe
---------------------------
A python function to create a 8K textured starglobe with a mia_material_x_passes shading network.
"""
def createStarglobe():
  import os

  # ---------------------------------------------------------------------
  # Set up the base folder path for the Domemaster3D textures
  # ---------------------------------------------------------------------
  # Set the file texture variables to "" if you don't want a file to be specified
  #StarglobeMapFileTexture = ""

  StarglobeMapFileTexture = getSourceImagesPath("starglobe_quadsphere_2k.jpg")
  #StarglobeMapFileTexture = getModelsPath("starglobe_quadsphere_8k.jpg")

  starglobe_material_name = "starglobe_material"

  # Get the Domemaster3D Addons path for the obj mesh
  StarglobeModelFile = getSourceImagesPath("starglobe_mesh.obj")
  #StarglobeModelFile = getModelsPath("starglobe_mesh.obj")

  # Remove the old starglobe model and texture
  #Application.DeleteObj("starglobe_mesh_starglobe_mesh_polyStarglobe.Scene_Material.starglobe_material")

  # Load the quads based starglobe sphere model
  starglobe_mesh_file = str(Application.ObjImport(StarglobeModelFile, 1, 0, False, True, False, True))
  # starglobe_mesh_starglobe_mesh_polyStarglobe1
  print ("Starglobe Mesh: " + starglobe_mesh_file)

  # Scale the starglobe model to 25 units
  #Application.Scale(starglobe_mesh_file, 25, 25, 25, "siAbsolute", "siPivot", "siObj", "siXYZ", "", "", "", "", "", "", "", 0, "")

 # Add a mental ray mia_material_x shader
  Application.CreateShaderFromProgID("mentalray.mia_material_x.1.0", "Sources.Materials.DefaultLib.Scene_Material", starglobe_material_name)
  Application.SIConnectShaderToCnxPoint("Sources.Materials.DefaultLib.Scene_Material."+starglobe_material_name+".result", "Sources.Materials.DefaultLib.Scene_Material.surface", False)

  # Set the mia_material_x properties to be a matte material
  Application.SetValue("Sources.Materials.DefaultLib.Scene_Material."+starglobe_material_name+".refl_gloss", 0, "")
  Application.SetValue("Sources.Materials.DefaultLib.Scene_Material."+starglobe_material_name+".reflectivity", 0, "")
  Application.SetValue("Sources.Materials.DefaultLib.Scene_Material."+starglobe_material_name+".diffuse_roughness", 0, "")
  Application.SetValue("Sources.Materials.DefaultLib.Scene_Material."+starglobe_material_name+".diffuse_weight", 1, "")

  # Set the diffuse color to black
  Application.SetValue("Sources.Materials.DefaultLib.Scene_Material."+starglobe_material_name+".diffuse.red", 0, "")
  Application.SetValue("Sources.Materials.DefaultLib.Scene_Material."+starglobe_material_name+".diffuse.green", 0, "")
  Application.SetValue("Sources.Materials.DefaultLib.Scene_Material."+starglobe_material_name+".diffuse.blue", 0, "")

  # Make the mia material shader act like an incandescent/surface shader material
  Application.SIApplyShaderToCnxPoint("Image", "Sources.Materials.DefaultLib.Scene_Material."+starglobe_material_name+".additional_color", "", "")
  Application.SICreateImageClip(StarglobeMapFileTexture, "", "")
  starglobeMapFileTexture_node = str(Application.SIConnectShaderToCnxPoint("Clips.starglobe_quadsphere_2k_jpg", "Sources.Materials.DefaultLib.Scene_Material.Image.tex", False))
  #starglobeMapFileTexture_node = str(Application.SIConnectShaderToCnxPoint("Clips.starglobe_quadsphere_8k_jpg", "Sources.Materials.DefaultLib.Scene_Material.Image.tex", False))

  #note cutout opacity could be used to make the night sky alpha channel transparent or solid

  #Optional Light Linking

  #Set the mia_material_x_passes shader to ignore the illumination from the lights in the scene with "light linking"
  #starglobe_mia.mode 0 = Custom Linking
  #starglobe_mia.mode 1 = Inclusive Linking
  #starglobe_mia.mode 2 = Exclusive Linking
  #starglobe_mia.mode 4 = Maya Linking

  #Note: All scene lights are skipped by default with "Exclusive linking" mode 2
  Application.SetValue("Sources.Materials.DefaultLib.Scene_Material."+starglobe_material_name+".mode", 2, "")


  #Set the views to textured
  Application.SetDisplayMode("Camera", "textured")


# -----------------------------------------------

# Create the latlong camera
#createLatLong_Camera()

# Create the fulldome stereo camera
#createFulldomeStereoRig()

# Create the FOV camera
#createDomeAFL_FOV_Camera()

# Create the WxH camera
#createDomeAFL_WxH_Camera()

# Create a screen space texture
#createRobLookup()

# Change the output resolution
#setRenderRes2K()

# Open the Wiki page
#openDomemasterWiki()

# Create a starglobe
createStarglobe()

