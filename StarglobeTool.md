|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Introduction #

A new starglobe tool was added to the Domemaster3D shader. The starglobe feature makes it easy to create starry sky backgrounds.

The starglobe uses a specially prepared spherical shape that uses a unique all polygon quads based geometry. This eliminates the issues caused by pinch points on a typical NURBS or polygon sphere.

Included with the Domemaster3D version 1.4 release are .ma, .max, .fbx, and .obj meshes and a set of custom starglobe texture maps.

# 3DS Max Starglobe #

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/3ds_max_starglobe.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/3ds_max_starglobe.png)

The Starglobe has been completely redone for 3DS max in the Domemaster3D 1.4 Beta 9 release. There is a **starglobe\_mesh\_2K.max** and **starglobe\_mesh\_8K.max**  version of the starglobe that can be found in the folder: **C:\Program Files\Domemaster3D\sourceimages**

This updated model fixes the self-illuminating texture issue that was present in previous 3DS Max releases. I would like to extend a special thanks to Roberto Ziche for looking into the issue and providing a solution.

# Softimage Starglobe #

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/softimage-starglobe.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/softimage-starglobe.png)

A Starglobe is available in the Domemaster3D for Softimage toolbar.

The default texture applied is a 2K resolution starglobe texture map. You can upgrade the default 2K texture map to an 8K texture map by linking in the starglobe\_quadsphere\_8k.jpg file that is stored in the Softimage Addons folder:

`C:\Users\<username>\Autodesk\Softimage_<version-number>\Addons\domemaster3D\Application\bitmaps`

# Maya Starglobe #

The starglobe tool is visible in the Maya shelf and allows a Maya user to create a night sky backdrop with a single click.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/starglobe-shelf-item.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/starglobe-shelf-item.png)

When you run the starglobe tool you can use the **Attach to Camera** options menu to select a camera in your scene. This menu item will cause the starglobe mesh to be point constrained to your fulldome camera rig.

This point constrain technique creates the impression of an infinitely large starry backdrop by causing the starglobe to follow the camera around the scene. The point constraint still allows you to rotate the view freely around the night sky backdrop using the standard Maya view navigation tools.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/starglobe-1.4b7.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/starglobe-1.4b7.png)

The new starglobe tool is based upon Jason Fletcher's starglobe texture map that is explained on the blog post "Stars to Surround the Scene":

http://thefulldomeblog.com/2013/06/22/stars-to-surround-the-scene/

# Starglobe Resources #

## Models ##
The starglobe models are stored in the **C:\Program Files\Domemaster3D\sourceimages** folder on Windows.

The model "starglobe.obj" is an all quads based polygon sphere with a custom UV layout that is optimized to avoid texture pinching at the poles.

The model "starglobe\_mesh.ma" has the same geometry as the starglobe.obj model but is stored in a Maya ascii file.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/quadsphere-geometry.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/quadsphere-geometry.png)

## Textures ##

The starglobe textures are stored in the **C:\Program Files\Domemaster3D\sourceimages** folder on Windows.

The texture map named "starglobe\_quadsphere\_2k.jpg" is a 2048x2048 resolution starglobe image in the custom quadsphere UV layout.

The texture map named "starglobe\_quadsphere\_8k.jpg" is a 8192x8192 resolution starglobe image in the custom quadsphere UV layout.

The texure map named "starglobe\_equirect\_8k.jpg" is a 8192x4096 resolution starglobe image in the latitude/longitude equirectangular format.

# Starglobe Texture Mapping #

The Maya Starglobe Shelf tool uses a novel approach to texture mapping where an incandescent Lambert material is used in the realtime viewports and a mental ray native mia\_material\_x\_passes shading network is used at render time.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/Domemaster3D-Maya-Starglobe.jpg](http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/Domemaster3D-Maya-Starglobe.jpg)

The benefit of this approach is the 2048x2048 texture map is linked to the realtime version of the Lambert shader and at 8192x8192 texture map is used at render time with the mental ray shader.The mental ray shading nodes have the additional feature of avoiding the common "blurry-line" artifact.

In order to avoid lighting issues on the starglobe mesh a custom light linking mode was used in the mia\_material\_x\_passes shader. This should remove the need to manually stop the starglobe from interacting with the lights in your Maya scene.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/mia_material_x_passes_light_linking.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/starglobe/mia_material_x_passes_light_linking.png)