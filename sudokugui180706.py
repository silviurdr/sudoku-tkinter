

from tkinter import *
from tkmacosx import Button


root = Tk()

number_not_entered = True


def key(event):
    global number_not_entered
    event.widget["text"] = repr(int(event.char))
    event.widget.config(width=50, height=50)
    number_not_entered = False


def leftClick(event):
    global number_not_entered
    while number_not_entered:
        event.widget.focus_set()
        event.widget.config(width=50, height=50)
        number_not_entered = False


starting_puzzle = dict.fromkeys(range(0, 81), " ")

print(starting_puzzle)

solved_numbers = [4, 3, 5, 2, 6, 9, 7, 8, 1, 6, 8, 2, 5, 7, 1, 4, 9, 3, 1, 9, 7, 8, 3, 4, 5, 6, 2, 8, 2, 6, 1, 9, 5, 3,
                  4, 7, 3, 7, 4, 6, 8, 2, 9, 1, 5, 9, 5, 1, 7, 4, 3, 6, 2, 8, 5, 1, 9,
                  3, 2, 6, 8, 7, 4, 2, 4, 8, 9, 5, 7, 1, 3, 6, 7, 6, 3, 4, 1, 8, 2, 5, 9]

solved_puzzle = dict.fromkeys(range(0, 81), " ")

for i in range(0, 81):
    solved_puzzle[i] = solved_numbers[i]

print(solved_puzzle)


l1 = Label(root, text="")
l2 = Label(root, text="A")
l3 = Label(root, text="B")
l4 = Label(root, text="C")
l5 = Label(root, text="D")
l6 = Label(root, text="E")
l7 = Label(root, text="F")
l8 = Label(root, text="G")
l9 = Label(root, text="H")
l10 = Label(root, text="I")


l1.grid(row=1, column=0, sticky=W, padx=20, pady=2)
l2.grid(row=2, column=0, sticky=W, padx=20, pady=2)
l3.grid(row=3, column=0, sticky=W, padx=20, pady=2)
l4.grid(row=4, column=0, sticky=W, padx=20, pady=2)
l5.grid(row=5, column=0, sticky=W, padx=20, pady=2)
l6.grid(row=6, column=0, sticky=W, padx=20, pady=2)
l7.grid(row=7, column=0, sticky=W, padx=20,  pady=2)
l8.grid(row=8, column=0, sticky=W, padx=20, pady=2)
l9.grid(row=9, column=0, sticky=W, padx=20, pady=2)
l10.grid(row=10, column=0, sticky=W, padx=20, pady=2)


laa = Label(root, text="")
la = Label(root, text="a", anchor=CENTER)
lb = Label(root, text="b")
lc = Label(root, text="c")
ld = Label(root, text="d")
le = Label(root, text="e")
lf = Label(root, text="f")
lg = Label(root, text="g")
lh = Label(root, text="h")
li = Label(root, text="i")
lspace = Label(root, text="")

lbb = Label(root, text="")
lcc = Label(root, text="")
ldd = Label(root, text="")
lee = Label(root, text="")
lff = Label(root, text="")
lgg = Label(root, text="")
lhh = Label(root, text="")
lii = Label(root, text="")

laa.grid(row=0, column=0, sticky=W, pady=2)
lbb.grid(row=0, column=1, sticky=W, pady=2)
lcc.grid(row=0, column=2, sticky=W, pady=2)
ldd.grid(row=0, column=3, sticky=W, pady=2)
lee.grid(row=0, column=4, sticky=W, pady=2)
lff.grid(row=0, column=5, sticky=W, pady=2)
lgg.grid(row=0, column=6, sticky=W, pady=2)
lhh.grid(row=0, column=7, sticky=W, pady=2)
lii.grid(row=0, column=8, sticky=W, pady=2)
laa.grid(row=0, column=9, sticky=W, pady=2)

