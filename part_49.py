def wrap(string, max_width):
    sr = ''''''  
    count = 0
    for i in string:
        if count == max_width:
            sr += '\n'
            count = 0
        sr = sr + i
        count += 1
    return  sr     




if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
