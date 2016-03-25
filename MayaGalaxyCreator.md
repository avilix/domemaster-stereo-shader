|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Introduction #

<a href='http://www.youtube.com/watch?feature=player_embedded&v=8gne70tg7mg' target='_blank'><img src='http://img.youtube.com/vi/8gne70tg7mg/0.jpg' width='800' height=450 /></a>

The **Galaxy Creator** tool is an add-on for the Domemaster3D Toolset that creates dynamic galaxies using Maya's particle system and a newton field. The Galaxy Creator tool is a MEL based user interface for Martin Watt's classic galaxies.mel script.

The Galaxy Creator tool can be used to create animations of evolving or colliding galaxies that can be played back in the Maya timeline or rendered using Mental Ray or the Maya Software Renderer.

# Table of Contents #


# Getting Started #

The Galaxy Creator tool launched by clicking on the yellow spiral galaxy shaped icon in the Domemaster3D shelf.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/galaxy_creator_domemaster3D-1.4b8.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/galaxy_creator_domemaster3D-1.4b8.png)

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/Domemaster3D-1.4-Beta8-galaxy.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/Domemaster3D-1.4-Beta8-galaxy.png)

# Galaxy Creator Controls #

The **Copy Particle Settings From** options menu lets you reload the settings used to create previous Galaxy Creator particle in your scene. This menu is populated using the node data that is stored in the particleShape node's Extra Attributes Section.

## Galaxy Type ##

**Galaxy Type** allows you to switch from a spiral galaxy to an elliptical galaxy with either radial or transverse orbits.

**Stars** (integer value)
This is the total number of stars added to the galaxy

**Galaxy Origin** {X,Y,Z}
An XYZ value that defines the starting position of the galaxy.
A value of {0,0,0} would create the galaxy at the origin.

**Galaxy Rotation** {X,Y,Z}
An XYZ value that defines the rotation of the galaxy.

**Galaxy Velocity** {X,Y,Z}
An XYZ value that defines the initial velocity speed for each axis. A value of {0,20,0} would cause the galaxy to move upwards on the Y axis.

**Simulation Speed**
This is a multiplier that can accelerate the speed of the galaxy simulation playback rate. This is achieved by changing the magnitude of the netwon field's strength.

## Spiral Galaxy Options ##

**Galaxy Orientation** (integer value from 0-2)

The **Galaxy Orientation** pop-up menu lets you choose what view direction will be used when a new galaxy is created.

  * The **Side View** option aligns the galaxy on the ZY plane.

  * The **Top View** option aligns the galaxy on the ZX plane.

  * The **Front View** option aligns the galaxy on the on the XY plane.

**Galaxy Radius** (integer value)
The size of the star galaxy defined by a radius value in the current Maya scene units.

**Spiral Arms** (integer value)
This is the total number of spiral branches that come out from the center of the spiral galaxy. The minimum number of Spiral Arms value is 2 arms.

**Galaxy Turns** (float value)
This is the number of spiral turns that each arm of the galaxy makes starting at the center of the galaxy and ending at the outer edge of the galaxy.

## Elliptical Galaxy Options ##

The **Orbit Type** radio button allow you to choose between **Radial** and **Transverse** orbital motion.


## Galaxy Color Shading ##

**Particle Type** (Options menu)
This control lets you switch the rendering style of the galaxy particles to either Cloud, MultiPoint, or MultiStreak.

The **Nucleus Color** swatch defines the look of the center of the galaxy.

The **Galaxy Color** swatch defines the look of the outer galaxy particles.

## Cloud Shading Options ##

The **Nucleus Particle Radius** sets the size of the central core of the galaxy. Increasing this value will create a large glowing central region.

The **Nucleus Glow Intensity** control will adjust the strength of the glow used on the galaxy's central nucleus. The glow is rendered using Maya's shader glow node.

The **Galaxy Particle Radius** sets the size of the particles used to create the outer galaxy arms. Increasing this value will create a thicker galaxy disc.

The **Galaxy Glow Intensity**  control will adjust the strength of the glow used on the galaxy's spiral arms. The glow is rendered using Maya's shader glow node.

## MultiPoint Shading Options ##

The **Galaxy Transparency** color picker controls the transparency of the stars in the galaxy's spiral arms. Generally, the particle transparency should be increased if you are increasing the density of the particles in the sim.

The **Galaxy Multi Count** setting will adjust the number of extra particle points added around the real particles used to create the galaxy's spiral arms.

The **Galaxy Multi Radius** control adjusts the spacing of the extra "Multi Count" particle points added to the galaxy's spiral arms.

