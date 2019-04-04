import os
import subprocess as sp 
import time
import sys
import threading
from colorama import *

#Color scheme for the CLI
G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'   # white

os.system('clear')

def banner():
	print
	print
	print
	print '                                            				  %s##################################'%(R)
	print '                                            				  %s#                                #'%(R)
	print '                                           				  %s#                                #'%(R)	
	print '                                            				  %s#    %sGood,Bad and the Ugly       %s#'%(R,W,R)
	print '                                            				  %s#                                #'%(R)
	print '                                            				  %s#                                #'%(R)
	print '                                            				  %s##################################'%(R)
	print '                                            				  %s    Developed By %sSaransh Rana'%(Y,W)
	print
	print
	print '                                           %sTool developed using Machine Learning to detect Malware and Intrusion Detection on your system and network.'%W
	print 
	print Style.RESET_ALL
	time.sleep(3)

def main():
	global G 
	global R
	global W
	global Y
	global B 
	banner()
	print
	print 
	print '%s################################################################################### %sENTERING GBU %s##################################################################################################################'%(G,R,G)
	print 
	time.sleep(1.6)
	print '%s<GBU:#>'%B
	time.sleep(0.14)
	print '%s<GBU:#> %s1. Malware Detection '%(B,W)
	time.sleep(0.14)
	print '%s<GBU:#> %s2. Intrusion Detection '%(B,W)
	time.sleep(0.14)
	var1 = raw_input('%s<GBU:#> %sYour choice: '%(B,W))
	time.sleep(0.14)
	if int(var1) == 1:
	
		malware_detection()
	
	elif int(var1) == 2:
	
		intrusion_detection()
	
	else:
	
		print '%s<GBU:#> %sInvalid Choice exiting..'%(B,W)
		time.sleep(1)
		os.system('clear')
		time.sleep(2)
		sys.exit(0)

def malware_detection():
	
	global G 
	global R
	global W
	global Y
	global B  

	#Starting Program
	os.system('clear')
	time.sleep(0.12)
	print
	print '%s#################################################################################################### %sRunning Malware Detection %s####################################################################################'%(G,R,G)
	print 
	#Input of the file
	var2 = raw_input('%s<GBU:#> %sEnter the Path of the File: '%(B,W))
	time.sleep(0.11)
	print '%s<GBU:#> %sSelected File: %s%s'%(B,W,R,var2)
	#File Check
	time.sleep(0.11)
	print '%s<GBU:#> %sChecking if file exists or not'%(B,W)
	time.sleep(3)
	if os.path.exists(var2) == True:
		print '%s<GBU:#> %sRunning Scan..'%(B,W)
		time.sleep(5)
		
		"""
			<PLACE FOR ML MODEL>
		"""
		
		#Output After running ML 
		print '%s<GBU:#> %sRan ML Model..'%(B,W)												
		time.sleep(2)
		print '%s<GBU:#> %sFinished Now..'%(B,W)
		
		#Check Another File
		var3 = raw_input('%s<GBU:#> %sCheck Another File (Y or N): '%(B,W))
		print Style.RESET_ALL
		var3 = var3.replace(" ","")
		if var3.lower() == 'y':
		
			os.system('clear')
			time.sleep(2)
			malware_detection()
		
		elif var3.lower() == 'n':
		
			time.sleep(2)
			print '%s<GBU:#> %sGoing Back to main program \r\n'%(B,W)
			os.system('clear')
			time.sleep(2)
			main()
		
		else:
		
			print '%s<GBU:#> %sInvalid choice going back to main program\r\n'%(B,W)
			os.system('clear')
			time.sleep(0.11)
			main()
	
	elif os.path.exists(var2) == False:

		print "%s<GBU:#> %sFile Doesn't Exists"%(B,W)
		time.sleep(2)
		var4 = raw_input("%s<GBU:#> %sRe-Upload the file(Y or N): "%(B,W))
		if var4.lower() == 'y':
			time.sleep(2)
			os.system('clear')
			malware_detection()
		elif var4.lower() == 'n':
			time.sleep(2)
			os.system('clear')
			main()
		else:
			print '%s<GBU:#> %sInvalid Choice\r\n'%(B,W)
			time.sleep(2)
			os.system('clear')
			main()
	
	else:

		print '%s<GBU:#> %s Caught Unexpected Error exiting now..'
		sys.exit(0)


def intrusion_detection():
	global G 
	global R
	global W
	global Y
	global B 

	print 'Hey'
	sys.exit(0)


main()

