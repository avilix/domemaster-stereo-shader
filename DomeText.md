|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|



# Introduction #

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/dometext_anaglyph.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/dometext_anaglyph.png)

The DomeText title tool makes it a snap to create raster titles and scrolling credits in Maya. When you add a new title element to your Maya scene the title creation settings are saved to the texture node. This makes it easy to re-edit and modify your DomeText title sequences.

The DomeText tool supports a wide variety of image output formats and is powered by the open source [ImageMagick library](http://www.imagemagick.org/script/index.php).

The ImageMagick library is included with the Windows 64-bit release of the Domemaster3D shader.

If you are interested in using the DomeText tool on Mac OS X, the ImageMagick library has to be downloaded separately.

This ImageMagick library is available from: http://www.imagemagick.org/script/binary-releases.php#macosx

For the technically inclined mac user you can also install ImageMagick using [MacPorts](https://www.macports.org/) with the command:
`sudo ports install ImageMagick`


# Dome Text User Interface #

This is a screenshot of the DomeText GUI. The window is dockable so you can have the window floating or attached to the left or right side of your Maya user interface.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/welcome-to-dometext.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/welcome-to-dometext.png)

## Copy Text Settings ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/copy-text-settings.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/copy-text-settings.png)

Any title created using the DomeText tool can be updated using the **Copy Text Settings From** options menu. This menu provides an easy way to reload the original creation settings for a title graphic into the DomeText window. It works by listing all of the DomeText created file nodes that exist in the Hypershade. When you select an item in the menu, the creation settings used in original title is recalled from the file node's Extra Attributes section and loaded into the DomeText window.

When a new title is created a default name is given to each file texture node like "dometextFileNode1". This is the name you will notice the next time you look in the **Copy Text Settings From** options menu after you create a few title elements.

If you want to better organize your Maya scene you can rename the "title card" file texture nodes in the Hypershade / Attribute Editor so you can find and reload the settings more easily. The next time you launch the DomeText tool you will see the new node names in the **Copy Text Settings From** options menu.

## Text Entry ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/text-entry.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/text-entry.png)

When you create a title you can type in or paste your title message in the text entry field. The entry field is flexible and supports extended characters and internationalized character encoding systems.

You are free to add spaces, tabs, and hard formatted newlines to your titles. The DomeText tool automatically wraps long paragraphs so you don't have to add hard returns to a block of text.

For larger title sequences you will need to manually set the Image Height (and possibly Image Width) to a higher setting in the Image Controls section. This will keep the title from being cropped off. If your titles are particularly long and tall you can set the Image Height to (auto) and manually scale the 1:1 aspect ratio of the generated text to match the length of the text.

## Font Styles ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/font-styles.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/font-styles.png)

The **Font** options menu lists all of the fonts that are installed in your operating system's font folder(s). The default font is the classic sanserif typeface "Arial".

On Windows the default font folder is:
  * C:\Windows\Fonts\

On Mac OS X the font folders are:
  * /Library/Fonts/
  * /System/Library/Fonts/
  * ~/Library/Fonts/

On Linux the default font folder is:
  * /usr/share/fonts/

The **Text Encoding** options menu controls the conversion of international character sets to the UTF-8 format. This allows the DomeText tool to handle non-Latin text entry with ease. The Text Encoding menu is very flexible and provides the choice of 93 character encoding types.

The default Text Encoding format is the Microsoft Windows default format known as "Western Europe" or "windows-1252".

If you want to use the Dome text tool with non English (non Latin) keyboard you should check your operating system's Control Panel / System Preferences window for the name of your current keyboard type and your localized / regional language settings. The DomeText tool has already been tested successfully with Chinese character sets using the "Traditional Chinese Big5" text encoding system and custom Chinese fonts.

**Note:** With some Chinese fonts you need to manually add newlines when creating larger paragraphs of text. This issue is due to the way the ImageMagick library calculates the length of a multi-byte UTF-8 block of text.

The **Font Style** options menu provides a selection of ImageMagick font controls to choose from. The main use for the Font Styles are to make the text appear a little bit thicker, or thinner.

The **Alignment** menu controls the position of the text in the image using a compass direction. **Center** alignment will place the text in the middle of the image. **North** places the text at the top of the image, and **South** places the text at the bottom. If you change the image height from (auto) to a specific size you will notice the vertical alignment controls have more effect. Most often you will want to go with the default value of **Center**.

The **Convert Characters to** controls let you reformat your text. You can change the text to UPPER CASE, lower case, Hex( 6e 65 61 74 ), or binary (01100010) formats. The Binary Words or Hex Words will fill the Dome Text image with a full screen of converted output.

The **Single Column** option adds a newline after every character grouping. If you combine the **Single Column** option with text animation, and a narrow but tall image size you can create slender ribbons of text that flow like the Matrix digital rain sequence.

The **Font Size** attribute controls the height and width of the rasterized Dome Text. This control uses **Points** as the measurement. In digital typography terms, it takes 72 points to equal 1 inch tall text. The valid range for the Font Size control is from 6 points to 2048 points. The default Dome Text font size is 96 points.

The **Kerning** control allows you to adjust the spacing between each character. This is useful if you want to make a paragraph of text appear condensed (tightly packed) or widely spaced out. This control uses **Points** as the measurement. You can use either a negative or positive value for kerning. A positive kerning value spaces text out. A negative kerning value will pull characters closer together than the default spacing for a font. This can be used to create an overlapping letter style which could be useful for a bold logo or title. The valid range for the Kerning control is from -1024 points to 2048 points.

## Color Styles ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/color-styles.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/color-styles.png)

The Color Styles section controls the background transparency setting, and the foreground and background colors used on the rendered DomeText.

The **Foreground Color** swatch controls the color of the rendered text. You can change the foreground color by clicking on the color swatch. If you want to keep the same hue and saturation but make the text brighter or darker you can use the slider in the DomeText window to the right of the color swatch.

In the color swatch window you can change your color picker from HSV (Hue Saturation Value) over to the RGB (Red Green Blue) color picker by clicking on the HSV popup menu and changing the color picker to RGB 0-1, or RGB 0-255. The RGB 0-255 format will be the most familiar color palette for longtime Adobe Photoshop users.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/changing-the-color-picker.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/changing-the-color-picker.png)

