if __name__ == '__main__':
    
    number_of_tests = int(raw_input())
    
    for _ in range(number_of_tests):
        string1 = raw_input()
        last_letter = string1[0]
        count = 0
        for i in range(1, len(string1)):
            if string1[i] == last_letter:
                count += 1
            else:
                last_letter = string1[i]
        print count 
