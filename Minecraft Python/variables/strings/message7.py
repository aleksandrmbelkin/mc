from mcpi.minecraft import Minecraft
mc = Minecraft.create()


pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = 9
blockType2 = 9 
blokType = mc.getBlock(x,y,z)
mc.postToChat(blockType == 9)


if blockType == 9 and blockType2 == 9:
    mc.postToChat('True')
else:
    mc.postToChat('False')
