
bl_info = {
    "name": "scripter",
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
import os
import subprocess 

# os.symlink(pathf,patht)
class OpenBlenderDir(bpy.types.Operator):
    """Open blender install dir"""
    bl_label = "Open blender Dir " 
    bl_idname = "scripter.open_blender_dir"
    def execute(self, context): 
        blender_path = os.path.dirname(bpy.app.binary_path)
        os.startfile(blender_path) 
        return {"FINISHED"}

class OpenAddonsDir(bpy.types.Operator):
    """Open current addons dir"""
    bl_label = "Open Addons Dir " 
    bl_idname = "scripter.open_addons_dir"
    def execute(self, context): 
        st = context.space_data
        text = st.text
        using_addons_path = bpy.utils.user_resource('SCRIPTS', "addons")
        os.startfile(using_addons_path) 
        return {"FINISHED"}

class OpenTextDir(bpy.types.Operator):
    """Open text dir"""
    bl_label = "Open Text Dir " 
    bl_idname = "scripter.open_dir"
    def execute(self, context): 
        st = context.space_data
        text = st.text
        dir_path = os.path.dirname(text.filepath)
        os.startfile(dir_path) 
        return {"FINISHED"}

class OpenWithDefault(bpy.types.Operator):
    """Open text with default editor"""
    bl_label = "Open With Default Editor " 
    bl_idname = "scripter.open_text_default"
    def execute(self, context): 
        st = context.space_data
        text = st.text
        os.startfile(text.filepath) 
        return {"FINISHED"}

class ReopenBlend(bpy.types.Operator):
    """Repoen blend file with blender"""
    bl_label = "Reopen Blend  " 
    bl_idname = "scripter.reopen"
    def execute(self, context): 
        #os.startfile(bpy.data.filepath) 
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
        layout.operator(OpenTextDir.bl_idname, icon = "FILESEL")
        layout.operator(OpenWithDefault.bl_idname)
        layout.operator(ReopenBlend.bl_idname, icon = "BLENDER")
        layout.operator(OpenBlenderDir.bl_idname, icon = "FILESEL")  
        layout.separator() 
        layout.label("addon")
        layout.operator(OpenAddonsDir.bl_idname, icon = "FILESEL") 
        layout.operator(LinkAddon.bl_idname, icon = "FILE_SCRIPT") 


class LinkAddon(Operator, ImportHelper):
    """link addon files to addons path"""
    bl_idname = "scripter.test"  
    bl_label = "Link Addon Files"
    files = CollectionProperty(type=bpy.types.OperatorFileListElement, options={'HIDDEN', 'SKIP_SAVE'})
    directory = StringProperty(maxlen=1024, subtype='FILE_PATH', options={'HIDDEN', 'SKIP_SAVE'})
    filter_python  = BoolProperty(default=True, options={'HIDDEN', 'SKIP_SAVE'})    
    filter_folder = BoolProperty(default=True, options={'HIDDEN', 'SKIP_SAVE'})
    type = EnumProperty(
            default = "ALL_THINGS",
            name="link type",
            description="",
            items=(('FILES', "Selected Python Files", "Selected files link to addon path"),
                   ('FOLDER', "Current Folder", "Current folder link to addon path"),
                   ('ALL_THINGS', "ALL Files/Folders", "All files/folder Under current diretory")                    
                  )
            )
            
    def execute(self, context):  
        type = self.type
        addons_path = bpy.utils.user_resource('SCRIPTS', "addons")
        if type == "FILES":
            for file in self.files:
                source = os.path.join(self.directory,file.name)
                target =os.path.join(addons_path,file.name)
                os.symlink(source,target)
        elif type == "FOLDER":
            current_path = os.path.dirname(self.directory)# 清除directory末尾的\\
            folder_name =os.path.basename(current_path)
            target =os.path.join(addons_path,folder_name)
            os.symlink(self.directory,target)
        elif type == "ALL_THINGS":
            for name in os.listdir(self.directory):
                source = os.path.join(self.directory, name)
                target =os.path.join(addons_path, name)
                os.symlink(source, target)
        return {'FINISHED'}

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)  

if __name__ == "__main__":
    register()


