|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Table of Contents #


# Introduction #

This is the "Getting Started Guide" that covers all of the steps required to start creating content for stereoscopic fulldome theaters using Autodesk Maya. This guide is designed to give artists an understanding of the manual node connections that are automated by the Domemaster3D Shelf in Maya.


## Step 1. Creating the Base Domemaster3D Shading Network ##
Before we add the DomeAFL\_FOV\_Stereo node to the scene we need to create the base shading network connections for the Domemaster3D shader. We are going to use the `rob_lookup_background` shader to preview our dome control textures in the special "screen coordinate space". The **rob** part of shader name is due to the fact it was developed by Roberto Ziche.

Let's get started.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/1.new-robLookupCamera.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/1.new-robLookupCamera.png)

Add a new perspective camera to the scene.

To use the `rob_lookup_background` shader we need to add a new camera to the scene. In the viewport, from the **Panels** menu select **Perspective > New**. This created a new camera. Let's change the name of the camera to **robLookupCamera**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/2.rename-the-camera.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/2.rename-the-camera.png)

Rename the camera robLookupCamera.

We are going to use the Hypershade to create the custom shading network. Click in the perspective view and hold down the spacebar to display the hotbox. From the north zone, select the **Hypershade/Render/Perspective** layout.

Click in the Hypershade and tap the spacebar to maximize the view.

Select the **Cameras** tab to display a list of the active cameras in our scene. Drag the **robLookupCameraShape** node from the Cameras tab to the work area.

In the create bar click on the **mental ray > lenses** section. Click on the **rob\_lookup\_background** icon in the create bar to add the shader to the Hypershade work area.

Let's connect the rob\_lookup\_background lens shader to the new camera. Using the middle mouse button drag the **rob\_lookup\_background** node onto the **robLookupCameraShape** node. In the connect pop-up menu select **default**.

This has connected **rob\_lookup\_background.message** to **robLookupCameraShape.miLensShader**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/3.add-rob_lookup-background-shader.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/3.add-rob_lookup-background-shader.png)

Connect a rob\_lookup\_background shader to the camera.

The next step is to create the texturing and screen space conversion nodes for the shading network.

In the create bar, click on the mental ray textures section. Add a "mib\_texture\_filter\_lookup" node to the work area. This node will merge the image data with the screen space UV coordinate system.

We are going to map a greyscale output from the mib\_texture\_filter\_lookup node to the rob\_lookup\_background shader's greyscale **tex** attribute.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/4a.connecting-mib-texture-filter-node.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/4a.connecting-mib-texture-filter-node.png)

Connect a mib\_texture\_filter\_Lookup node to the rob\_lookup\_background shader.

Using the middle mouse button drag the **mib\_texture\_filter\_lookup** node onto the **rob\_lookup\_background** node. In the connect pop-up menu select **Other...**

In the connection editor expand the mib\_texture\_filter's **outValue** attribute on the left side of the window and select the **outValueR** attribute. On the right side of the connection editor window select the **tex** attribute.

Click the close button in the connection editor to hide the window.

This has connected **mib\_texture\_filter\_lookup.outValueR** to**rob\_lookup\_background.tex**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/4b.connecting-mib_texture_filter_lookup-to-rob-lookup-background.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/4b.connecting-mib_texture_filter_lookup-to-rob-lookup-background.png)

Connect the mib\_texture\_filter\_lookup node to the rob\_lookup\_background node using the connection editor.

Next we are going to add a mentalrayTexture node to the work area. This node will load the actual file texture for the separation map. In the textures section of the create bar click on the **mentalrayTexture** node.

Select the **mentalrayTexture** node in the Hypershade work area. In the attribute editor, click on the folder icon next to the **Image Name** field. Select the **separation\_map.png** image from the project's sourceimages folder and click open.

In the Hypershade work area drag the **mentalrayTexture**node onto the**mib\_texture\_filter\_lookup** node. From the connect pop-up menu select **default**.

This has connected **mentalrayTexture.message** to**mib\_texture\_filter\_lookup.tex**

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/5.connect-the-mentalrayTexture-node.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/5.connect-the-mentalrayTexture-node.png)

