"""
Domemaster3D Camera Setup Script V1.4
Created by Andrew Hazelden  andrew@andrewhazelden.com

This script makes it easy to start creating fulldome stereoscopic content in Autodesk Maya.

------------------------------------------------------------------------------

Version History

Version 1.4
---------------
Oct 6, 2013

Renamed the fulldome rig creation script to domeCamera.py for clarity.
This script is compatible with the new StereoRigEditor based stereo fulldome rig

Version 1.3.5
---------------
Sept 27, 2013
Added features for previewing the dome radius (zero parallax zone), field of view, and safe viewing volumes

Reorganized the python scripts to put the domeAFL_FOV code with the domeAFL_FOV_Stereo camera code 

Version 1.3.4
---------------
Released June 27, 2013
Updated the the Automagic tool's dome grid color to a brighter yellow value. This makes the grid more visible in a Physical Sun & Sky scene.

Added a new HELP icon to the Maya Shelf toolset. This shelf item loads the domemaster stereo shader wiki page.


Version 1.3.3
---------------
Released May 30, 2013
Updated the default locator scale.

Fixed the dome ramp shelf tool item so the default ramp texture preset is applied when the tool is run multiple times.

Updated source image paths for Maya 2010 compatibility

Version 1.3.2
---------------
Released April 16, 2013
Edited the default camera connections for the lens shaders to work with the modified versions of the maya createMentalRayIndirectLightingTab.mel & AEmia_physicalskyTemplate.mel scripts. This fixes the problem of the Physical Sky & Sun system overwriting the first .miLensShader input on cameras in the scene.

The location of the default domemaster control map textures is now in the Program Files\Domemaster3D\sourceimages folder on Windows or the /Applications/Domemaster3D/sourceimages folder on Mac OS X. The Domemaster3D shelf tools have been updated to link to the new sourceimages folder.

Version 1.3
------------
Released Nov 4, 2012
Moved FOV and WxH functions into domeMaterial.py, changed the default lens shader connections to support the mental ray sky and sun system.


Version 1.1
------------
Released Aug 14, 2012
Improved python code and made it Maya 2010 compatible.


Version 1.0
------------
Released Aug 6, 2012
First release of the Domemaster3D auto-setup python scripts.

------------------------------------------------------------------------------

Installation instructions

Step 1.
Place the python scripts "domeCamera.py" and "__init__.py" 
in your Maya scripts folder.

Step 2.
Copy the Domemaster3D separation_map.png & turn_map.png into your 
current Maya project's sourceimages folder.

Step 3.
Source the python script in Maya using the python command:
import domeCamera as domeCamera

Step 4.
Test your current domemaster3D installation using the python command:
domeCamera.autosetup()

------------------------------------------------------------------------------

Domemaster3D AutoSetup
A python function to create a fulldome stereo rig and test grid in Maya.

Run using the command:
import domeCamera as domeCamera
domeCamera.autosetup()

------------------------------------------------------------------------------

Domemaster3D Fulldome Stereo Rig
A python function to create a fulldome stereo rig in Maya.

Run using the command:
import domeCamera as domeCamera
domeCamera.createFulldomeStereoRig()

------------------------------------------------------------------------------

Domemaster3D createDomeAFL_WxH_Camera
A python function to create a domeAFL_WxH lens shader and attach it to a camera.

Run using the command:
import domeMaterial as domeMaterial
domeMaterial.createDomeAFL_WxH_Camera()

------------------------------------------------------------------------------

Domemaster3D createDomeAFL_FOV_Camera
A python function to create a domeAFL_FOV lens shader and attach it to a camera.

Run using the command:
import domeMaterial as domeMaterial
domeMaterial.createDomeAFL_FOV_Camera()

------------------------------------------------------------------------------

Domemaster3D DomeGrid test background 
A python function to create a hemispherical yellow test grid in Maya. 

Run using the command:
import domeCamera as domeCamera
domeCamera.createDomeGrid()

------------------------------------------------------------------------------

Domemaster3D createTestShapes
A python function to create a test sphere and cube in Maya. 

Run using the command:
import domeCamera as domeCamera
domeCamera.createTestShapes()

------------------------------------------------------------------------------

Domemaster3D createRobLookup
A python function to create a mental ray screen space texture 
and connect it to a robLookupBackground lens shader. 

Run using the command:
import domeCamera as domeCamera
domeCamera.createRobLookup()
------------------------------------------------------------------------------

Domemaster3D createDomeRampTexture
A python function to create a mental ray screen space ramp texture 
and connect it to a robLookupBackground lens shader.

Run using the command:
import domeCamera as domeCamera
domeCamera.createDomeRampTexture()

------------------------------------------------------------------------------

Domemaster3D SetRenderRes
A python function to setup the basic mental ray 2K x 2K square render settings. 

Run using the command:
import domeCamera as domeCamera
domeCamera.setRenderRes()

------------------------------------------------------------------------------

"""


