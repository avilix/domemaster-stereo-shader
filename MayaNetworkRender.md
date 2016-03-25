|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Introduction #
In this tutorial I will go over the steps to create your first Maya 2014 + Smedge based fulldome network rendering.

To get started download a copy of the [Smedge render farm management software](http://uberware.net/) from Uberware. The trial version is fully functional and works on three systems for free.


# Setting up a Network Render #

**Step 1.** Install Smedge using the default options.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/0-install-smedge.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/0-install-smedge.png)

**Step 2.** Set up the Smedge scripts.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/1-create-usersetupmel.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/1-create-usersetupmel.png)

Create a plain text document called userSetup.mel in the Maya 2014 script folder:

> Documents/maya/2014x64/scripts/

Write a single line in the userSetup.mel text file with the MEL code:

> source "smedgeRender.mel";

This script tells Maya to automatically load the Smedge Render menu on start up.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/1-copy-smedge-mel-scripts.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/1-copy-smedge-mel-scripts.png)

Copy the Smedge script "smedgeRender.mel" from the Smedge utilities folder:
> C:\Program Files\Smedge\Utilities\smedgeRender.mel

Paste the "smedgeRender.mel" script into the Maya 2014 scripts folder:
> documents/maya/2014x64/scripts/

**Step 4.** Start Smedge for the first time.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/2-start-smedge.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/2-start-smedge.png)

Go to the Smedge **System menu** and select **Connect**. This will activate the Smedge GUI.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/3-connect-smedge.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/3-connect-smedge.png)

This image shows the basic Smedge GUI with one render node active. The rendering systems are listed at the bottom of the Smedge window by their computer name. In this example my system is listed as "HP".

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/4-smedge-is-running.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/4-smedge-is-running.png)


**Step 5.** Set your computer to be a Smedge Master.

In Smedge a render node is called an engine and the render queue is maintained by the master.

Let's tell Smedge that our workstation is a Smedge Master.

Start by switching to the Smedge Administrator mode so we can adjust the current settings. From the **System** menu select **Administrator Mode**.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/5-switch-to-administrator-mode.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/5-switch-to-administrator-mode.png)

To turn this system into a Smedge master go to the **System** menu and select **Components > Start the Master now**.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/6-start-the-master.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/6-start-the-master.png)

**Step 6.** Let's look at this system's Smedge options. We are going to look at the Smedge master configurations window. From the **System** menu, select **System Commands > Configure Master**.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/7-smedge-configure-master.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/7-smedge-configure-master.png)

In the Master Options window you can set the main preferences for each of the Smedge supported rendering programs. In the Product Settings tab you can look over the settings used for the specific software programs like Maya, 3DS Max, After Effects, etc...

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/8-master-options-window.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/8-master-options-window.png)

The Path Translations tab is a powerful Smedge feature that lets you convert the file paths used to render a project between a Windows, Mac, and Linux system.

This is important for rewriting a Windows style drive letter like "M:\" to a Linux drive mount location like "/mnt/media/", or a Mac network volume name like "/Volumes/Media/".

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/9-path-translations.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/9-path-translations.png)

**Step 7.** Smedge can be used as a local render queue by a single Maya artist by installing Smedge on a single system

To do a network render we need to install a copy of Smedge on a 2nd system. The remote copy of Smedge can be set up with the default options.

At this point I have two render nodes active and their names are HP and XEON which are listed at the bottom of the Smedge window.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/10-smedge-active-on-two-systems.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/10-smedge-active-on-two-systems.png)

**Step 8.** Since we have Smedge installed let's start Maya.

You need to have the Domemaster3D shader for Maya installed on your system to complete the rest of this network fulldome rendering guide.

You can download your copy using the link on the sidebar of this page.

Okay, it's time to launch Maya.

**Step 9.** Let's create a new project for this fulldome rendering test using the Project Window. A project folder is used to hold the all of project assets like the Maya scene files, textures which are known as "sourceimages", and the renderings which are stored in the "images" folder.

From the File menu select Project Window.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/11-maya-project-window.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/11-maya-project-window.png)

The Project Window will open. Click the **new** button to add new project.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/12-new-project-button.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/12-new-project-button.png)

