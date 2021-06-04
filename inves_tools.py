class tools:
	def __init__(self,whole,time=0,percentage=0,addition=0):
		self.whole=float(whole)
		self.percentage=percentage
		self.time=time
		self.addition=addition
		self.discounted_cashf=whole / (1 + (percentage/100))**time

	def inves(self):
	    whole=self.whole
	    perc=self.percentage/100
	    time=self.time
	    addition=self.addition
	    for x in range(time):
	    	whole=whole*(1+perc)
	    	whole+=addition
	    return whole
	def comma(self,dollar=False,decima=False):
	    arg=str(self.inves())
	    arg,deci=arg.split('.')
	    deci= "." + deci
	    arg=list(arg)
	    i=0
	    counter=0
	    for _ in arg:
	    	if counter==-3:
	    		arg.insert(i,",")
	    	elif counter<-3:
	    	    counter=0
	    	counter-=1
	    	i-=1
	    end_result=""
	    for el in arg:
	        end_result+=el
	    if decima==True:
	    	end_result+=deci	
	    if dollar==True:
	       final_result=f"{end_result}$"
	    elif dollar==False:
	       final_result=f"{end_result}" 
	    else:
	       return "Invalid dollar output"
	    return final_result
	def figures(self,d=False,dc=False):
	    counter=0
	    arg=self.comma(dollar=d,decima=dc)
	    for el in arg:
	        if el==',':
	           counter+=1
	    if counter==1:
	       return f"{arg} Thousand"
	    elif counter==2:
	       return f"{arg} Million"
	    elif counter==3:
	       return f"{arg} Billion"
	    elif counter==4:
	       return f"{arg} Trillion"                   
      	    	

	    
box=tools(1000000000,5,23.5)