"""
Show the Domemaster Wiki
--------------------------------
Loads the wiki page in your default web browser

Run using the command:
print("Open the Domemaster Wiki Page")
import domeCamera as domeCamera
domeCamera.openDomemasterWiki()

print("Open the Domemaster NING Group")
import domeCamera as domeCamera
domeCamera.openDomemasterNing()

print("Open the Domemaster Downloads Page")
import domeCamera as domeCamera
domeCamera.openDomemasterDownloads()


"""

def openDomemasterWiki():
	import webbrowser
	
	# Domemaster Stereo Shader - Wiki Page
	url = 'https://code.google.com/p/domemaster-stereo-shader/w/list'
	
	# Open URL in new window, raising the window if possible.
	webbrowser.open_new(url)
	
	
def openDomemasterNing():
	import webbrowser
	
	# Domemaster NING Group
	url = 'http://fulldome.ning.com/forum/topics/stereoscopic-domemaster-images'
	
	# Open URL in new window, raising the window if possible.
	webbrowser.open_new(url)


def openDomemasterDownloads():
	import webbrowser
	
	# Domemaster Stereo Shader - Download Page
	url = 'https://code.google.com/p/domemaster-stereo-shader/downloads/list'
	
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

  #This is the base path for the images folder
  baseImagesFolder = ""

  if platform.system()=='Windows':
    #Check if the program is running on Windows 
    baseImagesFolder = "C:/Program Files/Domemaster3D/sourceimages/"
  elif platform.system()== 'win32':
    #Check if the program is running on Windows 32
    baseImagesFolder = "C:/Program Files (x86)/Domemaster3D/sourceimages/"
  elif platform.system()== 'Darwin':
    #Check if the program is running on Mac OS X
    baseImagesFolder = "/Applications/Domemaster3D/sourceimages/"
  elif platform.system()== 'Linux':
    #Check if the program is running on Linux
    baseImagesFolder = "/usr/bin/Domemaster3D/sourceimages/"
  elif platform.system()== 'Linux2':
    #Check if the program is running on Linux
    baseImagesFolder = "/usr/bin/Domemaster3D/sourceimages/"
  else:
    # Create the empty variable as a fallback mode
    baseImagesFolder = ""

  combinedFileAndImagePath = baseImagesFolder + imageFileName

  print "[Domemaster3D is running on a " + platform.system() + " System]"
  print "[Requesting the image file]: " + combinedFileAndImagePath

  return combinedFileAndImagePath



"""
Domemaster3D AutoSetup
----------------------
A python function to create a fulldome stereo rig and test grid in Maya. 

"""
def autosetup():
  setRenderRes()
  createFulldomeStereoRig()
  createDomeGrid()
  createTestShapes()


"""
Domemaster3D SetRenderRes
----------------------
A python function to setup the basic mental ray 2K x 2K square render settings. 

"""

