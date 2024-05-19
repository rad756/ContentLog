import csv
import os
import sys
import tkinter as tk
from tkinter import Button, Entry, Frame, Label, Listbox, Toplevel, ttk

def main():
    global glo

    class glo:
        #Variables
        gameFile = "game.csv"
        systemFile = "system.csv"
        movieFile = "movie.csv"
        genreFile = "genre.csv"
        showFile = "show.csv"
        tempFile = "temp.txt"

        #Init GUI
        root = tk.Tk()
        mainTitle = "Content Log"




    glo.root.title(glo.mainTitle)
    glo.root.geometry("580x640")

    startFunc()
    makeGUI()
    populateGUI()


    glo.root.mainloop()

def makeGUI():
    makeNotebook()
    makeFrame()
    makeGame()
    makeMovie()
    makeShow()

def populateGUI():
    #Games
    populateGameListbox()
    populateGameSystems()
    populateGameFinished()

    #Movies
    populateMovieListbox()
    populateMovieGenre()
    populateMovieFinished()
    
    #Shows
    populateShowListbox()
    
def makeNotebook():
    global note

    class note:
        book = ttk.Notebook(glo.root)

    #create notebook, this does tabs
    note.book.pack(pady=10, expand=True)


def makeFrame():
    global frm
    class frm:
        game = ttk.Frame(note.book, width=900, height=550)
        movie = ttk.Frame(note.book, width=900, height=550)
        show = ttk.Frame(note.book, width=900, height=550)

    frm.game.pack(fill="both", expand=True)
    frm.movie.pack(fill="both", expand=True)
    frm.show.pack(fill="both", expand=True)

    note.book.add(frm.game, text="Games")
    note.book.add(frm.movie, text="Movies")
    note.book.add(frm.show, text="Show")

def makeGame():
    global game

    class game:
        #Frames
        frm1 = tk.Frame(frm.game, width=10, height=550)
        frm2 = tk.Frame(frm.game, width=10, height=550)

        frm1.grid(row=0, column=0, sticky="nsew")
        frm2.grid(row=0, column=1, sticky="nsew")

        frm.game.grid_columnconfigure(0, weight=5, minsize=300)
        frm.game.grid_columnconfigure(1, weight=1)

        #Variables
        count = 0

        #Frame 1
        lblDescription = Label(frm1, text="# - Game - System")
        lbx = Listbox(frm1, height=34, exportselection=False)#exportselection=False makes selection highlighted until a button is presses

        lbx.bind('<Double-1>', lambda x: copyGame())

        #Frame 2
        lblName = Label(frm2, text="Name")
        entName = Entry(frm2, width=30)
        lblSystems = Label(frm2, text="System")
        cbxSystems = ttk.Combobox(frm2, width=25)
        btnAdd = Button(frm2, text="Add Game", command=lambda: addGame())
        btnDelete = Button(frm2, text="Delete Game", command=lambda: deleteGame())
        btnChange = Button(frm2, text="Change Selected Game", command=lambda: changeGame())
        btnChangeSystems = Button(frm2, text="Change Systems", command=lambda: openSystemsWindow())
        lblFinshed = Label(frm2, text="Finished: ")


    game.lblDescription.pack(padx = 10, pady = 5)
    game.lbx.pack(fill=tk.BOTH, padx = 10, pady = 5)

    game.lblName.pack(padx = 10, pady = 5)
    game.entName.pack(padx = 10, pady = 5)
    game.lblSystems.pack(padx = 10, pady = 5)
    game.cbxSystems.pack(padx = 10, pady = 5)
    game.btnAdd.pack(padx = 10, pady = 5)
    game.btnDelete.pack(padx = 10, pady = 5)
    game.btnChange.pack(padx = 10, pady = 5)
    game.btnChangeSystems.pack(padx = 10, pady = 5)
    game.lblFinshed.pack(padx = 10, pady = 5)