Connect the mentalrayTexture node to the rob\_lookup\_background shader.

Now let's connect the mental ray nodes required to create the screen space texture coordinates.

Let's add a mib\_texture\_vector node to work area. In the create bar from the **mental ray > Textures** section, click on the **mib\_texture\_vector** node.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/6.setting-up-the-mib_texture_vector-selspace-setting.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/6.setting-up-the-mib_texture_vector-selspace-setting.png)

Set up the mib\_texture\_vector select space attribute.

Select the **mib\_texture\_vector** node in the work area. In the attribute editor you will see an attribute called **selspace**. This attribute stands for "select space" and it allows you to choose the source space used for texture mapping. Change the mib\_texture\_vector node's **selspace** value to **screen**. This setting allows us to project the separation map onto the camera using mental ray screen space UV coordinates.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/6b.Set-the-selspace-to-screen.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/6b.Set-the-selspace-to-screen.png)

Set the selspace attribute to screen

We need to add one more node to the work area. In the create bar from the **mental ray > textures** section, click to add a **mib\_texture\_remap** node. In the Hypershade work area, use the middle mouse button to drag the **mib\_texture\_vector** node onto the **mib\_texture\_remap** node. From the connect pop-up menu select **Other...**

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/7.connect-mib_texture_vector-node-to-mib_texture_remap.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/7.connect-mib_texture_vector-node-to-mib_texture_remap.png)

Connect the mib\_texture\_vector node to the mib\_texture\_remap node.

In the connection window select the mib\_texture\_vector **outValue** attribute on the left and the mib\_texture\_remap **input** attribute on the right.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/7b.connection-editor-mib_texture_vector-node-to-mib_texture_remap.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/7b.connection-editor-mib_texture_vector-node-to-mib_texture_remap.png)

Use the connection editor to connect the mib\_texture\_vector node to the mib\_texture\_remap node

Click the close button to hide the connection editor.

This has connected **mib\_texture\_vector.outValue** to the**mib\_texture\_remap.input**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/7c.node-connection-mib_texture_vector-node-to-mib_texture_remap.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/7c.node-connection-mib_texture_vector-node-to-mib_texture_remap.png)

This image shows the node connections for the mib\_texture\_vector and mib\_texture\_remap nodes.

We have one last node to add to the work area.

Using the middle mouse button drag the **mib\_texture\_remap** node onto the **mib\_texture\_filter\_lookup** node. From the connect popup menu select **Other...**

In the connection window select the mib\_texture\_remap **outValue** attribute on the left and the mib\_texture\_filter\_lookup **coord** value on the right. Click the close button to hide the connection editor.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/8.connection-editor-mib_texture_remap-to-mib_texture_filter_lookup.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/8.connection-editor-mib_texture_remap-to-mib_texture_filter_lookup.png)

This is the connection editor view of the mib\_texture\_remap to mib\_texture\_filter\_lookup connections.

Click the close button to hide the connection editor.

This has connected the **mib\_texture\_remap.outValue** to the**mib\_texture\_filter\_lookup.coord**.

If everything is hooked up properly the **mib\_texture\_filter\_lookup** node should now display a crescent shaped preview icon.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/8b.node-connection-mib_texture_remap-to-mib_texture_filter_lookup.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/8b.node-connection-mib_texture_remap-to-mib_texture_filter_lookup.png)

This is an image of the node connections for the mib\_texture\_remap and mib\_texture\_filter\_lookup nodes.

Let's cleanup the layout of the work area by clicking on the **rearrange graph icon** in the Hypershade toolbar. Click in the work area and press the **A** key on your keyboard to fill the view with the nodes.

With this shading network we can now preview the Domemaster3D screen space texture maps.

Let's see the results of the rob\_lookup\_background shader by doing a test render using the render view.

Tap the spacebar to return to the **Hypershade / Render / Perspective** layout.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/9.render-robLookupCamera.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/9.render-robLookupCamera.png)

Render the robLookupCamera.

In the render view from the Render menu, select **Render > robLookupCamera**. If the shading network is setup correctly we should see the black crescent shape from the separation texture map.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/9b.proper_robLooupCamera-result.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/9b.proper_robLooupCamera-result.png)

