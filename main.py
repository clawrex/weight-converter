weight = int(input("weight: "))

tell_ur_weight = input("(k)g or (L)bs: ")
if tell_ur_weight.upper() == "L":
     converted = weight * 0.45
     print(converted)
else:
 if tell_ur_weight.upper() == "K":
     converted = weight / 0.45
     print(converted)
