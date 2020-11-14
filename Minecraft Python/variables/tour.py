from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x = 46.566
y = 91.00000
z = 101.300
mc.player.setTilePos(x, y, z)
time.sleep(15)
x = 100.526
y = 563.117
z = 1000.432
mc.player.setTilePos(x, y, z)
time.sleep(36)
x = 46.566
y = 91.00000
z = 101.300
mc.player.setTilePos(x, y, z)