def setRenderRes():
  import maya.mel as mel
  import maya.cmds as cmds
  
  fulldomeRenderWidth = 2048
  fulldomeRenderHeight = 2048
  
  #Set the active renderer to mental ray to avoid Hypershade red node errors 
  mel.eval("setCurrentRenderer mentalRay")
  
  #---------------------------------------------------------------------
  # Setup the default render settings for a square domemaster image output
  # ---------------------------------------------------------------------
  cmds.setAttr( 'defaultResolution.width', fulldomeRenderWidth )
  cmds.setAttr( 'defaultResolution.height', fulldomeRenderHeight )
  cmds.setAttr( 'defaultResolution.deviceAspectRatio', 1)
  cmds.setAttr( 'defaultResolution.pixelAspect', 1)
  
  
  
"""
Domemaster3D Fulldome Stereo Rig
--------------------------------
A python function to create a fulldome stereo rig in Maya.
"""

def createFulldomeStereoRig():
  import maya.cmds as cmds
  import maya.mel as mel
  
  # ---------------------------------------------------------------------
  # Setup the default Maya / Mental Ray Settings
  # ---------------------------------------------------------------------
  cmds.loadPlugin( "stereoCamera", qt=True )
  
  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------
  
  #import maya.app.stereo.stereoCameraMenus as stereoCameraMenus
  #stereoCameraMenus.buildCreateMenu()
  #import maya.app.stereo.stereoCameraRig
  #maya.app.stereo.stereoCameraRig.createStereoCameraRig()
  
  from maya.app.stereo import stereoCameraRig
  rig = stereoCameraRig.createStereoCameraRig('DomeStereoCamera')
  #[u'DomeStereoCamera', u'DomeStereoCameraLeft', u'DomeStereoCameraRight']
  
  #Get the stereo camera rig shape nodes for the center/right/left cameras
  rig_center_shape_name =  getObjectShapeNode(rig[0])
  #[u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] #

  rig_left_shape_name =  getObjectShapeNode(rig[1])
  # Result: [u'stereoCameraLeftShape'] #

  rig_right_shape_name =  getObjectShapeNode(rig[2])
  # Result: [u'stereoCameraRightShape'] #
  
  """
  cmds.setAttr( rig[0]+'.rotateX', 90)
  cmds.setAttr( rig[0]+'.rotateY', 0)
  cmds.setAttr( rig[0]+'.rotateZ', 0)
  
  """
  
  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr( rig_left_shape_name[0]+'.renderable', 1) #stereoCameraLeftShape
  cmds.setAttr( rig_right_shape_name[0]+'.renderable', 1) #stereoCameraRightShape
  cmds.setAttr( 'topShape.renderable', 0)
  cmds.setAttr( 'sideShape.renderable', 0)
  cmds.setAttr( 'frontShape.renderable', 0)
  cmds.setAttr( 'perspShape.renderable', 0)
  
  #import maya.cmds as cmds
  #rig_center_shape_name =  getObjectShapeNode(rig[0])
  #lensShaderName = cmds.listConnections( rig_center_shape_name[0]+'.miLensShader')

  #Debugging test line
  #lensShaderName = "center_domeAFL_FOV_Stereo";
  #print ("Lens shader name: " + str(lensShaderName))
  
  # Select the center camera's domeAFL_FOV_Stereo node
  #cmds.select(lensShaderName, replace=True)
  
  #Select the center camera's domeAFL_FOV_Stereo node in the attribute editor
  #mel.eval ( ' showEditorExact("' + lensShaderName[0] + '") ' )

  return rig
  

