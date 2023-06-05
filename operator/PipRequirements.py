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
        requirements = os.path.join(
            bpy.utils.resource_path('USER'),
            'scripts/addons/AutoSDF_addon/operator/'
            'requirements.txt')
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
        
        source_folder = os.path.join(bpy.utils.script_paths()[1], 'AutoSDF_addon/AutoSDF/torch')  # Specify the path of the source folder
        destination_folder = os.path.expanduser('~/.cache')
        shutil.copytree(source_folder, destination_folder)

        return {'FINISHED'}