def makeMovie():
    global movie

    class movie:
        #Frames
        frm1 = tk.Frame(frm.movie, width=10, height=550)
        frm2 = tk.Frame(frm.movie, width=10, height=550)

        frm1.grid(row=0, column=0, sticky="nsew")
        frm2.grid(row=0, column=1, sticky="nsew")

        frm.movie.grid_columnconfigure(0, weight=5, minsize=300)
        frm.movie.grid_columnconfigure(1, weight=1)

        #Variables
        count = 0

        #Frame 1
        lblDescription = Label(frm1, text="# - Movie - Genre")
        lbx = Listbox(frm1, height=34, exportselection=False)#exportselection=False makes selection highlighted until a button is presses

        lbx.bind('<Double-1>', lambda x: copyMovie())

        #Frame 2
        lblName = Label(frm2, text="Name")
        entName = Entry(frm2, width=30)
        lblGenre = Label(frm2, text="Genre")
        cbxGenre = ttk.Combobox(frm2, width=25)
        btnAdd = Button(frm2, text="Add Movie", command=lambda: addMovie())
        btnDelete = Button(frm2, text="Delete Movie", command=lambda: deleteMovie())
        btnChange = Button(frm2, text="Change Selected Movie", command=lambda: changeMovie())
        btnChangeGenre = Button(frm2, text="Change Genres", command=lambda: openGenreWindow())
        lblFinshed = Label(frm2, text="Finished: ")


    movie.lblDescription.pack(padx = 10, pady = 5)
    movie.lbx.pack(fill=tk.BOTH, padx = 10, pady = 5)

    movie.lblName.pack(padx = 10, pady = 5)
    movie.entName.pack(padx = 10, pady = 5)
    movie.lblGenre.pack(padx = 10, pady = 5)
    movie.cbxGenre.pack(padx = 10, pady = 5)
    movie.btnAdd.pack(padx = 10, pady = 5)
    movie.btnDelete.pack(padx = 10, pady = 5)
    movie.btnChange.pack(padx = 10, pady = 5)
    movie.btnChangeGenre.pack(padx = 10, pady = 5)
    movie.lblFinshed.pack(padx = 10, pady = 5)

def makeShow():
    global show

    class show:
        #Frames
        frm1 = tk.Frame(frm.show, width=10, height=550)
        frm2 = tk.Frame(frm.show, width=10, height=550)

        frm1.grid(row=0, column=0, sticky="nsew")
        frm2.grid(row=0, column=1, sticky="nsew")

        frm.show.grid_columnconfigure(0, weight=5, minsize=300)
        frm.show.grid_columnconfigure(1, weight=1)

        #Variables
        finished = False

        #Frame 1
        lblDescription = Label(frm1, text="# - Show - Season - Episode - Finished")
        lbx = Listbox(frm1, height=34, exportselection=False)#exportselection=False makes selection highlighted until a button is presses

        lbx.bind('<Double-1>', lambda x: copyShow())

        #Frame 2
        lblName = Label(frm2, text="Name")
        entName = Entry(frm2, width=30)
        lblSeason = Label(frm2, text="Season")
        btnMoreSeason = Button(frm2, text="+", command=lambda: moreValue(show.entSeason))
        entSeason = Entry(frm2, width=10)
        btnLessSeason = Button(frm2, text="-", command=lambda: lessValue(show.entSeason))
        lblEpisode = Label(frm2, text="Episode")
        btnMoreEpisode = Button(frm2, text="+", command=lambda: moreValue(show.entEpisode))
        entEpisode = Entry(frm2, width=10)
        btnLessEpisode = Button(frm2, text="-", command=lambda: lessValue(show.entEpisode))
        lblFinished = Label(frm2, text="Finished")
        btnFinished = Button(frm2, text="No", command=lambda: showFinishedButtonFunc())
        btnAdd = Button(frm2, text="Add Show", command=lambda: addShow())
        btnDelete = Button(frm2, text="Delete Show", command=lambda: deleteShow())
        btnChange = Button(frm2, text="Change Selected Show", command=lambda: changeShow())


    show.lblDescription.pack(padx = 10, pady = 5)
    show.lbx.pack(fill=tk.BOTH, padx = 10, pady = 5)

    show.lblName.pack(padx = 10, pady = 5)
    show.entName.pack(padx = 10, pady = 5)
    show.lblSeason.pack(padx = 10, pady = 5)
    show.btnMoreSeason.pack(padx = 10, pady = 5)
    show.entSeason.pack(padx = 10, pady = 5)
    show.btnLessSeason.pack(padx = 10, pady = 5)
    show.lblEpisode.pack(padx = 10, pady = 5)
    show.btnMoreEpisode.pack(padx = 10, pady = 5)
    show.entEpisode.pack(padx = 10, pady = 5)
    show.btnLessEpisode.pack(padx = 10, pady = 5)
    show.lblFinished.pack(padx = 10, pady = 5)
    show.btnFinished.pack(padx = 10, pady = 5)
    show.btnAdd.pack(padx = 10, pady = 5)
    show.btnDelete.pack(padx = 10, pady = 5)
    show.btnChange.pack(padx = 10, pady = 5)

