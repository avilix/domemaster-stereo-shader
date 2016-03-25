|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|



# Introduction #

The DomeAFL\_FOV\_Stereo lens shader renders stereoscopic fulldome content using the mental ray renderer. The node operates by creating an angular fisheye output that is drawn using a panoramic style of stereo rendering which is different than a traditional parallel camera technique because it takes care of the left and right stereo crossover zone that would occur at the back of the fulldome theater screen.

Let's explore the Maya user interface for the render node.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_domeafl_fov_rendering.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_domeafl_fov_rendering.png)

# Adding a Fulldome Stereo Camera #

A stereo fulldome camera rig is added to your Maya scene using either the Domemaster3D menu in the rendering menu set, or the "stereo rig" tool in the Domemaster3D shelf.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/fulldome_stereo_rig_shelf_tool.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/fulldome_stereo_rig_shelf_tool.png)

Once a rig has been added to your scene, you can edit the fulldome settings by selecting the "DomeStereoCamera" in the outliner.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_outliner_domestereocamera.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_outliner_domestereocamera.png)

Next, you need to open the attribute editor window to the "center\_domeAFL\_FOV\_Stereo" tab. The domeAFL\_FOV\_Stereo node controls are now visible.

Note: The attributes on the left and right camera's domeAFL\_FOV\_Stereo nodes are driven using an expression from the center\_domeAFL\_FOV\_Stereo control.

# Attribute Editor Controls #

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_domeafl_fov_stereo_controls.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_domeafl_fov_stereo_controls.png)

Let's go over the controls, one at a time.

## Domemaster Stereo Shader Controls ##

The "Domemaster Stereo Shader" section has the primary controls for the fulldome lens shader.

### Camera ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_camera_control.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_camera_control.png)

The camera popup menu tells the node which view it's rendering. The options are "Center", "Left", and "Right". The "Center" control can be used to render a regular 2D fulldome image.

Since we added the fulldome stereo rig to the scene using the shelf preset the camera popup menu can be ignored because the lens shader camera controls are already tied into the correct left and right camera views in the stereo rig.

### Field of View ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_fov_control.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_fov_control.png)

The field of view control adjusts the focal length of the angular fisheye rendering. By default a fulldome image has a 180 degree field of view.

If you want to include a bit of the "ground" in the scene, it is possible to increase the field of view slightly to a value like 220 degrees and the final rendered image will still look acceptable in a dome.

Tip: If you want to render a full 360 degree angular fisheye image you will need to update the custom maps that are applied to the stereo separation, and turn attributes.

### Dome Radius ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_dome_radius_control.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_dome_radius_control.png)

The Dome Radius control can be thought of as a fulldome equivalent of the standard zero parallax zone in Maya's default stereo camera rig. This control adjusts the distance in the scene where the depth converges in the left and right eye views.

Objects placed closer to the camera than the dome radius distance appear to come out at the audience. Anything located in and around the dome radius distance appears in stereoscopic 3D as if it is sitting right on the wall of the fulldome theater screen. Objects placed further away from the camera than the dome radius value appear to the viewer as if they are existing beyond the physical wall of the planetarium screen.

### Dome Forward Tilt ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_forward_tilt_control.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_forward_tilt_control.png)

This control can be used to compensate for a tilted theater screen. If your theater has no tilt angle you can leave this value at zero.

### Cameras Separation ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_cameras_separation.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_cameras_separation.png)

This controls the stereo base of the stereo camera rig and is measured in scene units. Since a typical Maya scene is set to use centimeters the camera separation is set to 6 cm.

If you are working in a scene that has a large scale, or a scene with a small scale, you can freely change the dome radius, and camera separation values to match the world size and keep the stereoscopic effect comfortable on the eyes. However, when you are tuning the camera separation value and the dome radius values, you should keep a basic ratio between the two controls.

The default settings have a 60:1 ratio where the dome radius is set to 360 cm, and the camera separation is set to 6 cm. This would represent the scale of a 22 foot dome. If you wanted to have the same 60:1 ratio on a much smaller Maya scene you could set the dome radius to 3.6 and the camera separation to 0.06 units.

Some artists prefer to use a higher ratio value 120:1 with a dome radius of 720 cm with a camera separation of 6 cm. This would represent the scale of a 47 foot planetarium dome.

