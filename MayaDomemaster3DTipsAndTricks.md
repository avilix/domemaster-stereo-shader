|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Table of Contents


# Setting up a new Maya Project #

When you setup a new Maya project you need to add the default supporting image files for the Domemaster3D shader.

After you install the Domemaster3D shader for Maya you will find the default images in the C:\Program Files\Domemaster3D\sourceimages folder on Windows or the /Applications/Domemaster3D/sourceimages folder on Mac OS X.

## Default domeAFL\_FOV\_Stereo Textures ##

The default domeAFL\_FOV\_Stereo turn and separation texture maps are called:
  * turn\_map.png
  * separation\_map.png
  * head\_tilt\_map.png

These textures are automatically connected to the Domemaster3D stereo camera rig when you use the **Fulldome Stereo Rig** shelf tool.

### Turn Map ###
The turn\_map.png image is used to take care of the stereoscopic effect at the zenith area directly above the viewers head. The texture map removes a swirl effect that would be present without the turn control setting.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/turn_map-mini.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/turn_map-mini.png)

The turn map also takes care of the area 180 degrees behind the viewer where the stereoscopic effect would be reversed if the viewer rotated their head to look at the back of the fulldome screen.

The texture is applied in screen space coordinates which means it controls the effect in the final fisheye image.

### Separation Map ###
The separation\_map.png image is the default separation texture that controls the area on the screen where the stereoscopic effect is visible.

The texture is applied in screen space coordinates which means it controls the stereoscopic effect in the final fisheye image. The white area in the texture map is rendered without any stereoscopic effect. If you are creating your own separation texture maps you will want to blur the transition between the white "monoscopic" region and the black "stereoscopic" region in the texture map to smooth the transition zone.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/scaled_separation_map.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/scaled_separation_map.png)


### Head Tilt Map ###
The head\_tilt\_map.png image is the sample texture for the head tilt control in the domeAFL\_FOV\_Stereo shader. By default the texture isn't connected to the shading network when you use the **Fulldome Stereo Rig** shelf tool.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/head_tilt_map-mini.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/head_tilt_map-mini.png)


## Default Domemaster3D Mia\_Material Textures ##

The default mia\_material textures for a domemaster shading network are called:
  * bumpChecker.iff
  * Checker.iff

**Note:** You can edit the name of the default textures by updating the variables in the Domemaster3D shader's python scripts.

### Color Material Texture ###

The Checker.iff texture is applied to the diffuse channel of the  domemaster color mia\_material when you use the **Color Material** or **Color + Bump Material** shelf items.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/checker-mini.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/checker-mini.png)

This is a rendering of the default Color Material on a sphere:
![http://www.andrewhazelden.com/projects/domemaster3D/wiki/color-material-sample.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/color-material-sample.png)

### Color + Bump Material Bump Map Texture ###

The bumpChecker.iff texture is applied to the bump map shading network when you use the **Color + Bump Material** shelf item. The texture is saved as a 16-bit IFF file for smoother gradations.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/bumpChecker-mini.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/bumpChecker-mini.png)

This is a rendering of the default Color + Bump Material on a sphere with a bump effect factor of 5:

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/color-bump-material-sample.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/color-bump-material-sample.png)

**Note:**
If you want to increase the bump map strength you need to select the mib\_passthrough\_bump\_map node and change the bump effect **factor** attribute in the attribute editor.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/mib_passthrough_bump_map-bump-effect-factor.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/mib_passthrough_bump_map-bump-effect-factor.png)

## Fixing Mental Ray Missing Texture Warnings ##

If the Domemaster3D default texture maps become unlinked in current Maya scene you may get a mental ray missing texture warning that happens when a new **mentalraytexture** node is used without a connected file texture.

If the default textures are missing when you open a scene you will get a mental ray warning when you try and render a scene that uses the textures.

```
// Warning: (Mayatomr.Shader) : color_mentalrayTexture1: referenced texture file "{TEXS}/sourceimages/separation_map.png" doesn't exist, ignored // 
// Error: (Mayatomr.Output) : file error: {TEXS}/sourceimages/separation_map.png // 
// Error: (mental ray) : /sourceimages/separation_map.png: can't open file for reading (No such file or directory) // 
// Error: (mental ray) : {TEXS}/sourceimages/separation_map.png: registry entry {TEXS} not found // 
// Error: (mental ray) : {TEXS}/sourceimages/separation_map.png: registry entry {TEXS} has no value // 
// Error: (mental ray) : {TEXS}/sourceimages/separation_map.png: registry entry {TEXS} not found // 
// Error: (mental ray) : {TEXS}/sourceimages/separation_map.png: registry entry {TEXS} not found // 
```

