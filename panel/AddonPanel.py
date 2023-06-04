import bpy
from bpy.types import Panel
from ..operator.AddImage import AddImage
from ..operator.AddMask import AddMask
from ..operator.RunInference import RunInference
from ..operator.PipRequirements import PipRequirements
# The panel class allows us create panel that presents information and input-options for the addon`s user. 
class AddonPanel(Panel):
    # The label will be the label of the addon in the user interface.
    bl_label = "AutoSDF Network"
    # The idname is used to reference the panel outside the class.
    bl_idname = "AUTOSDF_PT_panel"
    # The space type and region type tells the program where we want the addon to be placed.
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    # Sets the name of the addon on the right site of the side-panel.
    bl_category = "AutoSDF Network"

    def draw(self, context):
        scene = context.scene.your_properties
        layout = self.layout
        col = layout.column() 
        # Add the button for the call to the operators
        col.operator(PipRequirements.bl_idname, icon = "SCRIPTPLUGINS")
        col.operator(AddImage.bl_idname, icon = "EVENT_U")
        col.operator(AddMask.bl_idname, icon = "MESH_PLANE")
        # Add the slider for the selection of the position of the inferenced object
        col.prop(scene, "X", icon='EVENT_X')
        col.prop(scene, "Y", icon='EVENT_Y')
        col.prop(scene, "Z", icon='EVENT_Z')
        col.operator(RunInference.bl_idname, icon = "PLAY")