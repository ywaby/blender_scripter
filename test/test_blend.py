import bpy

class Test(bpy.types.Operator):
    """Tooltip"""
    bl_label = "test blender code"
    bl_idname = "test.test_code"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return (space.type == 'NODE_EDITOR' and
                space.tree_type == 'ShaderNodeTree' and
                space.shader_type == 'OBJECT' and
                space.node_tree)

    def execute(self, context):
        print(context.space_data)
        import ipdb
        ipdb.set_trace()
        return {'FINISHED'}


def register():
    bpy.utils.register_class(Test)


def unregister():
    bpy.utils.unregister_class(Test)


if __name__ == "__main__":
    register()