la.grid(row=1, column=1, pady=2)
lb.grid(row=1, column=2, pady=2)
lc.grid(row=1, column=3, pady=2)
ld.grid(row=1, column=4, pady=2)
le.grid(row=1, column=5, pady=2)
lf.grid(row=1, column=6, pady=2)
lg.grid(row=1, column=7, pady=2)
lh.grid(row=1, column=8, pady=2)
li.grid(row=1, column=9, pady=2)
lspace.grid(row=1, column=10, padx=10, pady=2)


buttonAa = Button(root, fg="Orange", text=" ")
buttonBa = Button(root, fg="Orange", text=" ")
buttonCa = Button(root, fg="Orange", text="3")
buttonDa = Button(root, fg="Green", text=" ")
buttonEa = Button(root, fg="Green", text="4")
buttonFa = Button(root, fg="Green", text="")
buttonGa = Button(root, fg="Orange", text="5")
buttonHa = Button(root, fg="Orange", text="7")
buttonIa = Button(root, fg="Orange", text="")

buttonAa.grid(row=2, column=1, pady=2)
buttonBa.grid(row=3, column=1, pady=2)
buttonCa.grid(row=4, column=1, pady=2)
buttonDa.grid(row=5, column=1, pady=2)
buttonEa.grid(row=6, column=1, pady=2)
buttonFa.grid(row=7, column=1, pady=2)
buttonGa.grid(row=8, column=1, pady=2)
buttonHa.grid(row=9, column=1, pady=2)
buttonIa.grid(row=10, column=1, pady=2)


buttonAb = Button(root, fg="Orange", text="3")
buttonBb = Button(root, fg="Orange", text=" ")
buttonCb = Button(root, fg="Orange", text="6")
buttonDb = Button(root, fg="Green", text="8")
buttonEb = Button(root, fg="Green", text=" ")
buttonFb = Button(root, fg="Green", text="3")
buttonGb = Button(root, fg="Orange", text="4")
buttonHb = Button(root, fg="Orange", text="1")
buttonIb = Button(root, fg="Orange", text=" ")

buttonAb.grid(row=2, column=2, pady=2)
buttonBb.grid(row=3, column=2, pady=2)
buttonCb.grid(row=4, column=2, pady=2)
buttonDb.grid(row=5, column=2, pady=2)
buttonEb.grid(row=6, column=2, pady=2)
buttonFb.grid(row=7, column=2, pady=2)
buttonGb.grid(row=8, column=2, pady=2)
buttonHb.grid(row=9, column=2, pady=2)
buttonIb.grid(row=10, column=2, pady=2)

buttonAc = Button(root, fg="Orange", text="5")
buttonBc = Button(root, fg="Orange", text=" ")
buttonCc = Button(root, fg="Orange", text="7")
buttonDc = Button(root, fg="Green", text=" ")
buttonEc = Button(root, fg="Green", text="8")
buttonFc = Button(root, fg="Green", text=" ")
buttonGc = Button(root, fg="Orange", text=" ")
buttonHc = Button(root, fg="Orange", text="1")
buttonIc = Button(root, fg="Orange", text="2")

buttonAc.grid(row=2, column=3, pady=2)
buttonBc.grid(row=3, column=3, pady=2)
buttonCc.grid(row=4, column=3, pady=2)
buttonDc.grid(row=5, column=3, pady=2)
buttonEc.grid(row=6, column=3, pady=2)
buttonFc.grid(row=7, column=3, pady=2)
buttonGc.grid(row=8, column=3, pady=2)
buttonHc.grid(row=9, column=3, pady=2)
buttonIc.grid(row=10, column=3, pady=2)

buttonAd = Button(root, fg="Orange", text="3")
buttonBd = Button(root, fg="Orange", text="5")
buttonCd = Button(root, fg="Orange", text=" ")
buttonDd = Button(root, fg="Green", text="8")
buttonEd = Button(root, fg="Green", text=" ")
buttonFd = Button(root, fg="Green", text="3")
buttonGd = Button(root, fg="Orange", text="0")
buttonHd = Button(root, fg="Orange", text="1")
buttonId = Button(root, fg="Orange", text="9")