"""
Domemaster3D createDomeAFL_FOV_Camera
----------------------
A python function to create a domeAFL_FOV lens shader and attach it to a camera.
"""	
def createDomeAFL_FOV_Camera():
  import maya.cmds as cmds
  import maya.mel as mel	
  
  #Variables
  
  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------
  
  # Create a camera and get the shape name.
  cameraName = cmds.camera(name='domeAFL_FOV_Camera')
  cameraShape = cameraName[1]
  
  # ---------------------------------------------------------------------
  # Create the domeAFL_FOV node
  # ---------------------------------------------------------------------
  domeAFL_lens_node = cmds.shadingNode( 'domeAFL_FOV', n='domeAFL_FOV', asUtility=True  ) 
  
  # Primary lens shader connection:
  # Connect to the .miLensShaderList[0] input on the camera
  #cmds.connectAttr( domeAFL_lens_node+'.message', cameraShape+'.miLensShaderList[0]' )
  
  # Alternate lens shader connection:
  # Connect directly to the first .miLensShader input on the camera
  # Note: This first lens shader connection is overwritten by the mental ray Sun & Sky system
  cmds.connectAttr( domeAFL_lens_node+'.message', cameraShape+'.miLensShader' )
  
  # Scale the stereo camera rig locator larger 
  #cmds.setAttr(cameraShape+'.locatorScale', 1) #Scale Camera icon
  
  # Link the new attribute 'Cam Locator Scale' to the dome camera's locator size control
  cmds.addAttr( cameraName[0], longName='Cam_Locator_Scale', niceName='Cam Locator Scale', attributeType='double', defaultValue=1.0, minValue=0.001)
  cmds.setAttr( cameraName[0]+'.Cam_Locator_Scale', keyable=False, channelBox=True)
  cmds.connectAttr ( cameraName[0]+'.Cam_Locator_Scale', cameraShape+'.locatorScale', force=True)
  
  cmds.setAttr( cameraName[0]+'.rotateX', 90)
  cmds.setAttr( cameraName[0]+'.rotateY', 0)
  cmds.setAttr( cameraName[0]+'.rotateZ', 0)
  
  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr( cameraShape+'.renderable', 1) #domeAFL_FOV_CameraShape
  cmds.setAttr( 'topShape.renderable', 0)
  cmds.setAttr( 'sideShape.renderable', 0)
  cmds.setAttr( 'frontShape.renderable', 0)
  cmds.setAttr( 'perspShape.renderable', 0)
  
  # ---------------------------------------------------------------------
  # Setup the stereo rig camera attributes
  # ---------------------------------------------------------------------
  cmds.setAttr( cameraShape+'.focalLength', 4 )
 
  #Select the center camera domeAFL_FOV_Stereo node in the attribute editor
  #This will add the extra attributes to the camera
  mel.eval ( ' showEditorExact("' + domeAFL_lens_node + '") ' )
  
  # ---------------------------------------------------------------------
  #Set the default camera separation based upon the scene size
  # ---------------------------------------------------------------------
  #defaultDomeRadius = 2

  #Set the dome radius
  #cmds.setAttr(domeAFL_lens_node+'.Dome_Radius', defaultDomeRadius)
  #print("Dome Radius: " + str(defaultDomeRadius))
  
  

"""
Domemaster3D createDomeAFL_WxH_Camera
----------------------
A python function to create a domeAFL_WxH lens shader and attach it to a camera.
"""	

