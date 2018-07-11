from tkinter import *
import time

root = Tk()
root.geometry("1500x6000")
root.config(bg='sky blue')
root.title("GOPINATH HOTEL")
Tops = Frame(root, width=1600)
Tops.pack(side=TOP)

f1 = Frame(root, width=1000, height=800)
f1.pack(side=LEFT)

localtime = time.asctime(time.localtime(time.time()))

LABEL= Label(Tops, font=('Coolvetica', 40, 'bold'), text=" Gopinath The Grand ", fg="Black", bd=10, anchor='w')
LABEL.grid(row=0, column=0)

LABEL = Label(Tops, font=('arial', 10, 'bold'), text=localtime, fg="royal blue", bd=5, anchor='w')
LABEL.grid(row=0, column=1)

def Ref():

    if (Fries.get() == ""):
        CoFries = 0
    else:
        CoFries = float(Fries.get())
    if (Noodles.get() == ""):
        CoNoodles = 0
    else:
        CoNoodles = float(Noodles.get())
    if (Soup.get() == ""):
        CoSoup = 0
    else:
        CoSoup = float(Soup.get())
    if (Burger.get() == ""):
        CoBurger = 0
    else:
        CoBurger = float(Burger.get())
    if (Sandwich.get() == ""):
        CoSandwich = 0
    else:
        CoSandwich = float(Sandwich.get())
    if (Drinks.get() == ""):
        CoD = 0
    else:
        CoD = float(Drinks.get())
    CostofFries = CoFries * 25
    CostofDrinks = CoD * 65
    CostofNoodles = CoNoodles * 90
    CostofSoup = CoSoup * 140
    CostBurger = CoBurger * 260
    CostSandwich = CoSandwich * 300
    CostofMeal = "Rs", str(
        '%.2f' % (CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich))
    PayTax = ((CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich) * 0.2)
    TotalCost = (CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich)
    Ser_Charge = ((CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich) / 99)
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

def Reset():
    order.set("")
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")
order = StringVar()
Fries = StringVar()
Noodles = StringVar()
Soup = StringVar()
Burger = StringVar()
Sandwich = StringVar()
Drinks = StringVar()
SubTotal = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Cost = StringVar()
Total = StringVar()


lblorder = Label(f1, font=('arial', 16, 'bold'), text="Order Number", bd=16, anchor="w")
lblorder.grid(row=0, column=0)
txtorder = Entry(f1, font=('arial', 16, 'bold'), textvariable=order, bd=10, insertwidth=4, bg="powder blue",
                     justify='right')
txtorder.grid(row=0, column=1)

lblFries = Label(f1, font=('arial', 16, 'bold'), text="Fries", bd=16, anchor="w")
lblFries.grid(row=1, column=0)
txtFries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg="powder blue",
                 justify='right')
txtFries.grid(row=1, column=1)

lblNoodles = Label(f1, font=('arial', 16, 'bold'), text="Noodles", bd=16, anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles = Entry(f1, font=('arial', 16, 'bold'), textvariable=Noodles, bd=10, insertwidth=4, bg="powder blue",
                   justify='right')
txtNoodles.grid(row=2, column=1)

lblSoup = Label(f1, font=('arial', 16, 'bold'), text="Soup", bd=16, anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup = Entry(f1, font=('arial', 16, 'bold'), textvariable=Soup, bd=10, insertwidth=4, bg="powder blue",
                justify='right')
txtSoup.grid(row=3, column=1)

lblBurger = Label(f1, font=('arial', 16, 'bold'), text="Burger", bd=16, anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg="powder blue",
                  justify='right')
txtBurger.grid(row=4, column=1)

lblSandwich = Label(f1, font=('arial', 16, 'bold'), text="Sandwich", bd=16, anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich = Entry(f1, font=('arial', 16, 'bold'), textvariable=Sandwich, bd=10, insertwidth=4, bg="powder blue",
                    justify='right')
txtSandwich.grid(row=5, column=1)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    LABEL.grid(row=0, column=0)
    LABEL = Label(roo, font=('aria', 15,'bold'), text="---------   ", fg="white", anchor=W)
    LABEL.grid(row=0, column=2)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    LABEL.grid(row=0, column=3)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="Fries", fg="red", anchor=W)
    LABEL.grid(row=1, column=0)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="25", fg="red", anchor=W)
    LABEL.grid(row=1, column=3)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="Noodles", fg="red", anchor=W)
    LABEL.grid(row=2, column=0)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="65", fg="red", anchor=W)
    LABEL.grid(row=2, column=3)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="Soup", fg="red", anchor=W)
    LABEL.grid(row=3, column=0)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="90", fg="red", anchor=W)
    LABEL.grid(row=3, column=3)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="Burger", fg="red", anchor=W)
    LABEL.grid(row=4, column=0)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="140", fg="red", anchor=W)
    LABEL.grid(row=4, column=3)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="Sandwich", fg="red", anchor=W)
    LABEL.grid(row=5, column=0)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="260", fg="red", anchor=W)
    LABEL.grid(row=5, column=3)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="red", anchor=W)
    LABEL.grid(row=6, column=0)
    LABEL = Label(roo, font=('aria', 15, 'bold'), text="300", fg="red", anchor=W)
    LABEL.grid(row=6, column=3)

lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="powder blue",
                  justify='right')
txtDrinks.grid(row=0, column=3)

lblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor="w")
lblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="powder blue",
                justify='right')
txtCost.grid(row=1, column=3)

lblService = Label(f1, font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor="w")
lblService.grid(row=2, column=2)
txtService = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4, bg="powder blue",
                   justify='right')
txtService.grid(row=2, column=3)

lblStateTax = Label(f1, font=('arial', 16, 'bold'), text="State Tax", bd=16, anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg="powder blue",
                    justify='right')
txtStateTax.grid(row=3, column=3)

lblSubTotal = Label(f1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg="powder blue",
                    justify='right')
txtSubTotal.grid(row=4, column=3)

lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="powder blue",
                     justify='right')
txtTotalCost.grid(row=5, column=3)

btnprice=Button(f1,padx=16,pady=8, bd=16 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Price",
                bg="powder blue",command=price).grid(row=7, column=0)

btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total",
                  bg="powder blue", command=Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset",
                  bg="powder blue", command=Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit",
                 bg="powder blue", command=qExit).grid(row=7, column=3)

btnCalc = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Calculator",
                 bg="powder blue").grid(row=7, column=4)



root.mainloop()