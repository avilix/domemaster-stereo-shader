Table of Contents



# Installation Instructions #
## Maya on Windows ##
<strong>Step 1.</strong> Unzip the domemaster3D.zip archive.

<strong>Step 2.</strong> Copy the appropriate "domeAFL\_FOV\_Stereo.dll" file from either the "Windows 32-bit LIB" or "Windows 64-bit LIB" folder or to your mental ray LIB folder:

On Maya 2012:
<blockquote>C:\Program Files\Autodesk\Maya2012\mentalray\lib\</blockquote>
On Maya 2013:
<blockquote>C:\Program Files\Autodesk\Maya2013\mentalray\shaders\</blockquote>
If you are running a 32-bit version of Maya install the 32-bit DLL. If you are running a 64-bit version of Maya install the 64-bit DLL.

<strong>Step 3.</strong> Copy the "domeAFL\_FOV\_Stereo.mi" mental ray include file to the include folder.
On Maya 2012:
<blockquote>C:\Program Files\Autodesk\Maya2012\mentalray\include\</blockquote>
On Maya 2013:
<blockquote>C:\Program Files\Autodesk\Maya2013\mentalray\shaders\include</blockquote>

<strong>Step 4.</strong> Copy the Maya AE Template file "AEdomeAFL\_FOV\_StereoTemplate.mel" to either the Maya AETemplates folder or to your user account's Maya script folder:
<blockquote>C:\Program Files\Autodesk\Maya2012\scripts\AETemplates\</blockquote>
or
<blockquote>My Documents\maya\2012\prefs\scripts</blockquote>

<strong>Step 5. </strong>Copy the python scripts "init.py", "domeMaterial.py", and "fulldomeStereoRig.py" from the "scripts" folder to your user account's Maya script folder:
<blockquote>My Documents\maya\2012\prefs\scripts</blockquote>

<strong>Step 6.</strong> Copy the "shelf\_Domemaster3D.mel" file from the "shelves" folder to your user account's Maya shelves folder:
<blockquote>My Documents\maya\2012\prefs\shelves</blockquote>

<strong>Step 7.</strong> Copy the Hypershade icons from the "Icons" folder to your Maya icons directory or to your user account's Maya icons directory:
<blockquote>C:\Program Files\Autodesk\Maya2012\icons\</blockquote>
or
<blockquote>My Documents\maya\2012\prefs\icons\</blockquote>

<strong>Step 8.</strong> Copy the textures from the "sourceimages" folder to your current project's sourceimage directory.

The textures "checker.iff" and "bumpChecker.iff" are the default file textures applied when the Color Material or Color + bump material shelf icons are run.

The head\_tilt\_map, separation\_map, and turn\_map textures are used to set up the DomeAFL\_FOV\_Stereo rig.

<strong>Step 9.</strong> The next time you start Maya you will find the "domeAFL\_FOV\_Stereo", "domeAFL\_FOV", "domeAFL\_WxH", and "rob\_lookup\_background" lens shaders in the Hypershade. Look in the create bar under the mental ray < lenses section.

## Maya on Mac OS X ##
This version of the domeAFL\_FOV\_Stereo shader mental ray shader was compiled for Maya 2011 and 2012 for Mac OS X 64-bit. Mac OS X 10.6 Snow Leopard is required.

<strong>Step 1</strong>. Unzip the domemaster3D.zip archive.

<strong>Step 2.</strong> Copy domeAFL\_FOV\_Stereo.dylib file from the "Mac OS X 64-bit LIB" folder to the mentalray lib directory:
<blockquote>/Applications/Autodesk/maya2012/Maya.app/Contents/mentalray/lib/</blockquote>
If you want to go inside the Maya.app package, right click on Maya.app and select "Show Package Contents" from the contextual menu. You may have to change the mental ray folder permissions to allow the shader to be written to the lib and include directories.

On Maya 2013:
<blockquote>/Applications/Autodesk/maya2013/mentalray/shaders/</blockquote>

<strong>Step 3.</strong> Copy the "domeAFL\_FOV\_Stereo.mi" mental ray include file to:
On Maya 2012:
<blockquote>/Applications/Autodesk/maya2012/Maya.app/Contents/mentalray/include</blockquote>
On Maya 2013:
<blockquote>/Applications/Autodesk/maya2013/mentalray/shaders/include</blockquote>

<strong>Step 4.</strong> Copy the Maya AE Template file "AEdomeAFL\_FOV\_StereoTemplate.mel" to either the Maya AETemplates folder or to your user account's Maya script folder:
<blockquote>/Applications/Autodesk/maya2012/Maya.app/Contents/scripts/AETemplates/</blockquote>
or
<blockquote>~/Library/Preferences/Autodesk/maya/2012-x64/prefs/scripts</blockquote>

