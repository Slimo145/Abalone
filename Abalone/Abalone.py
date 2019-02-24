#Button-1(left button) to pick marble
#Button-2(wheel) to move


from tkinter import *
from math import *

def create_board():
    l=[]
    l1=[]
    j=120
    c.create_polygon(200, 120-40*sqrt(3), 520, 120-40*sqrt(3),
                     680, 120+120*sqrt(3), 520, 200+240*sqrt(3),
                     200, 200+240*sqrt(3), 40, 120+120*sqrt(3),
                     fill='brown', outline='black')
    for i in range(5):
        c.create_oval(i*60-20+240, j-20, i*60+20+240, j+20, fill='wheat', outline='wheat')
        l+=[[i*60+240, j]]
        i+=1
    for q in range(4):
        for i in range(0,len(l),2):
            c.create_oval(l[i][0]-30-20, l[i][1]+30*sqrt(3)-20,
                          l[i][0]-30+20, l[i][1]+30*sqrt(3)+20,
                          fill='wheat', outline='wheat')
            c.create_oval(l[i][0]+30-20, l[i][1]+30*sqrt(3)-20,
                          l[i][0]+30+20, l[i][1]+30*sqrt(3)+20,
                          fill='wheat', outline='wheat')
            l1+=[[l[i][0]-30, l[i][1]+30*sqrt(3)]]
            l1+=[[l[i][0]+30, l[i][1]+30*sqrt(3)]]
        if len(l)%2==0:
            i=len(l)-1
            c.create_oval(l[i][0]+30-20, l[i][1]+30*sqrt(3)-20,
                          l[i][0]+30+20, l[i][1]+30*sqrt(3)+20,
                          fill='wheat', outline='wheat')
            l1+=[[l[i][0]+30, l[i][1]+30*sqrt(3)]]
        l=l1
        l1=[]
        
    for q in range(4):
        for i in range(1,len(l)-1,2):
            c.create_oval(l[i][0]+30-20, l[i][1]+30*sqrt(3)-20,
                          l[i][0]+30+20, l[i][1]+30*sqrt(3)+20,
                          fill='wheat', outline='wheat')
            c.create_oval(l[i][0]-30-20, l[i][1]+30*sqrt(3)-20,
                  l[i][0]-30+20, l[i][1]+30*sqrt(3)+20,
                          fill='wheat', outline='wheat')
            l1+=[[l[i][0]-30, l[i][1]+30*sqrt(3)]]
            l1+=[[l[i][0]+30, l[i][1]+30*sqrt(3)]]
        if len(l)%2==0:
            i=len(l)-1
            c.create_oval(l[i][0]-30-20, l[i][1]+30*sqrt(3)-20,
                          l[i][0]-30+20, l[i][1]+30*sqrt(3)+20,
                          fill='wheat', outline='wheat')
            l1+=[[l[i][0]-30, l[i][1]+30*sqrt(3)]]
        l=l1
        l1=[]
        
    c.create_polygon(780,540-60,780+30*sqrt(3),540-30,780+30*sqrt(3),540+30,
                     780,540+60,780-30*sqrt(3),540+30,780-30*sqrt(3),540-30,
                     fill='brown')
    c.create_line(780,480,780,600)
    c.create_line(780+30*sqrt(3),540-30,780-30*sqrt(3),540+30)
    c.create_line(780-30*sqrt(3),540-30,780+30*sqrt(3),540+30)
    

def set_marbles():
    global white
    global black
    for i in range(240,481,60):
        white+=[[i,120]]
        black+=[[i,120+240*sqrt(3)]]
    for i in range(210,511,60):
        white+=[[i,120+30*sqrt(3)]]
        black+=[[i,120+210*sqrt(3)]]
    for i in range(300,421,60):
        white+=[[i,120+60*sqrt(3)]]
        black+=[[i,120+180*sqrt(3)]]
    draw()

def draw():
    create_board()
    for i in white:
        c.create_oval(i[0]-20, i[1]-20, i[0]+20, i[1]+20, fill='white')
    for i in black:
        c.create_oval(i[0]-20, i[1]-20, i[0]+20, i[1]+20, fill='black')
        
