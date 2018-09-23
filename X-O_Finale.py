from turtle import *
from random import *


def table():    # crta tabelu
    clear()    # brise prethodno nacrtano
    hideturtle()    # sakriva kornjacu
    setheading(0)
    speed(100)    # brzina crtanja
    pensize(5)
    penup()
    setposition(-160, -75)
    pendown()
    fd(340)
    penup()
    setposition(-160, 35)
    pendown()
    fd(340)
    penup()
    setposition(-50, -185)
    pendown()
    lt(90)
    fd(330)
    penup()
    setposition(60, -185)
    pendown()
    fd(330)


def tip():    # crta izborni meni
    clear()
    hideturtle()
    speed(100)
    pensize(5)
    penup()
    setposition(-180, -45)
    setheading(0)
    pendown()
    fd(150)
    lt(90)
    fd(90)
    lt(90)
    fd(150)
    lt(90)
    fd(90)
    penup()
    setposition(-120, -15)
    pendown()
    write("1v1", font=("Arial", 20, "normal"))    # pise tekst
    penup()
    setposition(120, -45)
    setheading(0)
    pendown()
    fd(150)
    lt(90)
    fd(90)
    lt(90)
    fd(150)
    lt(90)
    fd(90)
    penup()
    setposition(170, -15)
    pendown()
    write("vsPC", font=("Arial", 20, "normal"))


def tezina():    # crta izbor tezine
    clear()
    hideturtle()
    speed(100)
    pensize(5)
    penup()
    setposition(-180, -45)
    setheading(0)
    pendown()
    fd(150)
    lt(90)
    fd(90)
    lt(90)
    fd(150)
    lt(90)
    fd(90)
    penup()
    setposition(-135, -15)
    pendown()
    write("Easy", font=("Arial", 20, "normal"))
    penup()
    setposition(120, -45)
    setheading(0)
    pendown()
    fd(150)
    lt(90)
    fd(90)
    lt(90)
    fd(150)
    lt(90)
    fd(90)
    penup()
    setposition(170, -15)
    pendown()
    write("Hard", font=("Arial", 20, "normal"))


def izbor(x, y):    # interakcija sa izbornim menijem
    if x in range(-180, -30) and y in range(-45, 45):    # igra 1v1
        table()    # crta tabelu
        onscreenclick(nopc)    # pokrece funkciju za 1v1
    elif x in range(120, 270) and y in range(-45, 45):    # igra vsPC
        tezina()    # crta meni za izbor tezine
        onscreenclick(izbortezine)    # pokrece funkciju izbortezine


def izbortezine(x, y):    # interakcija sa odabirom tezine
    if x in range(-180, -30) and y in range(-45, 45):
        table()
        onscreenclick(pce)    # funkcija za laganog protivnika
    elif x in range(120, 270) and y in range(-45, 45):
        table()
        onscreenclick(pch)    # funkcija za tezek protivnika


