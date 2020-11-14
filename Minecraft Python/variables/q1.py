from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
width = 40
height = 40
length = 40

blockType = 0

mc.setBlocks(x, y, z, x + width, y + height , z + length, blockType)