def check(ch,m):
    res=True
    i=0
    if len(ch)>0:
        while i<len(ch) and res==True:
            if ch[i]==m:
                res=False
                if len(ch)!=3 or i!=1:
                    ch.pop(i)
            i+=1
        if res==True:
            if len(ch)<3:
                if not one_line(m[0],m[1],ch):
                    res=False
            else:
                res=False
    return [res,ch]

def get_marble(event):
    global turn
    global chosen
    global set_flag
    global white
    global black
    x=event.x
    y=event.y
    if set_flag[0]:
        x0,y0=find_center(x,y)
        if x0>0:
            if set_flag[1]=='white' and not [x0,y0] in white and not [x0,y0] in black:
                white+=[[x0,y0]]
            elif set_flag[1]=='black' and not [x0,y0] in white and not [0,y0] in black:
                black+=[[x0,y0]]
            if len(white)==set_flag[2]:
                set_flag[1]='black'
            if len(black)==14:
                set_flag[0]=False
            draw()
    else:
        res=[]
        draw()
        if turn==0:
            for i in white:
                if abs(x-i[0])<20 and abs(y-i[1])<20:
                    res=i
        else:
            for i in black:
                if abs(x-i[0])<20 and abs(y-i[1])<20:
                    res=i
        if res!=[] and check(chosen,res)[0]:
            chosen=check(chosen,res)[1]
            chosen+=[res]
        chosen.sort()
        for i in chosen:
            c.create_oval(i[0]-20, i[1]-20, i[0]+20, i[1]+20, fill='grey')

def one_line(x,y,ch):
    res=False
    if len(ch)==1:
        if abs(x-chosen[0][0])<61 and abs(x-chosen[0][0])>1 and abs(y-chosen[0][1])<30*sqrt(3)+1:
            res=True
    else:
        dx=chosen[1][0]-chosen[0][0]
        dy=chosen[1][1]-chosen[0][1]
        x0=chosen[0][0]
        y0=chosen[0][1]
        if abs(y-(dy/dx)*(x-x0)-y0)<5:
            res=True
    return res

def is_marble(x,y):
    res=None
    for i in white:
        if abs(i[0]-x)<1 and abs(i[1]-y)<1:
            res='white'
    for i in black:
        if abs(i[0]-x)<1 and abs(i[1]-y)<1:
            res='black'
    return res

def get_square(a,b,c):
    la=sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    lb=sqrt((c[0]-b[0])**2+(c[1]-b[1])**2)
    lc=sqrt((a[0]-c[0])**2+(a[1]-c[1])**2)
    p=(la+lb+lc)/2
    res=sqrt(p*(p-la)*(p-lb)*(p-lc))
    return res

def on_board(n):
    res=True
    square=0
    v=[[240,120],[480,120],
       [600,120+120*sqrt(3)],[480,120+240*sqrt(3)],
       [240,120+240*sqrt(3)],[120,120+120*sqrt(3)]]
    for i in range(len(v)):
        square+=get_square(n,v[i],v[(i+1)%len(v)])
    if abs(square-86400*sqrt(3))>5:
        res=False
    return res
    
def move_marble(x,y,x0,y0,ch,t):
    if len(ch)>1:
        dx=x-ch[0][0]
        dy=y-ch[0][1]
        mar=[]
        res=True
        if t==1:
            while is_marble(x0,y0)=='white':
                mar+=[[x0,y0]]
                x0=x0+dx
                y0=y0+dy
            if is_marble(x0,y0)==None:
                if len(mar)<len(ch):
                    for i in range(len(mar)):
                        change('w',mar[i],dx,dy)
                    for i in range(len(ch)):
                        change('b',ch[i],dx,dy)
            else:
                res=False
        if t==0:
            while is_marble(x0,y0)=='black':
                mar+=[[x0,y0]]
                x0=x0+dx
                y0=y0+dy
            if is_marble(x0,y0)==None:
                if len(mar)<len(ch):
                    for i in range(len(mar)):
                        change('b',mar[i],dx,dy)
                    for i in range(len(ch)):
                        change('w',ch[i],dx,dy)
            else:
                res=False
    return res

