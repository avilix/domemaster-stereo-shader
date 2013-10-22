Domemaster3D Stereo Lens Shader for Maya x64 and 3DS Max x64
Version 1.4 B4 - Oct 21, 2013

Maintained by Andrew Hazelden
andrew@andrewhazelden.com

About This Shader
----------------------
The Domemaster Stereo lens shader is a custom mental ray shader that creates a stereoscopic 3D fisheye image. The lens shader provides advanced controls to optimize the viewing experience for stereoscopic dome renderings. 

The shader collection also supports fulldome 2D rendering using either the DomeAFL_FOV shader, the DomeAFL_WxH shader, or the "center" camera option in the DomeAFL_FOV_Stereo shader.


Version 1.4 Beta 4 Changes
---------------------------------
Oct 21, 2013

Maya Changes
-----------------

DomeAFL_FOV_Stereo - Now with a real-time OpenGL Stereo3D preview viewport using 4mm wide angle (non-fisheye) hardware rendering
  Added a custom preRender and postRender mel script called domeRender.mel
  The domeRender.mel script allows the Maya stereo camera rig + domeAFL_FOV_Stereo shader to display a realtime anaglyph 3D preview in the viewport. The openGL display mode shows a stereo3D version of the scene with the current camera separation, and dome radius (zero parallax values) and a 4 mm wide angle (non-fisheye) field of view.
  The domeRender.mel script also adjusts the domemaster3D camera rig's internal "shape node" focal length to solve the blurry line artifact with a toggle between 4mm FOV in the viewport and 500mm FOV at render time.
  
Dome Viewer
  Added a fulldome and panoramic image+movie viewer. The viewer supports all image and movie formats that can be opened using the Maya File Texture and Movie Nodes. You can display immersive images, image sequences, and movie files with accelerated RAM playback. Tilted fulldome theater screens can be simulated with the "Dome Tilt" attribute.
    
  A Bradbury alignment grid has been included for previewing calibrated fulldome scenes.

  The following panoramic viewing modes are supported:
    180 Degree Fulldome
    360 Degree Angular Fisheye
    Mirror Ball
    Equirectangular (LatLong)
    Cube Map 3x2
    Vertical Cross Cube
    Horizontal Cross Cube
    Vertical Tee Cube
    Horizontal Tee Cube
    Vertical Strip Cube
    Horizontal Strip Cube
    Mental Ray Horizontal Strip Cube

Starglobe Updates
  Updated the Starglobe tool so the "Attach to Camera" menu uses the base camera name like 'persp' instead of the camera's shape node name like 'perspShape1'.

Dome Text Upgrades
  Added 93 international character encoding formats
	Added controls for converting characters to:
    Upper Case
    Lower Case
    Hex Words
    Hex Single Column
    Binary Words
    Binary Single Column
	Added DomeText aim constraints
  Added Cylinder geometry support
  Added Lambert material support
  Added text animation features for automatic left/right/up/down scrolling text
  Changed the caption for the Copy Node Settings menu to "Copy Text Settings From"
  Added folder icon to Save Image As field
  Added Flip Text Direction control for horizontal text mirroring on a plane or cylinder surface

Galaxy Creator
 Changed the caption for the Copy Node Settings menu to "Copy Particle Settings From"
 
Updated userSetup.py script for better compatibility with mentalCore. The code to auto-reload the mental ray plugin "Mayatomr" at startup has been commented out.

Version 1.4 Beta 2 Changes
---------------------------------
Oct 6, 2013

Maya Changes
-----------------
Added DomeText Lambert shading options with incandescent texture mapping

Added DomeText text encoding support for English ASCII, Western Europe cp1252, all languages utf_8, Chinese Traditional Big5, Chinese Simplified gb2312, and Hong Kong Supplementary Character Set big5hkscs to UTF8 text conversion support.


Version 1.4 Beta 2 Changes
---------------------------------

3DS Max Changes
---------------

Starglobe Update
I've created a few different format starglobe models to make it easier for 3DS MAX users. The files are stored in the C:\Program Files\Domemaster3D\sourceimages folder.

