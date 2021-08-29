frequenza = float(input())




if frequenza < 3*10**9:
    print("Radiowawes")
elif 3*10**9 >= frequenza < 3*10**12:
    print("Microwaves")
elif 3*10**12 >= frequenza < 4.3*10**14:
    print("Infrered Light")
elif 4.3*10**14 >= frequenza < 7.5*10**14:
    print("Visible Light")
elif 7.5*10**14 >= frequenza < 3*10**17:
    print("Ultraviolet Light")
elif 3*10**17 >= frequenza <= 3*10**19:
    print("X-rays")
elif  frequenza >= 3*10**17:
    print("Gamma Rays")