def change(color,n,dx,dy):
    global white
    global black
    global w_left
    global b_left
    if color=='w':
        i=0
        while i<len(white) and (abs(white[i][0]-n[0])>1 or abs(white[i][1]-n[1])>1):
            i+=1
        white[i]=[white[i][0]+dx,white[i][1]+dy]
        if not on_board(white[i]):
            del(white[i])
            c.itemconfig(w_left,text='White: '+str(len(white)))
    if color=='b':
        i=0
        while i<len(black) and (abs(black[i][0]-n[0])>1 or abs(black[i][1]-n[1])>1):
            i+=1
        black[i]=[black[i][0]+dx,black[i][1]+dy]
        if not on_board(black[i]):
            del(black[i])
            c.itemconfig(b_left,text='Black: '+str(len(black)))

def find_center(x,y):
    resx=-1
    resy=-1
    y0=120
    x0=240
    for i in range(9):
        for j in range(9):
            if abs(y-y0)<20 and abs(x-x0)<20:
                resx,resy=x0,y0
            x0+=60
        y0+=30*sqrt(3)
        x0=120+((i+1)%2)*30
    return resx,resy

def get_arrow(xc,yc,x,y):
    res=[False,-1]
    v=[[[xc,yc-60,],[xc+30*sqrt(3),yc-30],[xc,yc]],   #NE,E,SE,SW,W,NW
       [[xc+30*sqrt(3),yc+30],[xc+30*sqrt(3),yc-30],[xc,yc]],
       [[xc,yc+60,],[xc+30*sqrt(3),yc+30],[xc,yc]],
       [[xc,yc+60,],[xc-30*sqrt(3),yc+30],[xc,yc]],
       [[xc-30*sqrt(3),yc-30,],[xc-30*sqrt(3),yc+30],[xc,yc]],
       [[xc,yc-60,],[xc-30*sqrt(3),yc-30],[xc,yc]]]
    print(x,y)
    for i in range(len(v)):
        square=0
        for j in range(len(v[i])):
            square+=get_square([x,y],v[i][j],v[i][(j+1)%len(v[i])])
        if abs(square-900*sqrt(3))<1:
            res=[True,i]
        print(res)
    if res[1]==0:
        dx,dy=30,-30*sqrt(3)
    elif res[1]==1:
        dx,dy=60,0
    elif res[1]==2:
        dx,dy=30,30*sqrt(3)
    elif res[1]==3:
        dx,dy=-30,30*sqrt(3)
    elif res[1]==4:
        dx,dy=-60,0
    elif res[1]==5:
        dx,dy=-30,-30*sqrt(3)
    else:
        dx,dy=0,0
    return dx,dy

def get_direction(x0,y0,ch):
    global control
 #   control='left marble'
 #   control='pad'
    print(control)
    if control=='left marble':
        x,y=find_center(x0,y0)
        if abs(x-chosen[0][0])<61 and abs(x-chosen[0][0])>1 and abs(y-chosen[0][1])<30*sqrt(3)+1:
            dx=x-ch[0][0]
            dy=y-ch[0][1]
    elif control=='pad':
        xc,yc=780,540
        dx,dy=get_arrow(xc,yc,x0,y0)
    print('dx,dy',dx,dy)
    return dx,dy
            
def move(event):
    global chosen
    global turn
    global t_turn
 #   x,y=find_center(event.x,event.y)
    res=False
    movement=False        
    if chosen!=[]: # and x>=0 and y>=0:
#        if abs(x-chosen[0][0])<61 and abs(x-chosen[0][0])>1 and abs(y-chosen[0][1])<30*sqrt(3)+1:
            dx,dy=get_direction(event.x,event.y,chosen)
 #           dx=x-chosen[0][0]
