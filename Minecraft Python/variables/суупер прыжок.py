from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
time.sleep(10)
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
y = y + 10
mc.player.setTilePos(x, y, z)
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
y = y - 11
blokType = 10
mc.setBlock(x, y, z, blokType)
