from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("Hello, world Minecraft!")
pos_x = mc.player.getTilePos().x
pos_y = mc.player.getTilePos().y
pos_z = mc.player.getTilePos().z
mc.postToChat("my pos x= " + str(pos_x))
mc.postToChat("my pos y= " + str(pos_y))
mc.postToChat("my pos z= " + str(pos_z))
mc.postToChat("Hello, my block is " + str(mc.getBlock(pos_x,pos_y-1,pos_z)))
mc.postToChat("Hello, world Minecraft! = " + str(mc.getBlock(-65,70,196)))