def startFunc():
    startGame()
    startSystem()
    startMovie()
    startGenre()
    startShow()

def startGame():
    if not os.path.isfile(glo.gameFile):
        with open(file, "w", newline="") as fw:
            writer = csv.writer(fw)
            startLine = ("Game", "Console")
            writer.writerow(startLine)

def startSystem():
    if not os.path.isfile(glo.systemFile):
        with open(file, "w", newline="") as fw:
            writer = csv.writer(fw)

def startMovie():
    if not os.path.isfile(glo.movieFile):
        with open(file, "w", newline="") as fw:
            writer = csv.writer(fw)
            startLine = ("Movie", "Genre")
            writer.writerow(startLine)

def startGenre():
    if not os.path.isfile(glo.genreFile):
        with open(file, "w", newline="") as fw:
            writer = csv.writer(fw)

def startShow():
    if not os.path.isfile(glo.showFile):
        with open(file, "w", newline="") as fw:
            writer = csv.writer(fw)
            startLine = ("Show", "Season", "Episode", "Finished")
            writer.writerow(startLine)

def populateGameListbox():
    game.lbx.delete(0,tk.END)
    with open(glo.gameFile, "r") as fr:
        reader = csv.reader(fr)
        count = 0

        for line in reader:
            if count == 0:
                count += 1
                continue
            line = ",".join(line)
            line = line.replace(",", " - ")
            index = count - 1
            game.lbx.insert(index, str(count) + " - " + line)
            count += 1

def populateMovieListbox():
    movie.lbx.delete(0,tk.END)
    with open(glo.movieFile, "r") as fr:
        reader = csv.reader(fr)
        count = 0

        for line in reader:
            if count == 0:
                count += 1
                continue
            line = ",".join(line)
            line = line.replace(",", " - ")
            index = count - 1
            movie.lbx.insert(index, str(count) + " - " + line)
            count += 1

def populateShowListbox():
    show.lbx.delete(0,tk.END)
    with open(glo.showFile, "r") as fr:
        reader = csv.reader(fr)
        count = 0

        for line in reader:
            if count == 0:
                count += 1
                continue
            line = ",".join(line)
            line = line.replace(",", " - ")
            index = count - 1
            show.lbx.insert(index, str(count) + " - " + line)
            count += 1

def populateGameSystems():
    values = []
    with open(glo.systemFile, "r") as fr:
        reader = csv.reader(fr)
        
        for line in reader:
            values.append(line)
        game.cbxSystems["values"] = values

def populateMovieGenre():
    values = []
    with open(glo.genreFile, "r") as fr:
        reader = csv.reader(fr)
        
        for line in reader:
            values.append(line)
        movie.cbxGenre["values"] = values

def populateGameFinished():
    game.lblFinshed.config(text="Finished: " + str(game.lbx.size()))

def populateMovieFinished():
    movie.lblFinshed.config(text="Finished: " + str(movie.lbx.size()))

def sortMainFile(file):
    temp = "temp.txt"
    lines = ""
    count = 0
    startLine = ""
    if os.path.isfile(file):
        with open(file, "r", newline="") as fr:
            lines = fr.readlines()
            startLine = lines[0]
            lines.pop(0)
            lines.sort(key=str.casefold)
        
        with open (temp, "a", newline="") as fa:
            fa.write(startLine)
            for line in lines:
                fa.write(line)
        
        os.remove(file)
        os.rename(temp, file)

