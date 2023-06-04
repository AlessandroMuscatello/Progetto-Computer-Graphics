from bpy.types import PropertyGroup

# The properties are imported for the user input for the addon.
from bpy.props import(StringProperty, PointerProperty, FloatProperty)

# Property group for input values. 
class AddonProperties(PropertyGroup):
    
    X: FloatProperty(
        name = "X",
        description = "X position of the new object",
        default = 1.0
        )
    Y: FloatProperty(
        name = "Y",
        description = "Y position of the new object",
        default = 1.0
        )
    Z: FloatProperty(
        name = "Z",
        description = "Z position of the new object",
        default = 1.0
        )
    img_file_path: StringProperty(
        name = "Image FilePath",
        description = "FilePath of the image to be inferenced",
        default = ""
        )
    mask_file_path: StringProperty(
        name = "",
        description = "FilePath of the mask of the image to be inferenced",
        default = ""
        )