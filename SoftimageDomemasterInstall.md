|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Domemaster3D for Softimage #

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/Using-the-domemaster3D-lens-shader.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/Using-the-domemaster3D-lens-shader.png)
The domemaster3D lens shader works with the mental ray renderer in Softimage.


## Table of Contents ##


## Introduction ##

The Domemaster3D Stereo Lens Shader is a custom mental ray shader that creates a stereoscopic 3D fisheye image. The lens shader provides advanced controls to optimize the viewing experience for stereoscopic dome renderings. This package also includes the 2D angular fisheye DomeAFL\_FOV and DomeAFL\_WxH lens shaders. The Domemaster 3D lens shader works with the Windows 64-bit version of Softimage.

This shader is based upon Roberto Ziche's **DomeAFL\_FOV\_Stereo lens shader** for 3DSMax and Daniel Ott's **Dome\_AFL lens shader**.

This is the user interface for the Domemaster3d lens shader. The DomeAFL\_FOV\_Stereo node allows you to render stereoscopic images for use in fulldome productions.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/domemaster-stereo-shader-settings.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/domemaster-stereo-shader-settings.png)


## Domemaster3D for Softimage Release History ##


### Version 1.4 Beta 4 - March 23, 2014 ###

Updated the Starglobe script to add realtime openGL and rendertime polygon subdivision smoothing on the "starry sky" quadsphere mesh.

Added a DomeViewer toolbar button that creates a fulldome media viewer in Softimage. You can use the tool to review domemaster angular fisheye images, or video files.

### Version 1.4 Beta 3 - March 4, 2014 ###

Updated the toolbar scripts to stop Softimage from opening the floating property windows when the python button scripts are launched. This significantly reduces the floating window clutter.

### Version 1.4 Beta 2 - March 3, 2014 ###

Improved the toolbar with a revised stereo camera rig, and improved starglobe tool, added a reference grid, an automagic fulldome tool, and new resolution presets.

Fixed an outstanding issue with the domeAFL\_FOV spdl file so the 2D lens shader works correctly.

### Version 1.4 Beta 1 - February 24, 2014 ###

Ported the Domemaster3D shelf from Maya to Softimage, added a Softimage version of the Starglobe tool.

### Version 1.1 - January 23, 2014 ###

The domeAFL library has been recompiled to match the shader binary in the Maya and 3DS Max release and the latlong\_lens shader has been added to the addon.

### Version 1.0 - June 15, 2012 ###

This is the beta version of the Domemaster3D Lens Shader for Softimage. It has been tested with Softimage 2013 64-bit on Windows 7.

## User Generated Movies ##

Here are a few interesting projects created by artists using the Domemaster3D shader.

### <a href='http://vimeo.com/51792909'>XETROV short film by Max Crow</a> ###

Xterov was created using the DomeAFL\_FOV shader with Softimage XSI and ICE.

<a href='http://vimeo.com/51792909'><img src='http://www.andrewhazelden.com/projects/domemaster3D/softimage/xterov_thumbnail.png' /></a>


## Installation Instructions ##
### Softimage on Windows ###

Open Softimage.

From the File Menu Select > Add-On > Install...

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/1.File-install-add-ons.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/1.File-install-add-ons.png)

In the Install Add-On window next to the Filename **Select a File...** section click on the button labeled **...**.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/2.install-addons-select-an-addon.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/2.install-addons-select-an-addon.png)

In the file dialogue select the file **domemaster3D.xsiaddon**. This is the add-on package file that contains the domemaster3D shader .dll and .spdl files. Click the **OK** Button.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/3.select-the-addon.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/3.select-the-addon.png)

The files that are contained in the **domemaster3D.xsiaddon** package will be listed in the Install Add-On window. Click the **Install** button to load the domemaster3D files.

By default the files will be copied into the folder:
<blockquote>C:\Users\Autodesk\Softimage_2013\Addons\domemaster3D</blockquote>

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/4.click-install.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/4.click-install.png)

Quit Softimage.

When you restart Softimage you can begin using the new lens shaders. The domemaster3D lens shaders will be listed in the Lens tab of the Render Tree.

You should now have the following new lens shaders:
  * domeAFL\_FOV
  * domeAFL\_FOV\_Stereo
  * domeAFL\_WxH
  * latlong
  * rob\_lookup\_background

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/preset-manager-lens-shader-nodes.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/preset-manager-lens-shader-nodes.png)

The Render Tree preset manager lists the available lens shaders.

## How to add a Lens Shader in Softimage ##
### Select Your Camera ###

Open the explorer window to view all of the cameras in the current scene. The hotkey is **Ctrl-8**.

Next, select a camera in the explorer window.

Press **Alt-Enter** to open the Scene\_Root:Camera:Camera editor window

### Choose Your Lens Shader ###

In the Camera Editor window click on the "Lens Shaders" tab. This view lists lens shaders currently applied to your camera.

