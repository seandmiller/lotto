from tkinter import * 
from random import randrange
from inves_tools import tools 
from PIL import ImageTk,Image
from time import sleep
 

 # user inserts bait data 
 # user inserts bet data 
 # random slot selections, based on random number gambler or house wins



window =Tk()
window.title('The Lotto')
the_house=Entry(window,fg='red')
gambler=Entry(window,fg='blue')
the_house.grid(row=1,column=0,columnspan=2)
gambler.grid(row=1,column=3,columnspan=2)
house=Label(window,text=the_house.get())
gamblr=Label(window,text=gambler.get())
house_lbl=Label(window,text="The House",fg='white',bg='red',padx=20)
gamblr_lbl=Label(window,text='The Gambler',bg='blue',fg='white',padx=20)
house_lbl.grid(row=0,column=0,columnspan=2)
gamblr_lbl.grid(row=0,column=3,columnspan=2)

img=Image.open('casino.jpg')
img=img.resize((480,370),Image.ANTIALIAS)
final_img=ImageTk.PhotoImage(img)

def name():
   if the_house.get()!="" and gambler.get()!="":


   	   house.config(text=the_house.get(),fg='red')
   	   gamblr.config(text=gambler.get(),fg='blue')
   	   house.grid(row=12,column=1)
   	   gamblr.grid(row=12,column=3)
   	   
# element destroyers 
   	   btn_name.destroy()
   	   the_house.destroy()
   	   gambler.destroy()
   	   gamblr_lbl.destroy()
   	   house_lbl.destroy()
frames=20
img_file='casino_gif.gif'
img1=Image.open('casino_gif.gif') # Max frames = 22

imga=[PhotoImage(file=img_file,format=f'gif -index {i}') for i in range(frames)]

img1_finale=ImageTk.PhotoImage(img1)

count=0
def gif(count):
	global anim
	im2=imga[count]
	m_image.config(image=im2,bg='#44055D')
	count += 1
	if count==frames:
		count=0
		
		m_image.config(image=final_img,bg='lightgray')
		return stop_anim()    
		 
	anim=window.after(50,lambda: gif(count))

    		
def stop_anim():
	window.after_cancel(anim)

def lever():
	gif(count)
	gambler_dlr=100
	house_dlr=1000
	draw=randrange(1,10)
	bet=float(bet_entry.get())
	bait=float(bait_entry.get())
	enuf_cash=True if bet <= house_dlr // 10 and bait <= gambler_dlr else False
	enuf_cash1=True if bet <=gambler_dlr and bait <= house_dlr else False
	win=True if draw==1 else False
	hook=True if bait==bet else False
	if enuf_cash==True and enuf_cash1==True:
		if win==True and hook==True:
			gambler_dlr+= bet * 20
			house_dlr-=bet * 20
			print(gambler_dlr,house_dlr)
  	   

btn_name=Button(window,text='o',command=name)
btn_name.grid(row=3,column=3)

bait_label=Label(window,text='The Bait',bg='red',fg='white')
bet_label=Label(window,text='The bet',bg='blue',fg='white')
bait_entry=Entry(window,fg='red')
bet_entry=Entry(window,fg='blue')

m_image=Label(window,image=final_img)

bait_label.grid(row=4,column=0)
bet_label.grid(row=4,column=4)
bait_entry.grid(row=5,column=0)
bet_entry.grid(row=5,column=4)

space=Label(window,pady=30)
space.grid(row=6,column=1)


m_image.grid(row=7,column=1,columnspan=3)

def pint():
	print('bad dabs')

the_lever=Button(window,text='lever',command=lever)
the_lever.grid(row=8,column=1,columnspan=3)
stp=Button(window,text='stop',command=stop_anim)


window.mainloop()	   
