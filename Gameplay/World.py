#
#	World.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 19/12/22
#	Copyright © 2023 Deusto. All Rights reserved
#

import glm
import pygame
from Engine.Audio import Mixer
import random
import threading
import time
from Gameplay import Cube, Skybox
from Engine.Graphics import GraphicsPipeline
from Engine.Physics import VoxelPhysicSystem
from Engine.Graphics.Components import Camera
import tkinter

# ------------------------------------------------------------------------
# Background Music
#
# Plays a random song every 5 minutes - Diferent Thread
# ------------------------------------------------------------------------
def Background_music():
    while True:
        music_list = ["Subwoofer Lullaby", "Clark", "Dry Hands", "Equinoxe", "Minecraft",
                    "Haggstrom", "Moog City", "Oxygene", "Sweden", "Wet Hands"]
        Mixer.audio.PlaySound("Content/Audio/Music/" + random.choice(music_list) + ".mp3")
        time.sleep(5 * 60)

class Scene:
    # ------------------------------------------------------------------------
    # Constructor
    #
    # Creates a world ready to be populated
    # ------------------------------------------------------------------------
    def __init__(self):
        self.mCamera = Camera.Camera()
        self.mCamera.position = glm.vec3(0, 1, 4)
        GraphicsPipeline.Gfx.SetCamera(self.mCamera)
        self.mObjects = []
        self.BuildMap()
        # skybox
        self.mSkybox = Skybox.SkyBox(tex_id='Content/Textures/skybox1/')
        self.mPressed = False
        self.texture = 'Content/Textures/img.png'
        self.mForce = glm.vec3(0, 0, 0)
        self.MusicThread = threading.Thread(target=Background_music)
        self.MusicThread.start()
        self.mMoving = False

    # ------------------------------------------------------------------------
    # BuildMap
    #
    # Creates a floor to walk on
    # ------------------------------------------------------------------------
    def BuildMap(self):
        VoxelPhysicSystem.Physx.SetBounds(glm.vec3(-250, -5, -250), glm.vec3(250, 250, 250))
        VoxelPhysicSystem.Physx.Setup()

        for x in range(-20, 20):
            for z in range(-20, 20):
                self.mObjects.append(Cube.Cube(pos=glm.vec3(x, -1, z), tex_id= 'Content/Textures/img_5.png'))

    # ------------------------------------------------------------------------
    # Save Scene
    #
    # Saves the scene on a separate file
    # ------------------------------------------------------------------------
    def SaveScene(self):
        files = [('Minepy map', '*.mnpy')]
        with tkinter.filedialog.asksaveasfile(filetypes=files, defaultextension=files) as file:
            savestring = ""
            for x in self.mObjects:
                savestring += str(x.mTransform.mPosition.x) + "$" + \
                              str(x.mTransform.mPosition.y) + "$" + \
                              str(x.mTransform.mPosition.z) + "$"
                savestring += x.mComponents[0].mTexture + "$"

            file.write(savestring)
            file.close()

    # ------------------------------------------------------------------------
    # Open Scene
    #
    # Opens and loads the scene from file
    # ------------------------------------------------------------------------
    def OpenScene(self):
        self.mObjects.clear()
        files = [('Minepy map', '*.mnpy')]

        file_name = tkinter.filedialog.askopenfilename(filetypes=files, defaultextension=files)

        with open(file_name, "r") as file:
            savestring = file.read().split('$')

            for i in range(int(len(savestring) / 4)):
                pos_x = int(float(savestring[i * 4 + 0]))
                pos_y = int(float(savestring[i * 4 + 1]))
                pos_z = int(float(savestring[i * 4 + 2]))
                texture = savestring[i * 4 + 3]
                self.mObjects.append(Cube.Cube(pos=glm.vec3(pos_x, pos_y, pos_z), tex_id= texture))

    # ------------------------------------------------------------------------
    # Update
    #
    # Updates the Scene
    # ------------------------------------------------------------------------
    def Update(self):
        self.mCamera.Update()
        keys = pygame.key.get_pressed()
        updatefactor = 0.005 * GraphicsPipeline.Gfx.GetDeltaTime()
        direction = glm.vec3(self.mCamera.forward.x, 0, self.mCamera.forward.z)
        perpendicular = glm.vec3(-direction.z, 0, direction.x)

        if keys[pygame.K_SPACE]:
            if not self.mPressed:
                raycast = VoxelPhysicSystem.Physx.RaycastClosestPointInmediatePrevious(self.mCamera.position, self.mCamera.forward)

                if raycast != self.mCamera:
                    self.mPressed = True
                    self.mObjects.append(Cube.Cube(pos=glm.vec3(raycast[0], raycast[1], raycast[2]), tex_id=self.texture))
                    Mixer.audio.PlaySound("Content/Audio/Sfx/PlacingBlock.mp3")

                self.mPressed = True
        else:
            self.mPressed = False

        if keys[pygame.K_BACKSPACE]:
            raycast = VoxelPhysicSystem.Physx.RaycastClosestPoint(self.mCamera.position, self.mCamera.forward)

            if raycast != self.mCamera:
                for j in self.mObjects:
                    if j.mTransform.mPosition == raycast:
                        self.mPressed = True
                        j.Destroy()
                        self.mObjects.remove(j)
                        Mixer.audio.PlaySound("Content/Audio/Sfx/Remove.mp3")
                        return

        stepping = VoxelPhysicSystem.Physx.IsColliding(self.mCamera.position, glm.vec3(0, -2, 0))

        if keys[pygame.K_u] and stepping:
            self.mForce += glm.vec3(0, 0.2, 0)

        if not stepping:
            self.mForce.y -= 0.016
        elif self.mForce.y < 0:
            self.mForce.y = 0
            self.mCamera.mPostition.y = int(self.mCamera.mPostition.y)

        self.mCamera.position += self.mForce

        update = glm.vec3(0, 0, 0)

        if keys[pygame.K_w]:
            update += direction * updatefactor
        if keys[pygame.K_s]:
            update -= direction * updatefactor
        if keys[pygame.K_a]:
            update -= perpendicular * updatefactor
        if keys[pygame.K_d]:
            update += perpendicular * updatefactor

        if keys[pygame.K_1]:
            self.texture = 'Content/Textures/img.png'
        elif keys[pygame.K_2]:
            self.texture = 'Content/Textures/img_1.png'
        elif keys[pygame.K_3]:
            self.texture = 'Content/Textures/img_2.png'
        elif keys[pygame.K_3]:
            self.texture = 'Content/Textures/img_3.png'
        elif keys[pygame.K_4]:
            self.texture = 'Content/Textures/img_4.png'
        elif keys[pygame.K_5]:
            self.texture = 'Content/Textures/img_5.png'
        elif keys[pygame.K_6]:
            self.texture = 'Content/Textures/img_6.png'
        elif keys[pygame.K_7]:
            self.texture = 'Content/Textures/img_7.png'
        elif keys[pygame.K_8]:
            self.texture = 'Content/Textures/img_8.png'
        elif keys[pygame.K_9]:
            self.texture = 'Content/Textures/img_9.png'
        elif keys[pygame.K_0]:
            self.texture = 'Content/Textures/img_10.png'

        if keys[pygame.K_o]:
            self.SaveScene()

        if keys[pygame.K_i]:
            self.OpenScene()

        if update.x != 0 and update.z != 0:
            block = VoxelPhysicSystem.Physx.IsColliding(self.mCamera.position,
                                                        glm.normalize(update)) or VoxelPhysicSystem.Physx.IsColliding(
                self.mCamera.position - glm.vec3(0, 1, 0), glm.normalize(update))

            if not block:
                self.mCamera.position += glm.normalize(update) / 10

                if not self.mMoving:
                    Mixer.audio.PlaySound("Content/Audio/Sfx/Footsteps.mp3", -1)
                self.mMoving = True
            else:
                if self.mMoving:
                    Mixer.audio.Pause("Content/Audio/Sfx/Footsteps.mp3")
                self.mMoving = False
        else:
            if self.mMoving:
                Mixer.audio.Pause("Content/Audio/Sfx/Footsteps.mp3")
            self.mMoving = False

        rel_x, rel_y = pygame.mouse.get_rel()
        self.mCamera.yaw += rel_x * 0.05
        self.mCamera.pitch = max(-89.99, min(89.99, self.mCamera.pitch - rel_y * 0.05))

    # ------------------------------------------------------------------------
    # Render
    #
    # Renders the scene
    # ------------------------------------------------------------------------
    def Render(self):
        for obj in self.mObjects:
            obj.Render()
        self.mSkybox.Render()
