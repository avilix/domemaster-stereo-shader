# Create Instant Galaxies in Maya #

## Introduction ##

![](screenshots/mixed_galaxy_with_stars.jpg)

The *Galaxy Creator* tool is an add-on for the Domemaster3D Toolset that creates dynamic galaxies using Maya's particle system and a newton field. The Galaxy Creator tool is a MEL based user interface for Martin Watt's classic galaxies.mel script.

The Galaxy Creator tool can be used to create animations of evolving or colliding galaxies that can be played back in the Maya timeline or rendered using Mental Ray or the Maya Software Renderer.


## Getting Started ##
The Galaxy Creator tool launched by clicking on the yellow spiral galaxy shaped icon in the Domemaster3D shelf.

![](screenshots/galaxy_creater_user_interface.png)

![](screenshots/galaxy_creator_in_maya_2014.png)
Here are a few galaxy values you can try out:

### Ring Galaxy #1   ###
  * Stars: 2000   
  * Radius: 20   
  * Spiral Arms: 400   
  * Galaxy Turns: 5  
  * Nucleus Color: (HSV) H: 35.22 /  S: 0.247 / V: 1.0  
  * Galaxy Particle Color: (HSV) H:249 / S:0.451 / V: 0.51  

![](screenshots/ring_galaxy_2.jpg)

### Ring Galaxy #2  ###
  * Stars: 3000  
  * Radius: 20  
  * Spiral Arms: 400  
  * Galaxy Turns: 10   
  * Nucleus Color: (HSV) H: 35.22 /  S: 0.247 / V: 1.0  
  * Galaxy Particle Color: (HSV) H:2.959 / S:0.646 / V:0.556  
 
![](screenshots/circular_galaxy_3.jpg)

## Galaxy Creator Controls ##

*Galaxy Orientation* (integer value from 0-2)

The *Galaxy Orientation* pop-up menu lets you choose what view direction will be used when a new galaxy is created. 

  * The *Side View* option aligns the galaxy on the ZY plane.

  * The *Top View* option aligns the galaxy on the ZX plane.

  * The *Front View* option aligns the galaxy on the on the XY plane.


*Number of Stars* (integer value)
This is the total number of stars added to the galaxy

*Galaxy Radius* (integer value)
The size of the star galaxy defined by a radius value in the current Maya scene units.

*Spiral Arms* (integer value)
This is the total number of spiral branches that come out from the center of the spiral galaxy. The minimum number of Spiral Arms value is 2 arms.

*Galaxy Turns* (float value)
This is the number of spiral turns that each arm of the galaxy makes starting at the center of the galaxy and ending at the outer edge of the galaxy.

*Galaxy Origin* {X,Y,Z}
An XYZ value that defines the starting position of the galaxy.
A value of {0,0,0} would create the galaxy at the origin.

*Galaxy Velocity* {X,Y,Z}
An XYZ value that defines the initial velocity speed for each axis. A value of {0,20,0} would cause the galaxy to move upwards on the Y axis.

The *Nucleus Color* swatch defines the look of the center of the galaxy.

The *Nucleus Particle Radius* sets the size of the central core of the galaxy. Increasing this value will create a large glowing central region.

The *Galaxy Color* swatch defines the look of the outer galaxy particles.

The *Galaxy Particle Radius* sets the size of the outer galaxy arms. Increasing this value will create a thicker galaxy disc.

The *Add Cloud Material* checkbox sets the particle to use a cloud particle display mode and adds a nucleus surface material and a galaxy surface material to the scene. If the Add Cloud Material checkbox is disabled the particles will be left as simple point based particles. This will skip the process of adding the custom surface materials.

The *Connect All newtonFields* checkbox links all of the galaxy newton fields to all of the particles in the scene. You can manually control these fields in the Dynamic Relationship Editor window.


## Galaxy Animation ##

The spiral galaxy animation was created with a large central glowing nucleus and 10 gaseous spiral arms.

