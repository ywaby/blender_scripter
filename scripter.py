'''docstring'''
bl_info = {
    "name": "Scripter",
    "author": "ywaby",
    "version": (0, 0, 1),
    "blender": (2, 78),
    "description": "make script easier",
    "warning": "",
    "wiki_url": "http://github.com"
                "Scripts/Add_Mesh/Planes_from_Images",
    "tracker_url": "http://github.com",
    "support": "TESTING",
    "category": "Development"
}

import os
import subprocess
import bpy
from bpy.props import (
    StringProperty,
    BoolProperty,
    EnumProperty,
    IntProperty,
    FloatProperty,
    CollectionProperty,
    BoolVectorProperty,
    PointerProperty
)
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator


class DebugExt(bpy.types.Operator):
    """Establish remote debug"""
    bl_label = 'Establish remote debug'
    bl_idname = 'scripter.establish_remote_debug'

    def execute(self, context):
        import ptvsd
        ptvsd.enable_attach("my_secret", address=('127.0.0.1', 3000))
        ptvsd.wait_for_attach()
        return {'FINISHED'}


class ReopenBlend(bpy.types.Operator):
    """Repoen current blend file"""
    bl_label = "Reopen current Blend file"
    bl_idname = "scripter.reopen"

    def execute(self, context):
        # os.startfile(bpy.data.filepath)
        subprocess.Popen([bpy.app.binary_path, bpy.data.filepath])
        bpy.ops.wm.quit_blender()
        return {"FINISHED"}


class Scripter_tools(bpy.types.Panel):
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_label = "Scripter"
    bl_category = 'B2D'

    def draw(self, context):
        layout = self.layout
        st = context.space_data
        layout.operator(ReopenBlend.bl_idname, icon="BLENDER")


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
