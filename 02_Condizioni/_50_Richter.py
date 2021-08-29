potenza = float(input())



if potenza < 2.0:
    print("micro")
elif 2.0 >= potenza < 3:
    print("very minor")
elif 3.0 >= potenza < 4:
    print("minor")
elif 4.0 >= potenza < 5:
    print("Light")
elif 5.0 >= potenza < 6:
    print("Moderate")
elif 6.0 >= potenza < 7:
    print("Strong")
elif 7.0 >= potenza < 8:
    print("Major")
elif 8.0 >= potenza < 10:
    print("Great")
elif potenza >10:
    print("meteoric")