buttonAd.grid(row=2, column=4, pady=2)
buttonBd.grid(row=3, column=4, pady=2)
buttonCd.grid(row=4, column=4, pady=2)
buttonDd.grid(row=5, column=4, pady=2)
buttonEd.grid(row=6, column=4, pady=2)
buttonFd.grid(row=7, column=4, pady=2)
buttonGd.grid(row=8, column=4, pady=2)
buttonHd.grid(row=9, column=4, pady=2)
buttonId.grid(row=10, column=4, pady=2)

buttonAe = Button(root, text="9")
buttonBe = Button(root, fg="Orange", text="1")
buttonCe = Button(root, fg="Orange", text=" ")
buttonDe = Button(root, fg="Green", text="2")
buttonEe = Button(root, fg="Green", text=" ")
buttonFe = Button(root, fg="Green", text="5")
buttonGe = Button(root, fg="Orange", text=" ")
buttonHe = Button(root, fg="Orange", text="7")
buttonIe = Button(root, fg="Orange", text="0")

buttonAe.grid(row=2, column=5, pady=2)
buttonBe.grid(row=3, column=5, pady=2)
buttonCe.grid(row=4, column=5, pady=2)
buttonDe.grid(row=5, column=5, pady=2)
buttonEe.grid(row=6, column=5, pady=2)
buttonFe.grid(row=7, column=5, pady=2)
buttonGe.grid(row=8, column=5, pady=2)
buttonHe.grid(row=9, column=5, pady=2)
buttonIe.grid(row=10, column=5, pady=2)


buttonAf = Button(root, fg="Orange", text="3")
buttonBf = Button(root, fg="Orange", text="1")
buttonCf = Button(root, fg="Orange", text=" ")
buttonDf = Button(root, fg="Green", text="9")
buttonEf = Button(root, fg="Green", text=" ")
buttonFf = Button(root, fg="Green", text="3")
buttonGf = Button(root, fg="Orange", text="6")
buttonHf = Button(root, fg="Orange", text="2")
buttonIf = Button(root, fg="Orange", text="8")

buttonIf.config(height=50, width=50)

buttonAf.grid(row=2, column=6, pady=2)
buttonBf.grid(row=3, column=6, pady=2)
buttonCf.grid(row=4, column=6, pady=2)
buttonDf.grid(row=5, column=6, pady=2)
buttonEf.grid(row=6, column=6, pady=2)
buttonFf.grid(row=7, column=6, pady=2)
buttonGf.grid(row=8, column=6, pady=2)
buttonHf.grid(row=9, column=6, pady=2)
buttonIf.grid(row=10, column=6, pady=2)

buttonAg = Button(root, fg="Orange", text="3")
buttonBg = Button(root, fg="Orange", text="5")
buttonCg = Button(root, fg="Orange", text=" ")
buttonDg = Button(root, fg="Green", text="8")
buttonEg = Button(root, fg="Green", text=" ")
buttonFg = Button(root, fg="Green", text="3")
buttonGg = Button(root, fg="Orange", text="0")
buttonHg = Button(root, fg="Orange", text="1")
buttonIg = Button(root, fg="Orange", text="9")

buttonAg.grid(row=2, column=7, pady=2)
buttonBg.grid(row=3, column=7, pady=2)
buttonCg.grid(row=4, column=7, pady=2)
buttonDg.grid(row=5, column=7, pady=2)
buttonEg.grid(row=6, column=7, pady=2)
buttonFg.grid(row=7, column=7, pady=2)
buttonGg.grid(row=8, column=7, pady=2)
buttonHg.grid(row=9, column=7, pady=2)
buttonIg.grid(row=10, column=7, pady=2)