def sortTypeFile(file):
    temp = "temp.txt"
    lines = ""
    if os.path.isfile(file):
        with open(file, "r", newline="") as fr:
            lines = fr.readlines()
            lines.sort(key=str.casefold)
        
        with open (temp, "a", newline="") as fa:
            for line in lines:
                fa.write(line)
        
        os.remove(file)
        os.rename(temp, file)

def addGame():
    if game.entName.get() == "" or game.cbxSystems.get() == "" or game.cbxSystems.current() < 0:
        print("INCOMPLETE INFO TO ADD")
    else:
        with open(glo.gameFile, "a") as fa:
            fa.write(game.entName.get() + "," + game.cbxSystems.get() + "\n")

        sortMainFile(glo.gameFile)
        populateGameListbox()
        populateGameFinished()

def addMovie():
    if movie.entName.get() == "" or movie.cbxGenre.get() == "" or movie.cbxGenre.current() < 0:
        print("INCOMPLETE INFO TO ADD")
    else:
        with open(glo.movieFile, "a") as fa:
            fa.write(movie.entName.get() + "," + movie.cbxGenre.get() + "\n")

        sortMainFile(glo.movieFile)
        populateMovieListbox()
        populateMovieFinished()

def addShow():
    if show.entName.get() == "" or show.entSeason.get() == "" or show.entSeason.get().isdigit() != True or show.entEpisode.get() == "" or show.entEpisode.get().isdigit() != True:
        print("INCOMPLETE INFO TO ADD")
    elif int(show.entSeason.get()) < 0 or int(show.entEpisode.get()) < 0:
        print("Season and Episode have to be ZERO or ABOVE")
    else:
        if show.finished:
            finished = "Yes"
        else:
            finished = "No"
        with open(glo.showFile, "a") as fa:
            fa.write(show.entName.get() + "," + show.entSeason.get() + "," + show.entEpisode.get() + "," + finished + "\n")

        sortMainFile(glo.showFile)
        populateShowListbox()

def deleteGame():
    temp = "temp.cvs"
    if len(game.lbx.curselection()) == 0:
        print("EMPTY SELECTION")
    else:
        num = int(''.join(map(str,game.lbx.curselection()))) #THIS CHANGES TUPLE TO INT
        num += 1 #Makes it not delete item under
        with open(glo.gameFile, "r") as fr:
            reader = csv.reader(fr)

            with open(temp, "w", newline="") as fw:
                writer = csv.writer(fw)
                count = 0
                for line in reader:

                    if count == num:
                        count += 1
                        continue
                    writer.writerow(line)
                    count += 1
        
        if os.path.isfile(glo.gameFile) and os.path.isfile(temp):
            os.remove(glo.gameFile)
            os.rename(temp, glo.gameFile)
            populateGameListbox()
            populateGameFinished()

def deleteMovie():
    temp = "temp.cvs"
    if len(movie.lbx.curselection()) == 0:
        print("EMPTY SELECTION")
    else:
        num = int(''.join(map(str,movie.lbx.curselection()))) #THIS CHANGES TUPLE TO INT
        num += 1 #Makes it not delete item under
        with open(glo.movieFile, "r") as fr:
            reader = csv.reader(fr)

            with open(temp, "w", newline="") as fw:
                writer = csv.writer(fw)
                count = 0
                for line in reader:

                    if count == num:
                        count += 1
                        continue
                    writer.writerow(line)
                    count += 1
        
        if os.path.isfile(glo.movieFile) and os.path.isfile(temp):
            os.remove(glo.movieFile)
            os.rename(temp, glo.movieFile)
            populateMovieListbox()
            populateMovieFinished()

def deleteShow():
    temp = "temp.cvs"
    if len(show.lbx.curselection()) == 0:
        print("EMPTY SELECTION")
    else:
        num = int(''.join(map(str,show.lbx.curselection()))) #THIS CHANGES TUPLE TO INT
        num += 1 #Makes it not delete item under
        with open(glo.showFile, "r") as fr:
            reader = csv.reader(fr)

            with open(temp, "w", newline="") as fw:
                writer = csv.writer(fw)
                count = 0
                for line in reader:

                    if count == num:
                        count += 1
                        continue
                    writer.writerow(line)
                    count += 1
        
        if os.path.isfile(glo.showFile) and os.path.isfile(temp):
            os.remove(glo.showFile)
            os.rename(temp, glo.showFile)
            populateShowListbox()