def nopc(x, y):    # provjerava gdje je korisnik kliknuo
    if x in range(-160, -50) and y in range(35, 155):     # polje 1
        if l.count(1) != 0:    # provjerava je li zauzeto polje
            if len(l) % 2 != 0:    # provjerava da li je red na x
                xl.append(1)    # dodaje zauzeto polje znakom "x" listi xl
                setheading(45)    # priprema za crtanje x
                for i in range(5):    # crta x
                    penup()
                    setpos(-105, 90)
                    pendown()
                    fd(60)
                    rt(90)
            else:    # ako nije red na x onda je red na o
                yl.append(1)    # dodaje zauzeto polje znakom "o" listi yl
                setheading(90)    # priprema za crtanje
                penup()
                setpos(-65, 90)
                pendown()
                circle(40)
            l.remove(1)    # oznacava da je polje zauzeto
    if x in range(-50, 60) and y in range(35, 155):    # polje 2
        if l.count(2) != 0:
            if len(l) % 2 != 0:
                xl.append(2)
                setheading(45)
                for i in range(5):
                    penup()
                    setpos(5, 90)
                    pendown()
                    fd(60)
                    rt(90)
            else:
                yl.append(2)
                setheading(90)
                penup()
                setpos(45, 90)
                pendown()
                circle(40)
            l.remove(2)
    if x in range(60, 170) and y in range(35, 155):    # polje 3
        if l.count(3) != 0:
            if len(l) % 2 != 0:
                xl.append(3)
                setheading(45)
                for i in range(5):
                    penup()
                    setpos(115, 90)
                    pendown()
                    fd(60)
                    rt(90)
            else:
                yl.append(3)
                setheading(90)
                penup()
                setpos(155, 90)
                pendown()
                circle(40)
            l.remove(3)
    if x in range(-160, -50) and y in range(-75, 45):    # polje 4
        if l.count(4) != 0:
            if len(l) % 2 != 0:
                xl.append(4)
                setheading(45)
                for i in range(5):
                    penup()
                    setpos(-105, -20)
                    pendown()
                    fd(60)
                    rt(90)
            else:
                yl.append(4)
                setheading(90)
                penup()
                setpos(-65, -20)
                pendown()
                circle(40)
            l.remove(4)
    if x in range(-50, 60) and y in range(-75, 45):    # polje 5
        if l.count(5) != 0:
            if len(l) % 2 != 0:
                xl.append(5)
                setheading(45)
                for i in range(5):
                    penup()
                    setpos(5, -20)
                    pendown()
                    fd(60)
                    rt(90)
            else:
                yl.append(5)
                setheading(90)
                penup()
                setpos(45, -20)
                pendown()
                circle(40)
            l.remove(5)
    if x in range(60, 170) and y in range(-75, 45):    # polje 6
        if l.count(6) != 0:
            if len(l) % 2 != 0:
                xl.append(6)
                setheading(45)
                for i in range(5):
                    penup()
                    setpos(115, -20)
                    pendown()
                    fd(60)
                    rt(90)
            else:
                yl.append(6)
                setheading(90)
                penup()
                setpos(155, -20)
                pendown()
                circle(40)
            l.remove(6)
    if x in range(-160, -50) and y in range(-185, -65):    # polje 7
        if l.count(7) != 0:
            if len(l) % 2 != 0:
                xl.append(7)
                setheading(45)
                for i in range(5):
                    penup()
                    setpos(-105, -130)
                    pendown()
                    fd(60)
                    rt(90)
            else:
                yl.append(7)
                setheading(90)
                penup()
                setpos(-65, -130)
                pendown()
                circle(40)
            l.remove(7)
    if x in range(-50, 60) and y in range(-185, -65):    # polje 8
        if l.count(8) != 0:
            if len(l) % 2 != 0:
                xl.append(8)
                setheading(45)
                for i in range(5):
                    penup()
                    setpos(5, -130)
                    pendown()
                    fd(60)
                    rt(90)
            else:
                yl.append(8)
                setheading(90)
                penup()
                setpos(45, -130)
                pendown()
                circle(40)
            l.remove(8)
    if x in range(60, 170) and y in range(-185, -65):    # polje 9
        if l.count(9) != 0:
            if len(l) % 2 != 0:
                xl.append(9)
                setheading(45)
                for i in range(5):
                    penup()
                    setpos(115, -130)
                    pendown()
                    fd(60)
                    rt(90)
            else:
                yl.append(9)
                setheading(90)
                penup()
                setpos(155, -130)
                pendown()
                circle(40)
            l.remove(9)
    if win(xl) is True:    # provjerava da li je x pobjednik
        print("Winner is X")
        penup()
        setposition(-270, 160)
        pendown()
        write("Winner is X", font=("Arial", 80, "bold"))
        exitonclick()    # zatvara turtle
    elif win(yl) is True:    # provjerava da li je o pobjednik
        print("Winner is O")
        penup()
        setposition(-270, 160)
        pendown()
        write("Winner is O", font=("Arial", 80, "bold"))
        exitonclick()
    elif len(l) == 0:    # ukoliko nema vise prznih mjesta ispisuje "draw"
        print("Draw")
        penup()
        setposition(-120, 160)
        pendown()
        write("Draw", font=("Arial", 80, "bold"))
        exitonclick()


