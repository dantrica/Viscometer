#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk

import tkMessageBox 

class Prot1:
    def __init__(self):
        self.viscosidad = 0
        self.window = Tk()
        self.window.title("Honey tester")
        self.window.resizable()
        self.window.configure(background= 'white')
        self.window.iconbitmap("Images/Icon.ico")
        

        menuBar = Menu(self.window)
        self.window.config(menu = menuBar)
        Ayuda = Menu(menuBar, tearoff = 0)
        Method = Menu(menuBar, tearoff = 0)
        But = Menu(menuBar, tearoff = 0)
        menuBar.add_cascade(label = "Help", menu = Ayuda)
        Ayuda.add_cascade(label = "Information", menu = Method)
        Method.add_command(label = "Process", command = self.Proc)
        Method.add_cascade(label = "Button", menu = But)
        But.add_command(label = "Time", command = self.l1)
        But.add_command(label = "Density of honey", command = self.l2)
        But.add_command(label = "Density of the sphere", command = self.l3)
        But.add_command(label = "Choose the sphere constant ", command = self.l4)
        But.add_command(label = "Calculate", command = self.l5)     
        
        frame2 = Frame(self.window, bg = "white")
        frame2.pack(side = LEFT)
        frame0 = Frame(self.window , bg = "white")
        frame0.pack()
        frame1 = Frame(self.window, bg = "white")
        frame1.pack()

        self.space = 5
        self.width = 500
        self.height = 152
        
        label = Label(frame0, text = "Time [s]: ", bg = "white").grid(row=1, column=1, pady=self.space)
        
        self.tiempo = StringVar()
        
        entrytiempo = Entry(frame0, textvariable = self.tiempo ).grid(row=1, column=2)
        
        label = Label(frame0, text = "Density of honey [g/cm^3]:", bg = "white").grid(row=2, column=1)
        
        self.Dm = StringVar()
        
        entryDm = Entry(frame0, textvariable = self.Dm ).grid(row=2, column=2)
        
        label = Label(frame0, text = "Density  of the sphere [g/cm^3]:", bg = "white").grid(row=3, column=1, pady=self.space)
        
        self.De = StringVar()
        
        entryDe = Entry(frame0, textvariable = self.De ).grid(row=3, column=2)
        
        label = Label(frame0, text = "Chosee sphere constant:", bg = "white").grid(row=4, column=1, columnspan=2, pady=self.space)
        
        Logo = ImageTk.PhotoImage(Image.open("Images/Icon.png"))
        canvas1 = Canvas(frame0, width = 89, height = 99, bg = "white")
        canvas1.create_image( 45, 50, image = Logo)
        canvas1.grid(row=1, column=3, rowspan=3, padx = self.space*10)
        
        
        self.K = IntVar()
        bt1= Radiobutton(frame1, text="",  bg = "white", variable = self.K,
                         value = 0,
                         command = self.processRadiobutton2).grid(row=1, column=1, pady=self.space)
        Label(frame1, text = "K = 0.01036 Density: 2.220 [g/cm^3] \n Diameter: 0.158 cm  ", bg="light green").grid(row=1, column=2)


        
        bt2= Radiobutton(frame1, text="",  bg = "white", variable = self.K,
                         value = 1,
                         command = self.processRadiobutton2).grid(row=1, column=3)
        Label(frame1, text = "K = 0.10321  Density: 2.221 [g/cm^3] \n Diameter: 0.156 cm", bg="light green").grid(row=1, column=4)
        
        
        
        bt3= Radiobutton(frame1, text="",  bg = "white", variable = self.K,
                         value = 2,
                         command = self.processRadiobutton2).grid(row=1, column=5)
        Label(frame1, text = "K = 0.10788  Density: 8.125 [g/cm^3] \n Diameter: 0.156 cm", bg="light green").grid(row=1, column=6)
        
        Esferas1 = ImageTk.PhotoImage(Image.open("Images/Esfera123.png"))
        canvas1 = Canvas(frame1, width = self.width, height = self.height)
        canvas1.create_image( self.width/2, self.height/2, image = Esferas1)
        canvas1.grid(row=2, column=1, columnspan=6, pady=self.space)
        
        bt4= Radiobutton(frame1, text="",  bg = "white", variable = self.K,
                         value = 3,
                         command = self.processRadiobutton2).grid(row=3, column=1, pady=self.space)
        Label(frame1, text = "K = 0.78071  Density: 8.122 [g/cm^3] \n Diameter: 1.51 cm", bg="light green").grid(row=3, column=2)
        


    
        bt5= Radiobutton(frame1, text="",  bg = "white", variable = self.K,
                         value = 4,
                         command = self.processRadiobutton2).grid(row=3, column=3)
        Label(frame1, text = "K = 7.12867  Density: 8.121 [g/cm^3] \n Diameter: 0.139 cm", bg="light green").grid(row=3, column=4)
        
        bt6= Radiobutton(frame1, text="",  bg = "white", variable = self.K,
                         value = 5,
                         command = self.processRadiobutton2).grid(row=3, column=5)
        Label(frame1, text = "K = 35.07413  Density: 8.122 [g/cm^3] \n Diameter: 1.09 cm", bg="light green").grid(row=3, column=6)

        Esferas2 = ImageTk.PhotoImage(Image.open("Images/Esfera456.png"))
        canvas1 = Canvas(frame1, width = self.width, height = self.height)
        canvas1.create_image( self.width/2, self.height/2, image = Esferas2)
        canvas1.grid(row=4, column=1, columnspan=6, pady=self.space)        
        
        btcalc = Button(frame1, text = "Calculate",
                        command = self.calculos).grid(row=5, column=1, columnspan=6, pady=self.space)
        
        
        self.pure = StringVar()
        Label(frame1, textvariable = self.pure, bg = "white").grid(row=6, column=1, columnspan=5, pady=self.space)
        self.pure.set("the purity of this sample is unknown")
        
        Viscosimetro = ImageTk.PhotoImage(Image.open("Images/Viscosimetro.png"))
        
        LogoUIS = ImageTk.PhotoImage(Image.open("Images/Logo.png"))
        canvas1 = Canvas(frame1, width = 150, height = 92, bg = "white")
        canvas1.create_image( 75, 46, image = LogoUIS)
        canvas1.grid(row=6, column=5,columnspan=3, padx = self.space * 2)
        
        canvas2 = Canvas(frame2, width = 300, height = 600)
        canvas2.create_image( 150, 300, image = Viscosimetro)
        canvas2.pack()
        
        self.cte = 0.01036 #Predeterminado la primera K.
        self.window.mainloop()
    def processRadiobutton2(self):
        if self.K.get()== 0:
            self.cte = 0.01036
        elif self.K.get()== 1:
            self.cte = 0.10321
        elif self.K.get()== 2:
            self.cte = 0.10788
        elif self.K.get()== 3:
            self.cte = 0.78071
        elif self.K.get()== 4:
            self.cte = 7.12867
        elif self.K.get()== 5:
            self.cte = 35.07413
        else:
            self.cte = 0.01036
        
    def calculos(self):
        Ke =self.cte
        densE = float(self.De.get())
        densM = float(self.Dm.get())
        t = float(self.tiempo.get())
        self.viscosidadPureHoney = 1206.88438
        self.desviacionEstandar = 21.71194309
        self.viscosidad = Ke*(densE - densM)*t
        if abs(self.viscosidad - self.viscosidadPureHoney) <= self.desviacionEstandar:
            self.pure.set("the viscosity of the sample is:" 
                          + str(self.viscosidad) 
                          + " therefore the this sample is pure")
        elif self.viscosidad - self.viscosidadPureHoney >= self.desviacionEstandar:
            self.pure.set("la viscosidad de la muestra es:" 
                          + str(self.viscosidad) 
                          + " therefore this sample isnt pure, and posibly \n"
                          +"has an extra amount of solutes")
        elif self.viscosidad - self.viscosidadPureHoney <= -self.desviacionEstandar:
            self.pure.set("the viscosity of the sample is:" 
                          + str(self.viscosidad) 
                          + " therefore this sample isnt pure, and posibly \n"
                          +"is a little bit deluted")
    def Proc(self):
         tkMessageBox.showinfo("Information", "This software needs some experimental "
                               + "data, that are taken by a ball viscometer"
                               + " , a stopwatch and weighing machine, this data "
                               + "are the denisty of the sample ofhoney and the sphere "
                               + " and the time it takes the sphere to travel the measuring "
                               + "distance, as well as the measurement constants"
                               + " of the sphere used."
                               +" https://docs.google.com/document/d/1c4xGfsVt0t9aec2vUNaG8TKU8_XSwseWFXyW9BbSBjk/edit ") 
    def l1(self):
        tkMessageBox.showinfo("Information", "In this box you enter the "
                               + "time it takes the sphere to travel "
                               + "the measurement distance, which is measured "
                               + "with a stopwatch.")
    def l2(self):
         tkMessageBox.showinfo("Information", "In this box you enter the "
                               + "value of the density of the sphere that is measured"
                               + " using a scale and the volume of the container"
                               + " in which it is measured.")   
    def l3(self):
         tkMessageBox.showinfo("Information", "In this box you enter the "
                               + "value of the density of the sphere that should be "
                               + "liste in a paper with the viscometer.")   
    def l4(self):
         tkMessageBox.showinfo("Information", "This allows to choose the value "
                               + "of the measurement constant that the sphere possesses"
                               + " with which the measurement will be made, and that should be" 
                               + "in a paper next to the viscometer") 
    def l5(self):
         tkMessageBox.showinfo("Information", "The calculate button fulfills "
                               + "the function of starting the calculations for the "
                               + "purity check.")          
Prot1() 
