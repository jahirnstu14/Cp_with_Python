def main():
    bhajjo = input().strip()
    bhajok = int(input().strip())

    bhagshesh = 0

    for char in bhajjo:
        bhagshesh = (bhagshesh * 10 + (ord(char) - ord('0'))) % bhajok

    print(bhagshesh)

if __name__ == "__main__":
    main()
