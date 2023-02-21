a = float(input("digite a: "))
b = float(input("digite b: "))
c = float(input("digite c: "))
d = float(input("digite d: "))
e = float(input("digite e: "))
if b==0 and a==0 or c==0:
    print("es una parabola")
if b==0 and a==c:
    print("es una circunferencia")
if b==0 and d==0:
    print("el centro de la conica esta sobre el eje Y")
if b==0 and e==0:
    print("el centro de la conica esta sobre el eje x")
if b==0 and a>0 and c>0:
    print("es una elipse")
if b==0 and a<0 and c<0:
    print("es una elipse")   
if b==0 and a>0 and c<0:
    print("es una hiperbola")
if b==0 and a<0 and c>0:
    print("es una hiperbole")
print("hallaste la conica")