def pce(x, y):    # easy pc
    if x in range(-160, 190) and y in range(-190, 160):
        if len(l) % 2 != 0:    # provjerava da li je korisnik na potezu
            if x in range(-160, -50) and y in range(35, 155):    # polje 1
                if l.count(1) != 0:    # provjerava da li je slobodno polje
                    xl.append(1)    # dodaje zauzeto polje znakom "x" listi xl
                    setheading(45)    # priprema za crtanje
                    for i in range(5):    # crtanje znaka x
                        penup()
                        setpos(-105, 90)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(1)    # oznacava polje kao zauzeto
            if x in range(-50, 60) and y in range(35, 155):    # polje 2
                if l.count(2) != 0:
                    xl.append(2)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(5, 90)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(2)
            if x in range(60, 170) and y in range(35, 155):    # polje 3
                if l.count(3) != 0:
                    xl.append(3)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(115, 90)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(3)
            if x in range(-160, -50) and y in range(-75, 45):    # polje 4
                if l.count(4) != 0:
                    xl.append(4)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(-105, -20)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(4)
            if x in range(-50, 60) and y in range(-75, 45):    # polje 5
                if l.count(5) != 0:
                    xl.append(5)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(5, -20)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(5)
            if x in range(60, 170) and y in range(-75, 45):    # polje 6
                if l.count(6) != 0:
                    xl.append(6)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(115, -20)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(6)
            if x in range(-160, -50) and y in range(-185, -65):    # polje 7
                if l.count(7) != 0:
                    xl.append(7)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(-105, -130)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(7)
            if x in range(-50, 60) and y in range(-185, -65):    # polje 8
                if l.count(8) != 0:
                    xl.append(8)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(5, -130)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(8)
            if x in range(60, 170) and y in range(-185, -65):    # polje 9
                if l.count(9) != 0:
                    xl.append(9)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(115, -130)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(9)
        if win(xl) is True:    # provjerava da li je x pobjednik
            print("Winner is X")
            penup()
            setposition(-270, 160)
            pendown()
            write("Winner is X", font=("Arial", 80, "bold"))
            exitonclick()
        if len(l) != 0:    # provjerava da li ima slobodnih mjesta
            pceasy()    # funkcija za laganog protivnika
            if win(yl) is True:    # provjerava da li je o pobjednik
                print("Winner is O")
                penup()
                setposition(-270, 160)
                pendown()
                write("Winner is O", font=("Arial", 80, "bold"))
                exitonclick()
        elif len(l) == 0:
            print("Draw")
            penup()
            setposition(-120, 160)
            pendown()
            write("Draw", font=("Arial", 80, "bold"))
            exitonclick()


