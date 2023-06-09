import bpy
from bpy.types import Operator
import subprocess
import sys
import os

class PipRequirements(Operator):
    bl_idname = "install.requirements"
    bl_label = "Install Requirements"
    bl_description = "Install required requirements for the network"


    def execute(self, context):
        py_path = os.path.join(
            bpy.utils.resource_path('LOCAL'),
            'python/bin/python3.10')
        subprocess.call([py_path, "-m", "ensurepip"])
        
        # install required packages
        # Find current script directory (the Blender plugin directory)
        script_dir = os.path.dirname(os.path.realpath(__file__))
        
        # Install required packages

        requirements = os.path.join(script_dir, 'requirements.txt')
        print('requirements path = '+requirements)
        subprocess.call([py_path, "-m", "pip", "install", '-r', requirements])

        # install git for pytorch3d separated
        import sys
        import torch
        pyt_version_str=torch.__version__.split("+")[0].replace(".", "")
        version_str="".join([
            f"py3{sys.version_info.minor}_cu",
            torch.version.cuda.replace(".",""),
            f"_pyt{pyt_version_str}"
        ])
        subprocess.call([py_path, "-m", "pip", "install", "fvcore", "iopath"])
        subprocess.call([py_path, "-m", "pip", "install", "--no-index",
                        "--no-cache-dir", "pytorch3d", "-f",
                         "https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/"+version_str+"/download.html"])
        
        # copy the resnet checkpoint to .cache to avoid fail when downloading
        import shutil
        destination_folder = os.path.expanduser('~/.cache/torch/hub/checkpoints')
        if not os.path.exists(destination_folder):
            # Create the folder if it doesn't exist
            os.makedirs(destination_folder)
        # Copy the file to the destination folder
        source_file = os.path.join(bpy.utils.script_paths()[1], 'addons/AutoSDF_addon/AutoSDF/torch/hub/checkpoints/resnet18-f37072fd.pth')
        shutil.copy2(source_file, destination_folder)
        return {'FINISHED'}