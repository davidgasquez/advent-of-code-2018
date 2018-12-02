with open("input.txt") as f:
    numbers = f.readlines()


def search_frequency(number_list):
    seen = set()
    result = 0

    while True:
        for i in number_list:
            result += int(i)
            if result in seen:
                return result

            seen.add(result)


part_1 = sum(map(int, numbers))
part_2 = search_frequency(numbers)

print(part_1)
print(part_2)
