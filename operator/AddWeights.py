import bpy
from bpy.types import Operator
import zipfile
import os

# This operator will open Blender's file chooser when invoked
# and store the selected filepath in a global property and print it
# to the console using window_manager.fileselect_add()
class AddWeights(Operator):
    bl_idname = "add.weights"
    bl_label = "Add Weights"
    bl_description = "Load the custom weights for the network"
    filepath : bpy.props.StringProperty(subtype="FILE_PATH")


    @classmethod
    def poll(cls, context):
        return context.object is not None

    # Function called when the file has been selected in the Window Manager 
    def execute(self, context):
        # Weights to be found
        check_list = ['bert2vq_epoch-145', 'pvqvae-snet-all-LR1e-4-T0.2-rerun-epoch140', 'resnet2vq-pix3d_img-all-LR1e-4-cleanCode-pix3dMode-noBG-epoch40', 'rand_tf-snet_code-all-LR1e-4-clean-epoch200']
        # Path to save the new weights
        output_path = os.path.join(
                    bpy.utils.resource_path('USER'),
                    'scripts/addons/AutoSDF_addon/AutoSDF/saved_ckpt'
        )
        with zipfile.ZipFile(self.filepath, 'r') as zip_ref:
            # Checks that there are at least four files.
            file_names = zip_ref.namelist()
            if len(file_names) < 4:
                def draw(self, context):
                    self.layout.label(text="Not enough files inside the zip. Using default weights.")
                bpy.context.window_manager.popup_menu(draw, title="Error", icon='INFO')
                return {'FINISHED'}
            # Checks that the new file names are correct.
            for name in file_names:
                if os.path.splitext(name)[0] not in check_list:
                    def draw(self, context):
                        self.layout.label(text="File name '"+os.path.splitext(name)[0]+"' not correct.")
                    bpy.context.window_manager.popup_menu(draw, title="Error", icon='INFO')
                    return {'FINISHED'}
            # Delete old external weights
            for item in os.listdir(output_path):
                item_path = os.path.join(output_path, item)
                os.remove(item_path)
            zip_ref.extractall(output_path)
                
        return {'FINISHED'}

    # Function called when button is pressed
    def invoke(self, context, event):
        # Opens the Window Manager File Selector
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}