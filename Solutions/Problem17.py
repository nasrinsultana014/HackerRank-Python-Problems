def mutate_string(string, position, character):
    characters = list(string)
    characters[position] = character
    return "".join(characters)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)