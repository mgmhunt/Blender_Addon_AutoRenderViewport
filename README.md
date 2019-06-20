# ALPHA USE AT OWN RISK

# Blender Addon - Auto Render Viewport

(Very alpha (my first Blender program!), hacked together quickly but it semi-works on Mac, Blender 2.80 beta - there are some timers etc that might lock up your system but it seems to run OK at the mo... )

Panel can be found under 3D View > View > Render Viewport

Will save the viewport to a file (defined in render settings), every 'interval' when the Auto Render button is toggled on. Turn it off to change the frequency and then turn it back on again. Manual Render will trigger a single render.

Try TIFF with no compression (and B&W) as a fast file format to save to, to reduce lag.  Can change if basic layout works.

Can use with second monitor to view 'linked' files update quickly while working on layouts in Illustrator or InDesign for example. You'll need to figure out how to switch apps quickly to force a refresh in the 'linked' app, custom shortcuts on the OS could do it, or just click other window and click back.

Maybe someway of communicating via OS Scripting to achieve refresh.

Could assign shortcut key to Manual Render to avoid UI lag.

### Feature Ideas
- Multiple files, from multiple views
- Render from cameras only (or option View or Camera)
- Different file format and rendering settings then the actual render (although having the same settings pixel-wise makes sure render will fit external layout mockup?)

### Code Issues
- Better handling of Timers... not sure how to manage the memory objects
- Write to tmp file and then overwrite the main file (to avoid linked programs trying to read while Blender is writing)
- Much error checking etc!!