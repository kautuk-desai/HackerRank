from collections import Counter as counter


def main():
    m, n = map(int, input().strip().split(' '))
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if answer:
        print("Yes")
    else:
        print("No")


def ransom_note(magazine, ransom):
    if len(ransom) > len(magazine):
        return False

    magazine_dict = counter(magazine)
    ransom_dict = counter(ransom)

    for key, value in ransom_dict.items():
        if key not in magazine_dict:
            return False
        elif value > magazine_dict[key]:
            return False

    return True


if __name__ == '__main__':
    main();
