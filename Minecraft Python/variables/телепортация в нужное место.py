from mcpi.minecraft import Minecraft
mc = Minecraft.create()

points = int (input("Введите количество очков: "))
if points >2 and points <4:
    mc.player.setPos(1694, 67, 376)
elif points >4 and points <6:
    mc.player.setPos(1726, 64, 401)
elif points >6 and points <8:
    mc.player.setPos()
elif points <= 2:
    mc.player.setPos(1710, 63, 430)
 
