from mcpi.minecraft import Minecraft
mc = Minecraft.create()
try:
    noOfSunglasses = int(input("Введите тип блока."))
except:
   print("Неверно.Введите число.")

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
blockType = (noOfSunglasses)
print("Неверно.Введите число.")
mc.setBlock(x, y, z, blockType)