def pch(x, y):    # hard pc
    if x in range(-160, 190) and y in range(-190, 160):
        if len(l) % 2 != 0:    # provjerava da li je korisnik na potezu
            if x in range(-160, -50) and y in range(35, 155):    # polje 1
                if l.count(1) != 0:    # provjerava da li je slobodno polje
                    xl.append(1)    # dodaje zauzeto polje znakom "x" listi xl
                    setheading(45)    # priprema za crtanje
                    for i in range(5):    # crtanje znaka x
                        penup()
                        setpos(-105, 90)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(1)    # oznacava polje kao zauzeto
            if x in range(-50, 60) and y in range(35, 155):    # polje 2
                if l.count(2) != 0:
                    xl.append(2)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(5, 90)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(2)
            if x in range(60, 170) and y in range(35, 155):    # polje 3
                if l.count(3) != 0:
                    xl.append(3)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(115, 90)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(3)
            if x in range(-160, -50) and y in range(-75, 45):    # polje 4
                if l.count(4) != 0:
                    xl.append(4)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(-105, -20)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(4)
            if x in range(-50, 60) and y in range(-75, 45):    # polje 5
                if l.count(5) != 0:
                    xl.append(5)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(5, -20)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(5)
            if x in range(60, 170) and y in range(-75, 45):    # polje 6
                if l.count(6) != 0:
                    xl.append(6)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(115, -20)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(6)
            if x in range(-160, -50) and y in range(-185, -65):    # polje 7
                if l.count(7) != 0:
                    xl.append(7)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(-105, -130)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(7)
            if x in range(-50, 60) and y in range(-185, -65):    # polje 8
                if l.count(8) != 0:
                    xl.append(8)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(5, -130)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(8)
            if x in range(60, 170) and y in range(-185, -65):    # polje 9
                if l.count(9) != 0:
                    xl.append(9)
                    setheading(45)
                    for i in range(5):
                        penup()
                        setpos(115, -130)
                        pendown()
                        fd(60)
                        rt(90)
                    l.remove(9)
        if win(xl) is True:    # provjerava da li je x pobjednik
            print("Winner is X")
            penup()
            setposition(-270, 160)
            pendown()
            write("Winner is X", font=("Arial", 80, "bold"))
            exitonclick()
        else:
            if len(l) != 0:    # provjerava da li ima slobodnih mjesta
                a = pchard()    # funkcija za teskog protivnika
                if a == 1:    # polje 1
                    yl.append(1)    # dodaje zauzeto polje znakom "o" listi yl
                    setheading(90)    # priprema za crtanje
                    penup()
                    setpos(-65, 90)
                    pendown()
                    circle(40)
                    l.remove(1)    # oznacava polje kao zauzeto
                elif a == 2:    # polje 2
                    yl.append(2)
                    setheading(90)
                    penup()
                    setpos(45, 90)
                    pendown()
                    circle(40)
                    l.remove(2)
                elif a == 3:    # polje 3
                    yl.append(3)
                    setheading(90)
                    penup()
                    setpos(155, 90)
                    pendown()
                    circle(40)
                    l.remove(3)
                elif a == 4:    # polje 4
                    yl.append(4)
                    setheading(90)
                    penup()
                    setpos(-65, -20)
                    pendown()
                    circle(40)
                    l.remove(4)
                elif a == 5:    # polje 5
                    yl.append(5)
                    setheading(90)
                    penup()
                    setpos(45, -20)
                    pendown()
                    circle(40)
                    l.remove(5)
                elif a == 6:    # polje 6
                    yl.append(6)
                    setheading(90)
                    penup()
                    setpos(155, -20)
                    pendown()
                    circle(40)
                    l.remove(6)
                elif a == 7:    # polje 7
                    yl.append(7)
                    setheading(90)
                    penup()
                    setpos(-65, -130)
                    pendown()
                    circle(40)
                    l.remove(7)
                elif a == 8:    # polje 8
                    yl.append(8)
                    setheading(90)
                    penup()
                    setpos(45, -130)
                    pendown()
                    circle(40)
                    l.remove(8)
                elif a == 9:    # polje 9
                    yl.append(9)
                    setheading(90)
                    penup()
                    setpos(155, -130)
                    pendown()
                    circle(40)
                    l.remove(9)
            if win(yl) is True:    # provjerava da li je o pobjednik
                print("Winner is O")
                penup()
                setposition(-270, 160)
                pendown()
                write("Winner is O", font=("Arial", 80, "bold"))
                exitonclick()
            elif len(l) == 0:
                print("Draw")
                penup()
                setposition(-120, 160)
                pendown()
                write("Draw", font=("Arial", 80, "bold"))
                exitonclick()


