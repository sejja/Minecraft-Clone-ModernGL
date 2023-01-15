class Carrier_Struct:
    def __init__(self, app):
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

carry = None #To Be Defined