To fix the error you need to make sure the Domemaster3D textures are in the C:\Program Files\Domemaster3D\sourceimages folder on Windows or the /Applications/Domemaster3D/sourceimages folder on Mac OS X. It is possible to copy the default textures into your current project's sourceimages directory and tell Maya to refresh your scene.

If you get a missing texture error you can refresh your active scene either:

Switch to a new Maya scene ( File > New Scene ) and then re-open your current scene file.

or

Quit and restart Maya.

# Controlling Stereoscopic Depth #

This is a screenshot of the domeAFL\_FOV\_Stereo shader in the Maya attribute editor.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3d-maya-stereocontrols.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3d-maya-stereocontrols.png)

## Dome Radius ##
The **Dome Radius** value acts as a fulldome equivalent to the zero parallax zone in stereoscopic imaging.  The Dome Radius will allow you to control the convergence of the left and right cameras. This radius is a distance measurement in scene units from the camera. The default value is 360 units.

**Notes:**
  * If you want an object to come out of the screen at the audience place the object closer to the camera than the dome radius distance.
  * Objects near the dome radius distance will appear to have the same depth as the fulldome screen.
  * Objects located past the dome radius distance will appear to exist beyond the depth of the fulldome screen.

**Tip:** It is possible to key-frame animate the dome radius value if you are flying the stereo camera through a long sequence that needs to adjust the zero parallax zone for viewer comfort.

It is also possible to use a render "layer override" with Maya's render layer system to change the dome radius and cameras separation values. You might want to do this to "sculpt" the stereo depth in a scene to adjust the amount of stereo displacement between the foreground, midground, and background elements.

## Stereo Rig Camera Separation ##
The **Cameras Separation** value controls the stereobase of the left and right cameras. This value is measured in scene units.

The default setting is 6 cm.

You can freely adjust the cameras separation value until you get the correct amount of stereoscopic effect in your rendered image. Typically the cameras separation value will change depending on the scale of the scene.

**Example:** A microscopic scene will have a different setting than an indoor scene, or an interplanetary scene.

**Tip:** You can key-frame animate this attribute if you are traveling in a single shot from a back yard scene on earth to exploring planets in outer space.

### Camera Locator Scale ###

When you want to make the camera's icon larger in the perspective viewport most artists will select the camera icon and change the Camera's **ScaleX/ScaleY/ScaleZ** attributes.

Unfortunately this will also effect the DomeAFL\_FOV\_Stereo node's calculation for the camera separation value.

If you want to make the camera's icon in the Maya viewport larger it is important to select the camera and change the camera's **Locator Scale** attribute found in the **Object Display** section of the Attribute Editor.

If you want to change the scale of the cameras in the stereo rig you will have to change the locator scale attribute for the center, left, and right cameras.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/camera-locator-scale-attribute.jpg](http://www.andrewhazelden.com/projects/domemaster3D/wiki/camera-locator-scale-attribute.jpg)

This is the effect of properly scaling the Camera's Locator Scale attribute. You have a nice, easy to select camera and the stereo base calculations will work properly.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/viewport-camera-locator-scale.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/viewport-camera-locator-scale.png)


## Separation Multiplier ##
The **Separation Multiplier** attribute controls the area on the fulldome screen where the stereoscopic 3D effect is visible through the use of a custom texture map.

The Separation Multiplier attribute supports either a ramp texture or a mental ray file texture based shading network. The only requirements for the texture is that it provides a grayscale input and it has to be applied in screen space coordinates.

To make it easier to use the Separation Multiplier attribute there are two "screen space" tools in the Domemaster3D shelf.

### Screen Space Ramp ###

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeRamp.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domeRamp.png)

The **Screen Space Ramp** shelf item creates an editable gradient using the Maya ramp texture node. This is a quick way to keep the stereoscopic effect on the front part of the fulldome screen.

By default a new ramp node is connected to a rob\_lookup\_background node. This allows the effect to be previewed in the render view. When you want to use this shading network with the DomeAFL\_FOV\_Stereo node you can connect a greyscale output from the ramp node to the DomeAFL\_FOV\_Stereo nodes **Separation Multiplier** input.

