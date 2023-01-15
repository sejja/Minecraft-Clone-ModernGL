#
#	Carrier.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 06/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

class Carrier_Struct:
    # ------------------------------------------------------------------------
    # __init__
    #
    # Defines an empty Content diccionary
    # ------------------------------------------------------------------------
    def __init__(self):
        self.content = {}

    # ------------------------------------------------------------------------
    # Destroy
    #
    # Destroys all the content stored
    # ------------------------------------------------------------------------
    def Destroy(self):
        for x in self.content:
            x.Destroy()

    # ------------------------------------------------------------------------
    # Set App
    #
    # The Main App Instance
    # ------------------------------------------------------------------------
    def SetApp(self, app):
        self.app = app

    # ------------------------------------------------------------------------
    # GetDeltaTime
    #
    # Gets the time elapsed between frames
    # ------------------------------------------------------------------------
    def GetDeltaTime(self):
        return self.app.delta_time

    # ------------------------------------------------------------------------
    # GetWindowWidth
    #
    # Get the Width of the window
    # ------------------------------------------------------------------------
    def GetWindowWidth(self):
        return self.app.WIN_SIZE[0]

    # ------------------------------------------------------------------------
    # GetWindowHeight
    #
    # Get the Height of the window
    # ------------------------------------------------------------------------
    def GetWindowHeight(self):
        return self.app.WIN_SIZE[1]

    # ------------------------------------------------------------------------
    # Add Content
    #
    # Adds Content to the Application Carrier
    # ------------------------------------------------------------------------
    def AddContent(self, name, object):
        self.content[name] = object

    # ------------------------------------------------------------------------
    # Add Content
    #
    # Adds Content to the Application Carrier
    # ------------------------------------------------------------------------
    def GetContent(self, name):
        return self.content[name]

#SINGLETON PATTERN
carry = Carrier_Struct()