[http://www.youtube.com/watch?v=S3SdbesRQME](http://www.youtube.com/watch?v=S3SdbesRQME)

----------


This is a simulation of three colorful galaxies colliding.  

[http://www.youtube.com/watch?v=b8zg2NReHbo](http://www.youtube.com/watch?v=b8zg2NReHbo)

----------


## Galaxy Creation Tips ##

You can run the Galaxy Creator script multiple times and mix-and-match the different galaxy elements in your scene.

If you delete a spiral galaxy, don't forget to remove the unwanted nucleus particle shape too.

You can stack multiple gaseous spiral galaxies in the scene and change their colors and particle radius values to get interesting shading effects.

When multiple galaxies are added to a scene, Maya will simulate complex galaxies collisions that create intricate patterns from the intermixing of particle colors. In the next example, three galaxies were arranged in a triangle style formation around the grid origin.

[http://www.youtube.com/watch?v=ZEmDLYamV2Q](http://www.youtube.com/watch?v=ZEmDLYamV2Q)

The galaxies were created using the Galaxy Creator "right view" setting and moved / rotated around to point towards the origin. I found it easier to move the camera around in Maya when I used the "right view" galaxy mode vs animating the galaxies with a "top view" created galaxy collision layout.

I added lots of motion blur to cause the cloudy particle render type to create a streaky particle blur effect. I did this by setting the motion blur to blur each frame by a value larger than the normal "one frame" increment to get longer trails on the particles.

I used the radiusPP particle expression described below to soften the edge (shrink the radius) of the edge particles in the galaxies.

If you want to be able to rewind/play your scene in the Maya timebar you can use the "particle disk caching" option found under the "Solvers" menu in the in the Dynamics menu set.

![](screenshots/colored_galaxy_particles.jpg)

![](screenshots/b.maya_triple_galaxy_rendered.png)

![](screenshots/c.colored_galaxy_particles_2.jpg)

![](screenshots/d.maya_triple_galaxy_merged.png)

## Galaxy Shading ##

The galaxy shader uses a combined shading group with a particleCloud and surfaceShader to represent the galaxy particle colors. 

The surfaceShader is used for the real-time viewport shading and the particleCloud is used for shading the cloud effect in the render view.

![](screenshots/galaxy_creator_in_maya_2010.png)

![](screenshots/simple_galaxy.jpg)

## Using Expressions to Fade the Galaxy Edge Particles  ##

If you want more control over a particle based galaxy in Maya, a radiusPP particle expression can  adjust the particle fade off between the center and edges of the galaxy shape. RadiusPP stands for Radius Per Particle.

A RadiusPP attribute is created automatically by the Galaxy Creator script. If you use the MEL script editor to run the old galaxies.mel script you need to add the RadiusPP value manually. 

Select the particleShape node. In the attribute editor use the "Add a Dynamic attribute" section to add a per particle attribute. Click on the *General* button. 

In the "Add Attribute" window click on the *Particle* tab and select *RadiusPP*. Click the *OK* button to close the window. The RadiusPP value gives you control over the width of each particle in the particleShape node.

If the new attribute was added correctly, a RadiusPP entry should be listed in the Per Particle (Array) attribute section. If RadiusPP doesn't show up, try selecting and then deselecting the particle shape in the Viewport to force Maya to redraw the Attribute Editor window.

![](screenshots/a.dual_spiral_galaxies.jpg)

## Let's Add a Particle Creation Expression ##

Particle creation expressions are helpful because they allow you to define a custom setting for each of the particles in a particleShape node before a simulation is run.

Right click on the field to the right of the *RadiusPP* attribute and select "Creation Expression...". This will add a new particle creation expression that will control the particles before the first frame of the dynamics simulation begins.

In the Expression Editor paste in the following RadiusPP expression:

<pre><code>
//Galaxy Edge Fade Effect
//Uses the radiusPP Control

//Size of the Galaxy
float $galaxyRadius = 23.0;

//Size of the cloud particle
float $galaxyParticleRadius = 0.6;

//Thicken Galaxy Center Ratio (Range 0.1-0.75)
float $galaxyParticleRatio = 0.2;


//Calculate the particle's distance from the galaxy origin
vector $pos = particleShape2.position;
vector $galaxyOrigin = <<0,0,0>>;
vector $dist = <<($galaxyOrigin.x-$pos.x), ($galaxyOrigin.y-$pos.y), ($galaxyOrigin.z-$pos.z)>>;
float $magDist = mag($dist);

//Calculate the final particle size
float $galaxyPercent = 1-($magDist / $galaxyRadius);
float $galaxyBaseParticle = ($galaxyParticleRadius*$galaxyParticleRatio);
float $galaxyParticleSize = ($galaxyParticleRadius*$galaxyPercent);

//Set the per particle size
particleShape2.radiusPP = $galaxyParticleSize + $galaxyBaseParticle;

//End
</code></pre>


The value `$galaxyRadius` lets you manually enter the size of the galaxy.

The `$galaxyOrigin` attribute lets you enter an offset for the X,Y,Z position of the galaxy if it is moved away from the world origin.

By changing the `$galaxyParticleRadius` value you can control the overall side of the cloud particles.

The `$galaxyParticleRatio` value controls how thick the center of the particle shape is compared to the edges. A value between 0.1-0.75 is usually appropriate.

In order to use the particle creation expression you need to change the text "particleShape2" near the top and bottom of the script by entering the name of your current particle object. 

Once you have pasted the sample particle expression text in the Expression Editor window, you can click the "Create Button" to save the new expression.