The **Background Color** swatch controls the area behind the rendered text. The background color value you choose here is also used as the "default color" value on the Maya file texture node which will become visible if text animation is used to scroll the dome text message outside the visible UV space of your supporting dome text geometry. If you want a solid fill color to be visible in the background behind your dome text you need to uncheck the "Transparent Background" control.

The **Transparent Background** checkbox allows you to create text that is rendered without any background fill color. This control is enabled by default.

**Note:** When the transparent background option is enabled the text has a smooth anti-aliased alpha channel but is rendered with a hard edged RGB color channel. This is done on purpose so the text renders correctly and smoothly in mental ray with a premultipled alpha channel. Having the hard edged color channel will reduce the risk of dark colored edge fringing artifacts that would occur if you have a saturated and colorful IBL background in your Maya scene.

If you un-check the transparent background option the text will be rendered with a fully anti-aliased color channel.

## Image Controls ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/image-controls.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/image-controls.png)

The Image Controls section allows you to choose the folder where the DomeText image is saved, the file name and file type, and the image width and height.

The **Save Image As** text field allows you to choose the file name and destination folder for the Dome Text generated image.

By default, the DomeText image is given an automatic file name like "sourceimages/text\_string\_2013-11-10\_00.01.14.png" but you can enter a custom file name of your choosing. Clicking the folder icon will open up a file dialog that allows you to navigate the file system on your computer.

By default the title text is saved as a raster .png image but you can also save the image to a tiff, targa, jpg, bmp, or psd format by typing in a custom file extension.

It is generally recommended to save the DomeText images in your current Maya project's sourceimages folder. This makes it easy to locate the files and use them with your batch rendering / network rendering software.

The **Image Width** and **Image Height** controls adjust the size of the generated DomeText image. The Image Height control adjusts the vertical height of the DomeText. The Image Width control adjusts the horizontal width of the DomeText. The dimensions are measured in pixels.

If you type a long message into the text entry field you will need to choose how the text is formatted and word wrapped by setting the image width and height to match the aspect ratio (shape) of the text block you want on screen.

