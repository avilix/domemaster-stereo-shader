|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/DomeViewer) on Github.|
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# DomeViewer for Softimage Introduction #

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/domeviewer_xsi.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/domeviewer_xsi.png)

The DomeViewer tool creates an immersive fulldome image+movie viewer in Softimage. You can use the "Clips" property editor window to change the media file displayed on the fulldome viewer mesh. The 1 click DomeViewer toolbar button makes it easy to explore high resolution domemaster angular fisheye formatted still images, and video files.

# DomeViewer for Maya Introduction #

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/Fulldome_Image_Viewer_With_Grids.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/Fulldome_Image_Viewer_With_Grids.png)

The Dome Viewer tool creates an immersive fulldome and panoramic image+movie viewer.

The viewer supports all image and movie formats that can be opened using the Maya File Texture and Movie Nodes. You can display immersive images, image sequences, and movie files with accelerated RAM playback in the Maya viewport. Tilted fulldome theater screens can be simulated with the "Dome Tilt" attribute.

The following panoramic formats are supported:
  * 180 Degree Fulldome
  * 360 Degree Angular Fisheye
  * Mirror Ball
  * Equirectangular / LatLong / Spherical
  * Cube Map 3x2
  * Cylindrical
  * Vertical Cross Cube
  * Horizontal Cross Cube
  * Vertical Tee Cube
  * Horizontal Tee Cube
  * Vertical Strip Cube
  * Horizontal Strip Cube
  * Mental Ray Horizontal Strip Cube1
  * Quadsphere (Starglobe)

The dome viewer tool supports the following media formats:
  * png
  * tif
  * tga
  * jpg
  * bmp
  * psd
  * exr
  * mov - available on Mac OS X
  * qt - available on Mac OS X
  * avi - available on Windows

# Dome Viewer User Interface #

This is a screenshot of the DomeViewer GUI. The window is dockable so you can have the window floating or stuck to the left or right side of your Maya user interface.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/domeviewer-v1.5.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/domeviewer-v1.5.png)

## Panorama Options ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/panorama-options.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/panorama-options.png)

The **Panorama Format** options menu allows you to choose the type of panoramic imagery you want to view. If you click on the menu, you can use the up and down arrows to cycle through the different panorama display modes.

A small thumbnail image is used to show what a sample image looks like in each panoramic format type.

## Media Loading Options ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/media-loading-options.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/media-loading-options.png)

The **Media Type** options menu allows you to choose the type of imagery you want to load in the viewer. You can choose between Still Image, Image Sequence, and Movie File.

When you set the **Media Type** to the Movie File setting a **movie** node is added to the Dome Viewer shading network. On Windows the movie playback node supports AVI files. On Mac OS X the movie playback node supports Quicktime .mov and .qt files.

If you want to display a high resolution animation in the Dome Viewer it is recommended to use the image sequence option over the movie file.

The folder icon next to the **Image Name** field allows you to select media from your hard drive.

## Viewer Options ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/viewer-options.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/viewer-options.png)

The **Dome Tilt Angle** allows you to tip the viewer geometry to simulate a tilted dome theater screen. For example a value of **45** sets the theater screen to have a forward tilt of 45 degrees.

The **Field of View** control adjusts the panoramic camera's field of view in degrees.

**Image Exposure** controls the brightness of the image in the viewer. For a floating point image you can easily use values beyond the normal 0-1 / 0-255 dynamic range.

The **Color Tint** swatch allows you to apply a subtle color correction / color gain to the panoramic image. This can be used to add warmth to a sunrise scene or adjust for a color cast in the image. You can adjust the Image Exposure and Color Tint settings later by opening the Outliner, selecting the domeViewer item, and then changing the settings in the Attribute Editor's Extra Attributes section.

## Time Controls ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/time-controls.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/time-controls.png)

The time controls are needed if you choose either the **Image Sequence** or the **Movie File** setting in the **Media Type** options menu.