Let's attach a new lens shader to the current camera. In the "Lens Shaders" tab click the Add button

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/camera-editor.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/camera-editor.png)

Click the Add button in the Camera Editor to add a lens shader.

Pick one of the lens shaders from the pop-up menu such as domeAFL\_FOV\_Stereo.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/camera-editor-add-button.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/camera-editor-add-button.png)

Choose a lens shader from the pop-up menu.

## Domemaster3D Lens Shader Controls ##

Field of View: The field of view for the rendered fisheye image.

**Camera:** Choices are Center/Left/Right. Selects the camera to use for rendering. Center skips 90% of the calculations and gives you a highly optimized standard angular fisheye shader.

**Dome Radius:** (focus plane) This is actually the distance at which the camera's line of sight converge, so it's not really the dome size.

**Dome Forward Tilt:** Dome tilt in degrees. Note that this value is not used unless you enable Dome Tilt Compensation.

**Camera Separation:** The initial separation of the L/R camera's.

**Separation Multiplier:** A value between 0-1 that multiples the Camera Separation. This attribute is meant to be used with a grayscale texture mapped to the screen space using the right button. It's used to control the amount of 3D effect, and eliminate it where desired.

**Turn Multiplier:** A value 0-1 that controls the amount of the head turn. To be used with a grayscale texture. Typical use, keep the head straight while looking at the top of the dome.

**Head Tilt:** A value 0-1 (with 0.5 being the "neutral" value) that tilts the cameras (or head) left/right. 0 means 90 degrees to the left, 1 means 90 degrees to the right (if I remember correctly).

**Dome Tilt Compensation:** Enabling this option, shifts all the calculations by the # of degrees specified in Dome Forward Tilt. (Basically, it keeps the cameras/head vertical while the dome rotates forward.)

Maps used for the various multipliers and tilt settings will have to be custom made for the proper dome tilt.

**Vertical Mode:** Enable the vertical dome mode, which automatically adjusts the head turn and adds a turn compensation for the upper and lower part of the dome. It's a simplified and optimized version of the Dome Tilt Compensation with a 90 degrees tilt. It is faster and easier to use.

## Node connections ##

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/Render-Tree-view.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/Render-Tree-view.png)

This is a screenshot of the render tree with the custom texture map applied using the camera's screen space.

Set the mib\_texture\_vector "selspace" aka. select space value to 4 (screen space) to enable the camera UV space projection. This means the texture will be loaded using a projection to the UV space coordinates of the camera.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/mib_texture_vector-settings-for-screen-space.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/mib_texture_vector-settings-for-screen-space.png)

Set the mib\_texture\_vector selspace value to 4 to map the texture to screen space.

```
mib_texture_vector.out -> mib_texture_remap.input

mib_texture_remap.out -> mib_texture_filter_lookup.coord
separation_map_png.tex -> mib_texture_filter_lookup.tex

mib_texture_filter_lookup.out -> Color_to_Scalar.input -> rob_lookup_background.tex

rob_lookup_background.out -> Camera Lens Shader.item

```

## How to make the custom map connections ##

Start by placing your texture maps for controlling the camera separation and turn maps in the "Pictures" folder for your current Softimage project.

Select your current camera and open the Render tree. The hotkey is **Shift-7**.

In the Render Tree toolbar click the update icon (circular arrows) to load the current nodes in the Render Tree view. Display the preset manager view.

### Connect the Domemaster 3D Shader ###

Scroll down in the Render tree sidebar to the SPDL Shaders -> lens section. Add a "domeAFL\_FOV\_stereo" shader to the work area.

Connect domeAFL\_FOV\_Stereo.out to the Camera Lens Shaders.item

### Let's create the supporting nodes for the custom separation map ###

The rob\_lookup\_background shader lets you preview your camera coordinate space Separation and Head Turn Map textures before you map them to the domemaster shader DomeAFL\_FOV\_Stereo node.

Scroll up to the Processing -> Conversion section in the render tree. Add a "Color to Scalar" node to the work area. This node will convert the texture from an RGB image into a greyscale "tex" image. Connect Color\_To\_Scalar.out to rob\_lookup\_background.tex

Scroll down in the Render tree sidebar to the mental ray -> texture section. Add a "mib\_texture\_filter\_lookup" node to the work area. This node merges the image data with our custom camera space UV coordinates. Connect mib\_texture\_filter\_lookup.out to Color\_to\_Scalar.input.

Double click on the mib\_texture\_filter\_lookup node in the render tree to open the editor. In the editor window next to the tex attribute click the New button. In the pop-up menu select "New From File...".

A "New Image Clip" dialogue will appear that lets you select a file texture from your hard drive. Select the file "separation\_map.png" from the "domemaster3D\_sample\_project\Pictures" folder. Click the "OK" Button.

The mib\_texture\_filter\_lookup node should now display a crescent shaped preview icon in the "tex" section.

