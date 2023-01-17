import moderngl

import AssetManager
import GraphicsPipeline


class graphicsPipeline:
    def SetApp(self, app):
        self.app = app
        self.ctx = moderngl.create_context()
        self.ctx.enable(flags=moderngl.DEPTH_TEST | moderngl.CULL_FACE)
        self.depth_texture = self.ctx.depth_texture([1600, 900])  # WINSIZE
        self.depth_texture.repeat_x = False
        self.depth_texture.repeat_y = False

    def GetContext(self):
        return self.ctx

    def render_shadow(self):
        if not 'self.depth_fbo' in locals():
            self.depth_texture = GraphicsPipeline.Gfx.get_depth_texture()
            self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

        self.depth_fbo.clear()
        self.depth_fbo.use()

        for obj in self.app.scene.objects:
            obj.render_shadow()

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

    def render(self):
        self.render_shadow()
        self.ctx.screen.use()
        self.app.scene.render()

    def destroy(self):
        self.depth_fbo.release()

    def get_depth_texture(self):
        return self.depth_texture

Gfx = graphicsPipeline()