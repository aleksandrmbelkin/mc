from mcpi.minecraft import Minecraft
mc = Minecraft.create()
blokType = 1
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
blockType = int(input("Ведите тип блока:"))
mc.setBlock(x, y, z, blockType)
