from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 1730
y = 56
z = 397
gift= mc.getBlock(x,y,z)
print (gift)

if gift != 0:
    if gift == 38:
        print ("cheng bloks")
        mc.setBlocks(1729,55,396,1729,56,396,0)
    else:
        mc.setBlocks(1731,54,396,1731,54,396,10)
else:
    print ("Поставте блок на стамент")
    mc.setBlocks(1729,55,396,1729,56,396,1)
    




        











