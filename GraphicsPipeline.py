class graphicsPipeline:
    def __init__(self, app):
        self.app = app
        self.depth_texture = self.app.mesh.texture.textures['depth_texture']
        self.depth_fbo = self.app.ctx.framebuffer(depth_attachment=self.depth_texture)

    def render_shadow(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()

        for obj in self.app.scene.objects:
            obj.render_shadow()

    def render(self):
        self.render_shadow()
        self.app.ctx.screen.use()
        self.app.scene.render()

    def destroy(self):
        self.depth_fbo.release()