if __name__ == '__main__':
    
    number_of_stones = int(raw_input())
    element = []
    for i in range(number_of_stones):
        element.append(raw_input())
        
    element_set = []
    for i in element:
        item = set(i)
        element_set.append(item)
        
    gemstones = element_set[0]
    for i in element_set:
        gemstones = gemstones.intersection(i)
        
    print len(gemstones)