The **Image Width** can be set to:
  * 64  px
  * 128 px
  * 256 px
  * 512 px
  * 1024 px
  * 1536 px
  * 2048 px
  * 3072 px
  * 4096 px
  * 8192 px

The **Image Height** can be set to:
  * (auto)
  * 64  px
  * 128 px
  * 256 px
  * 512 px
  * 1024 px
  * 1536 px
  * 2048 px
  * 3072 px
  * 4096 px
  * 8192 px

If you set the Image Height to the (auto) mode the DomeText raster texture is created with an automatically sized height that will fit all of the entered text on-screen. The downside with the (auto) height is you will have to scale your generated shape to the correct aspect ratio manually with the scale tool in Maya as this mode sets the text to use a 1:1 aspect ratio on the output geometry.

## Shape Controls ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/shape-controls.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/shape-controls.png)

You can use the **Align Text to Camera** options menu to select a Maya camera in your scene. The DomeText tool will then create an aim constraint to keep the text caption aligned towards the selected camera during your animation. If you move the text element or the camera the DomeText supporting shape will update the rotation automatically to face towards the selected camera.

The **Texture Node** control lets you choose what type of shading nodes will be created. It is generally recommended to use the "Lambert" texture node if you want to create animated DomeText. The "Lambert" option links a classic Maya file texture node to the Lambert material's color and incandescent attributes. You also have the choice to use a surface shader, or a mia\_material\_x\_passes texture node. The downside with these options is the Maya viewport doesn't preview the materials in realtime. At this point in time, the Lambert and Surface Shader materials are the only material types that support the DomeText animation controls.