This is the result of rendering with the robLooupCamera.

In the next step we are going to add a stereo camera rig to our Maya scene and connect the custom texture maps to the domeAFL\_FOV\_Stereo node.

## Step 2. Creating a Stereo Camera Rig in Maya ##

It's possible to use the Domemaster3D shader with Maya's stereo camera rig. This setup makes it easy to animate the stereo camera in your scene and also allows you to preview your Maya renders in the render view using anaglyph 3D glasses.

### **Let's add a stereo camera rig to our scene.** ###
In the perspective viewport select the **Panels > Stereo > Create Stereo Camera** menu item.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/10a-adding-the-stereo-camera.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/10a-adding-the-stereo-camera.png)

Let's add a stereo camera to the scene.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/10b-adding-the-stereo-camera-closeup.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/10b-adding-the-stereo-camera-closeup.png)

This is a closeup of the Stereo menu.

We now have a stereo camera rig to our scene. We need to edit the stereo rig's camera attributes so it is compatible with the Domemaster3D shader. From the **Panels** menu select **Stereo > stereoCamera**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/11.stereo-camera-view.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/11.stereo-camera-view.png)

This is the view through the stereo camera viewport.

In the attribute editor make sure the **stereoCameraCenterCamShape** tab is selected. Scroll down to the **Stereo** section.

We need to modify the default stereo rig attributes to allow the DomeAFL\_FOV\_Stereo shader to control the camera separation settings. Start by setting the **Interaxial Separation** to **0.0**. Next we need to change the **Stereo** pop-up menu from **Off-axis** to **Off**. This will disable the standard stereo convergence settings.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/12.stereoCamera-attributes.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/12.stereoCamera-attributes.png)

Here are the attributes for the stereoCamera.

Let's change the realtime viewport's field of view attributes. In the attribute editor change the focal length to 15 millimeters so we have a wider field of view. This makes it easier to frame the shot. This field of view setting will only affect the realtime viewport in the perspective view. The domeAFL\_FOV\_stereo shader will still control the angular fisheye field of view attribute at render time.

## Step 3. Adding the domeAFL\_FOV\_Stereo Node ##
In this step we are going to add a domeAFL\_FOV\_Stereo node and connect it to the stereo camera rig.

Click in the Hypershade and tap the spacebar to maximize the view.

The custom texture map shading network we created in step 1 is important for controlling the positioning of the stereoscopic effect on the fulldome screen and to reduce rendering artifacts that would be visible from the head turn feature at top of the fulldome screen.

In the cameras tab we need to select the left and right cameras used by the stereo camera rig and the robLookupCamera created in the previous step. Click in the cameras tab and hover your mouse cursor over the camera node icons to see the full length names of the cameras.

Select the **robLookupCameraShape**, the **stereoCameraLeftShape** and **stereoCameraRightShape** nodes.

Click the **show input connections** icon in the Hypershade toolbar. This is has added the nodes to the work area and displayed the node's input connections.

\![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/13.adding-the-cameras-to-the-work-area.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/13.adding-the-cameras-to-the-work-area.png)

Add the selected cameras to the work area.

Let's add a domeAFL\_FOV\_stereo node to work area. From the create bar select the **mental ray > lenses** section. Then click on the **domeAFL\_FOV\_Stereo** icon to add the node to the work area.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/14.Adding-the-domeAFL_FOV_stereo-node.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/14.Adding-the-domeAFL_FOV_stereo-node.png)

Add the domeAFL\_FOV\_Stereo node to the work area.

This node will be used for rendering the angular fisheye view for the left camera in the stereo rig. Click on the **domeAFL\_FOV\_Stereo** node in the work area. In the attribute editor use the **camera** pop-up menu to set the camera view to "**Left**".

For this tutorial we will leave the **Camera's Separation** value at **6 cm**.

If you scale the size of the camera's transform node to make the icon larger in the perspective view, it will result in the camera scale having a direct multiplying effect on the current **camera separation** value.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/14b.setting-the-camera-to-left.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/14b.setting-the-camera-to-left.png)"

