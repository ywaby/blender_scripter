feature
- reopen blender (sometime need reopen blender for fix bug) 
- open text with external editor
- append sys.path


## dev environment
addon project structure
```
project name
    |-README.md
    |-LICENSE
    |-dist
    |-docs
    |-test
    |-src
        |-__init__.py
        |-data.blend
        |-...
    |-.gitignore
    |-.pylintrc
```
dev tools
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

tips
- add link addon to blender addon dir
- console first
- run blender in vscode terminal
- use python console and text editor to test code
```sh
blender --python-console --background
blender --background -P test.py
# use system python package
# when install blender from office site
PYTHONPATH="/usr/local/lib/python3.7/dist-packages/:/usr/lib/python3/dist-packages" ./blender ... 
PYTHONPATH="/usr/local/lib/python3.7/dist-packages/:/usr/lib/python3/dist-packages" ./blender --python-console

# python-console with IPython
PYTHONPATH="/usr/local/lib/python3.7/dist-packages/:/usr/lib/python3/dist-packages" ./blender --python-console --background
import IPython;IPython.embed() # for autocomplete
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
- link addon to addon path 
- reload(unregister()->register()) all addons for
- use ipdb for breakpoint
- show info
```py
# terminal
print() 
# info windows
self.report() 
# pop windows
def oops(self, context):
    self.layout.label("You have done something you shouldn't do!")
bpy.context.window_manager.popup_menu(oops, title="Error", icon='ERROR')
```



### package
- package with python script: [package task](./task.py)

## release to blender office
https://developer.blender.org/project/view/3/


## reference
- [vscode](https://code.visualstudio.com/)
- [vscode-python](https://github.com/DonJayamanne/pythonVSCode)
- [blender api](https://docs.blender.org/api/master/index.html)
- https://docs.blender.org/api/master/info_tips_and_tricks.html
- templates->python
- blender buildin script