If you use a classic Maya file texture node you might have to use the "blurry grey streak" tip in the Domemaster3D Shader's Tips & Tricks Wiki article to fix a common rendering artifact:

  * [Creating domeAFL Optimized Surface Materials](https://code.google.com/p/domemaster-stereo-shader/wiki/MayaDomemaster3DTipsAndTricks#Creating_domeAFL_Optimized_Surface_Materials)

  * [Native Maya Surface Materials Blurry Streak Fix](https://code.google.com/p/domemaster-stereo-shader/wiki/MayaDomemaster3DTipsAndTricks#Native_Maya_Surface_Materials_Blurry_Streak_Fix)

There is an option in the **Texture Node** popup menu labeled "Skip Node Creation" that will create a new raster title image and skip the addition of a file texture node in the scene. Note: The "Update Existing Node" option hasn't been implemented yet.

The **Supporting Shape** control allows you to apply the DomeText to either a flat **plane** or a curved **cylinder** shape.

The **Orientation Axis** options menu allows you to create the new DomeText surface object in your scene aligned to the Right(X), Top(Y), or Front (Z) view.

The **Shape Height** control allows you to choose how big to make the DomeText geometry in your scene. The shape height creates the DomeText shape in your scene by calculating the image aspect ratio from the image width and height you entered in the Image Controls section. This setting is measured using scene units.

If you want a cylinder shape to have a larger diameter you need to increase the **Image Width** setting found under the **Image Control** section to pad out the border of the DomeText generated image.

## Texture Placement ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/texture-placement.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/texture-placement.png)

The **Flip Text Direction** control will mirror your text horizontally which is handy if you chose to use the cylinder shape and want to make the text readable with the camera placed either on the inside or the outside of the shape.

The **Text Wrapping** modes allow you to have the scrolling DomeText message repeat infinitely when the file texture node is scrolled "offscreen" using the texture offset controls on the place2Dtexture Node. The horizontal **WrapU** or vertical **WrapV** attributes provide control over each axis of texture tiling. The names WrapU and WrapV represent texture repetitions on the U and V texture coordinate system.

If you are creating a scrolling title sequence you will probably want to disable the WrapV checkbox so the credits only scroll once vertically on-screen.

## Text Animation Controls ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/text-animation-controls.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/text-animation-controls.png)

The **Auto Scroll Direction** popup menu allows you to have the text scroll in a preset direction. You can choose between **Off**, **Scroll Left**, **Scroll Right**, **Scroll Up**, and **Scroll Down**.

For a stationary title leave the **Auto Scroll Direction** to **Off**.

A typical scrolling credits sequence would use the **Scroll Up** direction.

The **Start Frame** and **End Frame** options let you set the duration of a single scrolling cycle that moves the text using the motion selected in the Auto Scroll Direction control. By default the text scrolls using linear interpolation. You can change the animation curve style in the Maya Graph Editor window.

The **Loop Animation** control makes it easy to create a continuously animated title element. When the **Loop Animation** checkbox is enabled the the text will continue to scroll intently using the same scrolling velocity that was defined using the **Start Frame** and **End Frame** animation controls. This looping animation effect is done using a "post infinity" animation curve option.

Note: If you want the text to scroll continuously it is important to have the text wrapping "WrapU" and "WrapV" options enabled.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/cylindrical-dome-text.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/cylindrical-dome-text.png)

You can place a continuously scrolling message on the cylinder shape and the text will chase around in a circular fashion using either the **Scroll Left** or **Scroll Right** direction.

If you want to have a cylinder with a short height and a large diameter you can change the image width and height values to a wide screen aspect ratio like an image width of 8192 pixels, and an image height of 512 or 256 pixels.

## Custom ImageMagick Text Options ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/custom-imagemagick-text-options.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/custom-imagemagick-text-options.png)

The powerful open source Imagemagick graphics library is used to generate the DomeText graphic elements. The `Custom ImageMagick Text Options` field allows you to paste in your own [Imagemagick terminal commands](http://www.imagemagick.org/script/convert.php) that will be added to the command line when the DomeText image is generated.

If you click the Imagemagick Help wizard icon you can see the list of available options. This wizard icon links to the ImageMagick convert tool webpage:
http://www.imagemagick.org/script/convert.php

There are over 250 options available using the custom options text field. You can rotate and transform the frame, perform image filtering commands like like glows and blurs, load SVG graphics, and custom image background textures.

The -draw command allows you to create vector graphics primitives in the DomeText rendering context.

http://www.imagemagick.org/script/command-line-options.php#draw

## Generating the Text ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/dometext-buttons.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/dometext-buttons.png)

When you hit the **Create Text** button the new DomeText title is added to your scene.

You can review the image in the realtime viewport by enabling smooth shading + hardware texturing.

The **Load Image in Render View** button makes it possible to view the raw DomeText generated image in the Render View window. In the render view you can zoom in a pan the view using the normal view navigation controls. You can also inspect the color and alpha channels of the texture by toggling the controls in the Render View toolbar or by using the Display menu items.

Keep in mind when you view the DomeText image the Render View the "transparent background" setting was used to smooth the alpha channel in the texture and a hard edge was intentionally kept on the color channel to avoid color fringing during the mental ray rendering process.

# Re-editing DomeText #

After you create a DomeText title your settings are stored as re-editable "Extra Attributes" on the generated file texture node.

The notes field on the file texture node stores your entered title text message.

The DomeText creation data can be viewed using the Hypershade and the Attribute Editor. Select the file texture node and scroll down to the bottom of the Attribute Editor window to see the Extra Attributes.

Expand the Extra Attributes section. Every option that was selected in the DomeText tool is now visible as an extra attribute that is stored with the file texture node.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/extra-attributes.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/extra-attributes.png)

To re-edit an existing title you can reload these extra attribute settings. Let's try this out.

After you create a few sample DomeText titles, scroll up to the top of the DomeText window. The **Copy Text Settings From** popup menu allows you to recall previous DomeText creation settings. By selecting one of the items in the options menu you will reload the previous title setting in the title tool.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/restore-dometext-creation-settings.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/restore-dometext-creation-settings.png)

After you change the DomeText options you can click the "Create Text" button to create a revised title element.

# Animating the Text Manually #

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/animated-horizontal-vertical-translate.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/animated-horizontal-vertical-translate.png)

If you want to manually animate the text placement you can set keyframes on the vertical translate and horizontal translate controls. These settings are found on the Maya file texture node under the Extra Attributes section.

From my tests with the DomeText tool, I've found linear tangents work best for simple scrolling title elements. You can adjust the animation tangents using the Graph Editor window.

