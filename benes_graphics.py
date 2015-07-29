# Import a library of functions called 'pygame'
import pygame
from math import pi
import math

# Our logic code is here

level=input("Enter the Benes level")
Fheight=Fwidth=650
vsplits=2**(level+1)
vwidth=Fheight/vsplits
vy=[]
vx=[]
vy.append(vwidth)
#our x coordinate center for all diagrams will be 300 
vx.append(Fwidth/2) 
for i in range(0,(vsplits/2)-1):
    vy.append((vy[-1]+2*vwidth))
    vx.append(Fwidth/2)
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
    print i

# Our code ends here.Graphics starts
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [Fheight, Fwidth]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Graph Representation for Benes : " + str(level))
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    # Draw a circle

    for i in vcord:
        pygame.draw.circle(screen, BLUE, i, 2)

    for i in hcord:
        for k in i:
            pygame.draw.circle(screen, BLUE, k, 2)

    for i in hcord:
        if len(i)==4:
            for p in vcord:
                for k in i:
                    if (abs(k[1]-p[1]))==vwidth:
                        pygame.draw.line(screen, GREEN,p,k,1)

    maxlen=0

    for i in hcord:
        if len(i)>=maxlen:
            maxlen=len(i)

    noofiters = maxlen/2
    temp1=[]
    temp2=[]
    start=4
    #print "no of fileters %d" % noofiters
    while start<=noofiters:
        for k in hcord:
            if len(k)==start:
                temp1.append(k)
            elif len(k)==(start*2):
                temp2.append(k)

        workingList1=[]
        workingList2=[]

        for i in range(0,len(temp1)):
            workingList1 = temp1[i]
            workingList2 = temp2[i/2]
            #print workingList1[0]
            #print workingList2[0]
            while len(workingList1)!=0:
                pygame.draw.line(screen, GREEN,workingList1[0],workingList2[0],1)
                pygame.draw.line(screen, GREEN,workingList1[0],workingList2[1],1)
                workingList1 = workingList1[1:]
                workingList2 = workingList2[2:]
                #print len(workingList2)
                #pop the wL1.pop(0) and wL2.pop(0),wL2.pop(0)
                #popped two times to get two poppings
        start*=2

    
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()