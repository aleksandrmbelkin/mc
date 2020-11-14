from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
height = 10
blokType = 46
sidiheight = height
mc.setBlocks(x + 1, y, z + 1, x + 3, y + sidiheight - 1, z + 3, blokType)


pointheight = 20
mc.setBlocks(x + 2, y, z + 2, x + 2, y + pointheight - 1, z + 2, blokType)


baseheight = 5
mc.setBlocks(x, y, z, x + 4, y + baseheight - 1, z + 4, blokType)
