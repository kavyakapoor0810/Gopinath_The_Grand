from tkinter import *

import time

root = Tk()
root.geometry("2000x8000")
root.config(bg='cyan')
root.title("GOPINATH HOTEL")
Tops = Frame(root, width=8000,bg="cyan")
Tops.pack(side=TOP)

f1 = Frame(root, width=1000, height=800,bg="cyan")
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN,bg="cyan")
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

LABEL= Label(Tops, font=('Harlow Solid Italic', 70), text=" Gopinath The Grand Hotel", fg="Black",bg="cyan", bd=10, anchor='w').grid(row=1, column=0)

LABEL = Label(Tops, font=('arial', 10, 'bold'), text=localtime, fg="royal blue",bg="cyan", bd=5, anchor='w').grid(row=0, column=1)


def Ref():
    if (cheeseballs.get() == ""):
        Cocheeseballs = 0
    else:
        Cocheeseballs = float(cheeseballs.get())

    if (drymaunchurian.get() == ""):
        Codrymaunchurian = 0
    else:
        Codrymaunchurian = float(drymaunchurian.get())

    if (honeychillipotato.get() == ""):
        Cohoneychillipotato = 0
    else:
        Cohoneychillipotato = float(honeychillipotato.get())

    if (classicgreeksalad.get() == ""):
        Coclassicgreeksalad = 0
    else:
        Coclassicgreeksalad = float(classicgreeksalad.get())

    if (classicchickentikka.get() == ""):
        Coclassicchickentikka = 0
    else:
        Coclassicchickentikka = float(classicchickentikka.get())

    if (tomatosoup.get() == ""):
        Cotomatosoup = 0
    else:
        Cotomatosoup = float(tomatosoup.get())

    if (gngspecialsoup.get() == ""):
        Cogngspecialsoup = 0
    else:
        Cogngspecialsoup = float(gngspecialsoup.get())

    if (bbqpanner.get() == ""):
        Cobbqpanner = 0
    else:
        Cobbqpanner = float(bbqpanner.get())

    if (greenthai.get() == ""):
        Cogreenthai = 0
    else:
        Cogreenthai = float(greenthai.get())

    if (chillimushroom.get() == ""):
        Cochillimushroom = 0
    else:
        Cochillimushroom = float(chillimushroom.get())

    if (chillipanner.get() == ""):
        Cochillipanner = 0
    else:
        Cochillipanner = float(chillipanner.get())

    if (biryani.get() == ""):
        Cobiryani = 0
    else:
        Cobiryani = float(biryani.get())

    if (butterchicken.get() == ""):
        Cobutterchicken = 0
    else:
        Cobutterchicken = float(butterchicken.get())

    if (prantha.get() == ""):
        Coprantha = 0
    else:
        Coprantha = float(prantha.get())

    if (naan.get() == ""):
        Conaan = 0
    else:
        Conaan = float(naan.get())

    if (icecream.get() == ""):
        Coicecream = 0
    else:
        Coicecream = float(icecream.get())

    if (velvetcake.get() == ""):
        Covelvetcake = 0
    else:
        Covelvetcake = float(velvetcake.get())

    if (Drinks.get() == ""):
        CoDrinks = 0
    else:
        CoDrinks = float(Drinks.get())

    Costofcheeseballs = Cocheeseballs * 100
    Costofdrymaunchurian = Codrymaunchurian * 120
    Costofhoneychillipotato = Cohoneychillipotato * 200
    Costofclassicgreeksalad = Coclassicgreeksalad * 180
    Costofclassicchickentikka = Coclassicchickentikka * 230
    CostofCostoftomatosoup = Cotomatosoup * 180
    Costofgngspecialsoup = Cogngspecialsoup * 210
    Costofbbqpanner = Cobbqpanner * 250
    Costofgreenthai = Cogreenthai * 280
    Costofchillimushroom = Cochillimushroom * 250
    Costofchillipanner = Cochillipanner * 300
    Costofbiryani = Cobiryani * 220
    Costofbutterchicken = Cobutterchicken * 180
    Costofprantha = Coprantha * 10
    Costofnaan = Conaan * 15
    Costoficecream = Coicecream * 180
    Costofvelvetcake = Covelvetcake * 650
    CostofDrinks = CoDrinks * 50


    CostofMeal = "Rs", str(
        '%.2f' % (Costofcheeseballs + Costofdrymaunchurian + Costofhoneychillipotato + Costofclassicgreeksalad + Costofclassicchickentikka + CostofCostoftomatosoup+ Costofgngspecialsoup + Costofbbqpanner + Costofgreenthai + Costofchillimushroom + Costofchillipanner + Costofbiryani + Costofbutterchicken +Costofprantha + Costofnaan + Costoficecream + Costofvelvetcake + CostofDrinks))
    PayTax = ((Costofcheeseballs + Costofdrymaunchurian + Costofhoneychillipotato + Costofclassicgreeksalad + Costofclassicchickentikka + CostofCostoftomatosoup+ Costofgngspecialsoup + Costofbbqpanner + Costofgreenthai + Costofchillimushroom + Costofchillipanner + Costofbiryani + Costofbutterchicken +Costofprantha + Costofnaan + Costoficecream + Costofvelvetcake + CostofDrinks) * 0.2)
    TotalCost = (Costofcheeseballs + Costofdrymaunchurian + Costofhoneychillipotato + Costofclassicgreeksalad + Costofclassicchickentikka + CostofCostoftomatosoup+ Costofgngspecialsoup + Costofbbqpanner + Costofgreenthai + Costofchillimushroom + Costofchillipanner + Costofbiryani + Costofbutterchicken +Costofprantha + Costofnaan + Costoficecream + Costofvelvetcake + CostofDrinks)
    Ser_Charge = ((Costofcheeseballs + Costofdrymaunchurian + Costofhoneychillipotato + Costofclassicgreeksalad + Costofclassicchickentikka + CostofCostoftomatosoup+ Costofgngspecialsoup + Costofbbqpanner + Costofgreenthai + Costofchillimushroom + Costofchillipanner + Costofbiryani + Costofbutterchicken +Costofprantha + Costofnaan + Costoficecream + Costofvelvetcake + CostofDrinks) / 99)
    Service = "Rs", str('%.2f' % Ser_Charge)
    OverAllCost = "Rs", str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax = "Rs", str('%.2f' % PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)

