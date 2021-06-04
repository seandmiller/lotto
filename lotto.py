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

img=Image.open('casino_gif.gif')

final_img=ImageTk.PhotoImage(img)

def name():
   global hous_name
   hous_name=the_house.get()
   global gamblr_name 
   gamblr_name=gambler.get()

   if hous_name!="" and gamblr_name!="":


   	   house.config(text=f"The House: {hous_name}",fg='red')
   	   gamblr.config(text=f"Gambler: {gamblr_name}",fg='blue')
   	   house.grid(row=12,column=1)
   	   gamblr.grid(row=12,column=3)
# element destroyers 
   	   btn_name.destroy()
   	   the_house.destroy()
   	   gambler.destroy()
   	   gamblr_lbl.destroy()
   	   house_lbl.destroy()
hous_name=''
gamblr_name=''
img_file='casino_gif.gif'
img1=Image.open('casino_gif.gif') # Max frames = 22

frames=61
imga=[PhotoImage(file=img_file,format='gif - {}'.format(i)) for i in range(frames)]

img1_finale=ImageTk.PhotoImage(img1)



def gif(end,count):
	global anim
	
	im2=imga[count]
	m_image.config(image=im2,bg='darkgreen')
	count += 1
	if count==end:
		count=0
		
		m_image.config(image=final_img,bg='lightgray')
		return stop_anim()    
		 
	anim=window.after(50,lambda: gif(end_frame,count))

    		
def stop_anim():
	window.after_cancel(anim)
global gambler_dlr
gambler_dlr=100
global house_dlr
house_dlr=1000
itre=False
def lever(g, h,itr):
	global count
	count=0
	global end_frame
	end_frame=randrange(33,53)
	if end_frame >= 46:  
	  gif(61,count)
	else:
	  gif(end_frame,count)
	global gambler_dlr
	gambler_dlr=g
	global house_dlr
	house_dlr=h
	
	
	try:
	  bet=float(bet_entry.get())
	  bait=float(bait_entry.get())
	except:
	  bet=0
	  bait=0


	g_name=gamblr_name if gamblr_name!="" else 'The Gambler'
	h_name=hous_name if hous_name!="" else 'The House'
	enuf_cash=True if bet <= house_dlr // 10 and bait <= gambler_dlr else False
	enuf_cash1=True if bet <=gambler_dlr and bait <= house_dlr else False
	win=True if end_frame >= 46 else False #13% chance of winning 
	hook=True if bait==bet else False
	
	if enuf_cash==True and enuf_cash1==True:
		if win==True and hook==True:
			earnings=tools(bet*20).comma(dollar=True,decima=True)
			gambler_dlr+= bet * 20
			house_dlr-=bet * 20
			winner_msg.config(text=f'{g_name} has won {earnings}')
		elif win==True and hook==False:
			earnings=tools(bet*10).comma(dollar=True,decima=True)
			gambler_dlr+= bet * 10
			house_dlr-= bet * 10
			winner_msg.config(text=f'{g_name} has won {earnings}')
		elif win==False and hook==True:
			earnings=tools(bet*3).comma(dollar=True,decima=True)
			house_dlr+= bet * 3
			gambler_dlr -=bet*3
			winner_msg.config(text=f'{h_name} has won {earnings}')
		elif win==False and hook==False:
			earnings=tools(bet).comma(dollar=True,decima=True)
			house_dlr+=bet
			gambler_dlr-=bet
			winner_msg.config(text=f'{h_name} has won {earnings}')
	
	gambler_dlrF=tools(gambler_dlr).comma(dollar=True,decima=True)
	house_dlrF=tools(house_dlr).comma(dollar=True,decima=True)
	remaining_g=f"with only {gambler_dlrF} remaining" if gambler_dlr==0 else f"owing {gambler_dlrF} in the end!!!"
	remaining_h=f"{house_dlrF}\n isn't going to pay the lease!!!" if house_dlr==0 else f"Holy Shit!!!\n you're {house_dlrF} in debt!!"
	if gambler_dlr<=0:
		winner_msg.config(fg='red',text=f'{g_name} is absolute trash\n DESTROYED!!! \n {remaining_g}')
	elif house_dlr<=10:
		winner_msg.config(fg='blue',text=f'{h_name} {remaining_h}')		


	
	#print(house_dlr)
	#print(gambler_dlr)

	gamblr_money.config(text=gambler_dlrF)
	house_money.config(text=house_dlrF)


	#print(house_dlrF.comma(dollar=True,decima=True))

# 6

winner_msg=Label(window,text='Winner will be displayed here',pady=30)
winner_msg.grid(row=6,column=1,columnspan=3)


house_money=Label(window,text='1,000$',fg='red',borderwidth=2)
gamblr_money=Label(window,text='100$',fg='blue',borderwidth=2)
house_money.grid(row=13,column=1)
gamblr_money.grid(row=13,column=3)


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

#space=Label(window,pady=30,padx=20)
#space.grid(row=6,column=1)


m_image.grid(row=7,column=1,columnspan=3)

the_lever=Button(window,text='lever',command=lambda: lever(gambler_dlr,house_dlr,itre))
the_lever.grid(row=8,column=1,columnspan=3)
stp=Button(window,text='stop',command=stop_anim)


window.mainloop()	   
