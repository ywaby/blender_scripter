#  ~/app/blender-2.80/blender test/dev.blend  -P test/test.py --background
import bpy
import sys
for path in bpy.context.preferences.addons['scripter'].preferences.py_extra_paths:
    if path.path not in sys.path:
        print(f'{path.path} not in sys.path')
print('test pass')
