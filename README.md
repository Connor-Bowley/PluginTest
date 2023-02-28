# PluginTest

This is a test of doing Python plugins. The main goal of the test was to add a plugin's classes into the "PluginCore" namespace. The important parts were:
- To be able to access classes from one plugin in another plugin via the PluginCore namespace.
- For this access to be available right away upon doing `import PluginCore`.

This test is a possible way that 3D Slicer could implement a Python-based plugin architecture, in addition to its existing module management facilities.

## Limitations

Known limitations of this method include:
- Requiring all plugins to be named a certain way.
    - This also requires the naming scheme to be unique enough that 3rd party packages won't accidentally match.
- As it stands, `import PluginCore` _must_ come before something like `import PluginTest_PluginA`.
    - If `import PluginTest_PluginA` is called first, there is a circular import, as it will `import PluginCore`, which will try to `import PluginTest_PluginA`.

## Reasons for wanting a Python based plugin manager for 3D Slicer

- Currently, one cannot use classes from loadable or scripted modules from the `slicer` namespace until after the application has loaded.
    - This effectively prevents MRML nodes from being imported from `slicer` for use with the parameter node wrapper.
    - It has been expressed that internal library names like `MRMLCorePython` or `vtkSlicerMarkupsModuleMRMLPython` should not be used.
    - Because of these reasons, a Python based plugin system that loads the plugin classes into the `slicer` namespace at Python import time is desireable.
- It would help move 3D Slicer toward a more pythonic approach, which will help down the road when Slicer's Python use is inverted such that Slicer is a Python package instead of just packaging Python.

This is not intended to replace the existing Slicer module factory and infrastructure, but just to work with it and above it to make Slicer's use from Python easier.
