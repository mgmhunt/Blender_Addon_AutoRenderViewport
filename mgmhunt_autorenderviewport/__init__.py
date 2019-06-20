# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "AutoRenderViewport",
    "author" : "mgmhunt",
    "description" : "ALPHA USE AT OWN RISK - Will save the viewport to a file (defined in render settings), every 'interval' when the Auto Render button is toggled on. Turn it off to change the frequency and then turn it back on again. Manual Render will trigger a single render.",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View 3D > View > Render Viewport",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )

from . MGMHUNT_ST_autorenderviewport     import MGMHUNT_ST_autorenderviewport
from . MGMHUNT_PT_autorenderviewport     import MGMHUNT_PT_autorenderviewport
from . MGMHUNT_OT_autorenderviewport     import MGMHUNT_OT_autorenderviewport

# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    MGMHUNT_ST_autorenderviewport,
    MGMHUNT_PT_autorenderviewport,
    MGMHUNT_OT_autorenderviewport
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.RenderViewportSettings = PointerProperty(type=MGMHUNT_ST_autorenderviewport)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.RenderViewportSettings