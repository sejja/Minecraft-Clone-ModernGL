import moderngl

class graphicsPipeline:
    def SetApp(self, app):
        self.app = app
        self.ctx = moderngl.create_context()
        self.ctx.enable(flags=moderngl.DEPTH_TEST | moderngl.CULL_FACE)

    def GetContext(self):
        return self.ctx

    def render_shadow(self):
        if not 'self.depth_fbo' in locals():
            self.depth_texture = self.app.mesh.texture.textures['depth_texture']
            self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

        self.depth_fbo.clear()
        self.depth_fbo.use()

        for obj in self.app.scene.objects:
            obj.render_shadow()

    def render(self):
        self.render_shadow()
        self.ctx.screen.use()
        self.app.scene.render()

    def destroy(self):
        self.depth_fbo.release()

Gfx = graphicsPipeline()