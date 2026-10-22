capital =0
tasa_anual=0
m=0

while True:
    capital= float(input("Digite el Capital: "))
    tasa_anual = float(input("Digite la tasa de interes anual: "))
    m = int(input("Digite la cantidad de años: "))
   
    
    
    if capital >= 0 and 0 < tasa_anual < 100 and m > 0:
       break

for i in range(1,m+1):    
    capital=capital*(1+tasa_anual/100)
    print("Año ", i, ": ",capital)
    

print("Saldo final: ",capital)