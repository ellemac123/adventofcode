

if __name__ == "__main__":
    input = []
    with open('input.txt', 'r') as infile:
        for i in infile.readlines():
            input.append(list(i.strip()))

    print(input)