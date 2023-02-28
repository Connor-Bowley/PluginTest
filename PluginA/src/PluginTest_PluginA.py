# IMPORTANT: MUST IMPORT PluginCore BEFORE ANY OF THE PLUGINS!!!!!
# Really, importing the other plugins by name should not be needed at all in most places.
import PluginCore

dependencies = ["PluginB"]
PluginCore.pluginLoader.loadPlugins(dependencies)

b = PluginCore.factory.makeNewClass("BClass")
assert b.x == 4

b2 = PluginCore.BClass()
assert b2.x == 4

print("Loaded A")

class PluginBModule:
    def __init__(self) -> None:
        self.parent.dependencies = dependencies

def getClasses():
    return []

def registerNodes(factory: PluginCore.Factory) -> None:
    pass
