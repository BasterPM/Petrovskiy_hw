import time


class SwimmingPool:
    def __init__(self, length: int):
        self.length = '=' * (length//10 - 1)


class Swimmer:
    def __init__(self, speed: int):
        self.speed = speed

    def to_swim(self, pool, distance: int):
        pause = 10 / self.speed
        a = 0
        b = 0
        c = True
        while c:
            if not a == distance:
                while a < distance//10 and b < len(pool.length):
                    time.sleep(pause)
                    print(pool.length[:b] + '*' + pool.length[b:])
                    a += 1
                    b += 1
                while a < distance//10 and b > 0:
                    time.sleep(pause)
                    print(pool.length[:b] + '*' + pool.length[b:])
                    a += 1
                    b -= 1
            else:
                c = False


# pool = SwimmingPool(100)
# swimmer = Swimmer(15)
# swimmer.to_swim(pool, 250)
