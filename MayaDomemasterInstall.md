|  This Google Code wiki page has been depreciated. Newer information is available on the [Domemaster Stereo Shader wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages) on Github.|
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Table of Contents



# Maya Installation Instructions #

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3D_version_1.3.4/domemaster-installer_splash.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3D_version_1.3.4/domemaster-installer_splash.png)

The Domemaster installer makes it easy to use the 64-bit Domemaster3D shader with Maya 2010-2014 on Windows and Maya 2011-2014 on Mac OS X. The installer allows you to choose which versions of Maya you want to use with the fulldome rendering shader.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3D_version_1.3.4/domemaster3D_maya_install.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3D_version_1.3.4/domemaster3D_maya_install.png)

The Domemaster3D installer creates a new folder on your hard drive to hold the Domemaster3D documentation, texture maps, source code, and the uninstaller program.

On Windows the Domemaster3D folder is located at:
`C:\Program Files\Domemaster3D`

On Mac OS X the Domemaster3D folder is located at:
`/Applications/Domemaster3D`

## Mac OS X 10.8 and 10.9 Tip ##

If you are running Mac OS X 10.8 or 10.9 you need to open your System Preferences and adjust the Gatekeeper / Security & Privacy settings to allow apps downloaded from "Anywhere" to run.

This will allow the unsigned Domemaster3D installer to copy the lens shader library into the Mental Ray shaders folder, and create the /Applications/Domemaster3D resource folder.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/mac/disable_gatekeeper_on_mac_os_x.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/mac/disable_gatekeeper_on_mac_os_x.png)

# Uninstaller Details #

The installation program creates a start menu folder for the Domemaster3D shader. If you want to uninstall the Domemaster3D software you can use the item in the Windows Start menu or the uninstaller application in the Domemaster3D program folder.

## Uninstall Start Menu Item ##

The Start Menu item is the easiest way to remove old versions of the Domemaster3D shader.

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3D_version_1.3.4/Domemaster3D-Uninstaller.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3D_version_1.3.4/Domemaster3D-Uninstaller.png)


## Uninstaller Program ##

![http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3D_version_1.3.4/Domemaster-Program-Folder.png](http://www.andrewhazelden.com/projects/domemaster3D/wiki/domemaster3D_version_1.3.4/Domemaster-Program-Folder.png)

You can uninstall all of the components in the Domemaster3D shader using the uninstall application in the Domemaster3D program folder.

On Windows the Domemaster3D uninstaller is located at:
`C:\Program Files\Domemaster3D\uninstall.exe`

On Mac OS X the Domemaster3D uninstaller is located at:
`/Applications/Domemaster3D/uninstall.app`

If you have run the installer multiple times you may notice a few rollback files left in the domemaster3D folder after the uninstallation is complete. At this point you can can delete the rollback folders and the Domemaster3D folder without any issues.