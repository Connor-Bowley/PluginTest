import PluginCore

class BClass:
    def __init__(self):
        self.x = 4

def getClasses():
    return [BClass]

def registerNodes(factory: PluginCore.Factory) -> None:
    factory.register("BClass", BClass)
