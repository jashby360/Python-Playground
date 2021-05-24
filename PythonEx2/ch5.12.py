line = 0
for i in range(100, 1000):
    if (i % 5) == 0 and (i % 6) == 0:
        line += 1
        print(i, end=(" " if line < 10 else "\n"))
        if line == 10:
            line = 0