def createDomeAFL_WxH_Camera():
  import maya.cmds as cmds
  #import maya.mel as mm	

  #Variables

  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------

  # Create a camera and get the shape name.
  cameraName = cmds.camera(name='domeAFL_WxH_Camera')
  cameraShape = cameraName[1]

  # ---------------------------------------------------------------------
  # Create the domeAFL_WxH node
  # ---------------------------------------------------------------------
  domeAFL_WxH_lens_node = cmds.shadingNode( 'domeAFL_WxH', n='domeAFL_WxH', asUtility=True  ) 

  # Primary lens shader connection:
  # Connect to the .miLensShaderList[0] input on the camera
  # cmds.connectAttr( domeAFL_WxH_lens_node+'.message', cameraShape+'.miLensShaderList[0]' )

  # Alternate lens shader connection:
  # Connect directly to the first .miLensShader input on the camera
  # Note: This first lens shader connection is overwritten by the mental ray Sun & Sky system
  cmds.connectAttr( domeAFL_WxH_lens_node+'.message', cameraShape+'.miLensShader' )

  # Scale the stereo camera rig locator larger 
  #cmds.setAttr(cameraShape+'.locatorScale', 1) #Scale Camera icon

  # Link the new attribute 'Cam Locator Scale' to the dome camera's locator size control
  cmds.addAttr( cameraName[0], longName='Cam_Locator_Scale', niceName='Cam Locator Scale', attributeType='double', defaultValue=1.0, minValue=0.001)
  cmds.setAttr( cameraName[0]+'.Cam_Locator_Scale', keyable=False, channelBox=True)
  cmds.connectAttr ( cameraName[0]+'.Cam_Locator_Scale', cameraShape+'.locatorScale', force=True)


  cmds.setAttr( cameraName[0]+'.rotateX', 90)
  cmds.setAttr( cameraName[0]+'.rotateY', 0)
  cmds.setAttr( cameraName[0]+'.rotateZ', 0)

  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr( cameraShape+'.renderable', 1) #domeAFL_WxH_CameraShape
  cmds.setAttr( 'topShape.renderable', 0)
  cmds.setAttr( 'sideShape.renderable', 0)
  cmds.setAttr( 'frontShape.renderable', 0)
  cmds.setAttr( 'perspShape.renderable', 0)

  # ---------------------------------------------------------------------
  # Setup the stereo rig camera attributes
  # ---------------------------------------------------------------------
  cmds.setAttr( cameraShape+'.focalLength', 4 )
  
  
"""
Domemaster3D DomeGrid test background 
--------------------------------------
A python function to create a hemispherical yellow test grid in Maya. 

"""

#Suggested Maya Scene Grid Settings:
#length and width: 360 units
#Grid lines every: 180 units
#Subdivisions: 2

