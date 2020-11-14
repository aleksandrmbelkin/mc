from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


x = 0
y = 0
z = 0


mc. player.setTilePos(x,y,z)


pos1 = mc.player.getPos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z


time.sleep(10)


pos2 = mc.player.getPos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z


xDistance = x2-x1
yDistance = y1-y2
zDistance = z1-z2


mc.postToChat(" " +  str(xDistance) + " " + str(yDistance) + " " + str(zDistance))