def qExit():
    root.destroy()

def price():
    roo = Tk()
    roo.geometry("400x600+0+0")
    roo.title("Price List")
    roo.config(bg='white')
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black",bg="white", bd=5).grid(row=0, column=1)
    LABEL = Label(roo, font=('aria', 15,'bold'), text="-------------       ", fg="black",bg="white", anchor=W).grid(row=0, column=3)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black",bg="white", anchor=W).grid(row=0, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Cheese Balls", fg="red",bg="white", bd=5).grid(row=1, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="100", fg="red",bg="white", anchor=W).grid(row=1, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Dry Maunchurian", fg="red",bg="white", bd=5).grid(row=2, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="120", fg="red",bg="white", anchor=W).grid(row=2, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Honey Chilli Potato", fg="red",bg="white", bd=5).grid(row=3, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="200", fg="red",bg="white", anchor=W).grid(row=3, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Classic Greek Salad", fg="red",bg="white", bd=5).grid(row=4, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="180", fg="red",bg="white", anchor=W).grid(row=4, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Classic Chicken Tikka", fg="red",bg="white", bd=5).grid(row=5, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="230", fg="red",bg="white", anchor=W).grid(row=5, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Tomato Soup", fg="red",bg="white", bd=5).grid(row=6, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="180", fg="red",bg="white", anchor=W).grid(row=6, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="GNG Special Soup", fg="red",bg="white", bd=5).grid(row=7, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="120", fg="red",bg="white", anchor=W).grid(row=7, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="BBQ Panner", fg="red",bg="white", bd=5).grid(row=8, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="250", fg="red",bg="white", anchor=W).grid(row=8, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Green Thai", fg="red",bg="white", bd=5).grid(row=9, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="280", fg="red",bg="white", anchor=W).grid(row=9, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Chilli Mushroom", fg="red",bg="white", bd=5).grid(row=10, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="250", fg="red",bg="white", anchor=W).grid(row=10, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Chilli Panner", fg="red",bg="white", bd=5).grid(row=11, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="300", fg="red",bg="white", anchor=W).grid(row=11, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Biryani + Raita", fg="red",bg="white", bd=5).grid(row=12, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="220", fg="red",bg="white", anchor=W).grid(row=12, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Butter Chicken + Naan", fg="red",bg="white", bd=5).grid(row=13, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="180", fg="red",bg="white", anchor=W).grid(row=13, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Prantha", fg="red",bg="white", bd=5).grid(row=14, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="10", fg="red",bg="white", anchor=W).grid(row=14, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Naan", fg="red",bg="white", bd=5).grid(row=15, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="15", fg="red",bg="white", anchor=W).grid(row=15, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Ice Cream", fg="red",bg="white", bd=5).grid(row=16, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="180", fg="red",bg="white", anchor=W).grid(row=16, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Red Velvet Cake", fg="red",bg="white", bd=5).grid(row=17, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="650", fg="red",bg="white", anchor=W).grid(row=17, column=5)

    LABEL = Label(roo, font=('aria', 10, 'bold'), text="Drinks", fg="red",bg="white", bd=5).grid(row=18, column=1)
    LABEL = Label(roo, font=('aria', 10, 'bold'), text="50", fg="red",bg="white", anchor=W).grid(row=18, column=5)