There is a set of 2K and 8K texture resolution 3DS Max scene files: starglobe_mesh_2K.max, and starglobe_mesh_8K.max
There is a set of 2K and 8K texture resolution FBX scene files: starglobe_mesh_2K.fbx, and starglobe_mesh_8K.fbx (You may have to flip the surface normals on the mesh for proper Max based rendering)
There is a set of 2K and 8K texture resolution OBJ scene files: starglobe_mesh_2K.obj, and starglobe_mesh_8K.obj 

Maya Changes
----------------

Updated Domemaster3D Shelf icons to a unified golden orange color palette

Added a Domemaster3D Menu to the rendering menu set

Added the DomeText GUI tool for creating fulldome titles in Maya. This tool is powered by the ImageMagick convert.exe utility which is stored in the Domemaster3D/bin folder. The tool uses the active fonts installed in the system's font folder. Note: When the "Transparent background" checkbox is enabled the rendered text has crisp anti-aliased edges in the alpha channel but the text color channels are rendered with hard edges to avoid black fringing due to alpha channel pre-multiplication.

The Galaxy Creator and DomeText user interfaces are dockable windows when used with Maya 2011 and higher.

Added a starglobe tool to the Maya shelf and Domemaster3D menu. The starglobe tool creates a night sky backdrop. The tool has a new GUI that lets you point constrain the starglobe mesh to any camera in your scene. The starglobe textures and the starglobe spherical model are stored in the Domemaster3D/sourceimages folder.

Added an in-scene DomeAFL and DomeAFL_FOV_Stereo preview geometry shape. The preview shape displays the camera's field of view and can be displayed as a wireframe, shaded, or wireframe on shaded surface. In the DomeAFL_FOV_Stereo shader the shape's size is linked to the Dome Radius control to preview the stereoscopic zero parallax zone setting. The double sided shading controls let you choose how the surface is displayed with either both sides shaded, or only the inside or outside visible.

Added scene scale detection for setting the default domeAFL_FOV_Stereo dome radius and camera separation values based upon your current Maya scene scale [cm / meter / km / inch / foot / mile].

Added a custom fulldome stereo rig preset to the Maya StereoRigEditor. This allows a new fulldome 3D rig to be created by going to the Menu Create  > Cameras > Stereo Camera (DomeStereoCamera)

Added a userSetup.py script to handle the installation of the Domemaster3D menu and the addition of the camera rig to the StereoRigEditor list.

The default stereo rig can now be changed between the normal Maya stereo rig and the Domemaster3D rig by switching to the Rendering Menu set. From the Domemaster3D menu, select Dome Cameras > Choose a Default Stereo Rig > ... 

Renamed several of the MEL and python scripts for improved clarity

Updated the Galaxy Creator GUI
  Added elliptical galaxy support with radial and transverse orbits
  Added Galaxy Rotation attribute
  Added MultiPoint and MultiStreak particle rendering controls
  Added popup help captions for each of the attributes.
  Added a copy node settings option to reuse existing galaxy creation settings
  Added a "Open the Hardware Render Buffer window" button and hardware rendering presets

Added customized AE Template files for the domeAFL_FOV, domeAFL_WxH, and rob_lookup_background shaders.
  
Added the panotools based mpremap.exe application to the Domemaster3D/bin folder so textures could be remapped to different panoramic formats.

Version 1.3.5 Changes
---------------------------

Included an .obj mesh and a starglobe texture map for 3DS Max users.

Added a starglobe tool to the Maya shelf to create a night sky backdrop. The starglobe textures are stored in the Domemaster3D/sourceimages folder and the starglobe spherical model is stored in the Domemaster3D/models folder.

Upgraded the Maya dome shaders to use the mia_material_x_passes shader

Added Glow Intensity attributes to the Galaxy Creator GUI 


Version 1.3.4 Changes
---------------------------

Updated the the Automagic tool's dome grid color to a brighter yellow value. This makes the grid more visible in a Physical Sun & Sky scene.

Added a new HELP icon to the Maya Shelf toolset. This shelf item loads the domemaster stereo shader wiki page.


