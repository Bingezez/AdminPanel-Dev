from random import randint


def random_code():
    return int(''.join([str(randint(0, 999)).zfill(3) for _ in range(2)]))


if __name__ == '__main__':
    pass