This is a screenshot of the Screen Space Ramp nodes in the Hypershade work area before they are connected to the DomeAFL lens shader.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/ramp-control-hypershade.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/ramp-control-hypershade.png)

This is an image with the ramp texture set to have the stereoscopic 3D effect visible on the front half of the fulldome screen. This setting will cause the stereoscopic depth effect to be cancelled out on the screen area behind the viewer.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/ramp-attribute-editor.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/ramp-attribute-editor.png)

The selected position and selected color attributes are the primary controls for editing the location of the screen space ramp. By default a V-axis ramp is used.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/ramp-based-front-only-stereo.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/ramp-based-front-only-stereo.png)

### Screen Space Texture ###
![http://www.andrewhazelden.com/projects/domemaster3D/wiki/rob_lookup_background.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/rob_lookup_background.png)

The **Screen Space Texture** shelf item creates a mental ray texture shading network. The default texture connected to the shading network is the image **sourceimages/separation\_map.png**

By default a new screen space texture network is connected to a rob\_lookup\_background node. This allows the effect to be previewed in the render view. When you want to use this shading network with the DomeAFL\_FOV\_Stereo node you can connect a greyscale output from the rob\_map\_mib\_texture\_filter\_lookup node to the DomeAFL\_FOV\_Stereo nodes **Separation Multiplier** input.

This is a preview of a typical separation texture map before it is connected to the DomeAFL lens shader:

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/scaled_separation_map.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/scaled_separation_map.png)

This is a screenshot of the Screen Space Texture nodes in the Hypershade work area.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/texture-map-control-hypershade.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/texture-map-control-hypershade.png)


## Stereoscopic Viewer Comfort ##

When you review your stereoscopic 3D edits, try and make sure the transition isn't too jarring for the viewer when you switch from a wide shot to a medium or closeup shot.

Feel free to art direct the dome radius value to meet the needs of your stereoscopic scene. The dome radius default value is just a starting point. For example if you want to bring an object out of the screen and closer to the viewer you might have to change the settings for both the **dome radius** and **cameras separation** to maximize viewer comfort.

As a general stereoscopic tip, don't push more than 30% of the scene outwards into the audience. Objects that dramatically and regularly pop out of the screen towards the viewer can cause eye strain so the effect should be used sparingly.

For maximum viewer comfort try and keep most of the background scene elements further away from the camera than the dome radius distance.

## Adjusting the Stereobase ##
When you are creating stereoscopic renderings care should be taken to make sure the stereobase of the cameras (the camera separation value) isn't too large for the particular scene.

If you are creating a macro shot or ECU (extreme closeup) shot of an object you will have to reduce the camera separation value below the standard "human eye" seperation value of 6 cm.

The nearest object in the scene will typically limit the maximum "safe" camera separation value.

If you are interested, there are several stereo calculator programs and utilities that offer formulas for computing comfortable stereo viewing parameters.

## Hyperstereo ##

Hyperstereo is the term for creating images with a larger stereobase (camera separation) than the normal human eye spacing of approx 6 cm.

If there are no objects located close to the camera you are free to experiment with increasing the camera separation value to create larger stereoscopic depth effects such as hyperstereo. This can be useful in scenes with distant backgrounds like a mountain ranges on the horizon, or in an outer space scene with distant planets and moons.

The only downside with creating hyperstereo renderings is the viewer's perception that they are giant's looking down at a miniature model of the world.

# Rendering 2D and 3D with the Fulldome Stereo rig #

If you use Maya for fulldome renderings you might find it handy to know that you can use the same fulldome stereo camera rig to render both the 2D and 3D images. You don't have to switch between using the domeAFL\_FOV and domeAFL\_FOV\_stereo lens shaders.

The benefit of this technique is existing fulldome camera animation doesn't have to be recreated again when you switch from 2D to 3D.

The default Fulldome Stereo rig that is created using the stereo camera tool in the domemaster3D shelf uses the DomeAFL\_FOV\_Stereo shader. The shelf item automatically adds a parented camera with a center camera view, and left & right cameras to the scene.

You can render the monoscopic 2D center camera view in the Maya render settings by selecting the renderable camera called "stereoCamera".

You can render the stereoscopic 3D left and right stereo pair images by selecting the camera labeled "stereoCamera (Stereo Pair)" in the render settings window.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/Domemaster3D-render-settings.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/Domemaster3D-render-settings.png)

# Creating domeAFL Optimized Surface Materials #