Let's set the project to use a network folder location. Click the folder icon to choose the project folder's location. In my case I saved the project on a M: drive that is a windows SMB share. When rendering on a network it is important that all the render nodes can access the same shared folder.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/13-select-project-folder-location.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/13-select-project-folder-location.png)

Click in the current project text field and type in "Fulldome\_test". This is the name for the new project folder.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/14-project-name.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/14-project-name.png)

Click **Accept** to create the new project.

**Step 10.** Add some geometry to the scene.

Let's use the Starglobe tool to add a scenic element to our project. Click on the Domemaster3D shelf and select the Starglobe shelf icon.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/15-add-a-starglobe.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/15-add-a-starglobe.png)

The Starglobe tool will open on the right side of the Maya user interface. Click the "Create Starglobe" button to add the starry sky backdrop to the Maya scene.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/16-create-a-starglobe.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/16-create-a-starglobe.png)

Click in the perspective viewport and press the 4 key to turn on smooth shading.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/17-press-4-key-smooth-shading.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/17-press-4-key-smooth-shading.png)

**Step 11.** Let's add a fulldome 2D camera to the scene.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/18-fov-shelf-tool.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/18-fov-shelf-tool.png)

Click in the Domemaster3D shelf on the FOV icon to add a 2D domeAFL\_FOV camera. This camera will render the scene with a 180 degree field of view angular fisheye camera.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/19-this-is-a-dome-camera.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/19-this-is-a-dome-camera.png)

Let's take a look at the scene through the fisheye camera.

Select the **Panels** menu in the perspective viewport and choose the **Perspective > domeAFL\_FOV\_CameraShape2** menu item. The viewport now shows the scene from inside the angular fisheye camera rig.


![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/20-look-through-the-camera.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/20-look-through-the-camera.png)

Right now the camera view shows a wide angle view of the scene with a rectangular window frame shape. When this camera view is rendered with mental ray you will notice the final frame has a circular border which is called a domemaster image.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/21-domeafl-view.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/21-domeafl-view.png)

**Step 12.** It's a good idea to review the render settings.

Let's use the Domemaster3D shelf resolution shortcuts to create a quick 1k resolution (1024x1024 pixel) fulldome rendering. Click the 1K icon.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/22-domemaster3d-1k-preset.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/22-domemaster3d-1k-preset.png)

Open the rendering menu set using the popup-menu at the top left of the Maya user interface. This will display the menus needed to launch a Smedge Render.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/23-rendering-menu-set.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/23-rendering-menu-set.png)

At this point we should take a moment to look over the current render settings. Let's open the render settings window.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/24-open-render-settings.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/24-open-render-settings.png)

For this test render, lets render to the PNG format. From the Image Format popup menu select "PNG (png)".

Now let's change the Frame / Animation extension to the `name.#.ext` option.

Set the frame padding to **4**. Frame padding adds a zero digit in front of the current frame number so the number field section of the filename is always 4 digits long. For example frame **1** is written as **0001**.

This is useful when you want to sort a folder view and see the images ordered correctly. Without frame padding frame 1, and frame 10 would be listed next to each other in a file window.

Set the start frame to 1 and the end frame to 1.

The current settings will create a rendering that uses a numbered image sequence with a file name like: starglobe\_test.0001.png

Make sure the renderable camera is set to use the domeAFL\_FOV camera.

Now let's click on the **Quality** tab in the render settings window.

Maya 2014 added a new control called **Unified Sampling** to adjust the anti-aliasing (crispness) of the final rendered image. Unified sampling was added to help simplify the number of settings that are required to tune the render quality.

Make sure the Sampling Mode is set to **"Unified Sampling"**.

Set the Quality setting to **1.0** .

mental ray Tip: If you are rendering a challenging scene with complex shading the Unified Sampling rate can be raised far above a unified setting of 1.0. The 1.0 setting is just a starting point that should give nice looking results on a standard scene.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/25-unified-quality.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/25-unified-quality.png)

**Step 13.** At this point let's open the Render View window.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/26-open-render-window.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/26-open-render-window.png)

I like to disable the **auto-resize** option in the render window. This makes it easier to work with the Render View when you are constantly changing the output resolution.

To disable the auto-resize checkbox select the **Options > Auto Resize** menu item.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/27-disable-auto-resize.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/27-disable-auto-resize.png)

Before we launch our first render we need to make sure the mental ray renderer is selected. The popup menu in the render window can be used to switch the active renderer.

