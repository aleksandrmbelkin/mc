from mcpi.minecraft import Minecraft
mc = Minecraft.create()


pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z


highesBlockY = mc.getHeight(x,z)
mc.postToChat(highesBlockY)
