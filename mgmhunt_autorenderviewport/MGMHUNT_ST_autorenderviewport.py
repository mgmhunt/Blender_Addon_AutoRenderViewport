import bpy


class MGMHUNT_ST_autorenderviewport(bpy.types.PropertyGroup):

    def executeOperator(self, context):
        if self.b_autorender:
            bpy.ops.mgmhunt.autorenderviewport('EXEC_DEFAULT')
        return

    b_autorender: bpy.props.BoolProperty(
        name="Auto Render",
        description="Automatically render to file after a viewport change.",
        default=False,
        update=executeOperator
    )

    f_RenderInterval: bpy.props.FloatProperty(
        name="Interval (sec)",
        description="Time between renders.",
        default=1,
        min=.1,
        soft_min=1,
        soft_max=30
    )

    i_RenderCount: bpy.props.IntProperty(
        name="Render Count",
        description="Number of renders.",
        default=0
    )