The **Galaxy Point Size** slider will adjust the size of the MultiPoint particles used to render the galaxy's spiral arms.

## MultiStreak Shading Options ##


The **Galaxy Transparency** color picker controls the transparency of the stars in the galaxy's spiral arms. Generally, the particle transparency should be increased if you are increasing the density of the particles in the sim.

The **Galaxy Multi Count** setting will adjust the number of extra particle points added around the real particles used to create the galaxy's spiral arms.

The **Galaxy Multi Radius** control adjusts the spacing of the extra "Multi Count" particle points added to the galaxy's spiral arms.

The **Galaxy Streak Line Width** setting will adjust the size of the MultiStreak lines used to render the galaxy's spiral arms.

The **Galaxy Streak Tail Fade** slider will adjust the feathering out of the MultiStreak lines used to render the galaxy's spiral arms.

The **Galaxy Streak Tail Size** control will adjust the length of the MultiStreak lines used to render the galaxy's spiral arms.

## Extra Controls ##

The **Add a galaxy material to the particles** checkbox sets the particle to use a cloud particle display mode and adds a nucleus surface material and a galaxy surface material to the scene. If the checkbox is disabled the particles will be left as simple point based particles. This will skip the process of adding the custom surface materials.

The **Using Lighting on particles** checkbox will enable the "Use Lighting" control on the galaxy's particleShape node. This causes the particle color to change based upon the lighting in the scene.

The **Connect All newtonFields** checkbox links all of the galaxy newton fields to all of the particles in the scene. You can manually control these fields in the Dynamic Relationship Editor window.

The **Skip Nucleus Particle Creation** checkbox will skip the creation of a nucleus particle shape + the addition of a newton field in your scene. This is useful if you want to mix and match multiple outer galaxy particles in your scene without adding an extra nucleus shape each time.

The **Extend PlayBack Range** to X frames control is used to adjust the playback range for the Maya scene.

## Buttons ##

The **Create Galaxy** button will make a new galaxy using the current settings.

The **Open the Hardware Render Buffer Window** button will load the hardware rendering window. This view is especially useful for creating fast galaxy animation previews.

**Tip:** You can use the standard Maya pan/dolly/zoom view navigation controls in the Hardware Render Buffer window.

# Galaxy Animation #

This is a simulation of three colorful galaxies colliding.
<a href='http://www.youtube.com/watch?feature=player_embedded&v=b8zg2NReHbo' target='_blank'><img src='http://img.youtube.com/vi/b8zg2NReHbo/0.jpg' width='800' height=450 /></a>

# Galaxy Creation Tips #

You can run the Galaxy Creator script multiple times and mix-and-match the different galaxy elements in your scene.

If you delete a spiral galaxy, don't forget to remove the unwanted nucleus particle shape too.

You can stack multiple gaseous spiral galaxies in the scene and change their colors and particle radius values to get interesting shading effects.

When multiple galaxies are added to a scene, Maya will simulate complex galaxies collisions that create intricate patterns from the intermixing of particle colors. In the next example, three galaxies were arranged in a triangle style formation around the grid origin.

<a href='http://www.youtube.com/watch?feature=player_embedded&v=ZEmDLYamV2Q' target='_blank'><img src='http://img.youtube.com/vi/ZEmDLYamV2Q/0.jpg' width='800' height=450 /></a>

The galaxies were created using the Galaxy Creator "right view" setting and moved / rotated around to point towards the origin. I found it easier to move the camera around in Maya when I used the "right view" galaxy mode vs animating the galaxies with a "top view" created galaxy collision layout.

I added lots of motion blur to cause the cloudy particle render type to create a streaky particle blur effect. I did this by setting the motion blur to blur each frame by a value larger than the normal "one frame" increment to get longer trails on the particles.

I used the radiusPP particle expression described below to soften the edge (shrink the radius) of the edge particles in the galaxies.

If you want to be able to rewind/play your scene in the Maya timebar you can use the "particle disk caching" option found under the "Solvers" menu in the in the Dynamics menu set.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/colored_galaxy_particles.jpg](http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/colored_galaxy_particles.jpg)

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/b.maya_triple_galaxy_rendered.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/b.maya_triple_galaxy_rendered.png)

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/c.colored_galaxy_particles_2.jpg](http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/c.colored_galaxy_particles_2.jpg)

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/d.maya_triple_galaxy_merged.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/d.maya_triple_galaxy_merged.png)

## Galaxy Shading ##

The galaxy shader uses a combined shading group with a particleCloud and surfaceShader to represent the galaxy particle colors.

