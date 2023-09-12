def matematica(a,b):
    
    newMath = a.replace("x",f"({b})")
    newMath = newMath.replace("^","**")
    print(newMath)
    x = int(input("de um valor para x\n"))
    print(newMath)
    print(eval(newMath))
    
print("(use * para multiplicacoes)")
f = input("f(x): ")
g = input("g(x): ")
modo = int(input("Qual operacao deseja fazer?\n1-fog\n2-gof\n3-fof\n4-gog\n"))


if(modo == 1):
    matematica(f,g)
elif(modo == 2):
    matematica(g,f)
elif(modo == 3):
    matematica(f,f)
elif(modo ==4):
    matematica(g,g)
else:
    print("valor nao valido.")
