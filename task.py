'''strdoc'''

import zipfile
import os
import shutil
from pytk import BaseNode


class ScriptProjectInit(BaseNode):
    """Scripter project init"""

    def execute(self, context):
        pass


class package(BaseNode):
    """package prject to release file (zip)"""

    def action(self):
        with zipfile.ZipFile('layers_image.zip', 'w',
                             zipfile.ZIP_DEFLATED) as tzip:
            tzip.write("./scripter.py")
            tzip.close()
        if not os.path.exists("./dist"):
            os.mkdir("./dist")
        shutil.move("layers_image.zip", "dist/layers_image.zip")


class link(BaseNode):
    """link project to blender addon path(need sudo)"""

    def action(self):
        src = os.path.abspath("./scripter.py")
        target = os.path.expanduser(
            "~/.config/blender/2.79/scripts/addons/scripter.py")
        if os.path.exists(target):
            os.remove(target)
        os.symlink(src, target)
