with open('input.txt', encoding='utf-8') as fptr:
    file = fptr.read()
    temp = file.split('\n')

with open('Pandemic.txt', 'w+') as fptr:
    try:
        for i in temp:
            fptr.write("{}, ".format(i))
        print("Success")
    except:
        pass