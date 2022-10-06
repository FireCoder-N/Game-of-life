import tkinter as tk
from tkinter import ttk
import tkinter.colorchooser as col
import random as ran
import time

class Myapp():
    def __init__(self,root):
        self.root=root
        #self.root.iconbitmap('img.ico')
        self.settings_screen()

    def settings_screen(self):
        self.root.geometry("500x350+500+150")
        self.root.title("Settings")
        self.root.configure(bg="#fab500")
        self.root.resizable(False, False)
        #______________________________player 1___________________________________________
        self.pl1=tk.Label(self.root, bg="#fab500",height=0)
        self.pl1.pack(pady=10,fill="both")

        def cp1():
            color=col.askcolor(parent=self.root)
            if color[1]!=None: 
                self.e12.delete(0,"end")
                self.e12.insert("end", color[1])

        self.l11=tk.Label(self.pl1,text="Player 1:", font="Arial 13", bg="#fab500",width=7)
        self.l11.pack(side="left", padx=7,pady=10,ipadx=1)
        self.l12=tk.Label(self.pl1, font="Arial 12", text="name: ", bg="#fab500")
        self.l12.pack(side="left", padx=10)
        self.e11=tk.Entry(self.pl1,font="Arial 11", width=8)
        self.e11.insert("end", "Player 1")
        self.e11.pack(side="left")
        self.l13=tk.Label(self.pl1, font="Arial 12", text="color: ", bg="#fab500", width=6)
        self.l13.pack(side="left", padx=10)
        self.e12=tk.Entry(self.pl1,font="Arial 10", width=8)
        self.e12.insert("end", "yellow")
        self.e12.pack(side="left")
        self.pb1=tk.Button(self.pl1, text="sample", command=cp1, height=1, font="Verdana 9", bg="#fab500", activebackground="#fab500",relief="solid",bd=1)
        self.pb1.pack(side="left",padx=10)
        #___________________________________ player2________________________________________
        self.pl2=tk.Label(self.root, bg="#fab500",height=0)
        self.pl2.pack(pady=0,fill="both")

        def cp2():
            color=col.askcolor(parent=self.root)
            if color[1]!=None: 
                self.e22.delete(0,"end")
                self.e22.insert("end", color[1])

        self.l21=tk.Label(self.pl2,text="Player 2:", font="Arial 13", bg="#fab500",width=7)
        self.l21.pack(side="left", padx=7,pady=10,ipadx=1)
        self.l22=tk.Label(self.pl2, font="Arial 12", text="name: ", bg="#fab500")
        self.l22.pack(side="left", padx=10)
        self.e21=tk.Entry(self.pl2,font="Arial 11", width=8)
        self.e21.insert("end", "Player 2")
        self.e21.pack(side="left")
        self.l23=tk.Label(self.pl2, font="Arial 12", text="color: ", bg="#fab500", width=6)
        self.l23.pack(side="left", padx=10)
        self.e22=tk.Entry(self.pl2,font="Arial 10", width=8)
        self.e22.insert("end", "red")
        self.e22.pack(side="left")
        self.pb2=tk.Button(self.pl2, text="sample", command=cp2, height=1, font="Verdana 9", bg="#fab500", activebackground="#fab500",relief="solid",bd=1)
        self.pb2.pack(side="left",padx=10)
        #___________________________________ grid________________________________________
        self.g=tk.Label(self.root, bg="#fab500",height=0)
        self.g.pack(pady=20,fill="both")

        def square_grid(event=None):
            if var.get()==1:
                self.gc2.set(self.gc1.get())
                self.gc2.configure(state="disabled")
            else:
                self.gc2.configure(state="readonly")

        var=tk.IntVar()
        self.lg1=tk.Label(self.g,text="Grid size:", font="Arial 13", bg="#fab500",width=7)
        self.lg1.pack(side="left", padx=7,pady=10,ipadx=1)
        self.gc1=ttk.Combobox(self.g,font="Calibri 13", width=4, values=[7,14,20,35,50,70])
        self.gc1.current(3)
        self.gc1.configure(state="readonly")
        self.gc1.pack(side="left",padx=7)
        self.gc1.bind("<<ComboboxSelected>>",square_grid)
        self.lg2=tk.Label(self.g,text="X", font="Arial 13", bg="#fab500",width=2)
        self.lg2.pack(side="left", padx=7,pady=10,ipadx=1)
        self.gc2=ttk.Combobox(self.g,font="Calibri 13", width=4, values=[7,14,20,35,50,70])
        self.gc2.pack(side="left",padx=7)
        self.gc2.configure(state="readonly")
        self.gch1=tk.Checkbutton(self.g, text="square", variable=var, bg="#fab500", font="Calibri 13",activebackground="#fab500",command=square_grid)
        self.gch1.pack(side="left", padx=20)
        self.gch1.select()
        square_grid()
        #___________________________________ control________________________________________
        self.con=tk.Label(self.root, bg="#fab500",height=0)
        self.con.pack(pady=0,fill="both")
        self.lc1=tk.Label(self.con, font="Arial 13", text="Moves per player: ", bg="#fab500",width=14)
        self.lc1.pack(side="left", padx=7,pady=10,ipadx=1)
        self.cc1=ttk.Combobox(self.con,font="Calibri 13", width=3, values=[5,6,7,8,9,10])
        self.cc1.current(1)
        self.cc1.pack(side="left",padx=10)
        self.lcb=tk.Label(self.con, font="Arial 13", text="", bg="#fab500",width=5)
        self.lcb.pack(side="left", padx=0,pady=0,ipadx=1)
        self.lc3=tk.Label(self.con, font="Arial 13", text="Iterations: ", bg="#fab500", width=8)
        self.lc3.pack(side="left", padx=10)
        self.cc2=ttk.Combobox(self.con,font="Calibri 13", width=3, values=[1,2,3,5,10])
        self.cc2.current(0)
        self.cc2.configure(state="readonly")
        self.cc2.pack(side="left",padx=0)
        #_____________________________________________________________________________________
        self.bok=tk.Button(self.root, text="Let's play! [Enter]", width=15,command=self.transit,font="Calibri 14",bg="#fab500",activebackground="#fab500", fg="blue", activeforeground="blue",relief="solid",bd=1)
        self.bok.pack(pady=0,padx=180,side="left")
        self.bind1=self.root.bind("<Return>", self.transit)

    def transit(self,event=None): #transition from settings screen to mainscreen
        self.root.overrideredirect(True)
        self.root.unbind("<Return>",self.bind1)
        del self.bind1
        self.player1=[]
        self.player1.append(self.e11.get())
        self.player1.append(self.e12.get())
        self.player2=[]
        self.player2.append(self.e21.get())
        self.player2.append(self.e22.get())
        self.grid_h=700//int(self.gc1.get())
        self.grid_v=700//int(self.gc2.get())
        self.iterations=int(self.cc2.get())
        if self.cc1.get().isnumeric(): self.moves=int(self.cc1.get())
        else: self.moves=6
        self.pl1.destroy()
        self.pl2.destroy()
        self.g.destroy()
        self.con.destroy()
        self.bok.destroy()
        self.root.configure(bg="#34ebd2")
        self.xothonis=self.root.winfo_screenwidth()
        self.yothonis=self.root.winfo_screenheight()
        self.root.geometry("{}x{}+0+0".format(self.xothonis,self.yothonis))
        self.root.title("Game of Life")
        self.mainscreen()

    def r_transit(self,event=None): #transition from mainscreen to settings screen
        self.root.unbind("<Control_L>",self.sb)
        self.canvas.destroy()
        self.root.overrideredirect(False)
        self.UI.destroy()
        self.infolabel.destroy()
        self.sc.destroy()
        self.cp.destroy()
        self.settings_screen()

    def mainscreen(self,event=None):
        try:
            #_________________________the mid right label. Includes availiable turns label and end turn button____________________
            self.UI = tk.Label(self.root, bg="#636bc9")
            self.UI.grid(row=0, column=1, padx=20, ipadx=30, pady=120, sticky="NW" )
            self.rem1 = tk.Label(self.UI, font="fixdsys 30", text=" Availiable moves: ", width=13, height=1, bg="#636bc9", fg="#ebe417")
            self.rem1.grid(row=0, column=0, padx=40, pady=20)
            self.rem2 = tk.Text(self.UI, bg="#636bc9", fg="#ebe417", font="fixdsys 35", height=1, width=3, relief="flat")
            self.rem2.insert("end", self.moves)
            self.rem2.configure(state="disabled")
            self.rem2.grid(row=0, column=1, pady=20)
            self.pt = tk.Button(self.UI, text="End turn", bg="#636bc9", activebackground="#4b52a3", fg="#ebe417", font="Arial 20", activeforeground="#ebbc2f", command=self.between)
            self.pt.grid(row=0,column=2, pady=20)
            #___________________________upper right label.Shows who plays_________________________________________________________
            self.infolabel = tk.Text(self.root, bg="#010536", font="fixdsys 30", width= 20, height=1, relief="flat")
            self.infolabel.grid(row=0, column=1, padx=20, ipadx=107, pady=20, sticky="NW")
            #___________________________Canvas on the left_______________________________________________________________________
            self.canvas=tk.Canvas(self.root, width=700, height=700, bg="#011714", highlightthickness=0)
            self.canvas.grid(row=0, padx=20, pady=20, sticky="NW")
            self.who_plays_first()
            self.create_grid()
            #___________________________the score label on bottom right corner____________________________________________________
            self.sc= tk.Label(self.root, bg="#fab500")
            self.sc.grid(row=0, column=1, padx=20, ipadx=30, pady=270, sticky="NW" )
            self.scorelabel = tk.Label(self.sc, font="fixdsys 30", text=" Score: ", width=13, height=1, bg="#fab500", fg="black")
            self.scorelabel.grid(row=0, column=0, padx=145, pady=10)
            self.sc1 = tk.Label(self.sc, bg=self.player1[1])
            self.sc1.grid(row=1, column=0, padx=50, pady=16)
            self.pls1 = tk.Label(self.sc1, font="fixdsys 18", text=self.player1[0]+" :", width=13, height=1, bg=self.player1[1], fg="black")
            self.pls1.grid(row=0, column=0, padx=50, pady=20)
            self.score1 = tk.Text(self.sc1, bg=self.player1[1], fg="black", font="fixdsys 25", height=1, width=7, relief="flat")
            self.score1.insert("end", 0)
            self.score1.configure(state="disabled")
            self.score1.grid(row=1, column=0)
            self.emptyline1=tk.Label(self.sc1, font="fixdsys 18", width=13, height=1, bg=self.player1[1])
            self.emptyline1.grid(row=3, column=0, padx=50)
            self.sc2 = tk.Label(self.sc, bg=self.player2[1])
            self.sc2.grid(row=2, column=0, padx=50, pady=19)
            self.pls2 = tk.Label(self.sc2, font="fixdsys 18", text=self.player2[0]+" :", width=13, height=1, bg=self.player2[1], fg="black")
            self.pls2.grid(row=0, column=0, padx=50, pady=20)
            self.score2 = tk.Text(self.sc2, bg=self.player2[1], fg="black", font="fixdsys 25", height=1, width=7, relief="flat")
            self.score2.insert("end", 0)
            self.score2.configure(state="disabled")
            self.score2.grid(row=1, column=0)
            self.emptyline2=tk.Label(self.sc2, font="fixdsys 18", width=13, height=1, bg=self.player2[1])
            self.emptyline2.grid(row=3, column=0, padx=50)
            #___________________________control panel on the bottom______________________________________________________________
            self.root.bind("<Escape>", self.close)
            self.sb=self.root.bind("<Control_L>", self.r_transit)
            self.cp=tk.Label(self.root,width=70,height=1,bg="#34ebd2")
            self.cp.grid(row=0, column=0, padx=20, ipadx=30, pady=740, sticky="NW" )
            self.clbt=tk.Button(self.cp,text="(×_×)", font="fixdsys 20", bg="#34ebd2",fg="red",activebackground="#34ebd2",activeforeground="red",command=self.close)
            self.clbt.grid(row=0, column=0)
            self.cll=tk.Label(self.cp,text="close [esc]", font="fixdsys 14", bg="#34ebd2",fg="red",activebackground="#34ebd2",activeforeground="red")
            self.cll.grid(row=1, column=0)
            self.sbt=tk.Button(self.cp,text="(´･_･`)", font="fixdsys 20", bg="#34ebd2",fg="red",activebackground="#34ebd2",activeforeground="red",command=self.r_transit)
            self.sbt.grid(row=0, column=1,padx=30)
            self.sl=tk.Label(self.cp,text="settings [ctrl]", font="fixdsys 14", bg="#34ebd2",fg="red",activebackground="#34ebd2",activeforeground="red")
            self.sl.grid(row=1, column=1,padx=30)
        except:
            pass

    def create_grid(self):
        self.gridmatrix=[]
        self.canvas.delete("grid_line")
        # Creates all horizontal lines at intevals of 100
        for i in range(0, 700, self.grid_h):
            self.canvas.create_line([(0, i), (700, i)], tag="grid_line", fill="#005e4d", width=2)

        # Creates all vertical lines at intevals of 100
        for i in range(0, 700, self.grid_v):
            self.canvas.create_line([(i, 0), (i, 700)], tag="grid_line", fill="#005e4d",width=2)

        for i in range (700//self.grid_h):
            L=[]
            for j in range(700//self.grid_v):
                L.append(0)
            self.gridmatrix.append(L)
        self.availiablemoves = self.moves
        self.canvas.bind("<Button-1>", self.toggle_rec)

    def toggle_rec(self,event): #create or destroy rectangle on click
        #on first click we record the current time, so that we can calculate how much time was needed to play all his/her moves. 
        for i in range(700//self.grid_h):
            for j in range(700//self.grid_v):
                if self.gridmatrix[i][j]!=0:
                    break
            else:
                continue
            break
        else:
            self.timestart = time.time()
            self.pt.configure(state="normal")
        #until here we record time of first click.


        x=self.position(event.x,"x")
        y=self.position(event.y,"y")
        if self.availiablemoves!=0 and self.gridmatrix[y-1][x-1]==0:
            rstt=self.canvas.create_rectangle((x-1)*self.grid_v+1,(y-1)*self.grid_h+1,x*self.grid_v-1,y*self.grid_h-1, fill=self.color)
            self.gridmatrix[y-1][x-1]=rstt
            self.availiablemoves -=1
        elif self.gridmatrix[y-1][x-1]!=0:
            self.canvas.delete(self.gridmatrix[y-1][x-1])
            self.gridmatrix[y-1][x-1]=0
            self.availiablemoves +=1
        
        self.rem2.configure(state="normal")
        self.rem2.delete("1.0","end")
        self.rem2.insert("end", self.availiablemoves)
        self.rem2.configure(state="disabled")

    def position(self,x,axis): #translate the coordinate of click on element of gridmatrix
        i=1
        if axis=="x":
            number=self.grid_v
        else:
            number=self.grid_h
        while True:
            if x<i*number:
                return i
            else:
                i+=1  

    def clear_grid(self):
        for i in range (700//self.grid_h):
            for j in range(700//self.grid_v):
                if self.gridmatrix[i][j]!=0:
                    self.canvas.delete(self.gridmatrix[i][j])
                    self.gridmatrix[i][j]=0

    def who_plays_first(self):
        ra = ran.randint(1,2)
        self.infolabel.configure(state="normal")
        self.infolabel.delete("1.0","end")
        if ra==1:
            self.color=self.player1[1]
            self.whoplays="Player 1"
            self.infolabel.configure(fg=self.color)
            self.infolabel.insert("end", " ~~~     {}, you play first.    ~~~".format(self.player1[0]))
        else:
            self.color=self.player2[1]
            self.whoplays="Player 2"
            self.infolabel.configure(fg=self.color)
            self.infolabel.insert("end", " ~~~     {}, you play first.    ~~~".format(self.player2[0]))
        self.infolabel.configure(state="disabled")

    def toggle_player(self): #determines whose turn is it
        self.clear_grid()
        self.create_grid()
        self.infolabel.configure(state="normal")
        self.infolabel.delete("1.0","end")
        if self.whoplays=="Player 1":
            self.whoplays="Player 2"
            self.color=self.player2[1]
            self.infolabel.configure(fg=self.color)
            self.infolabel.insert("end", " ~~~     {}, it's your turn.    ~~~".format(self.player2[0]))
        elif self.whoplays=="Player 2":
            self.whoplays="Player 1"
            self.color=self.player1[1]
            self.infolabel.configure(fg=self.color)
            self.infolabel.insert("end", " ~~~     {}, it's your turn.    ~~~".format(self.player1[0]))
        self.infolabel.configure(state="disabled")
        self.rem2.configure(state="normal")
        self.rem2.delete("1.0","end")
        self.rem2.insert("end", self.availiablemoves)
        self.rem2.configure(state="disabled")

    def next(self): #performs one iteration
        gridcopy=[]
        for i in range (700//self.grid_h):
            L=[]
            for j in range(700//self.grid_v):
                L.append(0)
            gridcopy.append(L)

        for i in range(700//self.grid_h):
            for j in range(700//self.grid_v):
                if i!=0 and i!=(700//self.grid_h)-1 and j!=0 and j!=(700//self.grid_v)-1:
                    if self.gridmatrix[i][j]!=0:
                        count=0
                        if self.gridmatrix[i-1][j-1]!=0: count+=1
                        if self.gridmatrix[i-1][j]!=0: count+=1
                        if self.gridmatrix[i-1][j+1]!=0: count+=1
                        if self.gridmatrix[i][j-1]!=0: count+=1
                        if self.gridmatrix[i][j+1]!=0: count+=1
                        if self.gridmatrix[i+1][j-1]!=0: count+=1
                        if self.gridmatrix[i+1][j]!=0: count+=1
                        if self.gridmatrix[i+1][j+1]!=0: count+=1
                        ###
                        if count<2 or count>3:
                            gridcopy[i][j]="-"
                        elif count==2 or count==3:
                            pass
                    elif self.gridmatrix[i][j]==0:
                        count=0
                        if self.gridmatrix[i-1][j-1]!=0: count+=1
                        if self.gridmatrix[i-1][j]!=0: count+=1
                        if self.gridmatrix[i-1][j+1]!=0: count+=1
                        if self.gridmatrix[i][j-1]!=0: count+=1
                        if self.gridmatrix[i][j+1]!=0: count+=1
                        if self.gridmatrix[i+1][j-1]!=0: count+=1
                        if self.gridmatrix[i+1][j]!=0: count+=1
                        if self.gridmatrix[i+1][j+1]!=0: count+=1
                        ###
                        if count==3:
                            gridcopy[i][j]="+"
                elif i==0 and j==0:
                    if self.gridmatrix[i][j]!=0:
                        count=0
                        if self.gridmatrix[i][j+1]!=0: count+=1
                        if self.gridmatrix[i+1][j]!=0: count+=1
                        if self.gridmatrix[i+1][j+1]!=0: count+=1
                        ###
                        if count<2:
                            gridcopy[i][j]="-"
                        elif count==2 or count==3:
                            pass
                    elif self.gridmatrix[i][j]==0:
                        count=0
                        if self.gridmatrix[i][j+1]!=0: count+=1
                        if self.gridmatrix[i+1][j]!=0: count+=1
                        if self.gridmatrix[i+1][j+1]!=0: count+=1
                        ###
                        if count==3:
                            gridcopy[i][j]="+"
                elif i==0 and j==(700//self.grid_v)-1:
                    if self.gridmatrix[i][j]!=0:
                        count=0
                        if self.gridmatrix[i][j-1]!=0: count+=1
                        if self.gridmatrix[i+1][j]!=0: count+=1
                        if self.gridmatrix[i+1][j-1]!=0: count+=1
                        ###
                        if count<2:
                            gridcopy[i][j]="-"
                        elif count==2 or count==3:
                            pass
                    elif self.gridmatrix[i][j]==0:
                        count=0
                        if self.gridmatrix[i][j-1]!=0: count+=1
                        if self.gridmatrix[i+1][j]!=0: count+=1
                        if self.gridmatrix[i+1][j-1]!=0: count+=1
                        ###
                        if count==3:
                            gridcopy[i][j]="+"
                elif i==0:
                    if self.gridmatrix[i][j]!=0:
                        count=0
                        if self.gridmatrix[i][j-1]!=0: count+=1
                        if self.gridmatrix[i+1][j-1]!=0: count+=1
                        if self.gridmatrix[i+1][j]!=0: count+=1
                        if self.gridmatrix[i+1][j+1]!=0: count+=1
                        if self.gridmatrix[i][j+1]!=0: count+=1
                        ###
                        if count<2 or count>3:
                            gridcopy[i][j]="-"
                        elif count==2 or count==3:
                            pass
                    elif self.gridmatrix[i][j]==0:
                        count=0
                        if self.gridmatrix[i][j-1]!=0: count+=1
                        if self.gridmatrix[i+1][j-1]!=0: count+=1
                        if self.gridmatrix[i+1][j]!=0: count+=1
                        if self.gridmatrix[i+1][j+1]!=0: count+=1
                        if self.gridmatrix[i][j+1]!=0: count+=1
                        ###
                        if count==3:
                            gridcopy[i][j]="+"
                elif i==(700//self.grid_h)-1 and j==0:
                    if self.gridmatrix[i][j]!=0:
                        count=0
                        if self.gridmatrix[i-1][j]!=0: count+=1
                        if self.gridmatrix[i-1][j+1]!=0: count+=1
                        if self.gridmatrix[i][j+1]!=0: count+=1
                        ###
                        if count<2:
                            gridcopy[i][j]="-"
                        elif count==2 or count==3:
                            pass
                    elif self.gridmatrix[i][j]==0:
                        count=0
                        if self.gridmatrix[i-1][j]!=0: count+=1
                        if self.gridmatrix[i-1][j+1]!=0: count+=1
                        if self.gridmatrix[i][j+1]!=0: count+=1
                        ###
                        if count==3:
                            gridcopy[i][j]="+"
                elif i==(700//self.grid_h)-1 and j==(700//self.grid_v)-1:
                    if self.gridmatrix[i][j]!=0:
                        count=0
                        if self.gridmatrix[i][j-1]!=0: count+=1
                        if self.gridmatrix[i-1][j]!=0: count+=1
                        if self.gridmatrix[i-1][j-1]!=0: count+=1
                        ###
                        if count<2:
                            gridcopy[i][j]="-"
                        elif count==2 or count==3:
                            pass
                    elif self.gridmatrix[i][j]==0:
                        count=0
                        if self.gridmatrix[i][j-1]!=0: count+=1
                        if self.gridmatrix[i-1][j]!=0: count+=1
                        if self.gridmatrix[i-1][j-1]!=0: count+=1
                        ###
                        if count==3:
                            gridcopy[i][j]="+"
                elif i==(700//self.grid_h)-1:
                    if self.gridmatrix[i][j]!=0:
                        count=0
                        if self.gridmatrix[i][j-1]!=0: count+=1
                        if self.gridmatrix[i-1][j-1]!=0: count+=1
                        if self.gridmatrix[i-1][j]!=0: count+=1
                        if self.gridmatrix[i-1][j+1]!=0: count+=1
                        if self.gridmatrix[i][j+1]!=0: count+=1
                        ###
                        if count<2 or count>3:
                            gridcopy[i][j]="-"
                        elif count==2 or count==3:
                            pass
                    elif self.gridmatrix[i][j]==0:
                        count=0
                        if self.gridmatrix[i][j-1]!=0: count+=1
                        if self.gridmatrix[i-1][j-1]!=0: count+=1
                        if self.gridmatrix[i-1][j]!=0: count+=1
                        if self.gridmatrix[i-1][j+1]!=0: count+=1
                        if self.gridmatrix[i][j+1]!=0: count+=1
                        ###
                        if count==3:
                            gridcopy[i][j]="+"
                elif j==0:
                    if self.gridmatrix[i][j]!=0:
                        count=0
                        if self.gridmatrix[i-1][j]!=0: count+=1
                        if self.gridmatrix[i-1][j+1]!=0: count+=1
                        if self.gridmatrix[i][j+1]!=0: count+=1
                        if self.gridmatrix[i+1][j+1]!=0: count+=1
                        if self.gridmatrix[i+1][j]!=0: count+=1
                        ###
                        if count<2 or count>3:
                            gridcopy[i][j]="-"
                        elif count==2 or count==3:
                            pass
                    elif self.gridmatrix[i][j]==0:
                        count=0
                        if self.gridmatrix[i-1][j]!=0: count+=1
                        if self.gridmatrix[i-1][j+1]!=0: count+=1
                        if self.gridmatrix[i][j+1]!=0: count+=1
                        if self.gridmatrix[i+1][j+1]!=0: count+=1
                        if self.gridmatrix[i+1][j]!=0: count+=1
                        ###
                        if count==3:
                            gridcopy[i][j]="+"
                elif j==(700//self.grid_v)-1:
                    if self.gridmatrix[i][j]!=0:
                        count=0
                        if self.gridmatrix[i-1][j]!=0: count+=1
                        if self.gridmatrix[i-1][j-1]!=0: count+=1
                        if self.gridmatrix[i][j-1]!=0: count+=1
                        if self.gridmatrix[i+1][j-1]!=0: count+=1
                        if self.gridmatrix[i+1][j]!=0: count+=1
                        ###
                        if count<2 or count>3:
                            gridcopy[i][j]="-"
                        elif count==2 or count==3:
                            pass
                    elif self.gridmatrix[i][j]==0:
                        count=0
                        if self.gridmatrix[i-1][j]!=0: count+=1
                        if self.gridmatrix[i-1][j-1]!=0: count+=1
                        if self.gridmatrix[i][j-1]!=0: count+=1
                        if self.gridmatrix[i+1][j-1]!=0: count+=1
                        if self.gridmatrix[i+1][j]!=0: count+=1
                        ###
                        if count==3:
                            gridcopy[i][j]="+"
                else:
                    print("missed sth?")

        #delete or draw a rectangle 
        for i in range(700//self.grid_h):
            for j in range(700//self.grid_v):
                if gridcopy[i][j]=="+" and self.gridmatrix[i][j]==0:
                    rstt=self.canvas.create_rectangle(j*self.grid_v+1,i*self.grid_h+1,(j+1)*self.grid_v-1,(i+1)*self.grid_h-1, fill=self.color)
                    self.gridmatrix[i][j]=rstt
                elif gridcopy[i][j]=="-" and self.gridmatrix[i][j]!=0:
                    self.canvas.delete(self.gridmatrix[i][j])
                    self.gridmatrix[i][j]=0
        self.root.after(700, None)

    def between(self): #when a player ends his turn and before the other player's turn
        if self.availiablemoves == 0:
            self.endtime = time.time()
            self.pt.configure(state="disabled")
            if self.iterations==0: #if by mistake 0 iterations are selected, the program will make one iteration.
                self.next()
            else:
                for i in range(self.iterations):
                    self.next()
            self.evaluate()
            self.root.after(2000, self.toggle_player)
            #self.root.after(3000, self.pt.configure(state="normal"))
            
    def evaluate(self): #calculate the score
        left=0
        for i in range(700//self.grid_h):
            for j in range(700//self.grid_v):
                if self.gridmatrix[i][j]!=0:
                    left+=1
        score = left
        score += (1.5**((left-self.moves)))/20
        score += score**(3/5)
        score += ran.uniform(0.5,1)*self.moves
        score -= ran.uniform(0.8,1)*((self.moves-left)/self.moves)
        score -= ran.uniform(0.6,1)*((self.moves-left)/self.iterations)
        score -= ran.uniform(0.6,1)*((int(self.endtime-self.timestart))/self.moves)
        if score<0:
            score=ran.choice([-1,-0.7,-0.6,-0.5,-0.2,0])*score
        if self.whoplays=="Player 1":
            self.score1.configure(state="normal")
            cur = int(self.score1.get("1.0","end"))
            self.score1.delete("1.0","end")
            cur += int(score+0.5)
            self.score1.insert("end", cur)
            self.score1.configure(state="disabled")
        elif self.whoplays=="Player 2":
            self.score2.configure(state="normal")
            cur = int(self.score2.get("1.0","end"))
            self.score2.delete("1.0","end")
            cur += int(score+0.5)
            self.score2.insert("end", cur)
            self.score2.configure(state="disabled")

    def close(self,event=None): #close the app
        self.root.destroy()



root=tk.Tk()
Myapp(root)
root.mainloop()
