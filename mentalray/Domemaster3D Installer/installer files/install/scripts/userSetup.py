# ---------------------------------------------------------------------
# Domemaster3D Startup Code V1.4 Build 2
# ---------------------------------------------------------------------

#Find the name of the stereo camera rig
def findDomeRig():
  import maya.cmds as cmds

  rigs = cmds.stereoRigManager(listRigs=True)
  print ("Stereo Camera rigs:")
  for rig in rigs:
    defs = cmds.stereoRigManager(rigDefinition=rig)
    print 'Rig "'+ rig +'": (language '+defs[0]+') create callback: '+defs[1]
    #Check for
    if (rig == "DomeStereoCamera"):
      return 1
      
  return 0

def getMayaVersion():
  import maya.mel as mel
  import maya.cmds as cmds

  #Check what Maya version is active

  #Check if we are running Maya 2011 or higher
  mayaVersion = mel.eval("getApplicationVersionAsFloat;")

  #Test this GUI using the Maya 2010 - non-docked GUI mode
  #mayaVersion = 2010;

  #Write out the current Maya version number
  print("Maya " + str(mayaVersion) + " detected.\n")
  
  return mayaVersion
  
#Check if a DomeStereoCamera rig exists in the scene  
def addNewDomeRig():
  import maya.mel as mel
  import maya.cmds as cmds
  import domeStereoRig as domeStereoRig

   #Check what Maya version is active
  mayaVersion = getMayaVersion()
  if (mayaVersion >= 2011):
    # Add the extra feature set for Maya 2011+
    if (findDomeRig() == 0):
      print ("A DomeStereoCamera rig has been added to the stereoRigManager.")
      # Register the DomeStereoCamera rig type
      # add[rig, language, createProcedure]
      # cameraSetFunc=[rig,callbback] 
      # Add the custom rig
      cmds.evalDeferred("cmds.stereoRigManager(add=['DomeStereoCamera', 'Python', 'domeStereoRig.createRig'])")
      # Add the custom callback set for Maya 2011+
      cmds.evalDeferred("cmds.stereoRigManager(cameraSetFunc=['DomeStereoCamera','domeStereoRig.attachToCameraSet'] )")
      # Make the new rig the default rig
      cmds.evalDeferred("cmds.stereoRigManager(defaultRig='DomeStereoCamera')")
    else:
      print ("A DomeStereoCamera rig already exists in the stereoRigManager.")
  else:
   # Maya 2010 or older was detected
   print ("The Domemaster3D stereo rig feature requires Maya 2011 and newer.")
    
# Load the Domemaster3D menu system in the rendering menu set    
def addNewDomeMenu():
  import maya.mel as mel
  print("Loading the Domemaster3D menu items...")
  mel.eval('source "domeMenu.mel";')
  mel.eval('createDomemaster3DMenu();')

#----------------------------------------------------------------------------
# Main Domemaster3D Startup function  
#----------------------------------------------------------------------------

import maya.cmds as cmds

# Add the extra feature set for Maya 2011+
mayaVersion = getMayaVersion()
if (mayaVersion >= 2011):
  # Add the Domemaster3D Stereo camera Rig
  import domeStereoRig as domeStereoRig
  # Make sure the stereo plug-in is loaded
  cmds.evalDeferred("cmds.loadPlugin('stereoCamera', quiet=True)")
  cmds.evalDeferred("addNewDomeRig()")

# Load the Domemaster3D menu system in the rendering menu set
cmds.evalDeferred("addNewDomeMenu()")

# Make sure the mental ray plugin was loaded
if not (cmds.pluginInfo("Mayatomr",q=True,loaded=True)):
    cmds.loadPlugin("Mayatomr")
else:
    pass

# ---------------------------------------------------------------------
# End Domemaster3D Startup Code
# ---------------------------------------------------------------------
