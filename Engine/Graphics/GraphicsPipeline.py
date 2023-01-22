import moderngl

class graphicsPipeline:
    def SetApp(self, app):
        self.app = app
        self.ctx = moderngl.create_context()
        self.ctx.enable(flags=moderngl.DEPTH_TEST | moderngl.CULL_FACE)
        self.depth_texture = self.ctx.depth_texture([1600, 900])  # WINSIZE
        self.depth_texture.repeat_x = False
        self.depth_texture.repeat_y = False
        self.lights = []

    def GetContext(self):
        return self.ctx

    def SetCamera(self, camera):
        self.camera = camera

    def GetCamera(self):
        return self.camera

    def GetLights(self):
        return self.lights

    def AddLight(self, light):
        self.lights.append(light)

    def render_shadow(self):
        if not 'self.depth_fbo' in locals():
            self.depth_texture = self.depth_texture
            self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

        self.depth_fbo.clear()
        self.depth_fbo.use()

        for obj in self.app.scene.mObjects:
            obj.ShadowRender()

    # ------------------------------------------------------------------------
    # GetDeltaTime
    #
    # Gets the time elapsed between frames
    # ------------------------------------------------------------------------
    def GetDeltaTime(self):
        return self.app.mDeltaTime

    # ------------------------------------------------------------------------
    # GetWindowWidth
    #
    # Get the Width of the window
    # ------------------------------------------------------------------------
    def GetWindowWidth(self):
        return 1600

    # ------------------------------------------------------------------------
    # GetWindowHeight
    #
    # Get the Height of the window
    # ------------------------------------------------------------------------
    def GetWindowHeight(self):
        return 900

    def render(self):
        self.render_shadow()
        self.ctx.screen.use()
        self.app.scene.Render()

    def destroy(self):
        self.depth_fbo.release()

    def GetDepthTexture(self):
        return self.depth_texture

Gfx = graphicsPipeline()