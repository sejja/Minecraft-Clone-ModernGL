#
#	Texture.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 17/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

import pygame
import moderngl
import GraphicsPipeline

class Texture:
    # ------------------------------------------------------------------------
    # Constructor
    #
    # Constructs a texture with the path of the image file
    # ------------------------------------------------------------------------
    def __init__(self, path):
        self.texture = pygame.image.load(path + ".png").convert()
        self.texture = pygame.transform.flip(self.texture, flip_x= False, flip_y= True)
        self.texture = GraphicsPipeline.Gfx.GetContext().texture(size= self.texture.get_size(), components= 3,
                                                            data= pygame.image.tostring(self.texture, 'RGB'))
        self.texture.filter = moderngl.NEAREST_MIPMAP_NEAREST, moderngl.NEAREST
        self.texture.build_mipmaps()
        self.texture.anisotropy = 32

    # ------------------------------------------------------------------------
    # Get Texture Object
    #
    # Gets the Texture OpenGL Handle
    # ------------------------------------------------------------------------
    def GetTexture(self):
        return self.texture

    # ------------------------------------------------------------------------
    # Destroy
    #
    # Releases the Data needed
    # ------------------------------------------------------------------------
    def Destroy(self):
        self.texture.release()