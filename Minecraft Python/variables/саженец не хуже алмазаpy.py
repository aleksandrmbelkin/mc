from mcpi.minecraft import Minecraft
mc = Minecraft.create()
almas = 57
sashenes = 6
BlockType = almas
x = 152
y = 73
z = 967
gift = mc.getBlock(x,y,z)
if almas:
    print("yeeeeeees")
elif sashenes:
    print ("seedling is not worse than diamond")
else:
    mc.postToChat("put a gift here: " + str(x) + "," + str(y) + "," + str(z))