def Reset():
    order.set("")
    cheeseballs.set("")
    drymaunchurian.set("")
    honeychillipotato.set("")
    classicgreeksalad.set("")
    classicchickentikka.set("")
    tomatosoup.set("")
    gngspecialsoup.set("")
    bbqpanner.set("")
    greenthai.set("")
    chillimushroom.set("")
    chillipanner.set("")
    biryani.set("")
    butterchicken.set("")
    prantha.set("")
    naan.set("")
    icecream.set("")
    velvetcake.set("")
    Drinks.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Tax.set("")
    Cost.set("")

order = StringVar()
cheeseballs = StringVar()
drymaunchurian = StringVar()
honeychillipotato = StringVar()
classicgreeksalad = StringVar()
classicchickentikka = StringVar()
tomatosoup = StringVar()
gngspecialsoup = StringVar()
bbqpanner = StringVar()
greenthai = StringVar()
chillimushroom = StringVar()
chillipanner = StringVar()
biryani = StringVar()
butterchicken = StringVar()
prantha = StringVar()
naan = StringVar()
icecream = StringVar()
velvetcake = StringVar()
Drinks = StringVar()
SubTotal = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Cost = StringVar()
Total = StringVar()


text_Input = StringVar()
operator = ""
def calc():

    txtdisplay = Entry(f2, font=('ariel', 20, 'bold'), textvariable=text_Input, bd=5, insertwidth=7, bg="white").grid(columnspan=5)

    def btnclick(numbers):
        global operator
        operator = operator + str(numbers)
        text_Input.set(operator)

    def clrdisplay():
        global operator
        operator = ""
        text_Input.set("")

    def eqals():
        global operator
        sumup = str(eval(operator))

        text_Input.set(sumup)
        operator = ""

    btn7 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="7", bg="powder blue",
                  command=lambda: btnclick(7)).grid(row=2, column=0)

    btn8 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="8", bg="powder blue",
                  command=lambda: btnclick(8)).grid(row=2, column=1)

    btn9 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="9", bg="powder blue",
                  command=lambda: btnclick(9)).grid(row=2, column=2)

    Addition = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="+", bg="powder blue",
                      command=lambda: btnclick("+")).grid(row=2, column=3)

##########################################################################################################################################################

    btn4 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="4", bg="powder blue",
                  command=lambda: btnclick(4)).grid(row=3, column=0)

    btn5 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="5", bg="powder blue",
                  command=lambda: btnclick(5)).grid(row=3, column=1)

    btn6 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="6", bg="powder blue",
                  command=lambda: btnclick(6)).grid(row=3, column=2)

    Substraction = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="-",
                          bg="powder blue", command=lambda: btnclick("-")).grid(row=3, column=3)

##########################################################################################################################################################

    btn1 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="1", bg="powder blue",
                  command=lambda: btnclick(1)).grid(row=4, column=0)

    btn2 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="2", bg="powder blue",
                  command=lambda: btnclick(2)).grid(row=4, column=1)

    btn3 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="3", bg="powder blue",
                  command=lambda: btnclick(3)).grid(row=4, column=2)

    multiply = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="*", bg="powder blue",
                      command=lambda: btnclick("*")).grid(row=4, column=3)

##########################################################################################################################################################

    btn0 = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="0", bg="powder blue",
                  command=lambda: btnclick(0)).grid(row=5, column=0)

    btnc = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="c", bg="powder blue",
                  command=clrdisplay).grid(row=5, column=1)

    btnequal = Button(f2, padx=16, pady=16, bd=4, width=16, fg="black", font=('ariel', 20, 'bold'), text="=",
                      bg="powder blue", command=eqals).grid(columnspan=4)

    Decimal = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text=".", bg="powder blue",
                     command=lambda: btnclick(".")).grid(row=5, column=2)

    Division = Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="/", bg="powder blue",
                      command=lambda: btnclick("/")).grid(row=5, column=3)

