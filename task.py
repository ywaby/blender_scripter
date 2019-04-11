import zipfile
import os
import shutil
from pytk import BaseNode

class link(BaseNode):
    def action(self):
        os.system("ln scripter.py ../addons/ ")


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

    