If you create the DomeText with WrapU and WrapV enabled the text will loop / wrap around the frame boundary when it is scrolled off the edge of the supporting geometry with the vertical & horizontal translate sliders. If you want to create a "single" title scrolling effect with no "edge of frame" looping you should disable the WrapU or WrapV controls.

If you create and animate scrolling text with a solid (non-transparent) background color, the DomeText tool sets the same background color used in the raster image as the **Default Color** value on the Maya file texture node. This makes it possible to scroll the raster title text off screen and maintain a solid color background on the geometry.

# My First DomeText Titles #

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/sample-title-crawl.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/sample-title-crawl.png)

Let's create a scrolling credits title sequence in Maya.

Start by clicking the DomeText icon in the Domemaster3D shelf.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/dometext-shelf-item.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/dometext-shelf-item.png)

Paste the following sample text in the Text Entry field:

```
Domemaster3D
Title Generator

A long time ago in a galaxy far, far away....there was a need for fast, editable title cards on a stereo fulldome screen. 

Only one tool dared to challenge this power... DomeText. 

DomeText possessed a strength the world had never seen. A strength surpassed only by the power of his heart. 

Wherever there was evil, wherever an innocent artist would suffer, there would be... DomeText.
```

In the Font Styles section, set the **Alignment** popup menu to **North** so the titles start at the top edge of the image.

Change the **Font Size** to **150** points for fairly large text.

Edit the Color Styles and set the foreground color to white text on a transparent background.

In the Image Controls section set the **Save Image As** field to use the file name **sample\_credits.png**

Set the image width to 2048 pixels. Set the image height to 4096 pixels. This will create a tall rectangle shape for the credits.

In the Shape Controls section set the Texture Node to "Lambert".

We are going to have the text placed on a Polygon plane so the Supporting Shape should be set to the default option of "Plane".

Leave the Orientation Axis at **Front(Z)** for text that is created facing the front view.

Let's change the Shape height to 35 for a polygon plane that is 35 units high in the Maya viewport.

Since we are creating scrolling titles let's uncheck the WrapV checkbox in the Texture Placement section. This will make sure the text won't be repeated on the vertical axis when the titles scroll.

In the Text Animation Controls lets set the Auto Scroll Direction to "Scroll Up". This will make the text scroll from the bottom of the screen to the top.

Set the Start Frame to **1** so the scrolling text animation starts on the first frame. Set the End Frame to **360** frames for a 15 second long title sequence ( assuming a 24 fps animation speed in Maya).

Uncheck the loop animation checkbox so the animated scrolling credits only scroll once.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/sample-credits-settings.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/dometext/sample-credits-settings.png)

Once you've set up the DomeText settings we are ready to create the new graphic elements.

Click the **Create Text** button to generate the new title elements.

You will need to set the viewport to use smooth shading with hardware texturing enabled to see the new title graphics. Set the out point in the Maya timeline to 360 frames to match the sequence duration. When you scrub the timeline in Maya you will see the animated title graphic scroll upwards in the viewport.

# DomeText Font Folders #

The DomeText tool will scan the default font folders on your computer to locate the installed fonts. This process is automatic and the list is updated every time you click the DomeText icon in the shelf.

On Windows the DomeText tool looks for fonts in the folder:

`C:\Windows\Fonts\`

On Mac OS X the DomeText tool looks for fonts in the following folders:

`~/Library/Fonts/`, `/Library/Fonts/`, and `/System/Library/Fonts/`

On Linux the DomeText tool looks for fonts in the following folder:

`/usr/share/fonts/`

# DomeText Fulldome Animation Example #

<a href='http://www.youtube.com/watch?feature=player_embedded&v=94i571O2E9o' target='_blank'><img src='http://img.youtube.com/vi/94i571O2E9o/0.jpg' width='425' height=344 /></a>

The DomeText Code Uplink Animation uses the convert characters to hex single column, and DomeText animation features to display a futuristic fulldome Matrix digital rain world.

# Closing Notes #

If you would like to see new features added to the DomeText tool, feel free to post a comment on the NING group or to send a feature suggestion using the [Domemaster Stereo Shader's \*Bug Reporter\* feature](https://code.google.com/p/domemaster-stereo-shader/issues/entry) on Google Code.