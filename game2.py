import msvcrt
import time

finish=10
count=0

print "Press enter key to get started!"

raw_input()
s_time=time.time()

print "Press d to move right\n"
while(1):
	key=msvcrt.getch()
	if key=='d':
		count=count+1
		print "-->",
		if count==finish:
			break
	else:
		print "You have lost the game"
		raw_input()
		exit()

count=0		
print "Press s to move down"
while(1):
	key=msvcrt.getch()
	if key=='s':
		count=count+1
		print "                                       |"
		if count==finish:
			break
	else:
		print "You have lost the game"
                raw_input()
		exit()

count=0
print "Press d to move right                  ",
while(1):
	key=msvcrt.getch()
	if key=='d':
		count=count+1
		print "-->",
		if count==finish:
			break
	else:
		print "You have lost the game"
		raw_input()
		exit()

		
time_elapsed=time.time()-s_time
print "\nCongrats You have finished the game"
print "\nTime taken is "+str(time_elapsed)
raw_input()
