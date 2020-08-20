from tkinter import Tk, Label, Button,  Spinbox
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
class VentanaEjemplo:
    def __init__(self, master):
        self.master = master
        master.title("Distribucion Binomial")
        self.etiqueta = Label(master, text="Numero de exitos n:")
        self.etiqueta.pack()
        self.n= Spinbox(master, from_=0, to=100)
        self.n.pack()
        self.etiqueta = Label(master, text="Probabilidad de exito p:")
        self.etiqueta.pack()
        self.p= Spinbox(master, from_=0.1, to=10)
        self.p.pack()
        self.etiqueta = Label(master, text="Maximo valor de x:")
        self.etiqueta.pack()
        self.x= Spinbox(master, from_=0.01, to=1)
        self.x.pack()
        self.botonSaludo = Button(master, text="Graficar", command=self.Graficar)
        self.botonSaludo.pack()
        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()
    def Graficar(self):
        N, P = np.int(self.n.get()), np.float(self.p.get()) # parametros de forma 
        binomial = stats.binom(N, P) # Distribución
        X = np.arange(binomial.ppf(0.01),
        binomial.ppf(np.float(self.x.get())))
        fmp = binomial.pmf(X) # Función de Masa de Probabilidad
        plt.plot(X, fmp, '--')
        plt.vlines(X, 0, fmp, colors='b', lw=5, alpha=0.5)
        plt.title('Distribución Binomial')
        plt.ylabel('probabilidad')
        plt.xlabel('valores')
        plt.show()
root = Tk()
miVentana = VentanaEjemplo(root)
root.mainloop()