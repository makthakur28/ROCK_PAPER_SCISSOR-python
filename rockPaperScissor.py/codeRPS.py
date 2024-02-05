from tkinter import *
from PIL import Image,ImageTk
import random

rps = Tk()
rps.title("Rock-Paper-Scissors")

rps.geometry('500x500')
rps.maxsize(500,500)
rps.minsize(500,500)
rps.config(background='lavender')

playLbl = Label(rps,text='PLAY!!',font=('Arial',18,'bold'),width=60)
playLbl.pack(fill=X)
playLbl.config(justify=CENTER,bg='lavender')

frame = Frame(rps,background='lavender')
frame.pack(fill=X)
frame1= Frame(frame,background='lavender')
frame1.pack(side=LEFT)
frame2= Frame(frame,background='lavender')
frame2.pack(side=RIGHT)
pUser = Label(frame1,text='User',font=('Verdana',12),background='lavender')
pUser.config()
pBot = Label(frame2,text='BOT',font=('Verdana',12),background='lavender')
pBot.config()

pUser.pack(fill=X,padx=100)
pBot.pack(fill=X,padx=100)

R2Frame = Frame(rps,background='lavender')
R2Frame.pack()

img_frame1=Frame(R2Frame)
img_frame2=Frame(R2Frame)
img_frame1.pack(side=LEFT,padx=75)
img_frame2.pack(side=RIGHT,padx=75)

# img1=Image.open(r'C:\Users\ASUS\Desktop\Python projects\rockPaperScissor.py\RPS_resources\rock.jpg')
# resized_img1=img1.resize((100,100))
# new_img1=ImageTk.PhotoImage(resized_img1)
img1_label=Label(img_frame1)
img1_label.pack()

# img2=Image.open(r'C:\Users\ASUS\Desktop\Python projects\rockPaperScissor.py\RPS_resources\paper.jpg')
# resized_img2=img2.resize((100,100))
# new_img2=ImageTk.PhotoImage(resized_img2)
img2_label=Label(img_frame2)
img2_label.pack()

framep = Frame(rps,background='lavender')
framep.pack(fill=X)
framep1= Frame(framep,background='lavender')
framep1.pack(side=LEFT)
framep2= Frame(framep,background='lavender')
framep2.pack(side=RIGHT)

uVar = StringVar()
bVar = StringVar()
ScoreUser = Label(framep1,text='',font=('Verdana',12),background='lavender',textvariable=uVar)
ScoreBot = Label(framep2,text='',font=('Verdana',12),background='lavender',textvariable=bVar)

ScoreUser.pack(fill=X,padx=75,pady=20)
ScoreBot.pack(fill=X,padx=100,pady=20)

Can1 = Canvas(rps,background='lavender')
Can1.pack(pady=20)
array=['paper.jpg','rock.jpg','scissor.jpg']


UScore=0
BScore=0
count=0

def bot_input(s):
    global UScore,BScore,count
    if count==10:
        if UScore>BScore:
            tVar.set("YOU WIN !!")
        elif UScore<BScore:
            tVar.set("BOT WIN!!")
        else:
            tVar.set('DRAW MATCH!!')
        UScore=BScore=count=0
        return
    count+=1
    #BOT
    inp=random.choice(array)
    img1=Image.open(r'C:\Users\ASUS\Desktop\Python projects\rockPaperScissor.py\RPS_resources\\'+inp)
    resized_img1=img1.resize((100,100))
    new_img1=ImageTk.PhotoImage(resized_img1)
    img2_label.config(image=new_img1)
    img2_label.image=new_img1

    #USER
    print(type(s))
    img2=Image.open(r'C:\Users\ASUS\Desktop\Python projects\rockPaperScissor.py\RPS_resources\\'+s)
    resized_img2=img2.resize((100,100))
    new_img2=ImageTk.PhotoImage(resized_img2)
    img1_label.config(image=new_img2)
    img1_label.image=new_img2

    #LOGIC PART
    if s=='rock.jpg' and inp=='paper.jpg':
        # print("BOT SCORED")
        BScore+=1
        # bVar+=1
        # str1 = "Score: "+str(BScore)
        # str2 = "Score: "+str(UScore)
        # uVar.set(str1)
        # bVar.set(str2)
        tVar.set("BOT SCORED..")

    elif s=='rock.jpg' and inp=='scissor.jpg':
        # print('YOU SCORED')
        UScore+=1
        # uVar.set(UScore)
        # str1 = "Score: "+str(UScore)
        # uVar.set(str1)
        tVar.set("YOU SCORED..")
    elif s=='paper.jpg' and inp=='scissor.jpg':
        # print('BOT SCORED')
        BScore+=1
        # bVar+=1
        # str1 = "Score: "+str(BScore)
        # bVar.set(str1)
        tVar.set("BOT SCORED..")
    elif s=='paper.jpg' and inp=='rock.jpg':
        # print('YOU SCORED')
        UScore+=1
        # uVar+=1
        # str1 = "Score: "+str(UScore)
        # uVar.set(str1)
        tVar.set("YOU SCORED..")
    elif s=='scissor.jpg' and inp=='paper.jpg':
        # print('BOT SCORED')
        UScore+=1
        # uVar+=1
        # str1 = "Score: "+str(UScore)
        # uVar.set(str1)
        tVar.set("YOU SCORED..")
    elif s=='scissor.jpg' and inp=='rock.jpg':
        # print('BOT SCORED')
        BScore+=1
        # bVar+=1
        # str1 = "Score: "+str(BScore)
        # bVar.set(str1)
        tVar.set("BOT SCORED..")
    else:
        # print('TIE')
        tVar.set("TIE")
    str1 = "Score: "+str(BScore)
    str2 = "Score: "+str(UScore)
    bVar.set(str1)
    uVar.set(str2)

rockBtn = Button(Can1,text='Rock',background='sky blue',command=lambda:bot_input('rock.jpg'))
paperBtn = Button(Can1,text='Paper',background='sky blue',command=lambda:bot_input('paper.jpg'))
scissorBtn = Button(Can1,text='Scissor',background='sky blue',command= lambda : bot_input('scissor.jpg'))

rockBtn.pack(side=LEFT,padx=10)
paperBtn.pack(side=LEFT,padx=10)
scissorBtn.pack(side=LEFT,padx=10)

tVar = StringVar()
output=Label(rps,text="",font=('times',16,'bold'),background='lavender',textvariable=tVar)
output.pack(pady=30)




   


rps.mainloop()