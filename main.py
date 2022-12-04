def main():
    n = int(input('Введите количество элементов: '))
    arr = []
    for _ in range(n):
        inp = input(f'Введите значение: ')
        arr.append(inp)
    arr_res = []
    for st in arr:
        if len(st) <= 3:
            arr_res.append(st)
    if arr_res:
        print(arr_res)
    else:
        print('Нет элементов')


if __name__ == '__main__':
    main()