Set the camera view to Left in the DomeAFL\_FOV\_Stereo node.

Now we are going to connect a greyscale channel from the separation texture map shading network to the domeAFL\_FOV\_Stereo node.

Using the middle mouse button drag the **mib\_texture\_lookup** node onto the **domeAFL\_FOV\_Stereo** node. From the connect pop-up menu, select **Other...**

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/15.connecting-mib_texture_filter_lookup-to-domeAFL_FOV_stereo.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/15.connecting-mib_texture_filter_lookup-to-domeAFL_FOV_stereo.png)

Connect the mib\_texture\_filter\_lookup node to the domeAFL\_FOV\_Stereo node.


On the left side of the connection editor, expand the domeAFL\_FOV\_Stereo **outValue** attribute and select **outValueR**. On the right side of the connection editor, select **Cameras\_Separation\_Map**.


![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/15b.connection-editor-mib_texture_filter_lookup-to-domeAFL_FOV_stereo.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/15b.connection-editor-mib_texture_filter_lookup-to-domeAFL_FOV_stereo.png)

Use the connection editor to connect the mib\_texture\_filter\_lookup node to the domeAFL\_FOV\_Stereo node

Close the connection editor.

This has connected **mib\_texture\_lookup.outValueR** to **domeAFL\_FOV\_Stereo.Cameras\_Separation\_Map**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/15c.node-connections-mib_texture_filter_lookup-to-domeAFL_FOV_stereo.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/15c.node-connections-mib_texture_filter_lookup-to-domeAFL_FOV_stereo.png)
Here are the node connections for the mib\_texture\_filter\_lookup and domeAFL\_FOV\_stereo nodes.


We're now going to connect a head turn texture map also known as the "Turn Multiplier" to the domeAFL\_FOV\_Stereo node. To save time, let's duplicate the existing mib\_texture\_lookup node's shading network.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/16.duplicating-the-shading-network.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/16.duplicating-the-shading-network.png)

Duplicate the shading network.

Select the **mib\_texture\_lookup** node in the work area. From the Hypershade's **Edit** menu, select **Duplicate > Shading Network**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/16b.duplicating-the-shading-network-closeup.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/16b.duplicating-the-shading-network-closeup.png)"

Use the Duplicate Shading Network menu item to copy the existing nodes.

Let's clean up the view in the work area by rearranging the nodes. Click the **rearrange graph** icon in the toolbar.

We need to link the head turn map PNG texture to the mental ray texture node. Select the copied **mentalrayTexture** node in the work area. In the attribute editor, click the folder icon next to the image name field. We are now going to select the head turn texture map. In the open dialog select **turn\_map.png** and click open.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/17.relink-the-texture-map.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/17.relink-the-texture-map.png)

Let's relink the texture map in the attribute editor.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/17b.select-the-turn_map-texture.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/17b.select-the-turn_map-texture.png)

Select the turn\_map.png texture in the sourceimages folder.

To force the node icon swatch to update lets reconnect the mentalrayTexture node to the mib\_texture\_filter\_lookup node. Click on the line connecting the two nodes and press the delete button. Using the middle mouse button drag the **mentalrayTexture** node onto the **mib\_texture\_filter\_lookup** node. From the connect pop-up, select **default**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/18.connect-the-turn-map-to-domeAFL_FOV_stereo-node.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/18.connect-the-turn-map-to-domeAFL_FOV_stereo-node.png)

Connect the turn-map to the domeAFL\_FOV\_Stereo node.

Now let's connect this shading network to the domeAFL\_FOV\_Stereo node. Using the middle mouse button drag the head turn map's **mib\_texture\_filter\_lookup** node onto the **domeAFL\_FOV\_Stereo** node. From the connect pop-up menu, select **other...**

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/18.connection-editor-mib_texture_filter-lookup-to-domeAFL_FOV_Stereo.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/18.connection-editor-mib_texture_filter-lookup-to-domeAFL_FOV_Stereo.png)

This is a view of the Connection editor showing the connections from the mib\_texture\_filter\_lookup node to the domeAFL\_FOV\_Stereo node.

