AGILE = "Agile"
SOFTWARE = "Software"
TESTING = "Testing"


def printing_words():
    try:
        num = int(input())
        while num >= 1:
            if num % 3 == 0 and num % 5 == 0:
                print(TESTING)
            elif num % 3 == 0:
                print(SOFTWARE)
            elif num % 5 == 0:
                print(AGILE)
            else:
                print(num)
            num -= 1
    except ValueError:
        print("Вы ввели не число")


if __name__ == '__main__':
    printing_words()