##############################################################################################################################################################


LABELorder = Label(f1, font=('Lucida Calligraphy', 10,'bold'), text="Order Number", bd=8,bg="cyan", anchor="w").grid(row=0, column=0)
TEXTorder = Entry(f1, font=('arial', 10), textvariable=order, bd=8, insertwidth=2, bg="white",justify='right').grid(row=0, column=1)

LABELcheeseballs = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Cheese Balls", bd=8,bg="cyan", anchor="w").grid(row=1, column=0)
TEXTcheeseballs = Entry(f1, font=('arial', 10, 'bold'), textvariable=cheeseballs, bd=8, insertwidth=2, bg="white",justify='right').grid(row=1, column=1)

LABELdrymaunchurian = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Dry Maunchurian", bd=8,bg="cyan", anchor="w").grid(row=2, column=0)
TEXTdrymaunchurian = Entry(f1, font=('arial', 10, 'bold'), textvariable=drymaunchurian, bd=8, insertwidth=2, bg="white",justify='right').grid(row=2, column=1)

LABELhoneychillipotato = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Honey Chilli Potato", bd=8,bg="cyan", anchor="w").grid(row=3, column=0)
TEXThoneychillipotato = Entry(f1, font=('arial', 10, 'bold'), textvariable=honeychillipotato, bd=8, insertwidth=2, bg="white",justify='right').grid(row=3, column=1)

LABELclassicgreeksalad = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Classic Greek Salad" , bd=8,bg="cyan", anchor="w").grid(row=4, column=0)
TEXTclassicgreeksalad = Entry(f1, font=('arial', 10, 'bold'), textvariable=classicgreeksalad , bd=8, insertwidth=2, bg="white",justify='right').grid(row=4, column=1)

LABELclassicchickentikka = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Classic Chicken Tikka", bd=8,bg="cyan", anchor="w").grid(row=5, column=0)
TEXTclassicchickentikka = Entry(f1, font=('arial', 10, 'bold'), textvariable=classicchickentikka, bd=8, insertwidth=2, bg="white",justify='right').grid(row=5, column=1)

LABELtomatosoup = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Tomato Soup", bd=8,bg="cyan", anchor="w").grid(row=6, column=0)
TEXTtomatosoup = Entry(f1, font=('arial', 10, 'bold'), textvariable=tomatosoup, bd=8, insertwidth=2, bg="white",justify='right').grid(row=6, column=1)

LABELgngspecialsoup = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="GNG Special Soup", bd=8,bg="cyan", anchor="w").grid(row=7, column=0)
TEXTgngspecialsoup = Entry(f1, font=('arial', 10, 'bold'), textvariable=gngspecialsoup, bd=8, insertwidth=2, bg="white",justify='right').grid(row=7, column=1)

#######################################################################################################################################################################

LABELbbqpanner = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="BBQ Panner", bd=8,bg="cyan", anchor="w").grid(row=0, column=2)
TEXTbbqpanner = Entry(f1, font=('arial', 10, 'bold'), textvariable=bbqpanner, bd=8, insertwidth=2, bg="white",justify='right').grid(row=0, column=3)

LABELgreenthai = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Green Thai", bd=8,bg="cyan", anchor="w").grid(row=1, column=2)
TEXTgreenthai = Entry(f1, font=('arial', 10, 'bold'), textvariable=greenthai, bd=8, insertwidth=2, bg="white",justify='right').grid(row=1, column=3)

LABELchillimushroom = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Chilli Mushroom", bd=8,bg="cyan", anchor="w").grid(row=2, column=2)
TEXTchillimushroom = Entry(f1, font=('arial', 10, 'bold'), textvariable=chillimushroom, bd=8, insertwidth=2, bg="white",justify='right').grid(row=2, column=3)

LABELchillipanner = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Chilli Panner", bd=8,bg="cyan", anchor="w").grid(row=3, column=2)
TEXTchillipanner = Entry(f1, font=('arial', 10, 'bold'), textvariable=chillipanner, bd=8, insertwidth=2, bg="white",justify='right').grid(row=3, column=3)

