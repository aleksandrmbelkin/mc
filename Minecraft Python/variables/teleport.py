from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
mc.player.setTilePos(x, y, z)
x = x + random .randint(-1000, 1000)
y = y + random.randint(-10, 200)
z = z + random.randint(-1000, 1000)
mc.player.setTilePos(x, y, z)
