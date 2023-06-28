# Titulo del programa

print("*"*20)
print("calculadora")
print("*"*20)

 # Solicitar datos por consola

numero1 = float(input("introducir el primer numero:"))
numero2 = float(input("introducir el segundo numero:"))

# Imprimir la operatoria

print("la suma es:", numero1+numero2)
print("la resta es:", numero1-numero2)
print("la multiplicacion es:", numero1*numero2)
print("la division es:", numero1/numero2)

# Este input mantiene abierto el programa

input()

if __name__ == '__main__':
	sys.exit(main())