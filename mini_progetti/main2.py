if __name__ == "__main__":
    # LITERAL VARIABLES:
    a = 20
    print("ID", id(a)) # Callble Objects
    print("TYPE", type(a)) # Callble Objects

    # [ESERCITAZIONE] => Tipi numerici 
    x = 100
    print(type(x))
    y = 0b1100100
    print(type(y))
    w = 975.0
    print(type(w))
    
    # [ESERCITAZIONE] => Tuple
    t1 = tuple(1,2)
    t2 = tuple(3,4)
    my_list = [t1, t2]
    my_list.append((5,6))

    # [ESERCITAZIONE] => Dizionari
    myDic = dict({10: "a", 20: "b"})
    mySmallDic = dict({30: "c"})
    l1 = myDic.items()
    myBigDic = dict(l1)
    exit(0)