from mcpi.minecraft import Minecraft
mc = Minecraft.create()

sssr = "Д"
xxxs = input ("Вы хотите защитить блоки от разрушений?")
if sssr == xxxs:
    mc.setting("world_immutable",True)
    mc. postToChat("Защита от разрушений выключена")
else:
    mc.setting("world_immutable",False)
    mc. postToChat("Защита от разрушений выключена")