On the left side of the connection editor, expand the **outValue** attribute and select **outValueR**. On the right side of the connection editor, select **Head Turn\_Map**.

Close the connection editor.

This has connected **mib\_texture\_filter\_lookup.outValueR** to**domeAFL\_FOV\_Stereo.Head Turn\_Map**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/18.node-connections-mib_texture_filter-lookup-to-domeAFL_FOV_Stereo.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/18.node-connections-mib_texture_filter-lookup-to-domeAFL_FOV_Stereo.png)

This is a view of the node connection between the mib\_texture\_filter\_lookup node and domeAFL\_FOV\_Stereo node.

Let's clean up the view in the work area by rearranging the nodes. Click the **rearrange graph** icon in the toolbar.

Let's connect this lens shader node to the left camera in the stereo rig. Using the middle mouse button drag the **domeAFL\_FOV\_Stereo** node onto the **stereoCameraLeftShape** node. From the connect pop-up menu, select **default**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/19.connect-domeAFL_fov_stereo_to_stereocameraleft.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/19.connect-domeAFL_fov_stereo_to_stereocameraleft.png)

Connect the domeAFL\_FOV\_Stereo node to the stereoCameraLeft node.

This has connected **domeAFL\_FOV\_Stereo.message** to **stereoCameraLeftShape.miLensShader**

Let's select the domeAFL\_FOV\_Stereo node and duplicate it for the right camera.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/19b.nodes-connected-domeAFL_fov_stereo_to_stereocameraleft.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/19b.nodes-connected-domeAFL_fov_stereo_to_stereocameraleft.png)

This is a view of the domeAFL\_FOV\_Stereo to stereoCameraLeft node connections.

Select the **domeAFL\_FOV\_Stereo** node in the work area and from the Hypershade's **Edit** menu, select **Duplicate > With Connection to Network.** This has duplicated the domeAFL\_FOV\_Stereo node and linked it to the existing custom texture map shading network.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/20.duplicate-nodes-with-connections-to-network.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/20.duplicate-nodes-with-connections-to-network.png)

Duplicate the nodes using the With Connections to Network menu item.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/21.dual-domeAFL_FOV_Stereo-nodes.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/21.dual-domeAFL_FOV_Stereo-nodes.png)

This is a view of the two domeAFL\_FOV\_Stereo nodes.

This node will be used for the right camera in the stereo rig. Click on new the **domeAFL\_FOV\_Stereo** node in the work area. In the attribute editor use the **Camera** pop-up menu to set the camera view to "**Right**".

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/21.right-camera-view-for-domeAFL_FOV_Stereo-node.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/21.right-camera-view-for-domeAFL_FOV_Stereo-node.png)

This is the right camera view for the domeAFL\_FOV\_Stereo node.

Let's connect this lens shader node to the right camera in the stereo rig. Using the middle mouse button drag the new **domeAFL\_FOV\_Stereo** node onto the **stereoCameraRightShape** node. From the **connect** pop-up menu, select **default**.

This has connected **domeAFL\_FOV\_Stereo.message** to**stereoCameraRightShape.miLensShader**

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/22.connect-right-domeAFL_FOV_Stereo-node-to-stereocamerarightshape-node.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/22.connect-right-domeAFL_FOV_Stereo-node-to-stereocamerarightshape-node.png)

Connect the right domeAFL\_FOV\_Stereo node to stereoCameraRightShape node

Select the two domeAFL\_FOV stereo nodes in the work area. Click the input and output connections icon in the Hypershade toolbar to regraph the scene.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/22.regraph-shading-network.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/22.regraph-shading-network.png)

Regraph the shading network.

This is the completed fulldome stereo camera rig with shared texture connections.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/23.finished-domemaster3d-shading-network.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/23.finished-domemaster3d-shading-network.png)

This is the finished Domemaster3D shading network.

## Step 4. Rendering a Domemaster Stereo Anaglyph Preview in the Maya Render View ##
In this step we are going to add a cube to the scene and render it as a stereoscopic domemaster image.

Switch back to the Hypershade / Perspective / Render layout by tapping the spacebar over the work area.

