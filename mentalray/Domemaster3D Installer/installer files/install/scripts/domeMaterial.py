"""
DomeAFL Mental Ray MIA Material  V1.3.3
--------------------------------
Created by Andrew Hazelden  andrew@andrewhazelden.com

Version History
----------------
Version 1.3.3
Released May 29, 2013

Updated the default locator scale


Version 1.3.2 - Build 1
Released April 16, 2013
Edited the default camera connections for the lens shaders to work with the modified versions of the maya createMentalRayIndirectLightingTab.mel & AEmia_physicalskyTemplate.mel scripts. This fixes the problem of the Physical Sky & Sum system overwriting the first .miLensShader input on cameras in the scene.

The location of the default domemaster control map textures is now in the Program Files\Domemaster3D\sourceimages folder on Windows or the /Applications/Domemaster3D/sourceimages folder on Mac OS X. The Domemaster3D shelf tools have been updated to link to the new sourceimages folder.

Version 1.3 - Build 27
Released Nov 4, 2012
Edited default presets for bump map shading network, added WxH and FOV camera tools, changed the default lens shader connections to support the mental ray sky and sun system.


Version 1.0
Beta Release Oct 31, 2012
Created first python script to create a domeAFL mental ray shading network



This script makes it easy to start creating fulldome content in Autodesk Maya.

This is a set of python functions for Maya that create domeAFL shader compatible surface materials.

The textures are loaded as mentalray textures and connected to a standard mia_material.

You can set the file textures to an empty path if you don't want a default texture applied to the mentalrayTexture nodes. On my system I get an error if I try and render a scene with an empty mentalrayTexture node. 



Installation instructions
-------------------------

Step 1.
Place the python scripts "domeMaterial.py" and "__init__.py" 
in your Maya scripts folder.

Step 2.
Copy the file textures bumpChecker.iff & checker.iff into your 
current Maya project's sourceimages folder.

Step 3.
Source the python script in Maya using the python command:
import domeMaterial as domeMaterial


Step 4.
Test your current domeAFL python script installation using the python command:
domeMaterial.createColorBumpMiaMaterial()

--------------------------------------
--------------------------------------

Create a color and Bump MIA material 
------------------------------------
A python function to create a mia_material with a shading network for color + bump textures.

Run using the command:
import domeMaterial as domeMaterial
domeMaterial.createColorBumpMiaMaterial()


--------------------------------------
--------------------------------------

Create a color MIA material 
---------------------------
A python function to create a mia_material with a shading network for color + bump textures.

Run using the command:
import domeMaterial as domeMaterial
domeMaterial.createColorMiaMaterial()


--------------------------------------
--------------------------------------

Domemaster3D createDomeAFL_WxH_Camera
----------------------
A python function to create a domeAFL_WxH lens shader and attach it to a camera.

Run using the command:
import domeMaterial as domeMaterial
domeMaterial.createDomeAFL_WxH_Camera()
--------------------------------------
--------------------------------------

Domemaster3D createDomeAFL_FOV_Camera
----------------------
A python function to create a domeAFL_FOV lens shader and attach it to a camera.

Run using the command:
import domeMaterial as domeMaterial
domeMaterial.createDomeAFL_FOV_Camera()
--------------------------------------
--------------------------------------

"""



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
    baseImagesFolder = "C:\\Program Files\\Domemaster3D\\sourceimages\\"
  elif platform.system()== 'win32':
    #Check if the program is running on Windows 32
    baseImagesFolder = "C:\\Program Files (x86)\\Domemaster3D\\sourceimages\\"
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
Create a color and Bump MIA material 
------------------------------------
A python function to create a mia_material with a shading network for color + bump textures.
"""

# Create a color and Bump MIA material    
def createColorBumpMiaMaterial():
	import os  
	import maya.cmds as cmds
	#import maya.mel as mm  
	

  # ---------------------------------------------------------------------
  #Setup the base folder path for the Domemaster3D control maps
  # ---------------------------------------------------------------------


	#Set the file texture variables to "" if you don't want a file to be specified
	#ColorMapFileTexture = ""
	#BumpMapFileTexture = ""
	
	ColorMapFileTexture = getSourceImagesPath("checker.iff")
	BumpMapFileTexture = getSourceImagesPath("bumpChecker.iff")
	
	#Get the selected geometry
	object_selection = cmds.ls(sl=True)
	
	
	# Create the render nodes
	
	#Create the mia_material + shading group
	dome_mia_shader_group_name = cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name='dome_mia_materialSG' )
	dome_mia_shader_name = cmds.shadingNode( 'mia_material', n='dome_mia_material', asShader=True)	
	
	#Apply the shading group to the selected geometry
	if object_selection:
		print("Applying the "+dome_mia_shader_name+" surface material to:")
		for obj in object_selection: 
			print obj
			
		for obj in object_selection: 
			cmds.select(obj)
			cmds.hyperShade(assign=dome_mia_shader_group_name)
	
	color_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='color_mib_texture_vector1', asUtility=True ) 
	color_tex_remap = cmds.shadingNode( 'mib_texture_remap', n='color_mib_texture_remap1',  asUtility=True) 
	color_tex_lookup= cmds.shadingNode( 'mib_texture_lookup', n='color_mib_texture_lookup1',  asUtility=True) 
	color_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='color_mentalrayTexture1', asTexture=True) 
	
	bump_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='bump_mentalrayTexture1', asTexture=True) 
	
	bump_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='bump_mib_texture_vector1', asUtility=True ) 
	bump_tex_remap = cmds.shadingNode( 'mib_texture_remap', n='bump_mib_texture_remap1',  asUtility=True) 
	bump_mib_bump_basis= cmds.shadingNode( 'mib_bump_basis', n='mib_bump_basis1',  asUtility=True) 
	bump_mib_passthrough_bump_map = cmds.shadingNode( 'mib_passthrough_bump_map', n='mib_passthrough_bump_map1', asUtility=True) 
	
	
	# Connect the nodes
	
	# Connect the mia_material shader to the shading group
	cmds.connectAttr(dome_mia_shader_name+'.outValue', dome_mia_shader_group_name+'.surfaceShader', f=True)
	cmds.connectAttr(dome_mia_shader_name+'.outValue', dome_mia_shader_group_name+'.miPhotonShader', f=True)
	cmds.connectAttr(dome_mia_shader_name+'.outValue', dome_mia_shader_group_name+'.miShadowShader', f=True)
	cmds.connectAttr(dome_mia_shader_name+'.outValue', dome_mia_shader_group_name+'.miMaterialShader', f=True)
	
	
	# Connect the color texture nodes
	cmds.connectAttr( color_tex_vector+'.outValue', color_tex_remap+'.input' )
	#mib_texture_vector.outValue -> mib_texture_remap.input
	
	cmds.connectAttr( color_tex_remap+'.outValue', color_tex_lookup+'.coord' )
	#mib_texture_remap.outValue -> mib_texture_lookup.coord
	
	cmds.connectAttr( color_mr_tex+'.message', color_tex_lookup+'.tex' )
	#mentalrayTexture.message -> mib_texture_lookup.tex
	
	cmds.connectAttr( color_tex_lookup+'.outValue', dome_mia_shader_name+'.diffuse' )
	#mib_texture_lookup.outValue -> mia_material.diffuse
	
	
	
	# Connect the bump map texture nodes
	cmds.connectAttr( bump_tex_vector+'.outValue', bump_tex_remap+'.input' )
	#mib_texture_vector.outValue -> mib_texture_remap.input
	
	cmds.connectAttr( bump_tex_remap+'.outValue', bump_mib_passthrough_bump_map+'.coord' )
	#mib_texture_remap.outValue -> mib_passthrough_bump_map.coord
	
	cmds.connectAttr( bump_mib_bump_basis+'.u', bump_mib_passthrough_bump_map+'.u' )
	cmds.connectAttr( bump_mib_bump_basis+'.v', bump_mib_passthrough_bump_map+'.v' )
	#mib_bump_basis2.u -> mib_passthrough_bump_map.u
	#mib_bump_basis2.v -> mib_passthrough_bump_map.v
	
	cmds.connectAttr( bump_mr_tex+'.message', bump_mib_passthrough_bump_map+'.tex' )
	#mentalrayTexture.message -> mib_passthrough_bump_map.tex
	
	cmds.connectAttr( bump_mib_passthrough_bump_map+'.outValue', dome_mia_shader_name+'.bump' )
	#mib_passthrough_bump_map.outvalue -> mia_material.bump
	
	
	# Set values for the shading nodes
	
	# Set the mia_material to be a matte material
	#cmds.setAttr(dome_mia_shader_name+".reflectivity", 0)
	
	# Set the mia_material to be a glossy material
	cmds.setAttr(dome_mia_shader_name+".refl_color", 1, 1, 1, type="double3")
	cmds.setAttr(dome_mia_shader_name+".reflectivity", 1)
	cmds.setAttr(dome_mia_shader_name+".refl_gloss", 0.3)
	cmds.setAttr(dome_mia_shader_name+".reflectivity", 1)
	cmds.setAttr(dome_mia_shader_name+".diffuse_roughness", 0)
	cmds.setAttr(dome_mia_shader_name+".diffuse_weight", 1)
	
	
	# Set the filename for the mental ray texture nodes
	cmds.setAttr( color_mr_tex+'.fileTextureName', ColorMapFileTexture , type="string")
	cmds.setAttr( bump_mr_tex+'.fileTextureName', BumpMapFileTexture, type="string")
	
	
	# Note mental ray bump directions are negative while the standard Maya bump2D depth value is positive
	# Set the bump step value to a default starting value of 0.0 to make the bump visible
	cmds.setAttr( bump_mib_passthrough_bump_map+".stepX", 0.0)
	cmds.setAttr( bump_mib_passthrough_bump_map+".stepY", 0.0)
	cmds.setAttr( bump_mib_passthrough_bump_map+".stepZ", 0.0)
	
	#Set the bump factor default to 10 to make the bump map visible
	cmds.setAttr(bump_mib_passthrough_bump_map+".factor", 1)
	
	#Select the surface material
	#cmds.select(dome_mia_shader_name, r=True)
	
	#Select the original objects
	if object_selection:
		cmds.select(object_selection)
		print("Selected: ")
		print(object_selection)
	
	
	#No objects were selected
	if not object_selection:
		#print "No objects selected"
		#Select the surface material
		cmds.select(dome_mia_shader_name, r=True)




"""
Create a color MIA material 
---------------------------
A python function to create a mia_material with a shading network for color + bump textures.
"""

# Create a color MIA material  
def createColorMiaMaterial():
	import maya.cmds as cmds
	#import maya.mel as mm  
	
	# Texture variables
	#Set the file texture variables to "" if you don't want a file to be specified
	#ColorMapFileTexture = ""
	
	ColorMapFileTexture = getSourceImagesPath("checker.iff")
	
	#Get the selected geometry
	object_selection = cmds.ls(sl=True)
	
	# Create the render nodes
	
	#Create the mia_material + shading group
	dome_mia_shader_group_name = cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name='dome_mia_materialSG' )
	dome_mia_shader_name = cmds.shadingNode( 'mia_material', n='dome_mia_material', asShader=True)	
		
	#Apply the shading group to the selected geometry
	if object_selection:
		print("Applying the "+dome_mia_shader_name+" surface material to:")
		for obj in object_selection: 
			print obj
			
		for obj in object_selection: 
			cmds.select(obj)
			cmds.hyperShade(assign=dome_mia_shader_group_name)	
	
	# Create the nodes
	color_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='color_mib_texture_vector1', asUtility=True ) 
	color_tex_remap = cmds.shadingNode( 'mib_texture_remap', n='color_mib_texture_remap1',  asUtility=True) 
	color_tex_lookup= cmds.shadingNode( 'mib_texture_lookup', n='color_mib_texture_lookup1',  asUtility=True) 
	color_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='color_mentalrayTexture1', asTexture=True) 
	

	# Connect the nodes
	
	# Connect the mia_material shader to the shading group
	cmds.connectAttr(dome_mia_shader_name+'.outValue', dome_mia_shader_group_name+'.surfaceShader', f=True)
	cmds.connectAttr(dome_mia_shader_name+'.outValue', dome_mia_shader_group_name+'.miPhotonShader', f=True)
	cmds.connectAttr(dome_mia_shader_name+'.outValue', dome_mia_shader_group_name+'.miShadowShader', f=True)
	cmds.connectAttr(dome_mia_shader_name+'.outValue', dome_mia_shader_group_name+'.miMaterialShader', f=True)
	
	
	# Connect the color texture nodes
	cmds.connectAttr( color_tex_vector+'.outValue', color_tex_remap+'.input' )
	#mib_texture_vector.outValue -> mib_texture_remap.input
	
	cmds.connectAttr( color_tex_remap+'.outValue', color_tex_lookup+'.coord' )
	#mib_texture_remap.outValue -> mib_texture_lookup.coord
	
	cmds.connectAttr( color_mr_tex+'.message', color_tex_lookup+'.tex' )
	#mentalrayTexture.message -> mib_texture_lookup.tex
	
	cmds.connectAttr( color_tex_lookup+'.outValue', dome_mia_shader_name+'.diffuse' )
	#mib_texture_lookup.outValue -> mia_material.diffuse

	
	# Set values for the shading nodes
	
	# Set the mia_material to be a matte material
	#cmds.setAttr(dome_mia_shader_name+".reflectivity", 0)
	
	# Set the mia_material to be a glossy material
	cmds.setAttr(dome_mia_shader_name+".refl_color", 1, 1, 1, type="double3")
	cmds.setAttr(dome_mia_shader_name+".reflectivity", 1)
	cmds.setAttr(dome_mia_shader_name+".refl_gloss", 0.3)
	cmds.setAttr(dome_mia_shader_name+".reflectivity", 1)
	cmds.setAttr(dome_mia_shader_name+".diffuse_roughness", 0)
	cmds.setAttr(dome_mia_shader_name+".diffuse_weight", 1)
	
	
	# Set the filename for the mental ray texture nodes
	cmds.setAttr( color_mr_tex+'.fileTextureName', ColorMapFileTexture , type="string")
	
	
	#Select the original objects
	if object_selection:
		cmds.select(object_selection)
		print("Selected: ")
		print(object_selection)
	
	#No objects were selected
	if not object_selection:
		#print "No objects selected"
		#Select the surface material
		cmds.select(dome_mia_shader_name, r=True)
				

"""
Domemaster3D createDomeAFL_FOV_Camera
----------------------
A python function to create a domeAFL_FOV lens shader and attach it to a camera.
"""	
def createDomeAFL_FOV_Camera():
	import maya.cmds as cmds
	#import maya.mel as mm	
	
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
	cmds.setAttr(cameraShape+'.locatorScale', 1) #Scale Camera icon
	
	cmds.setAttr( cameraName[0]+'.rotateX', 90)
	cmds.setAttr( cameraName[0]+'.rotateY', 0)
	cmds.setAttr( cameraName[0]+'.rotateZ', 0)
	
	# Changes the render settings to set the stereo camera to be a renderable camera
	#cmds.setAttr( 'stereoCameraLeftShape.renderable', 1)
	#cmds.setAttr( 'stereoCameraRightShape.renderable', 1)
	cmds.setAttr( cameraShape+'.renderable', 1) #domeAFL_FOV_CameraShape
	cmds.setAttr( 'topShape.renderable', 0)
	cmds.setAttr( 'sideShape.renderable', 0)
	cmds.setAttr( 'frontShape.renderable', 0)
	cmds.setAttr( 'perspShape.renderable', 0)
	
	# ---------------------------------------------------------------------
	# Setup the stereo rig camera attributes
	# ---------------------------------------------------------------------
	cmds.setAttr( cameraShape+'.focalLength', 4 )

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
	# Create the domeAFL_FOV node
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
	cmds.setAttr(cameraShape+'.locatorScale', 1) #Scale Camera icon
	
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