LABELbiryani = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Biryani + Raita", bd=8,bg="cyan", anchor="w").grid(row=4, column=2)
TEXTbiryani = Entry(f1, font=('arial', 10, 'bold'), textvariable=biryani, bd=8, insertwidth=2, bg="white",justify='right').grid(row=4, column=3)

LABELbutterchicken = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Butter Chicken + Naan", bd=8,bg="cyan", anchor="w").grid(row=5, column=2)
TEXTbutterchicken = Entry(f1, font=('arial', 10, 'bold'), textvariable=butterchicken, bd=8, insertwidth=2, bg="white",justify='right').grid(row=5, column=3)

LABELprantha = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Prantha", bd=8,bg="cyan", anchor="w").grid(row=6, column=2)
TEXTprantha = Entry(f1, font=('arial', 10, 'bold'), textvariable=prantha, bd=8, insertwidth=2, bg="white",justify='right').grid(row=6, column=3)

LABELnaan = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Naan", bd=8,bg="cyan", anchor="w").grid(row=7, column=2)
TEXTnaan = Entry(f1, font=('arial', 10, 'bold'), textvariable=naan, bd=8, insertwidth=2, bg="white",justify='right').grid(row=7, column=3)

#########################################################################################################################################################

LABELicecream = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Ice Cream", bd=8,bg="cyan", anchor="w").grid(row=0, column=4)
TEXTicecream = Entry(f1, font=('arial', 10, 'bold'), textvariable=icecream, bd=8, insertwidth=2, bg="white",justify='right').grid(row=0, column=5)

LABELvelvetcake = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Red Velvet Cake", bd=8,bg="cyan", anchor="w").grid(row=1, column=4)
TEXTvelvetcake = Entry(f1, font=('arial', 10, 'bold'), textvariable=velvetcake, bd=8, insertwidth=2, bg="white",justify='right').grid(row=1, column=5)

LABELDrinks = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Drinks", bd=8,bg="cyan", anchor="w").grid(row=2, column=4)
TEXTDrinksicecream = Entry(f1, font=('arial', 10, 'bold'), textvariable=Drinks, bd=8, insertwidth=2, bg="white",justify='right').grid(row=2, column=5)

LABELCost = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Cost of Meal", bd=8,bg="cyan", anchor="w").grid(row=3, column=4)
TEXTCost = Entry(f1, font=('arial', 10, 'bold'), textvariable=Cost, bd=8, insertwidth=2, bg="white",justify='right').grid(row=3, column=5)

LABELService = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Service Charges", bd=8,bg="cyan", anchor="w").grid(row=4, column=4)
TEXTService = Entry(f1, font=('arial', 10, 'bold'), textvariable=Service_Charge, bd=8, insertwidth=2, bg="white",justify='right').grid(row=4, column=5)

LABELStateTax = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="State Tax", bd=8,bg="cyan", anchor="w").grid(row=5, column=4)
TEXTStateTax = Entry(f1, font=('arial', 10, 'bold'), textvariable=Tax, bd=8, insertwidth=2, bg="white",justify='right').grid(row=5, column=5)

LABELSubTotal = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Sub Total", bd=8,bg="cyan", anchor="w").grid(row=6, column=4)
TEXTSubTotal = Entry(f1, font=('arial', 10, 'bold'), textvariable=SubTotal, bd=8, insertwidth=2, bg="white",justify='right').grid(row=6, column=5)

LABELTotalCost = Label(f1, font=('Lucida Calligraphy', 10, 'bold'), text="Total Cost", bd=8,bg="cyan", anchor="w").grid(row=7, column=4)
TEXTTotalCost = Entry(f1, font=('arial', 10, 'bold'), textvariable=Total, bd=8, insertwidth=2, bg="white",justify='right').grid(row=7, column=5)

#################################################################################################################################################################################

btnprice=Button(f1,padx=16,pady=8, bd=16 ,fg="black",font=('ariel' ,16,'bold'),width=8, text="Price",
                bg="powder blue",command=price).grid(row=8, column=0)

btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=8, text="Total",
                  bg="powder blue", command=Ref).grid(row=8, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=8, text="Reset",
                  bg="powder blue", command=Reset).grid(row=8, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=8, text="Exit",
                 bg="powder blue", command=qExit).grid(row=8, column=3)

btnCalc = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=8, text="Calculator",
                 bg="powder blue", command=calc).grid(row=8, column=4)


root.mainloop()