from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("Hello, world Minecraft!")
mc.postToChat("my pos x= " + str(mc.player.getTilePos().x))
mc.postToChat("my pos y= " + str(mc.player.getTilePos().y))
mc.postToChat("my pos z= " + str(mc.player.getTilePos().z))
mc.postToChat("Hello, world Minecraft!")
mc.postToChat("Hello, world Minecraft!")
