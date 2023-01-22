#
#	Texture.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 17/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

import pygame
import moderngl
from Engine.Graphics import GraphicsPipeline

class Texture:
    # ------------------------------------------------------------------------
    # Constructor
    #
    # Constructs a texture with the path of the image file
    # ------------------------------------------------------------------------
    def __init__(self, path):
        self.mTexture = pygame.image.load(path + ".png").convert()
        self.mTexture = pygame.transform.flip(self.mTexture, flip_x= False, flip_y= True)
        self.mTexture = GraphicsPipeline.Gfx.GetContext().texture(size= self.mTexture.get_size(), components= 3,
                                                                   data= pygame.image.tostring(self.mTexture, 'RGB'))
        self.mTexture.filter = moderngl.NEAREST_MIPMAP_NEAREST, moderngl.NEAREST
        self.mTexture.build_mipmaps()
        self.mTexture.anisotropy = 32

    # ------------------------------------------------------------------------
    # Get Texture Object
    #
    # Gets the Texture OpenGL Handle
    # ------------------------------------------------------------------------
    def GetTexture(self):
        return self.mTexture

    # ------------------------------------------------------------------------
    # Destroy
    #
    # Releases the Data needed
    # ------------------------------------------------------------------------
    def Destroy(self):
        self.mTexture.release()