Let's make sure the Render View window is set to look through the fulldome camera. From the Render menu select **Render > domeAFL\_FOV\_CameraShape2**. This will start the rendering process.

Tip: You can also switch the active render view by right clicking over the render or snapshot icons in the render view toolbar and choosing a camera in the popup-menu.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/28-select-the-render-camera.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/28-select-the-render-camera.png)

After a few moments the rendering will finish and you will see a circular domemaster image that shows the night sky.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/29-render-complete.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/29-render-complete.png)

Clicking the **Alpha Channel** button in the Maya render window will show the circular mask of the domemaster frame.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/30-circular-alpha-channel.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/30-circular-alpha-channel.png)

Click the **Show RGB channels** icon to switch back to the standard Render View color channels.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/31-show-rgb-channels.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/31-show-rgb-channels.png)

**Step 14.** It's time to save the Maya scene.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/32-save-the-scene.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/32-save-the-scene.png)

Since this is a new Maya scene we need to save it before we can launch a network render.

From the **File** menu, select **Save Scene**.

Give the scene a name like **starglobe\_test.ma** and click the **Save As** button.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/33-save-as-starglobe-test.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/33-save-as-starglobe-test.png)

**Step 15.** Let's prepare to launch our first network render.

From the **Render** menu, select **Smedge Render** with options. This will open the Smedge options window for the first time.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/34-smedge-render-menu.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/34-smedge-render-menu.png)

When Maya launches a new Smedge render it uses a tool called `submit.exe`. The first time we run the Smedge Render command we are asked to tell Maya where the Smedge Submit program was installed on the hard drive.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/35-smedge-submit-notice.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/35-smedge-submit-notice.png)

Open the **Settings** tab in the Smedge Render window.

Let's update the **Path to Submit** text field by clicking the "..." button.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/36-select-the-dot-dot-dot-button.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/36-select-the-dot-dot-dot-button.png)

On Windows we need to navigate to the `C:\Program Files\Smedge\` folder and select `submit.exe`.

Once you've got the submit.exe program selected, click the **Open** button.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/37-select-the-submit-program.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/37-select-the-submit-program.png)


Click on the basic info tab to review the current Smedge Render settings. Things look fine.

At this point we are ready to launch the render. Click the green coloured submit button to kick off the new Smedge render. The current Maya scene will be sent to the Smedge Master program and the network rendering will start.

Tip: Sometimes you might find it takes a while for the Smedge render window to close in Maya. Usually this means you quit the Smedge GUI program that was running in the Windows Taskbar. Once you open Smedge again the Smedge Render window in Maya will close and the render will start.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/38-click-submit.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/38-click-submit.png)

**Step 16.** Watch the render in Smedge.

You can watch the render progress in the Smedge GUI Window.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/39-smedge-gui-render-progress.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/39-smedge-gui-render-progress.png)

If you want to view the Maya render log you can click on the **History** tab in Smedge. Right click over a frame in the work section and select "View Process Output".

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/40-view-process-output.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/40-view-process-output.png)

The Process Output window shows the progress message data that is written to the render node's Maya render log. This window is helpful for troubleshooting issues like a shader failing to load, a missing texture, or a mental ray rendering issue like a low memory warning.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/41-render-log-data.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/41-render-log-data.png)

When the render completes you will see the resulting render time written in the Smedge **History** tab.

If your render job is an animation Smedge will estimate the project render time based upon the sequence duration and the current render time per frame.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/42-render-complete.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/42-render-complete.png)

**Step 17.** Let's run the Check File Sequences tool.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/43-run-the-cfs-tool.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/43-run-the-cfs-tool.png)

Smedge has a neat tool called "CFS" or Check File Sequences. This comes in handy when you are rendering an animation and you want to make sure all of the frames rendered correctly. The CFS window shows gaps in an image sequence frame range and will highlight frames that failed to render or are empty files with no file size.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/44-cfs-tool-result.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/44-cfs-tool-result.png)

In this demo our rendering task succeeded without any issues.

If you have a large project with many render nodes you might need to re-render a range of frames from your animation. The CFS menu has commands that can add the missing frames from your project to a new rendering job.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/45-cfs-options.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/smedge/45-cfs-options.png)

**Good luck and happy rendering.**