Maya Tools
---------------
The Maya Domemaster3D shelf has buttons for the following features:

-The "AutoMagic" tool creates a Domemaster3D fulldome stereo camera rig and a hemispherical yellow wireframe test scene
-The "Stereo Rig" tool creates a standard Domemaster3D stereo camera rig
-The "Dome Texture" tool creates a screen space file texture
-The "DomeRamp" tool creates a screen space ramp texture
-The "DomeAFL_FOV" tool creates a standard 2D domeAFL_FOV node + camera
-The "DomeAFL_WxH" tool creates a standard 2D domeAFL_WxH node + camera
-The "Color Material" tool creates a mia_material based mental ray shading network with support for color file textures.
-The "Color + Bump Material" tool creates a mia_material based mental ray shading network with support for color and bump file textures.
-The "Starglobe" tool creates a mia_material_x_passes based starry background for your fulldome scenes.
-The "DomeGrid" tool creates a hemispherical yellow wireframe reference grid.
-The "Galaxy Creator" tool creates dynamic particle based galaxies.
-The "DomeText" tool created raster titles and scrolling credits using the Dome Text GUI and ImageMagick.
-The "Viewer" tool creates an immersive fulldome and panoramic image+movie viewer.
-The "Wiki Help" tool loads the Domemaster Stereo Shader Wiki page in your web browser.
-The "Version Info" tool shows the current version number for the Domemaster Stereo Shader and provides links to the download page, and the NING group.

Note: The location of the default domemaster control map textures is now:
Windows:
C:\Program Files\Domemaster3D\sourceimages\

Mac OS X:
/Applications/Domemaster3D/sourceimages/

The Domemaster3D shelf tools have been updated to automatically link to the new sourceimages folder.


3DS Max Tools
---------------
After installing the Domemaster3D shader for 3DS Max, you will find 4 new Lens shaders in the Material/Map Browser Window:
-The "Domemaster Stereo Shader" is used for fulldome stereo rendering. The center option in the domemaster stereo shader can also be used to 2D fulldome rendering.
-The "domeAFL_FOV" shader is used for 2D angular fisheye fulldome rendering.
-The "domeAFL_WxH"shader is used for 2D WxH fulldome rendering.
-The "rob_lookup_background" is used to preview screen space texture maps before attaching them to the Domemaster Stereo Shader. Screen space coordinates are required when preparing turn maps, separation maps, and tilt maps.


Softimage Notes
----------------
Softimage provides an easy to use shader package installer format called an .xsiaddon. If you want to use the Domemaster3D shader with Softimage you can download the latest installer from the Domemaster Stereo Shader Google Code page:
http://code.google.com/p/domemaster-stereo-shader/


Documentation and Resources
----------------------------

Domemaster Stereo Shader Wiki
http://code.google.com/p/domemaster-stereo-shader/w/list

Join the discussion on the Domemaster Stereo Shader NING Group
http://fulldome.ning.com/forum/topics/stereoscopic-domemaster-images

Source Code:
http://code.google.com/p/domemaster-stereo-shader/


Project Developers
-------------------

Domemaster Stereo Shader for 3DS Max Created by Roberto Ziche
http://www.robertoziche.com/

Domemaster3D shader for Maya and Softimage by Andrew Hazelden
andrew@andrewhazelden.com
http://www.andrewhazelden.com/blog

Based upon Daniel Ott's DomeAFL Angular Fisheye Lens Shader
http://www.thedott.net/shaders/domeAFL/


Special Thanks
-----------------
I would like to thank the following people for their contributions:

Aaron Bradbury for the installer imagery from his Vortex fulldome short film.
http://www.luniere.com/project/vortex/

Aaron Bradbury for the inclusion of the fulldome alignment grid:
http://www.luniere.com/2013/03/07/hi-res-fulldome-alignment-grid/

Jason Fletcher for creating a high quality equirectangular starglobe texture.
http://thefulldomeblog.com/2013/06/22/stars-to-surround-the-scene/

Martin Watt for writing the original galaxies.mel script.

