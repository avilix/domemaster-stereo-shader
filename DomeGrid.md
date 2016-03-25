|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Introduction #

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domegrid/domegrid-controls.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domegrid/domegrid-controls.png)

The Maya based DomeGrid tool provides a simple hemispherical preview shape that can be used to test the fulldome lens shader. The controls for the DomeGrid are accessed by opening the Outliner and selecting the "domeGrid" transform node.

In the attribute editor, expand the **Extra Attributes** to change the settings.

# DomeGrid Controls #

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domegrid/domegrid-attributes.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domegrid/domegrid-attributes.png)

The following settings can be adjusted on the _domeGrid_ group node:
  * Field Of View
  * Dome Radius
  * Display Mode
  * Double Sided Shading
  * Grid Line Thickness
  * Grid Surface Color
  * Grid Surface Transparency
  * Grid Line Color
  * Grid Line Transparency

The **Field of View** control makes it easy to display a dome grid pattern with an arbitrary field of view. You could use a value like 180 degrees for a fulldome shape, 220 degrees for an extended fulldome shape, or 360 degrees for a fully spherical shape.

The **Dome Radius** control allows you to scale the size of the DomeGrid geometry in the viewport.

The **Display Mode** can be used to set the DomeGrid to **Off** (a hidden state), a **Wireframe** mode, a **Shaded** mode, or a **Wireframe on Shaded** mode.

The **Double Sided Shading** controls make it possible to look "through" the DomeGrid surface from either the front face or back face view.

The **Dome Line** and **Dome Surface** controls let you adjust the color, transparency, and thickness of the DomeGrid surface group.

The **Grid Line Thickness** value allows you to change the width of the domeGrid stroke lines. This setting controls the a paintFx toon node's stroke attributes. When you scale the **Dome Radius** value you will need to adjust the **Grid Line Thickness** to keep the same apparent stroke width.

The **Grid Surface Transparency** control allows you to have a solid, semi-transparent, or fully transparent grid background. This background color is controlled using the **Grid Surface Color** attribute.

# DomeGrid Example Video #
<a href='http://www.youtube.com/watch?feature=player_embedded&v=5yC4Vw-Asq8' target='_blank'><img src='http://img.youtube.com/vi/5yC4Vw-Asq8/0.jpg' width='425' height=344 /></a>

This is a preview video that shows a few of the DomeGrid features.