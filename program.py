def maxim(a,b,c):
    lista =[a,b,c]
    max=0
    for numar in lista:
        if numar>max:
            max = numar
    return max

def minim(a,b,c):
    lista = [a,b,c]
    min = a
    for numar in lista:
        if numar<min:
            min = numar
    return min

def biggest_div(a,b,c):
    cel_mai_mare_divizor=0
    i=minim(a,b,c)
    while(i>1):
        if(a%i==0 and b%i==0 and c%i==0):
            cel_mai_mare_divizor = i
            break
        i-=1
    if(i<=1):
        cel_mai_mare_divizor = "aceste numere nu au divizoare comune in afara de 1"
        return print(cel_mai_mare_divizor)
    return print("cel mai mare divizor comun a",a,b,"si",c,"este:",i)

def lowest_multiple(a,b,c):
    i=maxim(a,b,c)
    multiplu=0
    found_number = False
    while found_number == False:
        if(i%a==0 and i%b==0 and i%c==0):
            found_number = True
            multiplu = i
        else:
            i+=1
    return print("Cel mai mic multiplu comun a",a,b,"si",c,"este:", i)



try:
    a = int(input("Primul numar: "))
    b = int(input("Al doilea numar: "))
    c = int(input("Al treilea numar: "))

    biggest_div(a,b,c)
    lowest_multiple(a,b,c)
    print("Cel mai mare numar este: ",maxim(a,b,c))
    print("Cel mai mic numar este: ",minim(a,b,c))
except:
    print("Introduceti doar numere intregi! ")
finally:
    print("Program terminat! ")
    leave=input("Printati \"X\" pentru a iesi: ")
    while leave.upper()!="X":
        leave=input("")
    exit()