buttonAh = Button(root, fg="Orange", text="3")
buttonBh = Button(root, fg="Orange", text="5")
buttonCh = Button(root, fg="Orange", text=" ")
buttonDh = Button(root, fg="Green", text="8")
buttonEh = Button(root, fg="Green", text=" ")
buttonFh = Button(root, fg="Green", text="3")
buttonGh = Button(root, fg="Orange", text="0")
buttonHh = Button(root, fg="Orange", text="1")
buttonIh = Button(root, fg="Orange", text="9")

buttonAh.grid(row=2, column=8, pady=2)
buttonBh.grid(row=3, column=8, pady=2)
buttonCh.grid(row=4, column=8, pady=2)
buttonDh.grid(row=5, column=8, pady=2)
buttonEh.grid(row=6, column=8, pady=2)
buttonFh.grid(row=7, column=8, pady=2)
buttonGh.grid(row=8, column=8, pady=2)
buttonHh.grid(row=9, column=8, pady=2)
buttonIh.grid(row=10, column=8, pady=2)

buttonAi = Button(root, fg="Orange", text="3")
buttonBi = Button(root, fg="Orange", text="5")
buttonCi = Button(root, fg="Orange", text=" ")
buttonDi = Button(root, fg="Green", text="8")
buttonEi = Button(root, fg="Green", text=" ")
buttonFi = Button(root, fg="Green", text="3")
buttonGi = Button(root, fg="Orange", text="0")
buttonHi = Button(root, fg="Orange", text="1")
buttonIi = Button(root, fg="Orange", text="9")
buttonIspace = Label(root, text="")


buttonAi.grid(row=2, column=9, pady=2)
buttonBi.grid(row=3, column=9, pady=2)
buttonCi.grid(row=4, column=9, pady=2)
buttonDi.grid(row=5, column=9, pady=2)
buttonEi.grid(row=6, column=9, pady=2)
buttonFi.grid(row=7, column=9, pady=2)
buttonGi.grid(row=8, column=9, pady=2)
buttonHi.grid(row=9, column=9, pady=2)
buttonIi.grid(row=10, column=9, pady=2)
buttonIspace.grid(row=11, column=9, pady=10)


line1 = [buttonAa, buttonAb, buttonAc, buttonAd, buttonAe, buttonAf, buttonAg, buttonAh, buttonAi]
line2 = [buttonBa, buttonBb, buttonBc, buttonBd, buttonBe, buttonBf, buttonBg, buttonBh, buttonBi]
line3 = [buttonCa, buttonCb, buttonCc, buttonCd, buttonCe, buttonCf, buttonCg, buttonCh, buttonCi]
line4 = [buttonDa, buttonDb, buttonDc, buttonDd, buttonDe, buttonDf, buttonDg, buttonDh, buttonDi]
line5 = [buttonEa, buttonEb, buttonEc, buttonEd, buttonEe, buttonEf, buttonEg, buttonEh, buttonEi]
line6 = [buttonFa, buttonFb, buttonFc, buttonFd, buttonFe, buttonFf, buttonFg, buttonFh, buttonFi]
line7 = [buttonGa, buttonGb, buttonGc, buttonGd, buttonGe, buttonGf, buttonGg, buttonGh, buttonGi]
line8 = [buttonHa, buttonHb, buttonHc, buttonHd, buttonHe, buttonHf, buttonHg, buttonHh, buttonHi]
line9 = [buttonIa, buttonIb, buttonIc, buttonId, buttonIe, buttonIf, buttonIg, buttonIh, buttonIi]