def createDomeGrid():
  import maya.cmds as cmds
  import maya.mel as mel
  
  # --------------------------------------
  # Variables
  # --------------------------------------
  
  #Set the diameter of the final dome shape
  domeDiameter = 180
  
  # --------------------------------------
  # Remove any existing dome mesh
  # --------------------------------------
  
  #Remove an existing paintfx toon shader
  #if cmds.objExists('pfxToon1'): 
  #  print('Removing existing Domemaster3D object: pfxToon1')
  #  cmds.select( 'pfxToon1', replace=True)
  #  cmds.delete()
  
  if cmds.objExists('domeGridToon'): 
    print('Removing existing Domemaster3D object: domeGridToon')
    cmds.select( 'domeGridToon', replace=True)
    cmds.delete()
  
  if cmds.objExists('domeGridLinesSurfaceShader'): 
    print('Removing existing Domemaster3D object: domeGridLinesSurfaceShader')
    cmds.select( 'domeGridLinesSurfaceShader', replace=True)
    cmds.delete()
  
  if cmds.objExists('domeSurfaceShader'): 
    print('Removing existing Domemaster3D object: domeSurfaceShader')
    cmds.select( 'domeSurfaceShader', replace=True)
    cmds.delete()
  
  if cmds.objExists('domeGridLinesSurfaceShaderSG'): 
    print('Removing existing Domemaster3D object: domeGridLinesSurfaceShaderSG')
    cmds.select( 'domeGridLinesSurfaceShaderSG', replace=True)
    cmds.delete()
  
  if cmds.objExists('domeSurfaceShaderSG'): 
    print('Removing existing Domemaster3D object: domeSurfaceShaderSG')
    cmds.select( 'domeSurfaceShaderSG', replace=True)
    cmds.delete()
  
  # ---------------------------------------------
  
  if cmds.objExists('MeshGroup'): 
    print('Removing existing Domemaster3D object: MeshGroup')
    cmds.select( 'MeshGroup', replace=True)
    cmds.delete() 
  
  # Remove any existing dome test grid surfaces called 
  # polydome, polyTestSphere, or polyTestCube . 
  
  
  if cmds.objExists('polyDome'): 
    print('Removing existing Domemaster3D object: polyDome')
    cmds.select( 'polyDome', replace=True)
    cmds.delete()
  
  # --------------------------------------
  # Make the dome mesh
  # --------------------------------------
  
  #Create the base sphere with a 1 unit scale
  dome_name = cmds.polySphere( name='polyDome', radius = 1, subdivisionsX=36, subdivisionsY=20, axis=(0, 1, 0),  createUVs=2, constructionHistory=True)
  #print(dome_name)
  #[u'polyDome', u'polySphere1']
  
  #cmds.select( dome_name, replace=True);
  
  #Chop the polysphere into a hemispherical dome

  dome_shape_name = getObjectShapeNode(dome_name[0])
  
  cmds.select( dome_shape_name[0]+'.f[0:323]', dome_shape_name[0]+'.f[648:683]', replace=True)
  cmds.delete()
  
  #Scale the dome to its final size
  cmds.setAttr( dome_name[0]+'.scaleZ', domeDiameter)
  cmds.setAttr( dome_name[0]+'.scaleX', domeDiameter)
  cmds.setAttr( dome_name[0]+'.scaleY', domeDiameter)
  
  
  # --------------------------------------
  # Create the PaintFX Toon stroke outlines
  # --------------------------------------
  
  
  cmds.select( dome_name[0], replace=True);
  
  #Assign Toon outlines
  mel.eval("assignNewPfxToon;")
  cmds.setAttr('pfxToonShape1.profileLines', 0)
  cmds.setAttr('pfxToonShape1.borderLines', 0)
  cmds.setAttr('pfxToonShape1.creaseLineWidth', 15)
  cmds.setAttr('pfxToonShape1.creaseColor', 1, 1, 0, type="double3")
  cmds.setAttr('pfxToonShape1.hardCreasesOnly', 0)
  cmds.setAttr('pfxToonShape1.creaseBreakAngle', 0)
  cmds.setAttr('pfxToonShape1.creaseAngleMin', 0)
  cmds.setAttr('pfxToonShape1.creaseAngleMax', 0)
  
  cmds.setAttr('pfxToonShape1.meshVertexColorMode', 1)
  cmds.setAttr('pfxToonShape1.meshQuadOutput', 1)
  cmds.setAttr('pfxToonShape1.meshHardEdges', 1)
  
  #Create polygon Paintfx stroke output
  cmds.select( 'pfxToon1', replace=True);
  mel.eval("doPaintEffectsToPoly( 1,1,1,1,100000);")
  cmds.sets('surfaceShader1SG')
  
  # Standard Yellow Color
  # cmds.setAttr( 'surfaceShader1.outColor', 1, 1, 0, type="double3")
  
  # Super Bright Yellow Color for Physical Sky Comparability
  cmds.setAttr( 'surfaceShader1.outColor', 15, 15, 0, type="double3")
  
  cmds.rename( 'surfaceShader1', 'domeGridLinesSurfaceShader' )
  cmds.rename( 'surfaceShader1SG', 'domeGridLinesSurfaceShaderSG' )
  cmds.rename( 'pfxToon1', 'domeGridToon' )
  
  #Set the polygon surface to a black surface shader
  dome_shader_group_name = cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name='domeSurfaceShaderSG' )
  dome_shader_name = cmds.shadingNode( 'surfaceShader', name='domeSurfaceShader', asShader=True) 
  cmds.setAttr( dome_shader_name+'.outColor', 0, 0, 0, type="double3")
  cmds.connectAttr('domeSurfaceShader.outColor', 'domeSurfaceShaderSG.surfaceShader')
  mel.eval("assignSG domeSurfaceShader polyDome;")
  #('domeSurfaceShaderSG', edit=True, forceElement='polyDomeShape')
  
  #Set the polygon surface to be transparent
  cmds.setAttr( dome_shader_name+'.outTransparency', 1, 1, 1, type="double3")
  
  #Create a Display layer
  cmds.select( dome_name[0], 'MeshGroup', replace=True);
  
  #Check if the domeGridLayer exists
  if not cmds.objExists('domeGridLayer'):
    cmds.createDisplayLayer( name="domeGridLayer", number=1, nr=True)
    #Set the layer color to yellow
    cmds.setAttr('domeGridLayer.color', 17) 