def changeGame():
    if len(game.lbx.curselection()) == 0 or game.entName.get() == "" or game.cbxSystems.get() == "" or game.cbxSystems.current() < 0:
        print("Change skipped, no selection")
    else:
        deleteGame()
        addGame()

def changeMovie():
    if len(movie.lbx.curselection()) == 0 or movie.entName.get() == "" or movie.cbxGenre.get() == "" or movie.cbxGenre.current() < 0:
        print("Change skipped, no selection")
    else:
        deleteMovie()
        addMovie()

def changeShow():
    if show.entName.get() == "" or show.entSeason.get() == "" or show.entSeason.get().isdigit() != True or show.entEpisode.get() == "" or show.entEpisode.get().isdigit() != True:
        print("INCOMPLETE INFO TO ADD")
    elif int(show.entSeason.get()) < 0 or int(show.entEpisode.get()) < 0:
        print("Season and Episode have to be ZERO or ABOVE")
    else:
        deleteShow()
        addShow()

def copyGame():
    count = 0

    index = game.lbx.curselection()
    selText = game.lbx.get(index)
    selText = selText.split(" - ")
    name = selText.pop(1)
    gameSystem = selText.pop(1)
    index = selText.pop(0)
    index = int(index)
    index = index - 1
    
    with open(glo.systemFile, "r") as fr:
        lines = fr.readlines()

        for line in lines:
            line = line.replace("\n", "")
            if line == str(gameSystem):
                break
            count += 1
    
    game.entName.delete(0,"end")
    game.entName.insert(0, name)
    game.cbxSystems.current(count)

def copyMovie():
    count = 0

    index = movie.lbx.curselection()
    selText = movie.lbx.get(index)
    selText = selText.split(" - ")
    name = selText.pop(1)
    movieGenre = selText.pop(1)
    index = selText.pop(0)
    index = int(index)
    index = index - 1
    
    with open(glo.genreFile, "r") as fr:
        lines = fr.readlines()

        for line in lines:
            line = line.replace("\n", "")
            if line == str(movieGenre):
                break
            count += 1
    
    movie.entName.delete(0,"end")
    movie.entName.insert(0, name)
    movie.cbxGenre.current(count)

def copyShow():
    index = show.lbx.curselection()
    selText = show.lbx.get(index)
    selText = selText.split(" - ")
    name = selText.pop(1)
    season = selText.pop(1)
    episode = selText.pop(1)
    finished = selText.pop(1)
    index = selText.pop(0)
    index = int(index)
    index = index - 1
    
    show.entName.delete(0,"end")
    show.entName.insert(0, name)
    show.entSeason.delete(0,"end")
    show.entSeason.insert(0, season)
    show.entEpisode.delete(0,"end")
    show.entEpisode.insert(0, episode)
    if finished == "Yes":
        show.finished = True
        show.btnFinished.config(text="Yes")
    if finished == "No":
        show.finished = False
        show.btnFinished.config(text="No")

def openSystemsWindow():
    global sysWin

    class sysWin:
        newWindow = Toplevel(glo.root)
        newWindow.title("Change Systems")
        newWindow.geometry("275x175")

        lblNew = Label(newWindow, text="Add new system")
        entNew = Entry(newWindow)
        btnNew = Button(newWindow, text="Add System", command=lambda: addGameSystem())
        lblDelete = Label(newWindow, text="Select system to delete")
        cbxDelete = ttk.Combobox(newWindow)
        btnDelete = Button(newWindow, text="Delete Selected System", command=lambda: deleteGameSystem())

    populateGameSystemsNewWindow()

    sysWin.lblNew.pack(pady=2)
    sysWin.entNew.pack(pady=2)
    sysWin.btnNew.pack(pady=2)
    sysWin.lblDelete.pack(pady=2)
    sysWin.cbxDelete.pack(pady=2)
    sysWin.btnDelete.pack(pady=2)

