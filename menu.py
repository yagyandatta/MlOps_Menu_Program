import os
import getpass
import pyfiglet
import socket
import subprocess as sp
os.system("clear")

                        # <function-for-box-design>

def print_msg_box(msg, indent=1, width=None, title=None): 
    os.system("tput setaf 2")     
    """Print message-box with optional title."""   
    lines = msg.split('\n')       
    space = " " * indent
    if not width:   
        width = max(map(len, lines))  
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border     
    if title:           
        box += f'║{space}{title:<{width}}{space}║\n'  # title     
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border 
    print(box)


                        # <intro-message>

user = input("How do we call you? : ")
os.system("tput setaf 4")
title = pyfiglet.figlet_format("MENU-APP", font = "epic" )
print(title)
os.system("tput setaf 2")
msg = pyfiglet.figlet_format(f"welcome {user}", font = "digital" )
print(msg)




                        # <authentication>

passwd = getpass.getpass(" Enter Your Password : ")
os.system("tput setaf 1")
if passwd != "mlops":
	print("Password is Incorrect...")
	exit()



                        # <program-body>
os.system("tput setaf 2")
where = input(" Where you want to run? (local/remote) : ")
print(where)

                        # <menu-options>

while True:
	os.system("clear")
	os.system("tput setaf 3")
	print("\t\t\t Menu Options")
	os.system("tput setaf 5")
	print("\t\t-----------------------")
	msg = "press 0 : Linux\n" \
	      "Press 1 : ML\n" \
	      "Press 2 : DL\n" \
	      "Press 3 : Docker\n" \
	      "Press 4 : Kubernetes\n" \
	      "Press 5 : Exit\n" 
	print_msg_box(msg=msg, indent=2, title='All Services') 

	if where == "local":
		os.system("tput setaf 4")
		ch = input("Enter choice (service): ")
		print(ch)

		if int(ch) == 0:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg ="Press 1 : Check Date\n" \
				     "Press 2 : Check Calender\n" \
				     "Press 3 : Check your IP \n" \
				     "Press 4 : Check RAM Status \n" \
				     "Press 5 : Check Storage details \n" \
				     "press 6 : To Clear Cache\n" \
			       "press 7 : To Transfer File to Other Linux System\n" \
				     "press 8 : Go Back\n" \
				     "press 9 : Exit" 
				print_msg_box(msg=msg, indent=2, title='Linux Command:') 
				os.system("tput setaf 4")
				ch=input("choose your option : ")
				os.system("tput setaf 3")
				print(ch)
				if int(ch) == 0:
					exit()
				elif int(ch) == 1:
					os.system("date")


				elif int(ch) == 2:
					os.system("cal")

				elif int(ch) == 3:
					os.system("ifconfig")

				elif int(ch) == 4:
					os.system("free -m")
				elif int(ch) == 5:
					os.system("df -h")
				elif int(ch) == 6:
					os.system("echo 3 > /proc/sys/vm/drop_caches")
				elif int(ch) == 7:
					ip = input("Enter IP of target system : ")
					user = input("Enter username : ")
					src = input("Enter your source file path : ")
					dest = input("Enter destination folder path where you want to copy : ")
					output = getpass.getstatusoutput("scp {} {}@{}:{}".format(src, user,ip,dest))
				elif int(ch) == 8:
					break
				elif int(ch) == 9:
					exit()

				else:
					print("Incorrect Input")
				input("\nEnter To Continue...")

		elif int(ch) == 1:
			while True:
				os.system("clear")
				os.system("tput setaf 4")
				msg ="Press 1 : ml....\n" \
				     "press 9 : Go Back \n" \
				     "press 0 : Exit.."
				print_msg_box(msg=msg, indent=2, title='Hadoop Command:')
				os.system("tput setaf 4") 
				ch=input("choose your option : ")
				print(ch)
						#Hadoop-installation


				if int(ch) == 1:
					os.system("echo 'will update son' ")
				elif int(ch) == 9:
					break
				elif int(ch) == 0:
					exit()

				else:
					print("Incorrect Number")
				input("\nEnter to continue...")

		elif int(ch) == 5:
			exit()



	elif where == "remote":
		ip = input("Enter remote IP: ")
		print(ip)
		ch = input("Enter choice (service): ")
		print(ch)

		if int(ch) == 0:
			while True:
				os.system("clear")
				os.system("tput setaf 2")
				msg ="Press 1 : Check Date\n" \
				     "Press 2 : Check Calender\n" \
				     "Press 3 : Check IP\n" \
				     "Press 4 : Check Httpd Status\n" \
				     "Press 5 : Start Httpd \n" \
				     "press 6 : To Clear Cache\n" \
			       "press 7 : To Change Command Name\n" \
				     "press 8 : Go Back \n" \
				     "press 9 : To Exit\n" 
				print_msg_box(msg=msg, indent=2, title='Linux Command:') 
				os.system("tput setaf 4")
				ch=input("choose your option : ")
				print(ch)
				if int(ch) == 1:
					os.system("ssh {} date".format(ip))
				elif int(ch) == 2:
					os.system("ssh {} cal".format(ip))
				elif int(ch) == 3:
					os.system("ssh {} ifconfig".format(ip))
				elif int(ch) == 4:
					os.system("ssh {} systemctl status httpd".format(ip))
				elif int(ch) == 5:
					os.system("ssh {} systemctl start httpd".format(ip))
				elif int(ch) == 6:
					os.system("ssh {} echo 3 > /proc/sys/vm/drop_caches".format(ip))
				elif int(ch) == 7:
					print("change name")
				elif int(ch) == 8:
					break
				elif int(ch) == 9:
					exit()
				else:
					print("Incorrect Number")
				input("\nEnter To Continue...")


		elif int(ch) == 5:
			exit()



	else:
		os.system("tput setaf 1")
		print("login is not supported....")
		exit()

	input("\nplease Enter to Continue....")





















