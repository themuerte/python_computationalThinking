def divide_element_list(list_1, divider):
    
    
    try:
        return [i / divider for i in list_1]
    except ZeroDivisionError as e:
        print(e)
        return list_1


if __name__ == "__main__":
    
    list_p = list(range(10))
    divider = 3
    print(divide_element_list(list_p, divider))

