import pygame as pg
import sys
import glm
from Graphics.Components.Camera import Camera
from light import Light
from scene import Scene
import GraphicsPipeline
import AssetManager
import GameLoop


if __name__ == '__main__':
    app = GameLoop.GameLoop()
    app.camera = Camera()
    app.camera.position = glm.vec3(0, 1, 4)
    app.scene = Scene(app)
    app.run()
    app.scene.Destroy()
    AssetManager.Assets.Destroy()