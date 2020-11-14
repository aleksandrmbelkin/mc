from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

answer = input("Создать кратер? Д/Н")
if answer == 'Д':
    i = 80

    while i > 0:
        pos = mc.player.getPos()
        mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1,
                 pos.x - 1, pos.y - 1, pos.z - 1, 0)
        mc.postToChat("BAH! = " + str(i))
        i = i - 1
else:
    x = 54.566
    y = 91.00000
    z = 889.300
    mc.player.setTilePos(x, y, z)
  
