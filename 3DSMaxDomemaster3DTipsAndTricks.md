|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Table of Contents


# Automating Stereo Rendering in 3DS Max #

It's possible to automate the process of generating left & right views with the domemaster stereo shader in 3DS Max. Since the lens shader uses a mental ray generic UI builder .mi file, the shader's parameters are accessible using maxscript.

If you want to switch the lens shader's camera view you can access the **Camera** selector with:

```
renderers.current.camera_lens_shader.camera
```

You can set the view using on of the following values:

```
0 = Center
1 = Left
2 = Right
```

Using maxscript you can list the accessible lens shader parameters:
```
showproperties renderers.current.camera_lens_shader.camera
```


If you would like to know more about Maxscripting lens shaders check out the [MaxScript Help topic on the Mental Ray Renderer](http://docs.autodesk.com/3DSMAX/15/ENU/MAXScript-Help/files/GUID-EE96053B-6E67-4578-B1C7-2738CF47C5B1.htm)