def pceasy():    # pomocni pce
    a = choice(l)    # bira nasumicno polje iz liste preostalih polja
    if a == 1:    # polje 1
        yl.append(1)    # dodaje zauzeto polje znakom "o" listi yl
        setheading(90)    # priprema za crtanje
        penup()
        setpos(-65, 90)
        pendown()
        circle(40)
        l.remove(1)    # oznacava polje kao zauzeto
    elif a == 2:    # polje 2
        yl.append(2)
        setheading(90)
        penup()
        setpos(45, 90)
        pendown()
        circle(40)
        l.remove(2)
    elif a == 3:    # polje 3
        yl.append(3)
        setheading(90)
        penup()
        setpos(155, 90)
        pendown()
        circle(40)
        l.remove(3)
    elif a == 4:    # polje 4
        yl.append(4)
        setheading(90)
        penup()
        setpos(-65, -20)
        pendown()
        circle(40)
        l.remove(4)
    elif a == 5:    # polje 5
        yl.append(5)
        setheading(90)
        penup()
        setpos(45, -20)
        pendown()
        circle(40)
        l.remove(5)
    elif a == 6:    # polje 6
        yl.append(6)
        setheading(90)
        penup()
        setpos(155, -20)
        pendown()
        circle(40)
        l.remove(6)
    elif a == 7:    # polje 7
        yl.append(7)
        setheading(90)
        penup()
        setpos(-65, -130)
        pendown()
        circle(40)
        l.remove(7)
    elif a == 8:    # polje 8
        yl.append(8)
        setheading(90)
        penup()
        setpos(45, -130)
        pendown()
        circle(40)
        l.remove(8)
    elif a == 9:    # polje 9
        yl.append(9)
        setheading(90)
        penup()
        setpos(155, -130)
        pendown()
        circle(40)
        l.remove(9)


