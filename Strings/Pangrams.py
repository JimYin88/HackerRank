if __name__ == '__main__':

    A = raw_input().strip().lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = 'pangram'
    for letter in alphabet:
        if letter not in A:
            result = 'not pangram'
            break
    print result
