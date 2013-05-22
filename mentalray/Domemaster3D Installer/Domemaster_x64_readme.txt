Domemaster3D Stereo Lens Shader for Maya x64 and 3DS Max x64
Version 1.3.3

Maintained by Andrew Hazelden
andrew@andrewhazelden.com

About This Shader
------------------
The Domemaster Stereo lens shader is a custom mental ray shader that creates a stereoscopic 3D fisheye image. The lens shader provides advanced controls to optimize the viewing experience for stereoscopic dome renderings. 

The shader collection also supports fulldome 2D rendering using either the DomeAFL_FOV shader, the DomeAFL_WxH shader, or the "Center" camera option in the DomeAFL_FOV_Stereo shader.

Updated:

-The new "Galaxy" shelf icon runs the Galaxy Creator tool that creates dynamic particle based galaxies. The Galaxies Creator tool uses Martin Watt's classic galaxies.mel script.

-The location of the default domemaster control map textures is now in the C:\Program Files\Domemaster3D\sourceimages folder on Windows or the /Applications/Domemaster3D/sourceimages folder on Mac OS X. The Domemaster3D shelf tools have been updated to automatically link to the new sourceimages folder.

-There is a fix for the issue where the mental ray physical sky & sun system will overwrite existing connections to the .miLensShader port. The physical sky & sun system will now use the miLensShaderList[0] connection on a camera.


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
-The "Galaxy" tool runs the Galaxy Creator tool that creates dynamic particle based galaxies.


3DS Max Tools
---------------
After installing the Domemaster3D shader for 3DS Max, you will find 4 new Lens shaders in the Material/Map Browser Window:
-The "Domemaster Stereo Shader" is used for fulldome stereo rendering. The center option in the domemaster stereo shader can also be used to 2D fulldome rendering.
-The "domeAFL_FOV" shader is used for 2D angular fisheye fulldome rendering.
-The "domeAFL_WxH"shader is used for 2D WxH fulldome rendering.
-The "rob_lookup_background" is used to preview screen space texture maps before attaching them to the Domemaster Stereo Shader. Screen space coordinates are required when preparing turn maps, separation maps, and tilt maps.


Softimage Notes
----------------
Softimage provides an easy to use shader package installer format called a .xsiaddon. If you want to use the Domemaster3D shader with Softimage you can download the latest installer from the Domemaster Stereo Shader Google Code page:
http://code.google.com/p/domemaster-stereo-shader/



Project Developers
-------------------
Domemaster Stereo Shader for 3DS Max Created by Roberto Ziche
http://fulldome.ning.com/forum/topics/stereoscopic-domemaster-images

Domemaster3D shader for Maya and Softimage by Andrew Hazelden
andrew@andrewhazelden.com      
http://www.andrewhazelden.com/blog

Domemaster3D for Maya Blog Link:
http://bit.ly/Dome3D

Source Code:
http://code.google.com/p/domemaster-stereo-shader/

Based upon Daniel Ott's DomeAFL Angular Fisheye Lens Shader
http://www.thedott.net/shaders/domeAFL/

Special Thanks
I would like to thank Aaron Bradbury for the installer imagery from his Vortex fulldome movie.
http://www.luniere.com/project/vortex/

