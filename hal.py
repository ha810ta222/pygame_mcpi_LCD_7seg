from mcpi.minecraft import Minecraft
mc = Minecraft.create()

X = 0
Y = 6
A = (0, 1, 1, 1, 0,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 0,
     1, 1, 1, 1, 0,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     0, 1, 1, 1, 0)
for i in range(7):
    for n in range(5):
        S = n + i * 5
        if A[S] == 1:
            W = 41
        else:
            W = 42
        mc.setBlock(X, Y, 0, W, 0)
        X += 1
    X = 0
    Y -= 1

X = 6
Y = 6
B = (0, 0, 0, 1, 0,
     0, 0, 1, 1, 0,
     0, 1, 0, 1, 0,
     1, 0, 0, 1, 0,
     1, 1, 1, 1, 1,
     0, 0, 0, 1, 0,
     0, 0, 0, 1, 0)
for i in range(7):
    for n in range(5):
        S = n + i * 5
        if B[S] == 0:
            T = 42
        else:
            T = 41
        mc.setBlock(X + n, Y - i, 0, T, 0)
