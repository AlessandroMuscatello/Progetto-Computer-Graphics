# Requirements
By now this plugin/installation is tested only on linux!
The only needs (tested) are:
- linux as os
- git
- blender 3.5.1 

# Install the plugin
1. Make sure to have git installed.
2. Download this github and rename the downloaded folder in 'AutoSDF_addon'.
3. Download the pretrained weights from [this link](https://drive.google.com/drive/folders/1n8W_8CfQ7uZDYNrv487sd0oyhRoNLfGo?usp=sharing), and put them under `AutoSDF/saved_ckpt`.
4. Create a zip with all the files. (Inside the zip there must be only the 'AutoSDF_addon' folder with all the other folders and file inside it)
5. In Blender under edit/preferences/add-on click 'install add-on', select the zip file and wait for the install.
6. Activate the add-on.

# Use the add-on
1. Press 'n'. Then, on the right, press the tab 'AutoSDF Network'.
2. (ONLY FOR THE FIRST RUN) Click on install dependencies. It will probably take a while.
3. Select the image to be inferred and the mask relative to the image.
4. Run the inference and wait, the object will be created at the coordinates X, Y, Z specified with the sliders.