Let's add a polygon cube to the scene as a test object. We need to start by disabling interactive creation so we can specify the exact size of the polygon cube.

From the **Create** menu select **Polygon Primitives >Interactive Creation**. Now we can create an accurately sized polygon cube.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/24.interactive-creation.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/24.interactive-creation.png)

Disable interactive creation.

From the **Create** menu select **Polygon Primitives > Cube with options**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/25.create-polygon-cube-with-options.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/25.create-polygon-cube-with-options.png)

Select the create polygon primitives, cube with options menu item.

In the polygon cube options window set the **width** and **height** and **depth** to **300 units**. Click the Create button.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/25b.create-cube-with-300-unit-size.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/25b.create-cube-with-300-unit-size.png)

Create a square cube with a dimension of 300 units in size.

Let's attach a texture to the cube. Right-click in the perspective view, and from the marking menu select **Assign New Material...**

In the Assign New Materials window, select the **Lambert** material. We now have a Lambert surface material applied to the polygon cube.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/26.assign-new-material.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/26.assign-new-material.png)

Select the Assign New Material... item.

In the attribute editor rename the material to **checkerLambert**.

Let's connect the PNG file texture. In the attribute editor click on the map icon next to the color attribute.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/28.map-texture-to-checkerlambert.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/28.map-texture-to-checkerlambert.png)

Map a texture to the new checkerLambert material.

In the **Create Render Node** window, select the **File** node. A file node has been added to the shading network.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/29.asign-a-file-node.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/29.asign-a-file-node.png)

Assign a file node to the material.

Let's add a PNG texture to the file node using the attribute editor. Click on the folder icon next to the image name field.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/30a.select-file-texture.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/30a.select-file-texture.png)

Select the file texture.

In the open dialog, select**luminance-cube-texture.png** and click open.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/30b.select-file-texture-luminance-cube-texture.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/30b.select-file-texture-luminance-cube-texture.png)

Select the file texture luminance-cube-texture.png.

Press the 6 key to switch to smooth shaded mode.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/31.textured-cube.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/31.textured-cube.png)

This is a view of the textured polygon cube.

We need to add a light to scene. From the **Create** menu, select**Lights > Point Light**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/32a.create-menu-adding-the-point-light.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/32a.create-menu-adding-the-point-light.png)

Use the create menu to add a point light to the scene.

In the Attribute editor set the Point Light's intensity to 1.5 and press enter.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/32b.editing-the-point-lighting.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/32b.editing-the-point-lighting.png)

Edit the point light intensity attribute.

In the perspective viewport let's enable the light. From the Lighting menu select **Use All Lights**.

We need to reposition the stereoCamera before we render the scene. Open the **outliner** and select the **stereoCamera**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/33.selecting-the-stereoCamera-in-the-outliner.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/33.selecting-the-stereoCamera-in-the-outliner.png)

Select the stereoCamera in the outliner.

In the channel box set the camera's translation and rotation values to 0.0. You can now close the outliner.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/34.zeroing-out-the-transforms.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/34.zeroing-out-the-transforms.png)

Zero out the stereoCamera transforms using the channel box.

Before we render the scene we need to go over the render settings.

Click the **render settings** icon in the toolbar. Make sure the mental ray renderer is selected. Scroll down in the **common** tab of the render settings window. In the Renderable Camera's section make sure the **Renderable Camera** popup menu is set to **stereoCamera ( Stereo Pair )**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/35.render-settings-renderable-camera.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/35.render-settings-renderable-camera.png)

In the render settings set the renderable camera to the stereoCamera.

When you batch render the sequence Maya will automatically create two folders in the images directory - one for the left camera images and one for the right camera images. Each of the frames in your animation will result in a right and left image rendered to the appropriate folder.

Let's set the image size to a 2K resolution output (2048 x 2048) with a square 1:1 aspect ratio for our test render. In the **Image Size** section choose the **2K Square** preset. Close the render settings window

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/36.render-settings-image-size.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/36.render-settings-image-size.png)

Set the image size to 2048x2048.

To speed of the performance of the render view, lets use the 50% resolution setting. In the render view **Options** menu, select **Test Resolution > 50% settings ( 1024x1024)**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/37.Setting-up-the-render-view-test-resolution.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/37.Setting-up-the-render-view-test-resolution.png)