column1 = [buttonAa, buttonBa, buttonCa, buttonDa, buttonEa, buttonFa, buttonGa, buttonHa, buttonIa]
column2 = [buttonAb, buttonBb, buttonCb, buttonDb, buttonEb, buttonFb, buttonGb, buttonHb, buttonIb]
column3 = [buttonAc, buttonBc, buttonCc, buttonDc, buttonEc, buttonFc, buttonGc, buttonHc, buttonIc]
column4 = [buttonAd, buttonBd, buttonCd, buttonDd, buttonEd, buttonFd, buttonGd, buttonHd, buttonId]
column5 = [buttonAf, buttonBf, buttonCf, buttonDf, buttonEf, buttonFf, buttonGf, buttonHf, buttonIf]
column6 = [buttonAg, buttonBg, buttonCg, buttonDg, buttonEg, buttonFg, buttonGg, buttonHg, buttonIg]
column7 = [buttonAe, buttonBe, buttonCe, buttonDe, buttonEe, buttonFe, buttonGe, buttonHe, buttonIe]
column8 = [buttonAh, buttonBh, buttonCh, buttonDh, buttonEh, buttonFh, buttonGh, buttonHh, buttonIh]
column9 = [buttonAi, buttonBi, buttonCi, buttonDi, buttonEi, buttonFi, buttonGi, buttonHi, buttonIi]

three_or_three1 = [buttonAa, buttonAb, buttonAc, buttonBa,
                   buttonBb, buttonBc, buttonCa, buttonCb, buttonCc]


buttons_list = [buttonAb, buttonAa, buttonAc, buttonAd, buttonAe,
                buttonAf, buttonAg, buttonAh, buttonAi, buttonBa, buttonBb, buttonBc, buttonBd, buttonBe,
                buttonBf, buttonBg, buttonBh, buttonBi, buttonCa, buttonCb, buttonCc, buttonCd, buttonCe,
                buttonCf, buttonCg, buttonCh, buttonCi, buttonDa, buttonDb, buttonDc, buttonDd, buttonDe,
                buttonDf, buttonDg, buttonDh, buttonDi, buttonEa, buttonEb, buttonEc, buttonEd, buttonEe,
                buttonEf, buttonEg, buttonEh, buttonEi, buttonFa, buttonFb, buttonFc, buttonFd, buttonFe,
                buttonFf, buttonFg, buttonFh, buttonFi, buttonGa, buttonGb, buttonGc, buttonGd, buttonGe,
                buttonGf, buttonGg, buttonGh, buttonGi, buttonHa, buttonHb, buttonHc, buttonHd, buttonHe,
                buttonHf, buttonHg, buttonHh, buttonHi, buttonIa, buttonIb, buttonIc, buttonId, buttonIe,
                buttonIf, buttonIg, buttonIh, buttonIi]

for button in buttons_list:
    button.config(height=50, width=50)

orange_boxes = [buttonAa, buttonAb, buttonAc, buttonAg, buttonAh, buttonAi, buttonBa, buttonBb, buttonBc, buttonBg,
                buttonBh, buttonBi, buttonCa, buttonCb, buttonCc, buttonCg, buttonCh, buttonCi, buttonDd, buttonDe,
                buttonDf, buttonEd, buttonEe, buttonFd, buttonFe, buttonFf, buttonEf,  buttonGa, buttonGb,
                buttonGc, buttonGg, buttonGh, buttonGi, buttonHa, buttonHb,
                buttonHc, buttonHg, buttonHh, buttonHi, buttonIa, buttonIb, buttonIc, buttonIg, buttonIh, buttonIi]

for button in orange_boxes:
    button.config(background="gray95", fg="gray10")

grey_boxes = [buttonAd, buttonAe, buttonAf, buttonBd, buttonBe, buttonBf, buttonCd, buttonCe, buttonCf, buttonDa,
              buttonDb,  buttonDc, buttonDg, buttonDh, buttonDi, buttonEa, buttonEb,
              buttonEc, buttonEg, buttonEh, buttonEi, buttonFa, buttonFb, buttonFc, buttonFg, buttonFh, buttonFi,
              buttonGd, buttonGe, buttonGf, buttonHd, buttonHe, buttonHf, buttonId, buttonIe, buttonIf]

for button in grey_boxes:
    button.config(background="khaki1", fg="black")

for button in buttons_list:
    button.bind("<Button-1>", leftClick)


for button in buttons_list:
    button.bind("<Key>", key)

root.mainloop()
