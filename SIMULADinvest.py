while True:
    print("-----------------------------")
    print("SIMULADOR DE INVESTIMENTO")
    print("Seja bem-vindo(a) ao NicolasBenk  ")
    print("-----------------------------")

    print("Títulos disponíveis para simulação:")

    print("1-Tesouro Prefixado 2024")
    print("2-Tesouro Prefixado 2026")
#escolherinvest
    cliente = input("Qual investimento você gostaria de fazer? 1/2: ")

    if cliente == '1':
        valor_1=int(input("Qual valor você gostaria de investir agora?:"))
        valor_mes=int(input("Qual valor você irá investir mensalmente?:"))
#calc
        valor=(valor_mes*32)+valor_1
        ir=(valor*15)/100
        vir=valor-ir
        b=(valor*1.5)/100
        valor_l=valor*0.1081
        vb=valor+valor_l


        vliq=valor-(vir+b)
#result
        print("-----------------------------")
        print("   RESULTADO DO INVESTIMENTO      ")
        print("-----------------------------")
        print("Valor inicial: ", valor_1)
        print("Aportes de", valor_mes,"R$ por 32 meses")
        print("Valor total investido: ",valor)
        print("-----------------------------")
        print("Valor bruto: ", vb)
        print("I.R.: -", ir)
        print("B3: -",b)
        print("-----------------------------")
        again=str(input("Deseja realizar outra simulação? s/n:"))
#2
    else:
        valor_1= int(input("Qual valor você gostaria de investir agora?: "))
        valor_mes = int(input("Qual valor você irá investir mensalmente?: "))
#calc
        valor=(valor_mes*50)+valor_1
        ir=(valor*15)/100
        vir=valor - ir
        b=(valor*2.5)/100
        vl=valor*0.1081
        vb=valor+vl

        vliq=valor-(vir+b)
#result
        print("-------------------------------")
        print("   RESULTADO DA SIMULAÇÃO      ")
        print("-------------------------------")
        print("Valor inicial: ", valor_1)
        print("Aportes de", valor_mes,"R$ por 50 meses")
        print("Valor total investido: ",valor)
        print("-------------------------------")
        print("Valor bruto: ", vb)
        print("I.R.: -",ir)
        print("B3: -",b)
        print("-------------------------------")
#opti
        again=str(input("Deseja realizar outra simulação? s/n: "))

        if again== 'n':
          break
#eeeeeeeeeeeeeeeeee:D
print("Fin")