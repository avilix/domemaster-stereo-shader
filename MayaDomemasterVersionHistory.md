|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Table of Contents


# Version History #

This is the version history for the Maya Domemaster3D shader.


## Version 1.4 Beta 10 - Released Dec 27, 2013 ##

Added the latlong\_lens shader for rendering spherical/equirectangular imagery.

DomeViewer
> Added Double sided rendering controls


## Version 1.4 Beta 9 - Released Dec 9, 2013 ##

**3DS Max Changes**

Updated the 3DS Max Starglobe files to fix rendering issues. The new 3DS Max scenes are stored in the folder:
C:\Program Files\Domemaster3D\sourceimages

Added install option for 3DS Max 2015 (beta) support

**Maya Changes**

Added an install option for Maya 2015 (beta) support

Updated the Galaxy Creator, Starglobe, DomeText, and DomeViewer window's so the window settings are restored from the last setting. This allows the docked vs floating, and docked left/right window settings to be remembered.

Changed the default for the domeAFL\_FOV and domeAFL\_FOV\_Stereo node's preview shape to the wireframe rendering mode.

Changed the default particle type setting for the Galaxy Creator GUI to MultiPoint particles.

Improved Linux Compatibility
The Domemaster3D shader files on Linux are installed to the folder: /opt/Domemaster3D/

Updated the mental ray lens shader's linux x64 makefile

Compiled a new linux x64 mental ray lens shader build of domeAFL\_FOV\_Stereo.so"

Updated the DomeText tool to scan the linux font folders at: /usr/share/fonts/


**DomeViewer Update**

Added support for previewing textures in the quadsphere (starglobe) mesh projection to the DomeViewer.

Added a "Flip the Panoramic Image" checkbox that causes a mirror effect on the panoramic image by flipping the panoramic texture so you are viewing the texture map as if it was an environmental reflection map viewed from the outside. This effect is done by scaling the domeViewer shape (scaleX  `*` -1).

**DomeText Update**

Rewrote the Linux DomeText font scanning to scan through each of the font folders located in the linux font path: /usr/share/fonts/

Improved the Mac OS X DomeText font scanning. Fonts that are installed in the /Library/Fonts, /System/Library/Fonts, and ~/Library/Fonts folders are now added to the font menu list. The font folder path is added so it is possible to know which version of a font is selected.


## Version 1.4 Beta 8 - Released  Nov 20, 2013 ##

**Maya Changes**

Added a set of Maya shelf tools to change the render resolution.

Added a 16x8k equirectangular starglobe texture "starglobe\_equirect\_reversed\_16x8k.jpg" to the sourceimages folder. This texture has been reversed for the view "inside" the night sky environment.

This release adds the DomeViewer tool, the DomeText tool, and a lot of other improvements to the Mac OS X release.

If you are interested in using the DomeText tool on Mac OS X, the ImageMagick library has to be downloaded separately. This ImageMagick library is available from:
http://www.imagemagick.org/script/binary-releases.php#macosx

## Version 1.4 Beta 7 - Released Nov 8, 2013 ##

**Maya Changes**

Added Maya shelf tool to force the Mental Ray plugin to load. This is useful if Mental Ray didn't start-up automatically.

Improved the DomeViewer cylindrical, mirrorball, and angular360 degree meshes.

**Maya + 3DS Max**

Updated the starglobe texture maps. The previous version had the starglobe 2K and 8K quadsphere texture direction inverted.



## Version 1.4 Beta 6 - Released Oct 27, 2013 ##

**Maya Changes**

**DomeViewer**

  * Added cylindrical panorama support to the domeViewer
  * Added a new 360 angular fisheye, and mirrorball mesh
  * Improved transparency support on the grid overlay
  * Added image exposure and color tint controls

**DomeText**

  * Added wrapU and wrapV attributes to the GUI. (It is now easier to create scrolling credits by setting the auto scroll direction to "scroll up" and un-checking the WrapV checkbox.)
  * Updated the text mirror controls

Updated the DomeGrid default settings.

Added code to detect if the Domemaster3D shader is running in GUI mode or batch mode. This will skip running the userSetup.py code for adding a custom menu when running in batch mode.

**Improved Maya 2010 support**

  * Updated the domeStereoRig.py camera rig file for Maya 2010 support.
  * Improved the dome\_AFL\_FOV\_Stereo GUI code for Maya 2010 support .
  * Updated the Domemaster3D menu system for stereo rig support in Maya 2010.
  * Updated the starglobe GUI window for Maya 2010 support.
  * Updated the Maya Shelf files.

## Version 1.4 Beta 5 - Released Oct 24, 2013 ##


**Maya Changes**

Updated the domeAFL\_FOV\_Stereo camera preview code to fix a bug that stopped batch rendering from completing with the new domeRender.mel script.

## Version 1.4 Beta 4 - Released Oct 21, 2013 ##

**Maya Changes**

**DomeAFL\_FOV\_Stereo**

