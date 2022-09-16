def is_prime(n: int) -> bool:
    if n % 2 != 0:
        return True
    else:
        return False


def run():
    print(is_prime("5"))


if __name__ == '__main__':
    run()
