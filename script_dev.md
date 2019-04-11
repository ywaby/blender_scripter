
## dev environment
addon project structure
```
project name
    |-README.md
    |-LICENSE
    |-dist
    |-docs
    |-test
    |-...
    |-__init__.py
    |-.gitignore
    |-.pylintrc
    |-data.blend
```

```
blender
blender addon:
    scripter.py
    Icon Viewer
code editor: vscode 
vscode addon:
    blender development
    vscode-python
lint: pylints
format: autopep8
debug: ipdb
version control: git
fake-bpy-module
```

tip
- add dev dir to  filepath->Scripts
- run blender in vscode terminal
- use python console and text editor to test code
- console first
```
blender --python-console --background
blender --python-console --background
```

### install
```sh
sudo apt install python3 blender vscode git
sudo pip3 install ipdb autopep8 pylints
git clone https://github.com/nutti/fake-bpy-module
```

get extra path
```sh
blender --background --python-expr "import sys;print(sys.path)"
```

### autocomplete 
add extra path and fake-bpy-module path to [settings.json](.vscode/settings.json)  
### lints
add extra path and fake-bpy-module path to
[.pylintrc](.pylintrc)  

### debug
link addon to addon path 
reload all addon unregister()->register()  ：F8   
script from editor replace/register ：run script  
ipdb at breakpoint

https://github.com/AlansCodeLog/blender-debugger-for-vscode

show info
```py
print() # terminal
self.report() # info windows
# pop windows
def oops(self, context):
    self.layout.label("You have done something you shouldn't do!")
bpy.context.window_manager.popup_menu(oops, title="Error", icon='ERROR')
```

install from office site need use system package
```sh
PYTHONPATH="/usr/local/lib/python3.7/dist-packages/:/usr/lib/python3/dist-packages" ./blender ... 
PYTHONPATH="/usr/local/lib/python3.7/dist-packages/:/usr/lib/python3/dist-packages" ./blender --python-console
```

python-console
```sh
PYTHONPATH="/usr/local/lib/python3.7/dist-packages/:/usr/lib/python3/dist-packages" ./blender --python-console --background
import IPython;IPython.embed() # for autocomplete
```


### package
- package with python script

## release to blender office
https://developer.blender.org/project/view/3/


## reference
- [vscode](https://code.visualstudio.com/)
- [vscode-python](https://github.com/DonJayamanne/pythonVSCode)
- [blender api](https://docs.blender.org/api/master/index.html)
- https://docs.blender.org/api/master/info_tips_and_tricks.html
- 参考代码：templates->python
- blender buildin script