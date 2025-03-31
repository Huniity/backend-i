def main():
    my_list: list[float] = [...]
    my_set: set[float] = [...]
    my_tuple: tuple[float] = (...) # not permutable
    my_dict: dict[str,float] = {'a': 1.0}

    def add_to_list(value):
        my_list.append(value)

    my_tuple.__add__(2)
    add_to_list(2)
    print(my_tuple)

# if __name__ == "__main__":
#     main()

    lista = []

    for i in range(10):
            lista.append(i)
    
    nova_lista = [number for number in range(10)]
    nova_lista_even = [number for number in range(10) if number % 2 is 0]
    nova_tuple_even = (number for number in range(10) if number % 2 is 0)
    nova_set_even = {number for number in range(10) if number % 2 is 0}
    nova_dic_even = {index: number for index, number in range(10) if number % 2 is 0}


    print(lista)
    print(nova_lista)