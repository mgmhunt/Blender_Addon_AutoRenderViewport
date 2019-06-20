import bpy


class MGMHUNT_PT_autorenderviewport(bpy.types.Panel):
    bl_idname = "MGMHUNT_PT_autorenderviewport"
    bl_label = "Render Viewport"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "View"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        ob = context.object
        settings = context.scene.RenderViewportSettings

        layout.prop(settings, 'b_autorender', toggle=True)

        row.operator('mgmhunt.autorenderviewport',
                     text="Manual Render").b_manualRender = True

        layout.prop(settings, 'f_RenderInterval')

        layout.label(text="Render Count: "+str(settings.i_RenderCount))