Now with a real-time OpenGL Stereo3D preview viewport using 4mm wide angle (non-fisheye) hardware rendering
Added a custom preRender and postRender mel script called domeRender.mel
The domeRender.mel script allows the Maya stereo camera rig + domeAFL\_FOV\_Stereo shader to display a realtime anaglyph 3D preview in the viewport. The openGL display mode shows a stereo3D version of the scene with the current camera separation, and dome radius (zero parallax values) and a 4 mm wide angle (non-fisheye) field of view.
The domeRender.mel script also adjusts the domemaster3D camera rig's internal "shape node" focal length to solve the blurry line artifact with a toggle between 4mm FOV in the viewport and 500mm FOV at render time.

**Dome Viewer**

Added a fulldome and panoramic image+movie viewer. The viewer supports all image and movie formats that can be opened using the Maya File Texture and Movie Nodes. You can display immersive images, image sequences, and movie files with accelerated RAM playback. Tilted fulldome theater screens can be simulated with the "Dome Tilt" attribute.

A Bradbury alignment grid has been included for previewing calibrated fulldome scenes.

The following panoramic viewing modes are supported:
  * 180 Degree Fulldome
  * 360 Degree Angular Fisheye`*`
  * Mirror Ball`*`
  * Equirectangular (LatLong)
  * Cube Map 3x2
  * Vertical Cross Cube
  * Horizontal Cross Cube
  * Vertical Tee Cube
  * Horizontal Tee Cube
  * Vertical Strip Cube
  * Horizontal Strip Cube
  * Mental Ray Horizontal Strip Cube

> Note: `*`The 360 Degree Angular Fisheye and Mirror Ball panorama modes still need some work.

**Starglobe Updates**

  * Updated the Starglobe tool so the "Attach to Camera" menu uses the base camera name like 'persp' instead of the camera's shape node name like 'perspShape1'.

**Dome Text Upgrades**

  * Added 93 international character encoding formats
  * Added controls for converting characters to:
  * Upper Case
  * Lower Case
  * Hex Words
  * Hex Single Column
  * Binary Words
  * Binary Single Column
  * Added DomeText aim constraints
  * Added Cylinder geometry support
  * Added Lambert material support
  * Added text animation features for automatic left/right/up/down scrolling text
  * Changed the caption for the Copy Node Settings menu to "Copy Text Settings From"
  * Added folder icon to Save Image As field
  * Added Flip Text Direction control for horizontal text mirroring on a plane or cylinder surface

**Galaxy Creator**

  * Changed the caption for the Copy Node Settings menu to "Copy Particle Settings From"

Updated userSetup.py script for better compatibility with mentalCore. The code to auto-reload the mental ray plugin "Mayatomr" at startup has been commented out.

## Version 1.4 Beta 2 - Released Oct 6, 2013 ##

**3DS Max Changes**

**Starglobe Update**

I've created a few different format starglobe models to make it easier for 3DS MAX users. The files are stored in the `C:\Program Files\Domemaster3D\sourceimages` folder.

There is a set of 2K and 8K texture resolution 3DS Max scene files: **starglobe\_mesh\_2K.max**, and **starglobe\_mesh\_8K.max**
There is a set of 2K and 8K texture resolution FBX scene files: **starglobe\_mesh\_2K.fbx**, and **starglobe\_mesh\_8K.fbx** (You may have to flip the surface normals on the mesh for proper Max based rendering)
There is a set of 2K and 8K texture resolution OBJ scene files: **starglobe\_mesh\_2K.obj**, and **starglobe\_mesh\_8K.obj**

**Maya Changes**

Updated Domemaster3D Shelf icons to a unified golden orange color palette

Added a Domemaster3D Menu to the rendering menu set

Added the DomeText GUI tool for creating fulldome titles in Maya. This tool is powered by the ImageMagick convert.exe utility which is stored in the Domemaster3D/bin folder. The tool uses the active fonts installed in the system's font folder. Note: When the "Transparent background" checkbox is enabled the rendered text has crisp anti-aliased edges in the alpha channel but the text color channels are rendered with hard edges to avoid black fringing due to alpha channel pre-multiplication.

The Galaxy Creator and DomeText user interfaces are dockable windows when used with Maya 2011 and higher.

Added a starglobe tool to the Maya shelf and Domemaster3D menu. The starglobe tool creates a night sky backdrop. The tool has a new GUI that lets you point constrain the starglobe mesh to any camera in your scene. The starglobe textures and the starglobe spherical model are stored in the Domemaster3D/sourceimages folder.

Added an in-scene DomeAFL and DomeAFL\_FOV\_Stereo preview geometry shape. The preview shape displays the camera's field of view and can be displayed as a wireframe, shaded, or wireframe on shaded surface. In the DomeAFL\_FOV\_Stereo shader the shape's size is linked to the Dome Radius control to preview the stereoscopic zero parallax zone setting. The double sided shading controls let you choose how the surface is displayed with either both sides shaded, or only the inside or outside visible.

