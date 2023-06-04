import bpy
from random import *

from bpy.types import Operator

# The class contains the adaptation of the function to run the neural network
# and produces the object to be imported in blender
class RunInference(Operator):
    bl_idname = "create.object_from_inference"
    bl_label = "Run Inference"
    bl_description = "Runs the inference and creates the new object"


    def execute(self, context):
        import os
        import torch.backends.cudnn as cudnn
        import torchvision.utils as vutils
        import sys
        cudnn.benchmark = True
        
        # some utility function for visualization
        from ..AutoSDF.utils.util_3d import sdf_to_mesh #init_mesh_renderer, sdf_to_mesh

        from ..AutoSDF.utils.demo_util import get_shape_comp_opt, get_shape_comp_model
        from ..AutoSDF.utils.qual_util import load_resnet2vq_model, preprocess_img

        """ setup opt"""
        gpu_id = 0

        opt = get_shape_comp_opt(gpu_id=gpu_id)
        opt.vq_note = 'default'
        """ setup models """
        model = get_shape_comp_model(opt)    
        model.eval()

        # img marginal model
        resnet2vq = load_resnet2vq_model(opt)
        print('qui')
        """ setup renderer """
        #dist, elev, azim = 1.7, 20, 20
        #mesh_renderer = init_mesh_renderer(image_size=256, dist=dist, elev=elev, azim=azim, device=opt.device)

        """ setup pix3d img dataset and image marginal model """

        # load and preprocess image
        img_path = context.scene.your_properties.img_file_path
        img_mask_path = context.scene.your_properties.mask_file_path
        # img_path = "/home/alessandro/.config/blender/3.5/scripts/addons/AutoSDF_addon/AutoSDF/demo_data/chair_2598.jpg"
        # img_mask_path = "/home/alessandro/.config/blender/3.5/scripts/addons/AutoSDF_addon/AutoSDF/demo_data/chair_2598_mask.png"

        img_input = preprocess_img(img_path, img_mask_path)

        """ single-view reconstruction """
        nimgs = 3
        topk = 10
        alpha = 0.7

        # inference
        single_view_recon = model.single_view_recon(img_input, resnet2vq, bs=nimgs, topk=topk, alpha=alpha)
        inferenced_mesh = sdf_to_mesh(single_view_recon)
        
        # create the blender mesh
        bl_mesh = bpy.data.meshes.new('Inferenced Mesh')
        bl_mesh.from_pydata(inferenced_mesh.verts_packed(), [], inferenced_mesh.faces_packed())
        bl_mesh.update()
        # add the blender mesh to an object
        obj = bpy.data.objects.new("Inferenced Object", bl_mesh)
        
        scene = context.scene.your_properties
        obj.location = (scene.X, scene.Y, scene.Z)
        bpy.context.scene.collection.objects.link(obj)
        return {'FINISHED'}
    




