from bge import logic, render

scene = logic.getCurrentScene()
camList = scene.cameras
print(camList)
cont = logic.getCurrentController()
own = cont.owner

# Main cameras
camn = camList['NorthCamera_3']
cams = camList['SouthCamera_3']
camw = camList['WestCamera_3']
came = camList['EastCamera_3']

a = render.getWindowWidth()
b = render.getWindowHeight()

x = int((a - b) / 2)
y = int(b / 4)
z = int(b / 2)

# Set viewports
camn.setViewport(x + y, y + z, x + y + z, b)
cams.setViewport(x + y, 0, x + y + z, y)
camw.setViewport(x + y + z, y, x + 2 * y + z, y + z)
came.setViewport(x, y, x + y, y + z)
#"""

# Enable all viewports
for cam in [camn, cams, camw, came]:
    cam.useViewport = True

camn.useViewport = True
cams.useViewport = True
camw.useViewport = True
came.useViewport = True