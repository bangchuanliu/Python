def mod(base, num):
    if base == 0 or base == 1:
        return "Error: base should not be zero or one"
    return num % base


def main():
    base1, num1, base2, num2 = 3, 10, 5, 7
    mod1 = mod(base1, num1)
    mod2 = mod(base2, num2)
    print(mod1, mod2)


if __name__ == "__main__":
    main()
