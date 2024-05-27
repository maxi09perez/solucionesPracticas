Algoritmo sin_titulo
	Escribir "Ingrese un numero del 1 al 10"
	Leer num
	Definir cont Como Entero
	cont=1
	Si num > 0 Y num <= 10 Entonces
		Mientras cont<=10 Hacer
			Escribir num,"x",cont,"=",num*cont
			cont = cont + 1
		Fin Mientras
	SiNo
		Escribir "Numero incorrecto"
	Fin Si
	Escribir "Ingrese otro numero"
	Leer num2
	Si num2 > 0 Y num2 <= 10 Entonces
		Para i<-1 Hasta 10 Hacer
			Escribir num2,"x",i,"=",num2*i
		Fin Para
	SiNo
		Escribir "Numero incorrecto"
	Fin Si
FinAlgoritmo