Fulldome artist [Aaron Bradbury](http://www.luniere.com/) has suggested a ratio of approximately 154:1 gives a near ideal fulldome stereo result (with a 0.372 degree maximum separation on the rendered image). This would equate to a dome radius of 924, and a camera separation of 6 cm.

### Dome Tilt Compensation ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_dome_tilt_checkbox.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_dome_tilt_checkbox.png)

This checkbox enables or disables the Dome Forward Tilt control.

### Vertical Mode ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_vertical_mode_checkbox.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_vertical_mode_checkbox.png)

The vertical mode checkbox can be used if you have a curved fulldome screen that is mounted vertically against a wall and the viewers look forward at the screen.

## Stereo Display Controls ##

These controls are used to adjust the orange hemispherical preview shape that is added to the fulldome camera rig. The preview shape will update in realtime to show changes to the dome radius (the zero parallax zone), and the domeAFL\_FOV\_Stereo node's current field of view setting.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_fov_display_modes.jpg](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_fov_display_modes.jpg)

### FOV Display Mode ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_fov_display_mode_control.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_fov_display_mode_control.png)

The FOV display mode lets you choose the shading style used on the hemispherical preview surface that is attached to the stereo camera rig. The options are: Off, Wireframe, Shaded, and Wireframe on Shaded.

### Zero Parallax Color ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_zero_parallax_color_swatch.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_zero_parallax_color_swatch.png)

This color swatch controls the surface shader applied to the hemispherical preview shape.

### Zero Parallax Transparency ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_zero_parallax_transparency_control.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_zero_parallax_transparency_control.png)

The transparency slider allows you to make the hemispherical preview shape solid, or semi-transparent. The default value is 0.25 or 25% transparent.

A value of 0 makes the surface completely solid, and a value of 1.0 or 100% makes the surface invisible.

### Double Sided Shading ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_fov_double_sided_control.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_fov_double_sided_control.png)

Double sided shading make the inside and outside of the hemispherical preview shape visible. Setting the mode to show frontfaces or backfaces can make it easier to see through the hemispherical shape.


### Safe Viewing Controls ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_safe_viewing_controls.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_safe_viewing_controls.png)

These controls are still under development and will be used to display a dome optimized safe viewing volume shape that can be thought of as an "envelope zone" that the primary action in the scene should take place inside of.

The controls will adjust a preview shape that indicates the closest and furthest areas in the scene for comfortable stereoscopic depth viewing. The shape updates in realtime with the values from the current dome radius and camera separation attributes.

## Custom Maps ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_custom_maps_controls.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_custom_maps_controls.png)

This section allows you to link a screen space texture map to control the separation multiplier, turn multiplier, and the head tilt attributes.

These texture maps are applied with a fit-to-fill screen space mapping on the final image in the render view.

You can start with the default texture files that are stored in the C:\Program Files\Domemaster3D\sourceimages folder or use the DomeTexture and DomeRamp tools in the Domemaster3D shelf to add your own custom maps.

If you use the DomeRamp tool on the separation multiplier attribute you can dynamically adjust the stereoscopic depth levels in your scene with a Maya ramp node and apply artistic decisions like flattening the depth at the back of the theater screen.

## Image Orientation ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_image_orientation.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_image_orientation.png)

The FlipX and FlipY controls allow you to mirror the image horizontally or vertically at render time.

### FlipX Checkbox ###

This control will flip the rendered image horizontally.

### FlipY Checkbox ###

This control will flip the rendered image vertically.

## Extra Attributes ##

The DomeAFL\_FOV\_Stereo node has a few extra attributes that are used internally. These settings are to be used by a technical director and don't need to be adjusted by an artist.

### Dome Version ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_dome_version_control.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_dome_version_control.png)

The Dome Version attribute tracks the version of the software that was used to create the original camera rig. The current value is 1. This control will allow future editions of the DomeAFL\_FOV\_Stereo node to upgrade an existing camera rig and add new controls and preferences.

### Preview Shape ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_preview_shape_control.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_preview_shape_control.png)

This attribute tracks the name of the orange hemispherical preview shape that is attached to the current camera. This shape is created dynamically by the FOV Display Mode controls.

The preview shape "DomeStereoCameraPreviewHemisphere" and the preview curve 'DomeStereoCameraPreviewCurve" are parented to the domeStereoCamera rig so they follow the stereo rig in the scene when the camera is animated.

If you are curious, you can take a look in the outliner and expand the shape node + "plus sign" on the DomeStereoCamera rig. You will notice the preview curve and hemisphere geometry listed at the bottom of the stereo rig's group.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_outliner_preview_shape.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_outliner_preview_shape.png)


### Preview Curve ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_preview_curve_control.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_preview_curve_control.png)

This attribute tracks the name of the NURBS curve used to drive the creation of the orange hemispherical preview shape. The curve's shape adjusts in realtime based upon the domeAFL\_FOV\_Stereo node's current dome radius and the field of view settings.

Note: The preview curve is hidden from the Maya scene with the "Intermediate Object" checkbox on the NurbsCuve.

# Working in 3D #

When you are working in the Maya viewport you can get a realtime stereoscopic 3D view of your scene if you look through the stereo camera rig. This view is rendered with a wide angle mode in openGL and is very helpful for working out comfortable camera separation, and dome radius settings in realtime with a pair of red/cyan anaglyph 3D glasses.

Let's look through the stereo camera rig. Open the Panels menu in the viewport. Select the Stereo > DomeStereoCamera menu item. This will put us inside the stereo fulldome camera.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_switch_to_stereo_view.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_switch_to_stereo_view.png)

Let's enable openGL anaglyph 3D rendering in the viewport. In the Stereo menu in the viewport, select either "Anaglyph" for a full color display mode, or "Luminance Anaglyph" for a black and white anaglyph version of the scene.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_realtime_stereo_anaglyph.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/maya_realtime_stereo_anaglyph.png)

This screenshot shows a simple scene that has been rendered with the fulldome stereo camera on the left and openGL on the right (with luminance anaglyph mode enabled).

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/rendered_vs_realtime_fulldome_blockworld.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeafl_fov_stereo/rendered_vs_realtime_fulldome_blockworld.png)

Since the viewport lacks raytracing support we can't see an exact match of the distortion in the fulldome image.

Even with this limitation in place the viewport is still extremely useful because it can save you making countless fulldome renders trying to fine tune the dome radius (zero parallax zone) and the camera separation values. If the hardware viewport version of the scene feels comfortable on the eyes, the raytraced fulldome version shouldn't cause eye strain either.

We can use the hemispherical preview shape in shaded mode to "cut through" the scene in the viewport and check what objects have negative vs positive parallax. What this means is objects "inside" the hemispherical shape will appear to come off the theater screen towards the audience, and objects outside the hemispherical shape will appear to exist beyond the walls of the fulldome theater.