#            dy=y-chosen[0][1]
            x=dx+chosen[0][0]
            y=dy+chosen[0][1]
            print(chosen,x,y)
            if dx!=0:
                if one_line(x,y,chosen):
                    if x>chosen[0][0]:
                        x0=chosen[len(chosen)-1][0]+dx
                        y0=chosen[len(chosen)-1][1]+dy
                    else:
                        x0,y0=x,y
                    print(x0,y0)
                    print(is_marble(x0,y0))
                    if is_marble(x0,y0)==None:
                        for i in range(len(chosen)):
                            movement=True
                            if turn==0:
                                change('w',chosen[i],dx,dy)
                            if turn==1:
                                change('b',chosen[i],dx,dy)
                    elif is_marble(x0,y0)=='white':
                        if turn==1:
                           # movement=True
                            movement=move_marble(x,y,x0,y0,chosen,turn)
                    elif is_marble(x0,y0)=='black':
                        if turn==0:
                            movement=True
                            movement=move_marble(x,y,x0,y0,chosen,turn)
                else:
                    res=True
                    for i in chosen:
                        if is_marble(i[0]+dx,i[1]+dy)!=None:
                            res=False
                    if res==True:
                        for i in range(len(chosen)):
                            movement=True
                            if turn==0:
                                change('w',chosen[i],dx,dy)
                            if turn==1:
                                change('b',chosen[i],dx,dy)
            if movement:
                chosen=[]
                draw()
                turn=(turn+1)%2
                if turn==1:
                    c.itemconfig(t_turn,text='Turn: black', font='Arial 32')
                else:
                    c.itemconfig(t_turn,text='Turn: white', font='Arial 32')
    if len(white)==0 and len(black)!=0:
        print(len(white))
        c.itemconfig(t_turn, text='Black wins', font='Arial 32')
    elif len(white)!=0 and len(black)==0:
        c.itemconfig(t_turn, text='White wins', font='Arial 32')

def again():
    global turn
    global white
    global black
    global chosen
    global restart
    global set_b
    global t_turn
    global w_left
    global b_left
    global set_flag
    global c
    global control
    for widget in root.winfo_children():
        widget.destroy()
    c = Canvas(root, width = 720+160, height = 240*sqrt(3)+240)
    c.bind('<Button-1>',get_marble)
    c.bind('<Button-2>',move)
    c.pack()
    restart=Button(root,text='New game', command=again)
    restart.pack()
    set_b=Button(root,text='Set your board', command=set_board)
    set_b.pack()
    menu=Button(root, text='Menu', command=create_menu)
    menu.pack()
    t_turn=c.create_text(700,100,text='Turn: white', font='Arial 32')
    w_left=c.create_text(750,140,text='White: 14', font='Arial 24')
    b_left=c.create_text(750,170,text='Black: 14', font='Arial 24')
    set_flag=[False,'white',14]
    white=[]
    black=[]
    chosen=[]
    turn=0
    set_marbles()
    try:
        control
    except NameError:
        control='pad'

def set_board():
    global white
    global black
    global set_flag
    global control
    again()
    c.delete('all')
    white=[]
    black=[]
    create_board()
    set_flag=[True,'white',14]
    try:
        control
    except NameError:
        control='pad'

def get_mode():
#    global v
    global control
    if v.get()=="1":
        control='left marble'
    elif v.get()=="2":
        control='pad'

def set_mode():
    global v
    for widget in root.winfo_children():
        widget.destroy()
    c = Canvas(root, width = 720+160, height = 240*sqrt(3)+240)
    c.pack()
    MODES = [
        ("Left is origin", "1"),
        ("Pad", "2")
    ]
    v = StringVar()
    v.set("2")
    i=0
    for mode, number in MODES:
        b = Radiobutton(root, text=mode, variable=v, value=number, command=get_mode)
        b.place(x=350, y=300+50*i, anchor=W)
        i+=1
    back=Button(root, text='Back', command=again)
    back.pack()

def open_settings():
    for widget in root.winfo_children():
        widget.destroy()
    c = Canvas(root, width = 720+160, height = 240*sqrt(3)+240)
    c.pack()
    mode=Button(root, text='Select control', command=set_mode)
    mode.pack()

def create_menu():
    global c
    for widget in root.winfo_children():
        widget.destroy()
    c = Canvas(root, width = 720+160, height = 240*sqrt(3)+240)
    c.pack()
    restart=Button(root,text='New game', command=again)
    restart.pack()
    set_b=Button(root,text='Set your board', command=set_board)
    set_b.pack()
    settings=Button(root,text='Settings', command=open_settings)
    settings.pack()

root = Tk()
create_menu()

#Button-1(left button) to pick marble
#Button-2(wheel) to move