def pchard():    # pomocni pch
    if yl.count(1) == 1 and yl.count(2) == 1 and l.count(3) == 1:
        a = 3
    elif yl.count(1) == 1 and yl.count(3) == 1 and l.count(2) == 1:
        a = 2
    elif yl.count(2) == 1 and yl.count(3) == 1 and l.count(1) == 1:
        a = 1
    elif yl.count(4) == 1 and yl.count(5) == 1 and l.count(6) == 1:
        a = 6
    elif yl.count(4) == 1 and yl.count(6) == 1 and l.count(5) == 1:
        a = 5
    elif yl.count(5) == 1 and yl.count(6) == 1 and l.count(4) == 1:
        a = 4
    elif yl.count(7) == 1 and yl.count(8) == 1 and l.count(9) == 1:
        a = 9
    elif yl.count(7) == 1 and yl.count(9) == 1 and l.count(8) == 1:
        a = 8
    elif yl.count(8) == 1 and yl.count(9) == 1 and l.count(7) == 1:
        a = 7
    elif yl.count(1) == 1 and yl.count(4) == 1 and l.count(7) == 1:
        a = 7
    elif yl.count(1) == 1 and yl.count(7) == 1 and l.count(4) == 1:
        a = 4
    elif yl.count(4) == 1 and yl.count(7) == 1 and l.count(1) == 1:
        a = 1
    elif yl.count(2) == 1 and yl.count(5) == 1 and l.count(8) == 1:
        a = 8
    elif yl.count(2) == 1 and yl.count(8) == 1 and l.count(5) == 1:
        a = 5
    elif yl.count(5) == 1 and yl.count(8) == 1 and l.count(2) == 1:
        a = 2
    elif yl.count(3) == 1 and yl.count(6) == 1 and l.count(9) == 1:
        a = 9
    elif yl.count(3) == 1 and yl.count(9) == 1 and l.count(6) == 1:
        a = 6
    elif yl.count(6) == 1 and yl.count(9) == 1 and l.count(3) == 1:
        a = 3
    elif yl.count(1) == 1 and yl.count(5) == 1 and l.count(9) == 1:
        a = 9
    elif yl.count(1) == 1 and yl.count(9) == 1 and l.count(5) == 1:
        a = 5
    elif yl.count(5) == 1 and yl.count(9) == 1 and l.count(1) == 1:
        a = 1
    elif yl.count(3) == 1 and yl.count(5) == 1 and l.count(7) == 1:
        a = 7
    elif yl.count(3) == 1 and yl.count(7) == 1 and l.count(5) == 1:
        a = 5
    elif yl.count(5) == 1 and yl.count(7) == 1 and l.count(3) == 1:
        a = 3
    elif xl.count(1) == 1 and xl.count(2) == 1 and l.count(3) == 1:
        a = 3
    elif xl.count(1) == 1 and xl.count(3) == 1 and l.count(2) == 1:
        a = 2
    elif xl.count(2) == 1 and xl.count(3) == 1 and l.count(1) == 1:
        a = 1
    elif xl.count(4) == 1 and xl.count(5) == 1 and l.count(6) == 1:
        a = 6
    elif xl.count(4) == 1 and xl.count(6) == 1 and l.count(5) == 1:
        a = 5
    elif xl.count(5) == 1 and xl.count(6) == 1 and l.count(4) == 1:
        a = 4
    elif xl.count(7) == 1 and xl.count(8) == 1 and l.count(9) == 1:
        a = 9
    elif xl.count(7) == 1 and xl.count(9) == 1 and l.count(8) == 1:
        a = 8
    elif xl.count(8) == 1 and xl.count(9) == 1 and l.count(7) == 1:
        a = 7
    elif xl.count(1) == 1 and xl.count(4) == 1 and l.count(7) == 1:
        a = 7
    elif xl.count(1) == 1 and xl.count(7) == 1 and l.count(4) == 1:
        a = 4
    elif xl.count(4) == 1 and xl.count(7) == 1 and l.count(1) == 1:
        a = 1
    elif xl.count(2) == 1 and xl.count(5) == 1 and l.count(8) == 1:
        a = 8
    elif xl.count(2) == 1 and xl.count(8) == 1 and l.count(5) == 1:
        a = 5
    elif xl.count(5) == 1 and xl.count(8) == 1 and l.count(2) == 1:
        a = 2
    elif xl.count(3) == 1 and xl.count(6) == 1 and l.count(9) == 1:
        a = 9
    elif xl.count(3) == 1 and xl.count(9) == 1 and l.count(6) == 1:
        a = 6
    elif xl.count(6) == 1 and xl.count(9) == 1 and l.count(3) == 1:
        a = 3
    elif xl.count(1) == 1 and xl.count(5) == 1 and l.count(9) == 1:
        a = 9
    elif xl.count(1) == 1 and xl.count(9) == 1 and l.count(5) == 1:
        a = 5
    elif xl.count(5) == 1 and xl.count(9) == 1 and l.count(1) == 1:
        a = 1
    elif xl.count(3) == 1 and xl.count(5) == 1 and l.count(7) == 1:
        a = 7
    elif xl.count(3) == 1 and xl.count(7) == 1 and l.count(5) == 1:
        a = 5
    elif xl.count(5) == 1 and xl.count(7) == 1 and l.count(3) == 1:
        a = 3
    else:
        a = choice(l)
    return(a)


def win(a):    # provjerava da li je neko pobijedio
    if (a.count(1) == 1 and a.count(2) == 1 and a.count(3) == 1
    or a.count(4) == 1 and a.count(5) == 1 and a.count(6) == 1
    or a.count(7) == 1 and a.count(8) == 1 and a.count(9) == 1
    or a.count(1) == 1 and a.count(4) == 1 and a.count(7) == 1
    or a.count(2) == 1 and a.count(5) == 1 and a.count(8) == 1
    or a.count(3) == 1 and a.count(6) == 1 and a.count(9) == 1
    or a.count(1) == 1 and a.count(5) == 1 and a.count(9) == 1
    or a.count(3) == 1 and a.count(5) == 1 and a.count(7) == 1):
        return(True)    # vraca true ako je jedna od kombinacija zadovoljena


xl = []    # lista poteza x
yl = []    # lista poteza o
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # lista mogucih poteza

tip()    # crta pocetni meni
onscreenclick(izbor)    # interakcija sa pocetnim menijem
mainloop()    # ne dozvoljava turtle da se zatvori