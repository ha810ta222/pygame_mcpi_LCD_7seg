from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.setBlocks(-127, 0, -127, 127, 64, 127, 0, 0)
mc.setBlocks(-127, -1, -127, 127, -1, 127, 2, 0)
mc.setBlocks(-127, -2, -127, 127, -64, 127, 1, 0)
