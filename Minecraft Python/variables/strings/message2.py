from mcpi.minecraft import Minecraft
mc = Minecraft.create()
username = input ("Enter the user name:")
message = input ("Enter the message: ")
mc.postToChat(username + ": " + message)
