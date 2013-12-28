LatLong_lens shader for Softimage x64 on Windows
Feb 25, 2013 - Version 2.0 Beta

The original latlong_lens shader was written by Ralf Habel
ralf.habel@vi-motion.de

Softimage port by Andrew Hazelden
andrew@andrewhazelden.com
http://www.andrewhazelden.com

#Overview
This is the first Softimage 64-bit packaged version of the mental ray latlong_lens lens shader. The latlong_lens shader is designed to render equirectangular images. The shader can be used to create panoramic images with a single click of the render button.

#Installation
You can install the latlong_lens.addon in Softimage using the File > Add-Ons > Install... menu item.

#Shader Usage
To use the latlong_lens shader, open your the camera's property window. Click on the "Lens Shaders" tab and click the "Add" button to create a new lens shader. In the pop-menu select "latlong_lens". 

It is possible to mirror the rendering by enabling the lens shader's flipHorizontal attribute.

#Rendering Tip
The best equirectangular image output is from rendering with a 2:1 aspect ratio. (Like a 2048x1024 pixel or 4096x2048 pixel output)

#Links
The latlong_lens shader is also availble for 64-bit versions of Maya and 3DS Max:
http://www.andrewhazelden.com/blog/2011/01/latlong_lens-and-cubemap_lens-mental-ray-shaders-compiled-for-maya-2011-x64-on-windows/