The surfaceShader is used for the real-time viewport shading and the particleCloud is used for shading the cloud effect in the render view.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/galaxy_creator_in_maya_2010.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/galaxy_creator_in_maya_2010.png)

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/simple_galaxy.jpg](http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/simple_galaxy.jpg)

# Using Expressions to Fade the Galaxy Edge Particles #

If you want more control over a particle based galaxy in Maya, a radiusPP particle expression can  adjust the particle fade off between the center and edges of the galaxy shape. RadiusPP stands for Radius Per Particle.

A RadiusPP attribute is created automatically by the Galaxy Creator script. If you use the MEL script editor to run the old galaxies.mel script you need to add the RadiusPP value manually.

Select the galaxyParticleShape node. In the attribute editor use the "Add a Dynamic attribute" section to add a per particle attribute. Click on the **General** button.

In the "Add Attribute" window click on the **Particle** tab and select **RadiusPP**. Click the **OK** button to close the window. The RadiusPP value gives you control over the width of each particle in the galaxyParticleShape node.

If the new attribute was added correctly, a RadiusPP entry should be listed in the Per Particle (Array) attribute section. If RadiusPP doesn't show up, try selecting and then deselecting the particle shape in the Viewport to force Maya to redraw the Attribute Editor window.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/a.dual_spiral_galaxies.jpg](http://www.andrewhazelden.com/projects/domemaster3D/wiki/galaxy_creator/a.dual_spiral_galaxies.jpg)

# Changing the Nucleus Particle Size #

After a new particle is created in Maya it's size is defined in the particle shape node. Each particle stores it's radius in a per particle setting known as a radiusPP attribute. This means you need to use a custom expression to change the radius of the particles.

Let's change the size of the nucleus particle.

Select the nucleusParticle in the outliner and open the attribute editor you can change it's size.

Scroll down to the "Per Particle (Array) Attributes" section.

Right click on the field to the right of the **RadiusPP** attribute. In the popup menu select "Creation Expression..."

In the Expression Editor window click and paste in the expression:
nucleusParticleShape.radiusPP = 5;

Now click the "Create" button to save the expression. This has changed the nucleus size to 5 units in the viewport.

Let's try changing the nucleus particle size again.

To change the nucleus size to "1", click the edit button in the Expression Editor and change the expression to read:
nucleusParticleShape.radiusPP = 1;

Click the "Edit" button to save the changes.

## Let's Add a Particle Creation Expression ##

Particle creation expressions are helpful because they allow you to define a custom setting for each of the particles in a particleShape node before a simulation is run.

Right click on the field to the right of the **RadiusPP** attribute and select "Creation Expression...". This will add a new particle creation expression that will control the particles before the first frame of the dynamics simulation begins.

In the Expression Editor paste in the following RadiusPP expression:

```
//Galaxy Edge Fade Effect
//Uses the radiusPP Control

//Size of the Galaxy
float $galaxyRadius = 23.0;

//Size of the cloud particle
float $galaxyParticleRadius = 0.6;

//Thicken Galaxy Center Ratio (Range 0.1-0.75)
float $galaxyParticleRatio = 0.2;


//Calculate the particle's distance from the galaxy origin
vector $pos = galaxyParticleShape.position;
vector $galaxyOrigin = <<0,0,0>>;
vector $dist = <<($galaxyOrigin.x-$pos.x), ($galaxyOrigin.y-$pos.y), ($galaxyOrigin.z-$pos.z)>>;
float $magDist = mag($dist);

//Calculate the final particle size
float $galaxyPercent = 1-($magDist / $galaxyRadius);
float $galaxyBaseParticle = ($galaxyParticleRadius*$galaxyParticleRatio);
float $galaxyParticleSize = ($galaxyParticleRadius*$galaxyPercent);

//Set the per particle size
galaxyParticleShape.radiusPP = $galaxyParticleSize + $galaxyBaseParticle;

//End
```

The value `$galaxyRadius` lets you manually enter the size of the galaxy.

The `$galaxyOrigin` attribute lets you enter an offset for the X,Y,Z position of the galaxy if it is moved away from the world origin.

By changing the `$galaxyParticleRadius` value you can control the overall side of the cloud particles.

The `$galaxyParticleRatio` value controls how thick the center of the particle shape is compared to the edges. A value between 0.1-0.75 is usually appropriate.

In order to use the particle creation expression you need to change the text "galaxyParticleShape" near the top and bottom of the script by entering the name of your current particle object.

Once you have pasted the sample particle expression text in the Expression Editor window, you can click the "Create Button" to save the new expression.