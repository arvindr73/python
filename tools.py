import pyttsx3
import os
import sys
import time

pyttsx3.speak("Welcome to the tools demo..")


while True:
	print()
	print()
	print("\t\t\t\tWelcome to the Tools Demo !!")
	print()
	print()
	print("We Support following Text Editors\t\t\t We Support following Social Media Applications")
	print()
	print(" 1. Textpad                                                         1. Facebook")
	print(" 2. Notepad                                                         2. Youtube")
	print(" 3. Wordpad                                                         3. LinkedIN")
	print()
	print("Supported browsers are as under.\t\t\t Other Applications as below..")
	print()
	print(" 1. Chrome                                                          1. Excel")
	print(" 2. Internet Explorer - IE                                          2. Current Date-Time")
	print("                                                                    3. Tableau") 	
	print("                                                                    4. Outlook")	
	print("                                                                    5. Oracle VirtualBox/VirtualBox")	
	print("                                                                    6. Google")
	print("                                                                    7. AWS Console")
	print("                                                                    8. Calculator") 
	print("                                                                    9. Media Player") 
	print("                                                                   10. Windows Explorer") 
	print("                                                                   11. Putty") 
	print("____________________________________________________________________________________________________________________________") 
	print()
	print("Pls let me know your requirements : "  , end='')
	p = input()

	os.system("cls")
	
	if ("run" in p)  and (("chrome" in p) or ("browser" in p)):
	  os.system("start chrome")
	
	elif (("run" in p) or  ("execute" in p ) or ("start" in p)) and  (("internet explorer" in p) or ("IE" in p) or ("ie" in p) ):
	  os.startfile("C:/Program Files/Internet Explorer/iexplore.exe")
	  
	elif (("run" in p) or  ("execute" in p ) or ("start" in p)) and  (("Oracle VM" in p) or ("Virtual Box" in p) or ("oracle vm" in p)):
	  os.startfile("C:/Program Files/Oracle/VirtualBox/VirtualBox.exe") 
	
	elif (("run" in p) or  ("execute" in p ) or ("start" in p)) and  (("Tableau" in p) or ("Tableau Desktop" in p) or ("tableau" in p) ):
	  os.startfile("C:/Program Files/Tableau/Tableau 10.5/bin/tableau.exe") 
	  	 
	elif (("run" in p) or  ("execute" in p ) or ("start" in p)) and  (("notepad" in p) or ("editor" in p) ):
	  os.system("notepad")
	
	elif (("run" in p) or  ("execute" in p ) or ("start" in p)) and  (("textpad" in p) or ("editor" in p) ):
	  os.system("start textpad")

	elif (("run" in p) or  ("execute" in p ) or ("start" in p)) and  (("wordpad" in p) or ("editor" in p) ):
	  os.system("start wordpad")
	  
	elif (("run" in p) or ("start" in p)) and  ("excel" in p) :
	  os.system("start excel") 

	elif (("run" in p) or ("start" in p)) and  ("google" in p):
	  os.system('start chrome "https://www.google.com" --kiosk')
	
	elif (("run" in p) or ("start" in p)) and  ("youtube" in p):
	  os.system('start chrome "https://www.youtube.com" --kiosk')
	
	elif (("run" in p) or ("start" in p)) and  (("facebook" in p) or ("Facebook" in p)):
	  os.system('start chrome "https://www.facebook.com" --kiosk') 
	
	elif (("run" in p) or ("start" in p)) and  (("linkedin" in p) or ("LinkedIn" in p)):
	  os.system('start chrome "https://www.linkedin.com/feed/" --kiosk') 
	
	elif (("run" in p) or ("start" in p)) and  (("aws" in p) or ("AWS" in p)):
	  os.system('start chrome "https://console.aws.amazon.com/console/home?#" --kiosk') 
	    
	elif (("run" in p) or ("start" in p)) and  (("windows explorer" in p) or ("explorer" in p)):
	  os.system("start explorer")  
 
	elif (("run" in p) or ("start" in p)) and (("player" in p) or ("media" in p)):
	  os.system("start wmplayer")
	  
	elif (("run" in p) or ("start" in p)) and (("calc" in p) or ("calculator" in p)):
	  os.system("start calc")
	
	elif (("run" in p) or ("start" in p)) and (("outlook" in p) or ("Microsoft Outlook" in p)):
	  os.system("start outlook")
	
	elif (("show" in p) or ("display" in p)) and (("time" in p) or ("current time" in p)):
	  os.system("cls")
	  print('The current time is :', time.ctime())
	  time.sleep(2)
	
	elif (("run" in p) or ("start" in p)) and ("putty" in p):
	  os.system("start putty")
  
      
	elif  ("exit" in p)  or ("quit" in p) or ("bye" in p):
	  pyttsx3.speak("Hope you enjoyed the demo..")
	  pyttsx3.speak("Have a great day ahead..Byee !!")
	  break
	 
	else:
	  pyttsx3.speak(" Sorry.. we do not support your selected choice..Please try again !!")

