import bpy
from bpy.types import Operator

# This operator will open Blender's file chooser when invoked
# and store the selected filepath in a global property and print it
# to the console using window_manager.fileselect_add()
class AddImage(Operator):
    bl_idname = "add.image"
    bl_label = "Add Image"
    bl_description = "Adds the image for the inference"
    filepath : bpy.props.StringProperty(subtype="FILE_PATH")

    @classmethod
    def poll(cls, context):
        return context.object is not None

    # Function called when the file has been selected in the Window Manager 
    def execute(self, context):
        # Saves the image path in the global property
        context.scene.your_properties.img_file_path = self.filepath
        print('Image path selected: '+ context.scene.your_properties.img_file_path)
        return {'FINISHED'}

    # Function called when button is pressed
    def invoke(self, context, event):
        # Opens the Window Manager File Selector
        bpy.context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}