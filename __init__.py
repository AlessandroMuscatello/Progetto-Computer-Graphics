# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import bpy
from bpy.props import PointerProperty
import sys
from .PropertyGroup.AddonProperties import AddonProperties
from .operator.AddImage import AddImage
from .operator.AddMask import AddMask
from .operator.RunInference import RunInference
from .panel.AddonPanel import AddonPanel
from .operator.PipRequirements import PipRequirements
from .operator.AddWeights import AddWeights

# Plugin info
bl_info = {
    "name" : "AUTOSDF",
    "author" : "F. Battistelli, A. Maranesi, A. Muscatello",
    "description" : "The addon uses the pretrained AutoSDF Network to create an inferenced object from an image and a mask and imports it into the scene",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

__classes__ = (
    PipRequirements,
    AddonProperties,
    AddonPanel,
    AddImage,
    AddMask,
    RunInference,
    AddWeights,
)

# Register classes for addon
def register():
    sys.path.append("/usr/lib/python3/dist-packages")
    for cls in __classes__:
        bpy.utils.register_class(cls)
    bpy.types.Scene.your_properties = PointerProperty(type=AddonProperties)

# Unregister classes
def unregister():
    for cls in __classes__:
        bpy.utils.unregister_class(cls)   
    del bpy.types.Scene.your_properties