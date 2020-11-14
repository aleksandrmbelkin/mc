from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 29
y = 111
z = 124
blockTyre = 10
mc.setBlock(x,y,z,blockTyre)
y = y + 1
mc.setBlock(x,y,z,blockTyre)
y = y + 1
mc.setBlock(x,y,z,blockTyre)
y = y + 1
mc.setBlock(x,y,z,blockTyre)
