import random
import os
import math
from fractions import Fraction

while True:

    print ("Elegir una de las siguientes opciones: ")

    print("----------------------------------------------")
    msj= "1. Rectas paralela y perpendicular a una dada "
    print (msj)
    msj= "2. Análisis de una función lineal"
    print (msj)
    msj= "3. Análisis de una función cuadrática"
    print (msj)
    msj= "4. Sucesiones Aritméticas"
    print (msj)
    msj= "5. Sucesiones Geométricas"
    print(msj)
    print("----------------------------------------------")
    numero= int (input())
    os.system ("cls")

    # coeficiente principal =a
    # coeficiente lineal =b
    # termino independiente =c

    a=0 
    c=0
    b=0



    if (numero==1):

        print("Dos rectas son paralelas si tienen la misma pendiente, o inclinacion. Esta es dada por el coeficiente principal.")
        print("Dos rectas son perpendiculares si su pendiente es recíproca y de signo contrario de la pendiente de la otra recta.")
        print("\n")
        
        msj= "Definir el coeficiente principal: "
        print (msj)
        a= Fraction(input())
        
        #El siguiente while es para que el usuario no ingrese el 0
        while (a==0):
            print ("De utilizar el 0, volveria a la funcion constante. Por favor ingrese otro número")
            a= Fraction(input())
        

        msj= "Definir el termino independiente: "
        print (msj)
        c= Fraction(input())

        c1= random.randint(1,20)
        c2= random.randint(21,40)
        c3= random.randint(41,60)


        while(c1==c):
            c1= random.randint(1,20)
        while(c2==c):
            c2= random.randint(21,40)
        while(c3==c):
            c3= random.randint(41,60)


        msj= "Ecuación: y= " + str(a) + "x + " + str(c)
        print (msj)
        input ()
        os.system("cls")

        print ("1. Paralela:",a,"x +",c1)
        print ("2. Paralela:",a, "x +",c2)
        print ("3. Paralela:",a, "x +",c3)
        print ("1. Perpendicular:",Fraction(-1/a),"+",c1)
        print ("2. Perpendicular:",Fraction(-1/a),"+",c2)
        print ("3. Perpendicular:",Fraction(-1/a),"+",c3)
        


        # Generamos los datos para el grafico
        def f1(x):
            return a*x + c
        
        # Valores del eje x que toma el grafico
        x = range(-100,100)
        
        # Limitar los valores de los ejes.
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        
        # Establecer el color de los ejes.
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")


        # Creamos el grafico
        plt.plot(x, [f1(i) for i in x])
        plt.show()

        print("\n")

    elif (numero==2):

        msj= "Definir el coeficiente principal: "
        print (msj)
        a= Fraction(input())
        
        #El siguiente while es para que el usuario no ingrese el 0
        while (a==0):
            print ("De utilizar el 0, volveria a la funcion constante. Por favor ingrese otro número")
            a= Fraction(input())
        

        msj= "Definir el termino independiente: "
        print (msj)
        c= Fraction(input())
        
        msj= "Ecuación: y= " + str(a) + "x + " + str(c)
        print (msj)
        input ()
        os.system("cls")

        #Corte con el eje y
        print("La recta conrta al eje y en: " + str(c))

        #Corte con el eje x
        corteX= -c/a

        print("La recta corta al eje x en: " + str(corteX))

        if (a<0):
            print("La recta es decreciente")
        else:
            print("La recta es creciente")
            
        print("\n")

    elif (numero==3):
        #Eje de simetria
        xv=0
        yv=0

        msj= "Definir el coeficiente principal: "
        print (msj)
        a= Fraction(input())
        msj= "Definir el termino lineal: "
        print (msj)
        b= Fraction(input())
        msj= "Definir el termino independiente: "
        print (msj)
        c= Fraction(input())
        #El siguiente while es para que el usuario no ingrese el 0
        while (a==0):
            print ("De utilizar el 0, volveria a la funcion lineal. Por favor ingrese otro número")
            a= Fraction(input())
        
        
        msj= "Ecuación: y= " + str(a) + "x^2 + " + str(b) + "x + " + str(c)
        print (msj)
        input ()
        os.system("cls")


        #Determinante
        d= (b**2 - (4*a*c)) 
        if (d<0):
            print("Las raices no tienen solucion real. Ingrese una nueva ecuación: \n")
            
            msj= "Definir el coeficiente principal: "
            print (msj)
            a= Fraction(input())
            msj= "Definir el termino lineal: "
            print (msj)
            b= Fraction(input())
            msj= "Definir el termino independiente: "
            print (msj)
            c= Fraction(input())
            #El siguiente while es para que el usuario no ingrese el 0
            while (a==0):
                print ("De utilizar el 0, volveria a la funcion lineal. Por favor ingrese otro número")
                a= Fraction(input())
            
            
            msj= "Ecuación: y= " + str(a) + "x^2 + " + str(b) + "x + " + str(c)
            print (msj)
            input ()
            os.system("cls")
      
        elif (d==0):
            print("Las raices tienen multiplicidad doble")
            #Corte con el eje y
            print("La recta corta al eje y en: " + str(c))

            #Corte con el eje x
            if (b == 0):
                print = "La funcion no toca al eje de las x"
            else:
                raiz1 = (-b + (d)**0.5)/ (2*a)
                raiz2 = (-b - (d)**0.5)/ (2*a)

                print("La recta corta al eje x en: " + str(raiz1) + " y en " + str(raiz2))


            xv = -(b/2*a)
            yv = a*(xv)**2+ b*xv+ c

            print("Coordenadas del eje de simetria: (" + str(xv) + "," +str(yv) + ")" )

            if (a<0):
                #Ramas hacia abajo
                print("La funcion es decreciente en el intervalo (-∞," + str(xv) + ") y creciente en el intervalo (" + str(xv) + ",∞")
                print("La parabola tiene concavidad negativa o hacia abajo")

            else:
                #Ramas hacia arriba
                print("La funcion es creciente en el intervalo (-∞," + str(xv) + ") y decreciente en el intervalo (" + str(xv) + ",∞")
                print("La parabola tiene concavidad positiva o hacia arriba")

        else:

            #Corte con el eje y
            print("La recta corta al eje y en: " + str(c))

            #Corte con el eje x
            if (b == 0):
                print = "La funcion no toca al eje de las x"
            else:
                raiz1 = (-b + (d)**0.5)/ (2*a)
                raiz2 = (-b - (d)**0.5)/ (2*a)

                print("La recta corta al eje x en: " + str(raiz1) + " y en " + str(raiz2))


            xv = -(b/2*a)
            yv = a*(xv)**2+ b*xv+ c

            print("Coordenadas del eje de simetria: (" + str(xv) + "," +str(yv) + ")" )

            if (a<0):
                #Ramas hacia abajo
                print("La funcion es decreciente en el intervalo (-∞," + str(xv) + ") y creciente en el intervalo (" + str(xv) + ",∞")
                print("La parabola tiene concavidad negativa o hacia abajo")

            else:
                #Ramas hacia arriba
                print("La funcion es creciente en el intervalo (-∞," + str(xv) + ") y decreciente en el intervalo (" + str(xv) + ",∞")
                print("La parabola tiene concavidad positiva o hacia arriba")

        print("\n")
    elif (numero==4):
        print("Una sucesión es un conjunto de números ordenados. Cada número ocupa una sucesión y recibe el nombre de término.")
        print("Sucesión Aritmetica: cuando cada término se obtiene sumando un número al término precedente.")
        print("\n")
        
        primer_T= Fraction(input("Definir el primer término de la sucesión: "))
        diferencia= Fraction(input("Ingrese la diferencia que desea que tenga la sucesión: "))
        cant_terminos= int(input("Ingrese la cantidad de términos que desea conocer: "))
    
        while (cant_terminos<=4):
            print("La cantidad de términos debe ser mayor a 5, ingrese nuevamente: ")
            cant_terminos= int(input())
        
        print("\n")
        cont= 0
        print ("Llamaremos A a su suceción \n")
        if diferencia<0:
            print("Su suceción es decreciente ")
        elif diferencia==0:
            print("¡Hey! Tu sucesión es siempre el mismo número" )
        else:
            print("Su suceción es creciente ")
        print("\n")
        while(cont<cant_terminos):
            
            if cont==0:
                print("A= {",primer_T,"; ", end="")
                cont = cont + 1

            else:
                primer_T += diferencia
                print(primer_T, "; ", end="")

                cont = cont + 1
            if cont == cant_terminos -1:
                primer_T += diferencia
                print(primer_T, "}")
                break
            
        print("\n")


    elif (numero==5):
        print("Una sucesión es un conjunto de números ordenados. Cada número ocupa una sucesión y recibe el nombre de término.")
        print("Sucesión Geometrica: cuando cada término a sub n se obtiene multiplicando al término anterior.")
        print("\n")

        primer_T= Fraction(input("Definir el primer término de la sucesión: "))
        razon= Fraction(input("Ingrese la razón contenida en los terminos: "))
        cant_terminos= int(input("Ingrese la cantidad de términos que desea conocer: "))

        while (cant_terminos<=4):
            print("La cantidad de términos debe ser mayor a 5, ingrese nuevamente: ")
            cant_terminos= int(input())
        while (razon == 0 and primer_T == 0):
            print("No se puede elevar cero a la cero, ingrese nuevamente")
            primer_T= Fraction(input("Ingrese el primer término: "))
            razon= Fraction(input("Ingrese la razón: "))
        
        print("\n")
        cont= 0
        sucesion= primer_T * razon 

        while(cont<cant_terminos):

            if cont==0:
                print("a",cont+1 ,"=" ,primer_T)
                cont = cont + 1
            elif cont==1:
                print("a",cont ,"=" ,sucesion)
                cont = cont + 1
            elif cont==2:
                sucesion= sucesion * razon
                segundo_T= sucesion
                print("a",cont+1 ,"=" ,sucesion)
                cont = cont + 1
            else:
                sucesion= sucesion * razon
                print("a",cont+1,"=", sucesion)
                cont = cont + 1

        print("\n")
        
        if primer_T<segundo_T and primer_T<sucesion:
            print("La sucesión es creciente")
        if primer_T>segundo_T and primer_T>sucesion:
            print("La sucesión es decreciente")
        if primer_T<segundo_T and segundo_T>sucesion:
            print("La sucesión es alternada")
        if primer_T>segundo_T and segundo_T<sucesion:
            print("La sucesión es alternada")

        print("\n")
    else:
        print("Opcion invalida.\n Intente nuevamente: ")    
        print("\n")
    



        