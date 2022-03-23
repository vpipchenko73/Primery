def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

array = list(map(int, input('vvedi massiv chisel->').split()))
element = int(input('vvedi iscomyy element ->'))

print(find(array, element))