def de_num_romano_a_decimal(num):
    if len(num)==1:
        if num=="I":
            decimal=1
        elif num=="V":
            decimal=5
        elif num=="X":
            decimal=10
        elif num=="L":
            decimal=50
        elif num=="C":
            decimal=100
        elif num=="D":
            decimal=500
        elif num=="M":
            decimal=1000
        return decimal
    elif len(num)==2 and num=="IV":
            decimal=4
            return decimal
    else:
        if num[-1]=="I":
            decimal=1
        elif num[-1]=="V":
            decimal=5
        elif num[-1]=="X":
            decimal=10
        elif num[-1]=="L":
            decimal=50
        elif num[-1]=="C":
            decimal=100
        elif num[-1]=="D":
            decimal=500
        elif num[-1]=="M":
            decimal=1000
            
        return decimal + de_num_romano_a_decimal(num[:-1])

    
funcion=de_num_romano_a_decimal("CXXXXV")
print(f"El numero romano pasado a decimal queda :{funcion}")