#
#	AssetManager.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 06/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

import os
from Engine.Core.Assets import Importers

class AssetManager:
    # ------------------------------------------------------------------------
    # __init__
    #
    # Defines an empty Content diccionary
    # ------------------------------------------------------------------------
    def __init__(self):
        self.content = {}
        self.importers = {".png" : Importers.PNGImporter(),
                          ".shader" : Importers.SHADERImporter(),
                          ".obj" : Importers.OBJImporter()}

    # ------------------------------------------------------------------------
    # Destroy
    #
    # Destroys all the content stored
    # ------------------------------------------------------------------------
    def Destroy(self):
        for x in self.content:
            x.Destroy()

    # ------------------------------------------------------------------------
    # Add Content
    #
    # Adds Content to the Application Carrier
    # ------------------------------------------------------------------------
    def AddContent(self, name, object):
        self.content[name] = object

    # ------------------------------------------------------------------------
    # Asset Exists
    #
    # Returns wether an Asset exists or not
    # ------------------------------------------------------------------------
    def AssetExists(self, name):
        return name in self.content.keys()

    def RemoveAsset(self, name):
        self.content[name].Destroy()
        self.content.pop(name)

    # ------------------------------------------------------------------------
    # Add Content
    #
    # Adds Content to the Application Carrier
    # ------------------------------------------------------------------------
    def GetContent(self, name):
        if name in self.content.keys():
            return self.content[name]
        else:
            file_name, file_extension = os.path.splitext(name)
            asset = self.importers[file_extension].ImportFromFile(file_name)
            self.content[name] = asset
            return asset

#SINGLETON PATTERN
Assets = AssetManager()