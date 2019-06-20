import bpy


class MGMHUNT_OT_autorenderviewport(bpy.types.Operator):
    bl_idname = "mgmhunt.autorenderviewport"
    bl_label = "Operator to Render 3D viewport to file"
    bl_description = "Operator to render viewport using OpenGL to file"

    timer = None
    timerExists = False
    handlerExists = False
    b_manualRender: bpy.props.BoolProperty(default=False)

    def render(self, context):
        context.scene.RenderViewportSettings.i_RenderCount += 1
        context.area.tag_redraw()
        print("Render Number " +
              str(context.scene.RenderViewportSettings.i_RenderCount))

        bpy.ops.render.opengl(write_still=True, view_context=True)

    def execute(self, context):
        print("Execute...")

        if self.b_manualRender == True:
            print("Manual render...")
            self.render(context)
            self.b_manualRender = False
            return {'FINISHED'}

        autorender = context.scene.RenderViewportSettings.b_autorender
        if autorender:
            if not self.timerExists:
                print("No timer. Creating one...")

                self.timer = context.window_manager.event_timer_add(context.scene.RenderViewportSettings.f_RenderInterval,
                                                                    window=context.window)
                print("Timer created.")
                self.timerExists = True

                if not self.handlerExists:
                    context.window_manager.modal_handler_add(self)
                    self.handlerExists = True
                    print("Handler created.")

                return {'RUNNING_MODAL'}

        else:
            if self.timerExists:
                print("Auto Render off, removing timer.")
                context.window_manager.event_timer_remove(self.timerExists)
                self.timerExists = False

        return {'FINISHED'}

    def modal(self, context, event):
        if event.type == "TIMER" and not self.b_manualRender:
            autorender = context.scene.RenderViewportSettings.b_autorender
            print("Modal timer handler...")
            if not autorender and self.timerExists:
                print("Auto Render off, remove timer.")
                context.window_manager.event_timer_remove(self.timer)
                self.timerExists = False
                return {'CANCELLED'}

            print("Auto render...")
            self.render(context)
            return {'PASS_THROUGH'}

        return {'PASS_THROUGH'}
