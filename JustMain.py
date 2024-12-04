from tkinter import *

window = Tk()
window.title("JustCookie")
window.geometry("720x480")
window.minsize(480, 360)
window.maxsize(720, 480)
window.config(background='#00C886')

count = 0
def count_click():
    global count
    count+=1
    print(count)
    window.after(10000, fin)

frame = Frame(window, bg='#00C886')
infovar = StringVar()
infovar.set("Bonne Chance !")
info = Label(window, textvariable=infovar, fg='white', bg='#00C886',
              font=("Comic sans MS", 15), bd=0, width=15, height=1)
info.pack(side=BOTTOM, pady=13)

def fin():
    window.destroy()

label_title = Label(frame, text="Cookie Compteur", font=("Comic sans MS", 40), 
bd=7, relief=SUNKEN, bg='#00C850')
label_title.pack(side=TOP, pady=10)

width = 300
height =300
image = PhotoImage(file="cookie.png").zoom(1).subsample(5)
canvas = Canvas(frame, width=width, height=height, bg='#000000')
canvas.create_image(width/2, height/2, image=image)
#canvas.pack(pady=5)

sub_title2 = Label(frame, text=" Cliquez içi →  ", font=("Comic sans MS", 20), 
bd=7, relief=SUNKEN, bg='#00C850')
sub_title2.pack(side=(LEFT))

coookie_button = Button(frame, text="Cliquez ici !", image=image, 
                    command=(count_click), font=("Comic sans MS", 25), 
bg='blue', fg='#00C886', bd=13, relief=SUNKEN)
coookie_button.pack(side=LEFT, pady=13, padx=21)

sub_title = Label(frame, text=" ← Cliquez içi ", font=("Comic sans MS", 20), 
bd=7, relief=SUNKEN, bg='#00C850')
sub_title.pack(side=(RIGHT))

frame.pack(expand=YES)
window.mainloop()

file = open("scoreCookie.txt", "a+")
file.write(str(int( count))+"\n")
file.close()


def lire_scores():
    scores = []
    with open("scoreCookie.txt", "r") as fichier_scores:
        for ligne in fichier_scores.readlines():
            scores.append(int(ligne))
    return scores

liste_scores = lire_scores()
if liste_scores:
    score_max = max(liste_scores)
    print("Le meilleur score est :", score_max)
else:
    print("Aucun score n'a été enregistré.")

print("BIEN JOUE VOTRE SCORE EST DE {} CLICKS !".format(count))
print("Soit en moyennne {} clicks par secondes !".format(int(count)/10))
if count < 10 :
    print("C'est loin du reccord du monde de 27 clicks en 1 secondes :/")
elif count == 83 :
    print("C'est impossible...Le reccord du monde !!!")
elif 60 < count < 70 :
    print("Pas Mal ! Tu est a {} clicks du Reccord Du Monde !".format(int(83-count)))
elif 50 < count < 60 :
    print("C'est le score moyen ! Tu est a {} clicks du Reccord Du Monde !".format(int(83-count)))
elif 10 < count < 40 :
    print("Ton score est mauvais ! Reessaye !")
else:
    print("AIE AIE AIE, Tu est loin du Record du Monde ! Reessaye !")