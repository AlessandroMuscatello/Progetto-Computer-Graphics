# Requirements
By now this plugin/installation is tested only on linux!
The only needs (tested) are:
- Linux as os
- Git
- Blender 3.5.1 

# Install the plugin
1. Make sure to have git installed.
2. Download this github and rename the downloaded folder in 'AutoSDF_addon'.
3. Download the pretrained weights from [this link](https://drive.google.com/drive/folders/1n8W_8CfQ7uZDYNrv487sd0oyhRoNLfGo?usp=sharing), and extract them under `AutoSDF/saved_ckpt` or you could use the button integrated inside the Blender plugin (see below) .
4. Create a zip with all the files. (Inside the zip there must be only the 'AutoSDF_addon' folder with all the other folders and file inside it)
5. In Blender under edit/preferences/add-on click 'install add-on', select the zip file and wait for the install.
6. Activate the add-on.

# Use the add-on
1. Press 'n'. Then, on the right, click on the tab 'AutoSDF Network'.
2. (ONLY FOR THE FIRST RUN) Click on install dependencies. It will probably take a while.
4. If you didn't put the extracted weights in the folders as said in the previous paragraph, or you want to use you trained weights you could use the Add Weights button to select a .zip file containing the four requested weights file. The zip MUST only contain the weights files and the naming MUST be the same as the original naming of the files.
5. Select the image to be inferred and the mask relative to the image. (See below on how to create the mask)
6. Run the inference and wait, the object will be created at the coordinates X, Y, Z specified with the sliders.

# How to create the mask
The mask is a .png file of the same dimension of the original image from where you want to do the inference. The mask will have white pixels corresponsing to the position of the object in the original image, and black pixels on all the other pixels. An example can be found inside the AutoSDF/demo_data folder.
