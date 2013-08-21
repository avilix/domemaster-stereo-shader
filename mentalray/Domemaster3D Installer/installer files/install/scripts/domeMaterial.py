"""
DomeAFL Mental Ray MIA Material X Passes V1.3.5
--------------------------------
Created by Andrew Hazelden  andrew@andrewhazelden.com

Version History
----------------

Version 1.3.5 build 7 - 7am
August 20, 2013

Upgraded the Maya dome material shaders to use the mia_material_x_passes shader

Added a starglobe tool to the Maya shelf to create a night sky backdrop

The starglobe textures are stored in the Domemaster3D/sourceimages folder and the starglobe spherical model is stored in the Domemaster3D/models folder.


Version 1.3.3
Released May 29, 2013

Updated the default locator scale

Updated source image paths for Maya 2010 compatibility


Version 1.3.2 - Build 1
Released April 16, 2013
Edited the default camera connections for the lens shaders to work with the modified versions of the maya createMentalRayIndirectLightingTab.mel & AEmia_physicalskyTemplate.mel scripts. This fixes the problem of the Physical Sky & Sum system overwriting the first .miLensShader input on cameras in the scene.

The location of the default domemaster control map textures is now in the C:\Program Files\Domemaster3D\sourceimages folder on Windows or the /Applications/Domemaster3D/sourceimages folder on Mac OS X. The Domemaster3D shelf tools have been updated to link to the new sourceimages folder.

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

Create a starglobe
---------------------------
A python function to create a 8K textured starglobe with a mental ray native mia_material_x_passes shading network.

Run using the command:
import domeMaterial as domeMaterial
domeMaterial.createStarglobe()



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
Find out the path to the models folder
----------------------
A python function to check the operating system platform and the models folder. 

"""
def getModelsPath(modelFileName):

  # ---------------------------------------------------------------------
  #Setup the base folder path for the Domemaster3D models
  # ---------------------------------------------------------------------

  #Check OS platform for Windows/Mac/Linux Paths
  import platform

  #This is the base path for the images folder
  baseModelsFolder = ""

  if platform.system()=='Windows':
    #Check if the program is running on Windows 
    baseModelsFolder = "C:/Program Files/Domemaster3D/models/"
  elif platform.system()== 'win32':
    #Check if the program is running on Windows 32
    baseModelsFolder = "C:/Program Files (x86)/Domemaster3D/models/"
  elif platform.system()== 'Darwin':
    #Check if the program is running on Mac OS X
    baseModelsFolder = "/Applications/Domemaster3D/models/"
  elif platform.system()== 'Linux':
    #Check if the program is running on Linux
    baseModelsFolder = "/usr/bin/Domemaster3D/models/"
  elif platform.system()== 'Linux2':
    #Check if the program is running on Linux
    baseModelsFolder = "/usr/bin/Domemaster3D/models/"
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
  import maya.cmds as cmds
  #import maya.mel as mm  


  # ---------------------------------------------------------------------
  #Set up the base folder path for the Domemaster3D textures
  # ---------------------------------------------------------------------

  #Set the file texture variables to "" if you don't want a file to be specified
  #StarglobeMapFileTexture = ""

  StarglobeMapFileTexture = getSourceImagesPath("starglobe_quadsphere_8k.jpg")
  StarglobeMayaFileTexture = getSourceImagesPath("starglobe_quadsphere_2k.jpg")

  #Get the selected geometry
  object_selection = cmds.ls(sl=True)


  if cmds.objExists('polyStarglobe'): 
    print('Removing existing Domemaster3D object: polyStarglobe')
    cmds.select( 'polyStarglobe', replace=True)
    cmds.delete()

  #Load the quads based starglobe sphere model
  StarglobeModelFile = getModelsPath("starglobe_mesh.ma")

  #Load the Maya .ma format starglobe model into the scene
  starglobe_mesh_file = cmds.file (StarglobeModelFile, i=True, type='mayaAscii')


  #Create the mia_material + shading group
  starglobe_mia_shader_group_name = cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name='starglobe_materialSG' )
  starglobe_mia_shader_name = cmds.shadingNode( 'mia_material_x_passes', n='starglobe_material', asShader=True)	


  starglobe_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='starglobe_mib_texture_vector1', asUtility=True ) 
  starglobe_tex_remap = cmds.shadingNode( 'mib_texture_remap', n='starglobe_mib_texture_remap1',  asUtility=True) 
  starglobe_tex_lookup= cmds.shadingNode( 'mib_texture_lookup', n='starglobe_mib_texture_lookup1',  asUtility=True) 
  starglobe_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='starglobe_mentalrayTexture1', asTexture=True) 


  #Create the Lambert in-scene preview material
  starglobe_preview_shader_name = cmds.shadingNode( 'lambert', n='starglobe_preview_material', asShader=True)	
  starglobe_maya_tex = cmds.shadingNode( 'file', n='starglobe_FileTexture', asTexture=True) 
  starglobe_maya_placement = cmds.shadingNode( 'place2dTexture', n='starglobe_place2dTexture', asUtility=True) 


  #Connect the place2D texture to the Maya starglobe file texture
  cmds.connectAttr(starglobe_maya_placement+'.coverage', starglobe_maya_tex+'.coverage', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.translateFrame', starglobe_maya_tex+'.translateFrame', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.rotateFrame', starglobe_maya_tex+'.rotateFrame', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.mirrorU', starglobe_maya_tex+'.mirrorU', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.mirrorV', starglobe_maya_tex+'.mirrorV', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.stagger', starglobe_maya_tex+'.stagger', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.wrapU', starglobe_maya_tex+'.wrapU', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.wrapV', starglobe_maya_tex+'.wrapV', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.repeatUV', starglobe_maya_tex+'.repeatUV', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.offset', starglobe_maya_tex+'.offset', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.rotateUV', starglobe_maya_tex+'.rotateUV', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.noiseUV', starglobe_maya_tex+'.noiseUV', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.vertexUvOne', starglobe_maya_tex+'.vertexUvOne', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.vertexUvTwo', starglobe_maya_tex+'.vertexUvTwo', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.vertexUvThree', starglobe_maya_tex+'.vertexUvThree', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.vertexCameraOne', starglobe_maya_tex+'.vertexCameraOne', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.outUV', starglobe_maya_tex+'.uvCoord', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.outUvFilterSize', starglobe_maya_tex+'.uvFilterSize', f=True)

  # Connect the color texture nodes
  cmds.connectAttr( starglobe_tex_vector+'.outValue', starglobe_tex_remap+'.input' )
  #mib_texture_vector.outValue -> mib_texture_remap.input

  cmds.connectAttr( starglobe_tex_remap+'.outValue', starglobe_tex_lookup+'.coord' )
  #mib_texture_remap.outValue -> mib_texture_lookup.coord

  cmds.connectAttr( starglobe_mr_tex+'.message', starglobe_tex_lookup+'.tex' )
  #mentalrayTexture.message -> mib_texture_lookup.tex

  # Connect the stargobe texture to the diffuse color attribute
  #cmds.connectAttr( starglobe_tex_lookup+'.outValue', starglobe_mia_shader_name+'.diffuse' )
  #mib_texture_lookup.outValue -> mia_material_x_passes.diffuse

  # Make the mia material shader act like an incandescent/surface shader material
  cmds.connectAttr( starglobe_tex_lookup+'.outValue', starglobe_mia_shader_name+'.additional_color' )
  #mib_texture_lookup.outValue -> mia_material_x_passes.additional_color

  # Set values for the shading nodes

  # Set the mia_material to be a matte material
  #cmds.setAttr(starglobe_mia_shader_name+".reflectivity", 0)

  # Set the mia_material to be a glossy material
  cmds.setAttr(starglobe_mia_shader_name+".refl_color", 1, 1, 1, type="double3")
  cmds.setAttr(starglobe_mia_shader_name+".reflectivity", 0)
  cmds.setAttr(starglobe_mia_shader_name+".refl_gloss", 0.0)
  cmds.setAttr(starglobe_mia_shader_name+".diffuse_roughness", 0)
  cmds.setAttr(starglobe_mia_shader_name+".diffuse_weight", 1)

  #Set the material to a black diffuse color
  cmds.setAttr(starglobe_mia_shader_name+".diffuse", 0, 0, 0, type="double3")

  #note cutout opacity could be used to make the night sky alpha channel transparent or solid


  #Optional Light Linking

  #Set the mia_material_x_passes shader to ignore the illumination from the lights in the scene with "light linking"
  #starglobe_mia.mode 0 = Custom Linking
  #starglobe_mia.mode 1 = Inclusive Linking
  #starglobe_mia.mode 2 = Exclusive Linking
  #starglobe_mia.mode 4 = Maya Linking

  #Note: All scene lights are skipped by default with "Exclusive linking" mode 2
  cmds.setAttr(starglobe_mia_shader_name+".mode", 2)


  #End of Optional Light Linking

  #Load the file texture maps

  # Set the filename for the mental ray texture nodes
  cmds.setAttr( starglobe_mr_tex+'.fileTextureName', StarglobeMapFileTexture , type="string")

  # Set the filename for the maya file texture node
  cmds.setAttr( starglobe_maya_tex+'.fileTextureName', StarglobeMayaFileTexture , type="string")


  #Connect the Lambert preview shader

  # Connect the Maya starglobe file texture to the lambert preview material color and incandescent shader inputs
  cmds.connectAttr(starglobe_maya_tex+'.outColor', starglobe_preview_shader_name+'.color', f=True)
  cmds.connectAttr(starglobe_maya_tex+'.outColor', starglobe_preview_shader_name+'.incandescence', f=True)
 
  # Connect the Lambert in-scene preview shader to the shading group
  cmds.connectAttr(starglobe_preview_shader_name+'.outColor', starglobe_mia_shader_group_name+'.surfaceShader', f=True)

  # Connect the mia_material nodes

  # Connect the mia_material shader to the shading group
  cmds.connectAttr(starglobe_mia_shader_name+'.message', starglobe_mia_shader_group_name+'.miPhotonShader', f=True)
  cmds.connectAttr(starglobe_mia_shader_name+'.message', starglobe_mia_shader_group_name+'.miShadowShader', f=True)
  cmds.connectAttr(starglobe_mia_shader_name+'.message', starglobe_mia_shader_group_name+'.miMaterialShader', f=True)

  # Old mia_material to shading group connection - replaced by Lambert preview shader
  #cmds.connectAttr(starglobe_mia_shader_name+'.message', starglobe_mia_shader_group_name+'.surfaceShader', f=True)

  # Enable the Hypershade shading group "Suppress all Maya Shaders" checkbox so only the mental ray nodes will be used.
  # This ensures the preview material will be skipped from rendering in older versions of Maya.
  cmds.setAttr(starglobe_mia_shader_group_name+'.miExportMrMaterial', 1)


  #Assign the starglobe surface material to the shape: polyStarglobe
  #polyStarglobe

  #Apply the shading group to the selected geometry
  cmds.select("polyStarglobe")
  cmds.hyperShade(assign=starglobe_mia_shader_group_name)


  #set the default size (scale) of the starglobe backdrop
  cmds.setAttr( "polyStarglobe.scaleZ", 25)
  cmds.setAttr( "polyStarglobe.scaleX", 25)
  cmds.setAttr( "polyStarglobe.scaleY", 25)


  #Select the surface material
  #cmds.select(starglobe_mia_shader_name, r=True)

  #Select the original objects
  if object_selection:
    cmds.select(object_selection)
    print("Selected: ")
    print(object_selection)


  #No objects were selected
  if not object_selection:
    #print "No objects selected"
    #Select the surface material
    cmds.select(starglobe_mia_shader_name, r=True)



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
  #Set up the base folder path for the Domemaster3D control maps
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
 
  #Create a mia_material_x_passes shader
  dome_mia_shader_name = cmds.shadingNode( 'mia_material_x_passes', n='dome_mia_material', asShader=True)	

  #Create a mia_material shader
  #dome_mia_shader_name = cmds.shadingNode( 'mia_material', n='dome_mia_material', asShader=True)	  


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


  # Set the filename for the mental ray texture nodes
  cmds.setAttr( color_mr_tex+'.fileTextureName', ColorMapFileTexture , type="string")
  cmds.setAttr( bump_mr_tex+'.fileTextureName', BumpMapFileTexture, type="string")


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

  # Set the mia_material to be a glossy material
  cmds.setAttr(dome_mia_shader_name+".refl_color", 1, 1, 1, type="double3")
  cmds.setAttr(dome_mia_shader_name+".reflectivity", 1)
  cmds.setAttr(dome_mia_shader_name+".refl_gloss", 0.3)
  cmds.setAttr(dome_mia_shader_name+".diffuse_roughness", 0)
  cmds.setAttr(dome_mia_shader_name+".diffuse_weight", 1)

  # Set the mia_material to be a matte material
  #cmds.setAttr(dome_mia_shader_name+".reflectivity", 0)

  # Set the mia_material_x_passes shader to use bump mode to 0 so bump maps are displayed correctly
  cmds.setAttr(dome_mia_shader_name+".bump_mode", 0)

  # Note mental ray bump directions are negative while the standard Maya bump2D depth value is positive
  # Set the bump step value to a default starting value of 0.0 to make the bump visible
  cmds.setAttr( bump_mib_passthrough_bump_map+".stepX", 0.0)
  cmds.setAttr( bump_mib_passthrough_bump_map+".stepY", 0.0)
  cmds.setAttr( bump_mib_passthrough_bump_map+".stepZ", 0.0)

  #Set the bump factor default to 1 to make the bump map visible
  cmds.setAttr(bump_mib_passthrough_bump_map+".factor", 1)


  # Connect the nodes

  # Connect the mia_material shader to the shading group
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.surfaceShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miPhotonShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miShadowShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miMaterialShader', f=True)


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
  
  #Create a mia_material_x_passes shader
  dome_mia_shader_name = cmds.shadingNode( 'mia_material_x_passes', n='dome_mia_material', asShader=True)	

  #Create a mia_material shader
  #dome_mia_shader_name = cmds.shadingNode( 'mia_material', n='dome_mia_material', asShader=True)	  

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


  # Set the filename for the mental ray texture nodes
  cmds.setAttr( color_mr_tex+'.fileTextureName', ColorMapFileTexture , type="string")


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

  # Set the mia_material to be a glossy material
  cmds.setAttr(dome_mia_shader_name+".refl_color", 1, 1, 1, type="double3")
  cmds.setAttr(dome_mia_shader_name+".reflectivity", 1)
  cmds.setAttr(dome_mia_shader_name+".refl_gloss", 0.3)
  cmds.setAttr(dome_mia_shader_name+".diffuse_roughness", 0)
  cmds.setAttr(dome_mia_shader_name+".diffuse_weight", 1)

  # Set the mia_material to be a matte material
  #cmds.setAttr(dome_mia_shader_name+".reflectivity", 0)

  # Connect the nodes

  # Connect the mia_material shader to the shading group
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.surfaceShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miPhotonShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miShadowShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miMaterialShader', f=True)



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