'''test for ptvsd'''
import ptvsd
ptvsd.enable_attach("my_secret", address=('0.0.0.0', 3000))
# Enable the line of source code below only if you want the application to wait until the debugger has attached to it
# ptvsd.wait_for_attach()
print("step 1")
print("step 2")