<strong>Step 5. </strong>Copy the python scripts "init.py", "domeMaterial.py", and "fulldomeStereoRig.py" from the "scripts" folder to your user account's Maya script folder:
<blockquote>~/Library/Preferences/Autodesk/maya/2012-x64/prefs/scripts</blockquote>

<strong>Step 6.</strong> Copy the "shelf\_Domemaster3D.mel" file from the "shelves" folder to your user account's Maya shelves folder:
<blockquote>~/Library/Preferences/Autodesk/maya/2012-x64/prefs/shelves</blockquote>

<strong>Step 7.</strong> Copy the Hypershade icons from the "Icons" folder to your Maya icons directory or to your user account's Maya icons directory:
<blockquote>~/Library/Preferences/Autodesk/maya/2012-x64/prefs/icons</blockquote>

<strong>Step 8.</strong> Copy the textures from the "sourceimages" folder to your current project's sourceimage directory.

The textures "checker.iff" and "bumpChecker.iff" are the default file textures applied when the Color Material or Color + bump material shelf icons are run.

The head\_tilt\_map, separation\_map, and turn\_map textures are used to set up the DomeAFL\_FOV\_Stereo rig.

<strong>Step 9.</strong> The next time you start Maya you will find the "domeAFL\_FOV\_Stereo", "domeAFL\_FOV", "domeAFL\_WxH", and "rob\_lookup\_background" lens shaders in the Hypershade. Look in the create bar under the mental ray < lenses section.

The DomeAFL nodes should be visible in the Lenses section of the create bar.

## Maya on Linux ##
This version of the domeAFL\_FOV\_Stereo shader mental ray shader was compiled for Maya 64-bit on RHEL 6.2.

<strong>Step 1.</strong> Unzip the domemaster3D.zip archive.

<strong>Step 2.</strong>  Copy domeAFL\_FOV\_Stereo.so file from the "Linux X 64-bit LIB" folder to the mentalray lib directory:

On Maya 2012:
<blockquote>/usr/autodesk/maya2012-x64/mentalray/lib</blockquote>
On Maya 2013:
<blockquote>/usr/autodesk/maya2013-x64/mentalray/shaders/</blockquote>

<strong>Step 3.</strong> Copy the "domeAFL\_FOV\_Stereo.mi" mental ray include file to:
On Maya 2012:
<blockquote>/usr/autodesk/maya2012-x64/mentalray/include</blockquote>
On Maya 2013:
<blockquote>/usr/autodesk/maya2013-x64/mentalray/shaders/include<br>
</blockquote>

<strong>Step 4.</strong> Copy the Maya AE Template file "AEdomeAFL\_FOV\_StereoTemplate.mel" to either the Maya AETemplates folder or to your user account's Maya script folder:
<blockquote>/usr/autodesk/maya2012-x64/scripts/AETemplates/</blockquote>
or
<blockquote>~/maya/2012-x64/prefs/scripts</blockquote>
<strong></strong>If you are running a copy of Maya prior to Maya 2010 you don't need to install the AETemplate file:
<blockquote>AEdomeAFL_FOV_StereoTemplate.mel</blockquote>

<strong>Step 5.</strong> Copy the python scripts "init.py", "domeMaterial.py", and "fulldomeStereoRig.py" from the "scripts" folder to the Maya script folder:
<blockquote>/usr/autodesk/maya2012-x64/scripts</blockquote>
or
<blockquote>~/maya/2012-x64/prefs/scripts</blockquote>

<strong>Step 6.</strong> Copy the "shelf\_Domemaster3D.mel" file from the "shelves" folder to your user account's Maya shelves folder:
~/maya/2012-x64/prefs/shelves<strong></strong>

<strong>Step 7.</strong> Copy the Hypershade icons from the "Icons" folder to your Maya icons directory or to your user account's Maya icons directory:
<blockquote>/usr/autodesk/maya2012-x64/prefs/icons</blockquote>
<strong>Step 8.</strong> Copy the textures from the "sourceimages" folder to your current project's sourceimage directory.

The textures "checker.iff" and "bumpChecker.iff" are the default file textures applied when the Color Material or Color + bump material shelf icons are run.

The head\_tilt\_map, separation\_map, and turn\_map textures are used to set up the DomeAFL\_FOV\_Stereo rig.

<strong>Step 9.</strong> The next time you start Maya you will find the "domeAFL\_FOV\_Stereo", "domeAFL\_FOV", "domeAFL\_WxH", and "rob\_lookup\_background" lens shaders in the Hypershade. Look in the create bar under the mental ray < lenses section.