The **Start Frame** and **End Frame** allow you to choose what part of the animated sequence will be displayed.

The **Interactive Preview Cache** menu item enables RAM caching for the image sequence/movie. Once the sequence has loaded and played through the active start to end frame range the RAM caching will dramatically accelerate the playback speed.

## Extra Controls ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/extra-controls.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/extra-controls.png)

If the 180 degree fulldome mode is enabled you have the option of using the **Bradbury Alignment Grid**. This high resolution grid pattern allows you to precisely work out the placement of fulldome imagery in a calibrated space.

You can control the visibility and transparency of the Bradbury alignment grid by selecting the domeViewerGrid object's transform node in the outliner and editing the values in the Attribute Editor's Extra Attributes section.

The **Link Panorama to Camera** checkbox is useful if you are trying to navigate around in the panoramic image viewer. This control will **point constrain** the panoramic background to the viewer camera. The panoramic background will be linked so it follows the camera's motion, while allowing the camera view to freely tumble and roll in the viewport.

The **Show Focal Length in HUD** checkbox will turn on the current focal length HUD (Heads Up Display) message in the viewport. This is handy if you are trying to dynamically adjust the zoom level in the viewport using the **Zoom** view navigation control or the panoramic camera shape's focal length attribute.

The **Flip the Panoramic Image** checkbox will mirror the panoramic image so you are viewing the texture map as if it was an environmental reflection map. This effect is done by scaling the domeViewer shape (scaleX **-1).**

## Buttons ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/buttons.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/buttons.png)

The **Create Viewer** button adds an immersive viewer to the scene. **Note:** It is important to save your current scene before running this command as Maya won't ask you to save any unsaved changes before loading the DomeViewer.

The **Load Image in Render View** button loads the current image that is listed in the **Image Name** text field in the Render View window. The image is auto-sized to fit the Render View window size. You can view the image at the native resolution by pressing the 1:1 button in the Render View toolbar.

## View Navigation Controls ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/view-controls.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/view-controls.png)

After you add a Dome Viewer to your Maya scene you can use the standard Maya view navigation hotkeys + mouse buttons to easily navigate in the viewport. If you are on a laptop, or find your self using Maya with a graphics tablet or a trackpad you might find it helpful to use the set of view navigation controls in the lower part of the Dome Viewer window.

The **Roll** command makes it easy to simulate an "over the shoulder" style head rotation in a fulldome scene.

The **Zoom** control allows you to simulate different focal lengths when using the dome viewer. This control modifies the active camera shape node's focal length setting.

# Editing the Extra Attributes #

You can change the Dome Viewer's display mode, Exposure, Color Tint, and Transparency settings after creation using the Attribute Editor window.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/domeviewer-controls.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/domeviewer-controls.png)

Start by selecting either the **DomeViewer** node, or the **DomeViewerGrid** node in the outliner. Then open up the attribute editor and switch to the first tab named "DomeViewer" or "DomeViewerGrid". Scroll down to the Extra Attributes section (at the bottom of the Attribute Editor to see the custom settings.

The **Double Sided Shading** controls allow you to apply backface culling to the fulldome mesh and grid. This is useful if you want to view the fulldome "screen" from a distance and hide the foreground part of the screen that obscures the view.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/domeViewer-noculling.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/domeViewer-noculling.png)

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/domeviewer-backface-culling.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeviewer/domeviewer-backface-culling.png)

# Dome Viewer Example Video #

This is video clip that shows a preview of the Dome Viewer features.

<a href='http://www.youtube.com/watch?feature=player_embedded&v=hfIIDKswLm4' target='_blank'><img src='http://img.youtube.com/vi/hfIIDKswLm4/0.jpg' width='425' height=344 /></a>

# Special Thanks #

I would like to thank Aaron Bradbury for the fulldome alignment grid:

http://www.luniere.com/2013/03/07/hi-res-fulldome-alignment-grid/