The domeAFL shader usually works well with mental ray. However the most common rendering issue experienced with the domeAFL shader is known as a "blurry streaky" line artifact.

This artifact occurs near the spring line on a fulldome rendering when a default Maya "file" texture node is used. The rendering artifact is caused by the Maya file nodes' mip-map texture filtering. The best solution to this bug is to switch from using a Maya file node to a mental ray file texture node.

This is a cropped fisheye rendering of a planet that is textured using a Lambert material and a maya file texture. The blurry streak effect is visible on the left side of the planet.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/blurry-streak-artifact-maya-file-node.jpg](http://www.andrewhazelden.com/projects/domemaster3D/wiki/blurry-streak-artifact-maya-file-node.jpg)

This is a cropped fisheye rendering of a planet that is textured using a mia\_material and a mental ray file texture. The blurry streak effect is gone and the planet renders normally.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/blurry-streak-artifact-mental-ray-mia_material.jpg](http://www.andrewhazelden.com/projects/domemaster3D/wiki/blurry-streak-artifact-mental-ray-mia_material.jpg)

The mental ray file texturing node connections can be tedious to set up so two new material presets were added to the Domemaster3D shelf.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/Domemaster3D-shelf-materials.jpg](http://www.andrewhazelden.com/projects/domemaster3D/wiki/Domemaster3D-shelf-materials.jpg)

## Color Material Node Connections ##

The **Color Material** preset adds a mia\_material to the scene and uses a mental ray file texture node as the diffuse color texture.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/color-dome-mia_material-network.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/color-dome-mia_material-network.png)

## Color + Bump Material Node Connections ##

The **Color + Bump Material** preset adds a mia\_material to the scene and uses a mental ray file texture node as the diffuse color texture and sets up a mental ray bump map shading network.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/color-bump-dome-mia_material-network.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/color-bump-dome-mia_material-network.png)

## Connecting Bump Maps to the mia\_material\_x\_passes shader ##

The mia\_material\_x\_passes shader has a slighlty different feature set than the previous mia\_material shader.

If you want to connect a mental ray native bump map shading network you need to expand the "Advanced" section in the Attribute Editor and set the **Bump Mode** to zero. Once the setting is modified the bump maps show up on the material.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/mia_material_x_passes-bump-maps.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/mia_material_x_passes-bump-maps.png)

The mental ray bump node connections are:

```
mib_texture_vector.outValue -> mib_texture_remap.input

mib_texture_remap.outValue -> mib_passthrough_bump_map.coord

mib_bump_basis2.u -> mib_passthrough_bump_map.u
mib_bump_basis2.v -> mib_passthrough_bump_map.v

mentalrayTexture.message -> mib_passthrough_bump_map.tex

mib_passthrough_bump_map.outvalue -> mia_material_x_passes.bump
```

Note: The mib\_passthrough\_bump\_map's **factor** attribute controls the bump depth.

## Native Maya Surface Materials Blurry Streak Fix ##

If you need to use native Maya file nodes and Maya surface materials with the DomeAFL shader you can use an alternate solution to fix the "blurry streaky" line artifact. The fix is to use two different field of view values for the renderings - one in the DomeAFL node and one in the camera's attribute settings.

This sounds weird the first time you hear it but it does fix the problem!

When a scene is rendered with the DomeAFL angular fisheye shader, the FOV (field of view) for the rendering is controlled by the DomeAFL node in the attribute editor. This means we can change the value in the camera attribute window and it won't effect the camera framing in the final render.

For example if the domeAFL node was set to render a fisheye image with a 180 degree FOV, and your DomeAFL based perspective camera was set to display the real-time perspective view with a 4 mm setting you might see the "blurry streaky" line artifact in your mental ray renders.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/4_mm_fov_view.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/4_mm_fov_view.png)

This is the camera set to use a 4 mm FOV setting for the real-time viewport.

If we keep the DomeAFL node at a 180 degree FOV and changed the camera's FOV setting to 500 mm the "blurry streaky" line artifact disappears because the high zoom value on the FOV attribute seems to changes the way mental ray calculates mip-map texture filtering for the maya file texture nodes.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/500_mm_fov_fix.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/500_mm_fov_fix.png)

The only major downside for this technique is that the realtime viewport shows a preview with a highly zoomed 500 mm field of view. To fix the realtime view's field of view we can change the FOV setting only at render time using the **pre and post render MEL** script option in the Render Settings window.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/pre_and_post_render_fov_mel.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/pre_and_post_render_fov_mel.png)