Added scene scale detection for setting the default domeAFL\_FOV\_Stereo dome radius and camera separation values based upon your current Maya scene scale **[/ meter / km / inch / foot / mile](cm.md)**.

Added a custom fulldome stereo rig preset to the Maya StereoRigEditor. This allows a new fulldome 3D rig to be created by going to the Menu **Create  > Cameras > Stereo Camera (DomeStereoCamera)**

Added a userSetup.py script to handle the installation of the Domemaster3D menu and the addition of the camera rig to the StereoRigEditor list.

The default stereo rig can now be changed between the normal Maya stereo rig and the Domemaster3D rig by switching to the Rendering Menu set. From the Domemaster3D menu, select Dome Cameras > Choose a Default Stereo Rig > ...

Renamed several of the MEL and python scripts for improved clarity

**Updated the Galaxy Creator GUI**

  * Added elliptical galaxy support with radial and transverse orbits
  * Added Galaxy Rotation attribute
  * Added MultiPoint and MultiStreak particle rendering controls
  * Added popup help captions for each of the attributes.
  * Added a copy node settings option to reuse existing galaxy creation settings
  * Added a "Open the Hardware Render Buffer window" button and hardware rendering presets

Added customized AE Template files for the domeAFL\_FOV, domeAFL\_WxH, and rob\_lookup\_background shaders.

Added the panotools based mpremap.exe application to the Domemaster3D/bin folder so textures could be remapped to different panoramic formats.


## Version 1.3.5 Beta 1 - Released August 20, 2013 ##

Included an .obj mesh and a starglobe texture map for 3DS Max users.

Added a starglobe tool to the Maya shelf to create a night sky backdrop. The starglobe textures are stored in the Domemaster3D/sourceimages folder and the starglobe spherical model is stored in the Domemaster3D/models folder.

Upgraded the Maya dome shaders to use the mia\_material\_x\_passes shader

Added Glow Intensity attributes to the Galaxy Creator GUI

## Version 1.3.4 - Released June 27, 2013 ##

Updated the the Automagic tool's dome grid color to a brighter yellow value. This makes the grid more visible in a Physical Sun & Sky scene.

Added a new HELP icon to the Maya Shelf toolset. This shelf item loads the domemaster stereo shader wiki page.


## Version 1.3.3 - Released May 30, 2013 ##

A new Galaxies Creator tool has been added to the Domemaster3D shelf. The Galaxy Creator tool is a user interface for Martin Watt's classic galaxies.mel script.

The DomeRamp tool has been updated so the default black & white ramp style is applied if the tool is run multiple times.

The Domemaster3D python scripts have been updated to improved Maya 2010 compatibility. The bug fix was a revision to the sourceimages path variables.

A new Maya camera locator scale attribute is added to fulldome cameras that are created with the Domemaster3D shelf tools.

The Domemaster3D installer program was updated to support custom path selection for the 3DS Max mental ray shader and include folders. This is helpful if users have installed 3DS Max outside of the default location:
**C:\Program Files\Autodesk**


## Version 1.3.2 - Released April 16, 2013 ##

Added preliminary Maya 2014 support

The Maya camera connections for the lens shaders have been updated. There is a fix for the issue where the mental ray physical sky & sun system will overwrite existing connections to the .miLensShader port. The physical sky & sun system will now use the miLensShaderList[0](0.md) connection on a camera. This correction was done by updating copies of Maya's **AEmia\_physicalskyTemplate.mel** & **createMentalRayIndirectLightingTab.mel** files.

The location of the default domemaster control map textures is now in the **C:\Program Files\Domemaster3D\sourceimages** folder on Windows or the **/Applications/Domemaster3D/sourceimages** folder on Mac OS X. The Domemaster3D shelf tools have been updated to automatically link to the new sourceimages folder.


## Version 1.3 - Released Nov 4, 2012 ##

Changed the DomeAFL\_FOV and DomeAFL\_WxH source code to match the DomeAFL\_FOV\_Stereo view orientation. Recompiled the Domemaster3D Mac / Windows mental ray shaders.

Added a python script for creating a domeAFL compatible mia\_material shading network. This should solve the typical "blurry grey line" texture sampling artifact that happens near the spring line.

Changed the default lens shader connections in the python scripts to support the mental ray sky and sun system.


## Version 1.2 - Released Aug 8, 2012 ##

Added a Domemaster3D shelf, enabled domeAFL\_FOV\_Stereo FlipX/FlipY options, created a python stereo rig setup script, added an automatic screen space file texture and ramp texture script


## Version 1.1 - Released July 28, 2012 ##

Added a Maya stereo camera rig example, Linux Build + Makefile, a new getting started guide, and new shader icons


## Version 1.0 - Released April 18, 2012 ##

Initial version of the Domemaster3D shader for Maya. Added support for Mac OS X.