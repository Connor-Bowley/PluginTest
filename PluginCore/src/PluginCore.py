import importlib
import pkgutil

class Factory:
    def __init__(self):
        self.mapping = dict()

    def register(self, name, type_):
        self.mapping[name] = type_

    def makeNewClass(self, name):
        return self.mapping[name]()

factory = Factory()

# Would it be better to have a "SlicerLoader" module instead of
# putting the loader in the same module? It would allow the full core
# file to initialize before the plugin stuff started.
class PluginLoader:
    def __init__(self):
        self.discoveredPlugins = dict()

    def loadPlugins(self, plugins=None):
        # plugins=None means load all plugins
        print("+loadPlugins", plugins)
        if plugins:
            def isGoodName(name):
                return name.startswith("PluginTest_") and name[11:] in plugins
        else:
            def isGoodName(name):
                return name.startswith("PluginTest_")
        discoveredPlugins = {
            name: importlib.import_module(name)
            for finder, name, ispkg
            in pkgutil.iter_modules()
            if isGoodName(name)
        }
        for modname, mod in discoveredPlugins.items():
            for cls in mod.getClasses():
                globals()[cls.__name__] = cls
            mod.registerNodes(factory)

        self.discoveredPlugins.update(discoveredPlugins)
        print("-loadPlugins", plugins)


pluginLoader = PluginLoader()
pluginLoader.loadPlugins()