Here are two simple mel commands that will change the field of view when you render and image and then set the field of view back to normal afterwards.

Open the Render Settings window. Scroll down to the bottom of the window and expand the **Render Options** section.

### DomeAFL\_FOV\_Stereo Camera Blurry Streak Fix ###

Type the following line in the Pre render MEL field:
```
setAttr "stereoCameraCenterCamShape.focalLength" 500;
```

Type the following line in the Post render MEL field:
```
setAttr "stereoCameraCenterCamShape.focalLength" 4;
```

Make sure the MEL commands are typed in with straight quotes around the camera names. If you copy the commands right from the WIKI you might get curly quotes when you paste the text snippets into your MEL window.

Note: In the script example you can change the camera name by swapping your active camera name where the word **stereoCameraCenterCamShape** is written in the MEL field.

You can change your default focal length from 4 mm to a comfortable viewing setting of your choice in the Post render MEL field.

If you want to change the field of view settings for multiple cameras in your scene you can paste the code in the Pre render MEL & POST render MEL fields multiple times as long as you keep a semicolon between each line of code.

Multi-camera Pre render MEL field example:
```
setAttr "stereoCameraCenterCamShape.focalLength" 500; setAttr "persp1Shape.focalLength" 500; setAttr "pathAnimationCamShape.focalLength" 500;
```

In this example I am changing the field of view settings on three camera "shape" nodes called:
  * stereoCameraCenterCamShape
  * persp1Shape
  * pathAnimationCamShape

### DomeAFL\_FOV Camera Blurry Streak Fix ###

If your fulldome camera was called "domeAFL\_FOV\_Camera1" you would open the render settings window, scroll down to the Render Options section and do the following:

Type the following line in the Pre render MEL field:

```
setAttr "domeAFL_FOV_CameraShape2.focalLength" 500;
```


Type the following line in the Post render MEL field:

```
setAttr "domeAFL_FOV_CameraShape2.focalLength" 4;
```


I would like to thank Jason Fletcher of the Charles Hayden Planetarium for his guidance and help testing the DomeAFL mia\_material presets and the DomeAFL field of view override tip.

# Using Mental Ray Physical Sun & Sky #

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/sun-and-sky-render.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/sun-and-sky-render.png)

The domeAFL and domeAFL\_FOV\_Stereo shaders are compatible with the mental ray Physical Sun & Sky system in Maya. The Physical Sun & Sky feature allows artists to create outdoor renderings with a realistic sky, a visible sun disc, and final gather based lighting and shadows.

The domeAFL, domeWxH, and Fulldome Stereo rig tools in the Domemaster3D shelf now make the correct lens shader connections to support the mental ray Physical Sun and Sky system.

If you are manually connecting the domeAFL shaders to a camera the solution to enable mental ray sun & sky support is to switch from connecting to the camera.miLensShader input to use the camera.miLensShaderList input.

This is done because the primary lens shader connection is overwritten with a **mia\_exposure\_simple1** node by Maya's automatic mental ray Physical Sun & Sky "create" button.

## Manually setting up the Physical Sun & Sky System ##

If you don't want to use the camera tools in the Domemaster3D shelf, an alternate way is to connect a domeAFL shader to the camera.miLensShaderList input.

This first step is to start by adding the mental ray Physical Sun & Sky system to your Maya scene.

Open the render settings window.

Switch to the Indirect Lighting tab.

In the Environment section, look for the label text **Physical Sun & Sky**.

Click on the "Create" button to add the Physical Sun & Sky system to your scene.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/sun-and-sky-render-settings-create.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/sun-and-sky-render-settings-create.png)

Next you need to connect the DomeAFL lens shader to the miLensShaderList input. To do this select the camera in your scene scene.

Open the attribute editor window and scroll down to the mental ray section.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/sun-and-sky-expand-lens-shader-section.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/sun-and-sky-expand-lens-shader-section.png)

Expand thee **Lens Shaders** section and click the "Create" button.

In the **Create Render Node** window select either the DomeAFL\_FOV, DomeAFL\_WxH, or DomeAFL\_FOV\_Stereo lens shader.

The DomeAFL lens shader is now connected to the miLensShaderList input.

This is a view of the correct lens shader connections with a DomeAFL\_FOV lens shader and the Physical Sun & Sky system active.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/sun-sky-node-connections.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/sun-sky-node-connections.png)