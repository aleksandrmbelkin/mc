from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import math
x = 180
y =60
z = 1189
melon = 103
blockType = mc.getBlock(x, y, z)

if not melon == blockType:
    mc.postToChat("Нужно раздобыть еду: " + str(blockType))

