from math import *
from tkinter import *

root=Tk()
root.geometry("626x320")
root.resizable(0,0)
root.title("Ecuaciones de primer grado")

#-------------FUNCIONES-------------

def resultado():
	
	ValueA=ValorAusuario.get()
	ValueB=ValorBusuario.get()
	
	if float(ValueA)!=0:
		
		try:
			ResultadoFinal["text"]= (-float(ValueA)/float(ValueB))
			
		
		except:
			ZeroDivisionError
			ResultadoFinal["text"]= ("0")

			
	else:
		if float(ValueA)==0 and float(ValueB)!= 0:
			ResultadoFinal["text"]="La ecuación no tiene solución"

		else:

			ResultadoFinal["text"]="La ecuacion tiene infinitas soluciones"

def reiniciar():
	ValorAusuario.delete(0, "end")
	ValorBusuario.delete(0, "end")
	ResultadoFinal["text"]="Aquí se mostrará el resultado."	
	

#--------------INTERFAZ-------------


Explicacion=Label(root, text="Utiliza este formato: aX+b=0")
Explicacion.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
Explicacion.config( fg="red", bg="black", font=("", 36))

ValorA=Label(root, text="Dime el valor de a: ")
ValorA.grid(row=1, column=1, padx=10, pady=10)
ValorA.config(font=("", 18))

ValorB=Label(root, text="Dime el valor de b: ")
ValorB.grid(row=2, column=1, padx=10, pady=10)
ValorB.config(font=("", 18))

Resultado=Button(root, text="Resolver ecuación", command=resultado, borderwidth=5)
Resultado.grid(row=4, column=1, padx=10, pady=10, sticky="w")
Resultado.config(font=("", 18))

ResultadoFinal=Label(root, text="Aquí se mostrará el resultado")
ResultadoFinal.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
ResultadoFinal.config(font=("", 18))

ValorAusuario=Entry(root)
ValorAusuario.insert(0,"")
ValorAusuario.grid(row=1, column=2, pady=10, padx=10)
ValorAusuario.config(font=("", 18))

ValorBusuario=Entry(root)
ValorBusuario.grid(row=2, column=2, pady=10, padx=10)
ValorBusuario.config(font=("", 18))

Reiniciar=Button(root, text="Borrar todo.", command=lambda:reiniciar(), borderwidth=5)
Reiniciar.grid(row=4, column=2, padx=10, pady=10, sticky="e")
Reiniciar.config(font=("", 18))

root.mainloop()


#-------------- ECUACION-----------







