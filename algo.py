level=input("Enter the Benes level")
Fheight=Fwidth=600
vsplits=2**(level+1)
vwidth=Fheight/vsplits
vy=[]
vx=[]
vy.append(vwidth)
#our x coordinate center for all diagrams will be 300 
vx.append(300) 
for i in range(0,(vsplits/2)-1):
	vy.append((vy[-1]+2*vwidth))
	vx.append(300)
vcord=zip(vx,vy)
#vcord has the coordinate values for the center most vertical column of the Benes network
#harrpts=horizontal array points. It's the number of points in horizontal array when you read from top to bottom in Benes network like benes2 has [4,8,4] benes3 has [4,8,16,8,4]
baseno=4
#Benes1 has 4 nodes in the center horizontal. I am taking 4 as my baseno and based on this calulations for finding the coordinate has been done
# to genrate the above mentioned array logic the following above lines of code:
harrpts=[]
for i in range(1,level+1):
	temp=harrpts[:]
	mvalue=2**(i+1)
	harrpts.append(mvalue)
	harrpts+=temp
	temp=[]
print "The harrpts value is"
print harrpts
#End of the logic for calculating the number of points in any horizontal row
#Start of the logic for calculating the coordinates values for the horizontal nodes
hy=[]
hx=[]
hcord=[]
newheight=2*vwidth
hy.append(newheight)
for i in harrpts:
	hwidth=Fwidth/(2*i)
	hx.append(hwidth)
	for j in range(0,i-1):
		hx.append(hx[-1]+2*hwidth)	
		hy.append(newheight)
	hcord.append(zip(hx,hy))
	newheight=hy.pop()+2*vwidth
	print "this is the i value : "+str(i)
	hx=[]
	hy=[]
	hy.append(newheight)
print "\n\nThe coordinates of the benes network are:\n"
print "\n\nThe center nodes coordinates are:\n"
print vcord
print "\n\nThe coordinates of the horizontal row printed from top to bottom:\n"
for i in hcord:
	print i;