"""
Domemaster3D createTestShapes
----------------------
A python function to create a test sphere and cube in Maya. 
"""

def  createTestShapes():
  import maya.cmds as cmds

  if cmds.objExists('domeTestLight'): 
    print('Removing existing Domemaster3D object: domeTestLight')
    cmds.select( 'domeTestLight', replace=True)
    cmds.delete()

  if cmds.objExists('polyTestSphere'): 
    print('Removing existing Domemaster3D object: polyTestSphere')
    cmds.select( 'polyTestSphere', replace=True)
    cmds.delete()

  if cmds.objExists('polyTestCube'): 
    print('Removing existing Domemaster3D object: polyTestCube')
    cmds.select( 'polyTestCube', replace=True)
    cmds.delete()

  test_sphere_name = cmds.polySphere( name='polyTestSphere', radius=24, subdivisionsX=20, subdivisionsY=20, axis=(0, 1, 0),  createUVs=2, constructionHistory=True)
  cmds.setAttr(test_sphere_name[0]+'.translateX', 80)
  cmds.setAttr(test_sphere_name[0]+'.translateY', 75)

  test_cube_name = cmds.polyCube( name='polyTestCube', width=40, height=40, depth=40, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=(0, 1, 0),  createUVs=4, constructionHistory=True)
  cmds.setAttr(test_cube_name[0]+'.translateX', 0)
  cmds.setAttr(test_cube_name[0]+'.translateY', 75)
  cmds.setAttr(test_cube_name[0]+'.translateZ', -80)
  cmds.setAttr(test_cube_name[0]+'.rotateX', 88)
  cmds.setAttr(test_cube_name[0]+'.rotateY', 0)
  cmds.setAttr(test_cube_name[0]+'.rotateZ', 0)

  dome_light_shape_name = cmds.directionalLight()
  dome_light_name = getObjectParentNode( dome_light_shape_name )
  dome_light_name = cmds.rename (dome_light_name, "domeTestLight")

  cmds.setAttr( (dome_light_name+'.translateX'), -32)
  cmds.setAttr( (dome_light_name+'.rotateX'), 38)
  cmds.setAttr( (dome_light_name+'.rotateY'), 47)
  cmds.setAttr( (dome_light_name+'.rotateZ'), -62)



"""
Domemaster3D createRobLookup
----------------------
A python function to create a mental ray screen space texture 
and connect it to a robLookupBackground lens shader. 
"""

