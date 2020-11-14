from mcpi.minecraft import Minecraft
mc = Minecraft.create()

baildX = 399
baildY = 105
baildZ = 273

width = 10
height = 5
length = 6


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
inside =  baildX < x < baildX + width and baildY < y < baildY + height and baildZ < z < baildZ + length
