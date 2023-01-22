#
#	Main.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 18/12/22
#	Copyright © 2023 Deusto. All Rights reserved
#

from Gameplay import World
from Engine.Core.Assets import AssetManager
from Engine.Core import GameLoop

# ------------------------------------------------------------------------
# Main
#
# Program Entrypoint
# ------------------------------------------------------------------------
if __name__ == '__main__':
    Minecraft = GameLoop.GameLoop()
    Minecraft.scene = World.Scene()
    Minecraft.Run()
    Minecraft.scene.Destroy()
    AssetManager.Assets.Destroy()