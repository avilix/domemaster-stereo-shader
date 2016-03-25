|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Table of Contents


# 3D Studio Max Installation Instructions #

The Domemaster installer makes it easy to use the 64-bit Domemaster3D shader with 3DS Max 2009-2014. The installer allows you to choose which version of Max you want to use with the fulldome rendering shader.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3D_version_1.3.3/max_2014_support_added.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3D_version_1.3.3/max_2014_support_added.png)

If you customized the location of your of 3DS Max program folder, you can specify which folder you want to use for your 3DS Max mental ray shader & include files. This is useful if you moved your copy of 3DS Max from the default `C:\Program Files\Autodesk` folder.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3D_version_1.3.3/custom_max_folder_selection.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3D_version_1.3.3/custom_max_folder_selection.png)

The Domemaster3D installer creates a new folder on your hard drive to hold the Domemaster3D documentation, texture maps, source code, and the uninstaller program.

The folder is located at:

`C:\Program Files\Domemaster3D`

# Using the Map Browser #

This is a screenshot of the 3DS Max Material Browser after the Domemaster Stereo Shaders have been loaded.

![http://www.andrewhazelden.com/projects/domemaster3D/images/version-1.3/3dsmax_material_browser.png](http://www.andrewhazelden.com/projects/domemaster3D/images/version-1.3/3dsmax_material_browser.png)

When you start 3D Studio Max, you will have 5 new mental ray lens shaders:
  * Domemaster Stereo Shader
  * domeAFL\_FOV
  * domeAFL\_WxH
  * latlong\_lens
  * rob\_lookup\_background

The **Domemaster Stereo Shader** is a lens shader that is used to render a set of stereoscopic angular fisheye images. You can control which camera view is rendered with the **Camera** control set to render either **Left** or **right** view. If you set the camera mode to "Center" you can render an optimized 2D DomeAFL\_FOV style fulldome image.

The **DomeAFL\_FOV** lens shader is an updated version of the 2D fulldome angular fisheye lens shader.

The **DomeAFL\_WxH** lens shader is an updated version of the 2D fulldome angular fisheye lens shader that calculates the field of view based upon diameter and height controls.

The **latlong\_lens** shader is a spherical/equirectagular/latlong shader that can be used to create panoramic backdrops or HDRIs from your scene.

The **rob\_lookup\_background** lens shader is a utility shader that is used to double check the **Separation Multiplier**, **Turn Multiplier**, and **Head Tilt** texture maps are projected into "screen space" coordinates before they are applied to the **Domemaster Stereo Shader**.

# DomeAFL\_FOV\_Stereo Shader Controls #

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/04/domemaster_3DS_Max_UI.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/04/domemaster_3DS_Max_UI.png)

**Field of View**: The field of view for the rendered fisheye image.

**Camera**: Choices are Center/Left/Right. Selects the camera to use for rendering. Center skips 90% of the calculations and gives you a highly optimized standard angular fisheye shader.

**Dome Radius**: (focus plane) This is actually the distance at which the camera's line of sight converge, so it's not really the dome size.

**Dome Forward Tilt**: Dome tilt in degrees. Note that this value is not used unless you enable Dome Tilt Compensation.

**Camera Separation**: The initial separation of the L/R camera's.

**Separation Multiplier**: A value between 0-1 that multiples the Camera Separation. This attribute is meant to be used with a grayscale texture mapped to the screen space using the right button. It's used to control the amount of 3D effect, and eliminate it where desired.

**Turn Multiplier**: A value 0-1 that controls the amount of the head turn. To be used with a grayscale texture. Typical use, keep the head straight while looking at the top of the dome.

**Head Tilt**: A value 0-1 (with 0.5 being the "neutral" value) that tilts the cameras (or head) left/right. 0 means 90 degrees to the left, 1 means 90 degrees to the right (if I remember correctly).

**Dome Tilt Compensation**: Enabling this option, shifts all the calculations by the # of degrees specified in Dome Forward Tilt. (Basically, it keeps the cameras/head vertical while the dome rotates forward.)

Maps used for the various multipliers and tilt settings will have to be custom made for the proper dome tilt.

**Vertical Mode**: Enable the vertical dome mode, which automatically adjusts the head turn and adds a turn compensation for the upper and lower part of the dome. It's a simplified and optimized version of the Dome Tilt Compensation with a 90 degrees tilt. It is faster and easier to use.