# python3

#Rihards_Gedrovicis_221RDC023



def read_input():
    user_input = input()
    pattern = ""
    text = ""

    if "F" in user_input:
        file = open("./tests/06", "r")
        user_input = file.read()
        user_input = user_input.split('\n')
        pattern = user_input[0]
        text = user_input[1]

    elif "I" in user_input:
        pattern = input()
        text = input()

    pattern = pattern.strip()
    text = text.strip()
    return (pattern, text)

def print_occurrences(occurrences):
    print(' '.join(map(str, occurrences)))

def get_occurrences(pattern, text):
    indices = []
    for i in range(len(text)):
        if text[i] == pattern[0] and len(pattern) + i <= len(text):
            found = True
            for j in range(len(pattern)):
                if text[i+j] != pattern[j]:
                    found = False
            if found:
                indices.append(i)
    return indices

if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