In the render view set the test resolution to 50 percent.

Let's maximize the render view. Click in the render view and tap the space bar to go full-screen.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/38a.rendering-the-stereo-camera.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/38a.rendering-the-stereo-camera.png)

Render the stereo camera.

We are now ready to render the stereo camera. In the render view from the **Render** menu select **Render > Stereo Camera**. This will automatically render the left camera view then the right camera view. The resulting images will be composited together to give an anaglyph stereoscopic preview.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/38b.rendering-the-stereo-camera.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/38b.rendering-the-stereo-camera.png)

This is a closeup image of rendering the stereo camera.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/39a.viewing-the-stereo-rendering-in-the-renderview.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/39a.viewing-the-stereo-rendering-in-the-renderview.png)

You can view the stereo rendering as an anaglyph image directly in the render view.

Once the render is complete you can choose a stereoscopic display method for the preview. From the **Display** menu select the **Stereo Display** menu. You can choose between the following stereoscopic formats: anaglyph, luminance anaglyph, freeview parallel, freeview crossed, left only or right only.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/40.switching-stereo-display-modes.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/40.switching-stereo-display-modes.png)

You can switching stereo display modes in the render view.

This is an image showing the stereoscopic parallel freeview display mode.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/41.freeview-stereo-display-mode.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/41.freeview-stereo-display-mode.png)

This is an image of the Freeview Parallel stereo display mode.

Let's save the scene. From the **File** menu select **Save scene**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/42.save-the-maya-scene.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/42.save-the-maya-scene.png)

Let's save the current Maya scene.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/42b.save-the-maya-scene.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/42b.save-the-maya-scene.png)

Give the scene a file name.

## Batch Rendering ##
The stereo camera rig allows you to render stereoscopic domemaster image sequences using Maya's Batch Render command. If you want to render an animation set the output to the name.number.extension format in the render settings window.

Switch to the Rendering menu set.

From the **Render** menu select **Batch Render with options**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/43.batch-render-menu.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/43.batch-render-menu.png)

Select the batch render menu item.

In the mental ray Batch Render Options window click the **batch render and close** button.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/44.batch-render-and-close.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/44.batch-render-and-close.png)

Click the Batch render and close button.

When the batch render completes, switch to your desktop and open the images directory for your current Maya project. Maya automatically created folders called stereoCameraLeft and stereoCameraRight.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/45.rendered-stereocamera-images.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/45.rendered-stereocamera-images.png)

You can view the completed renderings in the images directory.

## Viewing the renderings using imf\_disp ##
You can use the mental ray image viewer imf\_disp that comes with Maya to view the stereo renderings.

Open imf\_disp program that is located in the Maya / mental ray / bin folder. From the **File** menu select**Open Stereo..**.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/46.opening-stereo-images-in-imf-disp.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/46.opening-stereo-images-in-imf-disp.png)

Open the stereo images in the imf\_disp utility.

In the open dialogue select the two stereo images. You can fit the stereo images to your screen by selecting the **View > Zoom > Zoom to Fit Window** menu item or by pressing the **W** key on your keyboard.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/47.zoom-view.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/47.zoom-view.png)

Zoom the view.

The imf\_display program has an exposure and gamma control you can use to adjust the brightness of the image.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/48.adjusting-exposure-and-gamma.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/48.adjusting-exposure-and-gamma.png)

You can adjust the exposure and gamma in imf\_disp viewer as you are previewing the images in stereoscopic 3D.

You can change the stereo display mode by selecting the **View > Stereo Display** menu item.

![http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/49.imf-display-stereo-display-modes.png](http://www.andrewhazelden.com/blog/wp-content/uploads/2012/07/49.imf-display-stereo-display-modes.png)

This menu shows the available imf\_display stereo display modes.

# Conclusions #
Congratulations for making it through this tutorial! There was a lot of stuff to cover but you have now rendered your first stereoscopic Domemaster image. We have gone over the steps required to make all the connections for a Domemaster3D shading network and how to create a fulldome stereo camera rig.