def openGenreWindow():
    global genWin

    class genWin:
        newWindow = Toplevel(glo.root)
        newWindow.title("Change Genres")
        newWindow.geometry("275x175")

        lblNew = Label(newWindow, text="Add new genre")
        entNew = Entry(newWindow)
        btnNew = Button(newWindow, text="Add Genre", command=lambda: addMovieGenre())
        lblDelete = Label(newWindow, text="Select genre to delete")
        cbxDelete = ttk.Combobox(newWindow)
        btnDelete = Button(newWindow, text="Delete Selected Genre", command=lambda: deleteMovieGenre())

    populateMovieGenreNewWindow()

    genWin.lblNew.pack(pady=2)
    genWin.entNew.pack(pady=2)
    genWin.btnNew.pack(pady=2)
    genWin.lblDelete.pack(pady=2)
    genWin.cbxDelete.pack(pady=2)
    genWin.btnDelete.pack(pady=2)

def populateGameSystemsNewWindow():
    values = []
    with open(glo.systemFile, "r") as fr:
        reader = csv.reader(fr)
        
        for line in reader:
            values.append(line)
        sysWin.cbxDelete["values"] = values

def populateMovieGenreNewWindow():
    values = []
    with open(glo.genreFile, "r") as fr:
        reader = csv.reader(fr)
        
        for line in reader:
            values.append(line)
        genWin.cbxDelete["values"] = values

def addGameSystem():
    if sysWin.entNew.get() == "":
        print("Cannot be empty")
    else:
        with open(glo.systemFile, "a") as fa:
            fa.write(sysWin.entNew.get() + "\n")
        sortTypeFile(glo.systemFile)
        populateGameSystems()
        populateGameSystemsNewWindow()

def addMovieGenre():
    if genWin.entNew.get() == "":
        print("Cannot be empty")
    else:
        with open(glo.genreFile, "a") as fa:
            fa.write(genWin.entNew.get() + "\n")
        sortTypeFile(glo.genreFile)
        populateMovieGenre()
        populateMovieGenreNewWindow()

def deleteGameSystem():
    temp = "temp.txt"
    count = 0

    if sysWin.cbxDelete.current() < 0:
        print("Wrong Selection")
    else:
        if os.path.isfile(glo.systemFile):
            with open(glo.systemFile, "r", newline="") as fr:
                lines = fr.readlines()
                lines.sort(key=str.casefold)
        
            with open (temp, "a", newline="") as fa:
                for line in lines:
                    if count == sysWin.cbxDelete.current():
                        count += 1
                        continue
                    else:
                        count += 1
                        fa.write(line)
        
            os.remove(glo.systemFile)
            os.rename(temp, glo.systemFile)
            populateGameSystems()
            populateGameSystemsNewWindow()

def deleteMovieGenre():
    temp = "temp.txt"
    count = 0

    if genWin.cbxDelete.current() < 0:
        print("Wrong Selection")
    else:
        if os.path.isfile(glo.genreFile):
            with open(glo.genreFile, "r", newline="") as fr:
                lines = fr.readlines()
                lines.sort(key=str.casefold)
        
            with open (temp, "a", newline="") as fa:
                for line in lines:
                    if count == genWin.cbxDelete.current():
                        count += 1
                        continue
                    else:
                        count += 1
                        fa.write(line)
        
            os.remove(glo.genreFile)
            os.rename(temp, glo.genreFile)
            populateMovieGenre()
            populateMovieGenreNewWindow()

def showFinishedButtonFunc():
    if show.finished:
        show.finished = False
        show.btnFinished.config(text="No")
    else:
        show.finished = True
        show.btnFinished.config(text="Yes")

def moreValue(ent):
    value = ent.get()
    if value == "":
        ent.insert(0, 1)
    elif value.isdigit() != True:
        print("Needs to be only digits")
    else:
        value = int(value)
        value += 1
        ent.delete(0, "end")
        ent.insert(0, value)

def lessValue(ent):
    value = ent.get()
    if value == "":
        ent.insert(0, 0)
    elif value.isdigit() != True:
        print("Needs to be only digits")
    elif int(value) < 1:
        print("Cannot be negative")
    else:
        value = int(value)
        value -= 1
        ent.delete(0, "end")
        ent.insert(0, value)

main()