def createRobLookup():
  import maya.cmds as cmds
  
  # ---------------------------------------------------------------------
  #Setup the base folder path for the Domemaster3D control maps
  # ---------------------------------------------------------------------
  
  #Variables
  separationMapFileTexture = getSourceImagesPath("separation_map.png")
  print "[Loading Separation Map]: " + separationMapFileTexture 
  
  
  # Create a camera and get the shape name.
  cameraName = cmds.camera(name='robLookupCamera')
  cameraShape = cameraName[1]
  
  # ---------------------------------------------------------------------
  # Create the robLookupBackground node
  # ---------------------------------------------------------------------
  rob_lens_node = cmds.shadingNode( 'rob_lookup_background', n='rob_lookup_background', asUtility=True  )
  cmds.connectAttr( rob_lens_node+'.message', cameraShape+'.miLensShader' )
  
  # ---------------------------------------------------------------------
  # Create the custom shading network connections
  # ---------------------------------------------------------------------
  
  # Create the nodes
  rob_map_tex_filter = cmds.shadingNode( 'mib_texture_filter_lookup', n='rob_map_mib_texture_filter_lookup1', asTexture=True)
  
  rob_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='rob_mib_texture_vector1', asUtility=True )
  rob_tex_remap = cmds.shadingNode( 'mib_texture_remap', n='rob_mib_texture_remap1',  asUtility=True)
  
  rob_map_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='rob_map_mentalrayTexture1', asTexture=True)
  
  # Set the node to use mode (4) which is screen space
  cmds.setAttr( rob_tex_vector+'.selspace', 4)
  
  # Connect the nodes
  cmds.connectAttr( rob_map_tex_filter+'.outValueR', rob_lens_node+'.tex' )
  cmds.connectAttr( rob_map_mr_tex+'.message', rob_map_tex_filter+'.tex' )
  
  cmds.connectAttr( rob_tex_vector+'.outValue', rob_tex_remap+'.input' )
  cmds.connectAttr( rob_tex_remap+'.outValue', rob_map_tex_filter+'.coord' )
  
  cmds.setAttr( rob_map_mr_tex+'.fileTextureName', separationMapFileTexture , type="string")




"""
Domemaster3D createDomeRampTexture
----------------------
A python function to create a mental ray screen space ramp texture 
and connect it to a robLookupBackground lens shader.
"""

def createDomeRampTexture():
  import maya.cmds as cmds
  
  # Create a camera and get the shape name.
  cameraName = cmds.camera(name='robLookupCamera')
  cameraShape = cameraName[1]
  
  # ---------------------------------------------------------------------
  # Create the robLookupBackground node
  # ---------------------------------------------------------------------
  rob_lens_node = cmds.shadingNode( 'rob_lookup_background', n='rob_lookup_background', asUtility=True  )
  cmds.connectAttr( rob_lens_node+'.message', cameraShape+'.miLensShader' )
  
  # ---------------------------------------------------------------------
  # Create the custom shading network connections
  # ---------------------------------------------------------------------
  
  # Create the Ramp node
 # Create the Ramp node
  dome_ramp = cmds.shadingNode( 'ramp', n='domeRamp', asTexture=True) 
  cmds.setAttr( dome_ramp+'.colorEntryList', s=2 )
  cmds.setAttr(dome_ramp+'.colorEntryList[0].ep', 0.5)
  cmds.setAttr( dome_ramp+'.colorEntryList[0].ec', 1, 1, 1, type="float3")
  cmds.setAttr(dome_ramp+'.colorEntryList[2].ep', 0.44999998807907104)
  cmds.setAttr( dome_ramp+'.colorEntryList[2].ec',  0, 0, 0, type="float3")
  
  # Create the texture space conversion node
  rob_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='rob_mib_texture_vector1', asUtility=True )
  
  # Set the node to use mode (4) which is screen space
  cmds.setAttr( rob_tex_vector+'.selspace', 4)
  
  #Connect the texture_vector node to the ramp node using the XY values for the UV coordinates.
  cmds.connectAttr( dome_ramp+'.outColor.outColorR', rob_lens_node+'.tex' )
  cmds.connectAttr( rob_tex_vector+'.outValue.outValueX', dome_ramp+'.uvCoord.uCoord' )
  cmds.connectAttr( rob_tex_vector+'.outValue.outValueY', dome_ramp+'.uvCoord.vCoord' )


"""
A python function to get the current object's shape node

getObjectShapeNode("stereoCamera")
# Result: [u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] # 

"""

def getObjectShapeNode ( object ) :
    import maya.cmds as cmds
    return cmds.listRelatives( object, children=True , shapes=True)


"""
A python function to get the current object's parent node

getObjectParentNode("nurbsSphereShape1")
# Result:  [u'nurbsSphere1'] #

"""

def getObjectParentNode ( object ) :
    import maya.cmds as cmds
    return cmds.listRelatives( object, parent=True)
