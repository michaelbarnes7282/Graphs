arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

def myFun(s):
    # print(s)
    # print(s[(len(s) - 1) // 2])
    length = len(s)
    middle = (length - 1) // 2
    if length % 2 == 0:
        return s[middle + 1]
    return s[middle]
        

arr.sort(key= myFun)
for item in arr:
    print(item)