Let's connect the custom nodes to create the camera space UV coordinates. Start by closing any floating editor windows.

We need to add two more nodes to the Render Tree. In the sidebar click on the mental ray -> textures section add a mib\_texture\_vector and a mib\_texture\_remap node.

Double click on the mib\_texture\_vector node. In the editor window change the mib\_texture\_vector node's selspace value to 4. This means the node will select the UV space for the texture from the current camera's UV coordinates. Close the floating editor window.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/mib_texture_vector-settings-for-screen-space.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/mib_texture_vector-settings-for-screen-space.png)

Set the mib\_texture\_vector selspace value to 4 to map the texture to screen space.

Connect the mib\_texture\_vector.out to the mib\_texture\_remap.input.

Connect the mib\_texture\_remap.out to the mib\_texture\_filter\_lookup.coord.

Deselect all of the nodes in the render tree. From the Tools menu in the Render Tree window select Rearrange (Ctrl-R) to cleanup the work area.

To see the results of the rob\_lookup\_background shader you need to click the "preview' or 'render' buttons.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/using-the-rob_lookup_background-shader.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/using-the-rob_lookup_background-shader.png)

This is what the rob\_lookup\_background shader looks like with a separation map applied.

### Example Domemaster3D Softimage Scenes ###

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/sample-project-files.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/sample-project-files.png)

The domemaster3D Softimage add-on comes with a few examples.

The scene **rob lookup background scene** is an example that shows the Render tree connections required to preview a mental ray screen space texture map using a lens shader.

The scenes **color-cube** and **luminance-cube** show a simple scene with the domeAFL\_FOV stereo lens shader and a checker textured cube.

The scenes color-cube-rig and luminance-cube-rig demonstrate a technique to use the Softimage stereo camera rig with the domeAFL\_FOV stereo lens shader. The domeAFL\_FOV lens shader was applied to the Left, Right and Center cameras in the Softimage stereo camera rig. For each physical camera in the rig the corresponding Domemaster3D shader was set to the appropriate view setting.

### Creating a Stereo Camera Rig ###

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/create-a-new-stereo-camera.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/create-a-new-stereo-camera.png)

You can create a new stereo camera rig using the Camera View menu item

From the Camera View menu, select New Camera > Stereo. We now have a new stereo camera rig in our scene. We need to edit the stereo rig's camera properties. From the Stereo menu item select **Properties...**

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/stereo-camera-properties1.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/stereo-camera-properties1.png)

You can edit the Softimage stereo camera rig properties using the stereo menu item.

In the camera properties window set the Stereo Type of **Off**. This will allow the DomeAFL\_FOV\_Stereo shader to control the camera separation settings.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/stereo-camera-properties.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/stereo-camera-properties.png)

When creating your own Softimage stereo camera rig set the Stereo Type to Off so the DomeAFL\_FOV Stereo node controls the camera separation.

You can now copy the domeAFL\_FOV\_Stereo shading network we created in the section titled "How to make the custom map connections" in the Render tree by selecting the nodes and selecting "Copy Shader Branch". Apply a copy of the whole shading network to the center "StereoCamera", right "StereoCameraRight", and left "StereoCameraLeft" cameras in the Stereo Camera Rig.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/stereo-camera-rig-explorer.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/stereo-camera-rig-explorer.png)

This is the Explorer view of the Softimage stereo camera r

Open the DomeAFL\_FOV\_Stereo node connected to each camera view in the rig. In the **DomeAFL\_FOV\_Stereo** node set the Camera popup menu item to match the name of the connected camera view.

For example set the camera setting to "Left" for the lens shader connected to the StereoCamera\_Left camera.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/stereo-camera-left.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/stereo-camera-left.png)

These are the settings I used for the **left camera** in the stereo rig.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/stereo-camera-right.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/stereo-camera-right.png)

These are the settings I used for the **right camera** in the stereo rig.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/center-stereo-camera-view.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/center-stereo-camera-view.png)

These are the settings I used for the **center camera** in the stereo rig.

You can render a "center" camera view by setting the DomeAFL\_FOV\_Stereo node to "Center" for the lens shader connected to the StereoCamera view.

### Rendering the Passes ###

You can render the Center, Left and Right camera passes at the same time by using the Render Manager.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/center-render-pass.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/center-render-pass.png)

The center camera is set to be rendered in the Default\_Pass in the render manager.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/left-render-pass.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/left-render-pass.png)

In the Render Manager I created another render pass called Left\_Pass. I set the Pass Camera to StereoCamera\_Left.

With the three passes created we can now render all the camera views at the same time.

![http://www.andrewhazelden.com/projects/domemaster3D/softimage/render-all-passes.png](http://www.andrewhazelden.com/projects/domemaster3D/softimage/render-all-passes.png)

To render the three cameras click the **Render > All Passes** Button.