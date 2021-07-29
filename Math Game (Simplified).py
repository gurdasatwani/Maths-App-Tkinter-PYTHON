import random

from tkinter import *

from tkinter import ttk

Score = 0

RCount = 0

WCount = 0

TOTAL = 0

Range = None

Choose_Expression = None

option = []

button = []

label = []

List = {
    "PLUS ( + )": "+",
    "MINUS ( - )": "-",
    "DIVIDE ( / )": "/",
    "MULTIPLY ( * )": "*",
    "ALL": "all",
}

ln = [("MATHS", "GAME"), ("orange", "white"), (60, 0), ("NEXT", "EXIT")]

main = Tk()
main.configure(bg="black")


for i in range(2):
    l = Label(
        main,
        text=ln[0][i],
        bg="black",
        fg=ln[1][i],
        font=("Helvetica", 23, "bold", "italic"),
    )
    label.append(l)
    label[i].grid(row=0, padx=ln[2][i], column=i, pady=100)
    btn = Button(main, text=ln[3][i], bg="black", fg="white", bd=15)
    button.append(btn)

for i in range(4):
    btn = Button(
        main,
        bg="black",
        fg="white",
        height=2,
        width=4,
        font=("Helvetica", 30, "bold"),
        bd=25,
    )
    button.append(btn)

for i in [
    f"SCORE {Score}",
    f"RIGHT {RCount}",
    f"WRONG {WCount}",
    f"TOTAL {TOTAL}",
    "",
    "",
]:
    l1 = Label(main, text=i, font=("Helvetica", 7, "bold"), bg="black", fg="white")
    label.append(l1)

for i in range(1, 5):
    option.append(i)
combobox = ttk.Combobox(main, values=option)
combobox["state"] = "readonly"
combobox.current(0)
main.option_add("*TCombobox*Listbox*Background", "black")
main.option_add("*TCombobox*Listbox*foreground", "white")


tl = Label(
    main,
    width=17,
    text="How Many Digits :",
    bg="black",
    fg="white",
    font=("Helvetica", 10),
)

screen = Label(main, width=14, font=("Helvetica", 25, "bold"), bg="black", fg="white")


for (i, r, p) in zip([tl, combobox], [1, 2], [20, 0]):
    i.grid(row=r, columnspan=2, sticky="e", padx=110, pady=p)


def START(Expression):

    Random = random.sample(Range, 2)

    Random = [str(x) for x in Random]

    if Expression == "all":

        Expression = random.choice(list(List.values()))

        screen.config(text=f"{Random[0]} {Expression} {Random[1]} = ?")

        option1 = eval(Random[0] + Expression + Random[1])

        option2 = eval(Random[0] + Expression + Random[1] + "+" + Random[0])

        option3 = eval(Random[0] + Expression + Random[1] + "-" + Random[0])

        option4 = eval(
            Random[0] + Expression + Random[1] + "+" + Random[0] + "-" + Random[1]
        )

        Expression = "all"

    else:

        Expression = Choose_Expression

        screen.config(text=f"{Random[0]} {Expression} {Random[1]} = ?")

        option1 = eval(Random[0] + Expression + Random[1])

        option2 = eval(Random[0] + Expression + Random[1] + "+" + Random[0])

        option3 = eval(Random[0] + Expression + Random[1] + "-" + Random[0])

        option4 = eval(
            Random[0] + Expression + Random[1] + "+" + Random[0] + "-" + Random[1]
        )

    Random_Place_List = [option1, option2, option3, option4]

    Random_Place = random.sample(Random_Place_List, 4)

    def Option(Num):

        global Score, RCount, WCount, TOTAL

        for i in range(2, 6):
            button[i].config(state="disable")
            button[i].config(state="normal")

        label[6].config(text="")

        TOTAL += 1

        if Num == int(option1):

            Score += 1

            RCount += 1

        else:

            Score -= 1

            WCount += 1

            label[6].config(
                text=f"The Answer Was {option1}",
                fg="red",
                font=("Helvetica", 10, "bold"),
            )

        START(Choose_Expression)

        if Score <= 0:

            Score = 0

            for i in range(2, 6):
                button[i].destroy()

            screen.config(text="GAME OVER..", state=DISABLED)
            label[7].destroy()
            button[1].grid(row=11, padx=430)

        for (n, i) in zip(
            [2, 3, 4, 5],
            [f"SCORE {Score}", f"RIGHT {RCount}", f"WRONG {WCount}", f"TOTAL {TOTAL}"],
        ):

            label[n].config(text=i)

    for (n, i) in zip([2, 3, 4, 5], [0, 1, 2, 3]):
        button[n].config(
            text=int(Random_Place[i]), command=lambda i=i: Option(int(Random_Place[i]))
        )


def Get_Combobox1():
    global Sign_Dict, Choose_Expression
    Choose_Expression = combobox.get()
    if Choose_Expression in List:
        for i in List.keys():
            if Choose_Expression == i:
                label[7].config(text=i, font=("Helvetica", 10, "bold"))
                label[7].grid()
                break
        Choose_Expression = List.get(Choose_Expression)

        del List["ALL"]

        for i in [combobox, button[0], label[0], label[1], tl]:
            i.destroy()

        for i in range(2, 6):
            label[i].grid(sticky="w")
        screen.grid(pady=300)
        label[6].grid(row=10, sticky="w", rowspan=2, padx=300)
        for (n, r, s, p) in zip(
            [1, 2, 3, 4, 5],
            [11, 12, 12, 13, 13],
            ["w", "w", "e", "w", "e"],
            [0, 0, 80, 0, 80],
        ):
            button[n].grid(row=r, sticky=s, padx=p)
        START(Choose_Expression)


def Get_Combobox():
    global Range
    Num = int(combobox.get())
    if Num == 1:
        Range = range(1, 10)
    elif Num == 2:
        Range = range(10, 100)
    elif Num == 3:
        Range = range(100, 1000)
    elif Num == 4:
        Range = range(1000, 10000)

    tl.config(text="Choose Expression :")
    option.clear()
    for i in List:
        option.append(i)
    combobox.config(values=option)
    combobox.current(0)

    button[0].config(command=Get_Combobox1)


for (n, i) in zip([0, 1], [Get_Combobox, main.destroy]):
    button[n].config(command=i)
for (n, n1, p) in zip([0, 1], [3, 4], [260, 270]):
    button[n].grid(row=n1, columnspan=2, sticky="e", padx=p, pady=50)


mainloop()
