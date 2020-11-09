import getpass
import os
os.system("clear")
os.system("tput setaf 3")
print("\t\t\t\t========================================================")
print("\t\t\t\t\tHeyy Welcome to my Automation Pythoon tool")


print("\t\t\t\t========================================================")
os.system("tput setaf 7")

passwd = getpass.getpass("Enter Password : ")
#passwd = input("Enter Password : ")
apass = "mihir"

if passwd != apass:
	print("Authentication incorrect")
	exit()


print("Where you would like to perform your job (local/remote) :" , end='')
location = input()
print(location)

if location == "remote":
    remoteIP = input("Enter your IP : ")

while True:
		os.system("clear")
		os.system("clear")
		os.system("tput setaf 3")
		print("\t\t\t\t========================================================")
		print("\t\t\t\t\tHeyy Welcome to my Automation Pythoon tool")
		print("\t\t\t\t========================================================")
		os.system("tput setaf 7")
		print("""
		Press 1: To See Date
		Press 2: To See Calender
		Press 3: Firefox
		Press 4: Configure Web Server
		press 5: To Create User
		Press 6: To Delete User
		Press 7: To Run Docker
		Press 8: To Setup Docker
		Press 9: Create Directory
		Press 10: To start  Datanode and NameNode
		Press 11: To upload files to hadoop cluster
		prees 12:Show all disk
		press 13:To create pv 
		press 14:To cretae vg
		prees 15:To dispaly vg and pv
		prees 16:To create partion in lvm
		prees 17:To display lv(partion in lvm) 
		Press 18: Exit
		""")
		print("Enter Your Choice : " , end="")
		ch = input()
		print(ch)

		if location == "local":
			if int(ch) == 1:
				os.system("date")
			elif int(ch) == 2:
				os.system("cal")
			elif int(ch) == 3:
				os.system("firefox")
			elif int(ch) == 4:
				while True:
					os.system("clear")
					print("""
					Press 1:Configure web server
					Press 2:Create file 
					press 3:Upload to server
					Press 4:Exit					
					""")
					w=int(input("Enter the your choice :"))
					if w==1:				
						os.system("yum install httpd -y")
						os.system("systemctl start httpd")
						os.system("systemctl enable httpd")
						input()
						os.system("tput setaf 2")# 2 for green
						print("===>Succesfully Configration web server<===")
						os.system("tput setaf 7")
					elif w==2:
						f=input("Enter the file Name for create:")
						os.system(f"vim {f}")
						input()
					elif w==3:
						print("Uploading ....")	
						
						os.system(f"cp {f} /var/www/html/")
						os.system("sleep 4")
						os.system("tput setaf 2")# 2 for green
						print("===>Succesfully Uploaded to server<===")
						os.system("tput setaf 7")
						input()
					elif w==4:
						break
			elif int(ch) == 5:
				print("can you please tell user name: " , end='')
				create_user = input()
				passwd = input("Enter Password for the new user: ")
				os.system("useradd {}".format(create_user))
				os.system("passwd {0}".format(passwd))
				os.system("lslogins -u")
			elif int(ch) == 6:
				print("please tell user name you want to delete: " , end='')
				delete_user = input()
				os.system("userdel {}".format(delete_user))

			elif int(ch) == 7:
				
				while True:
					os.system("clear")
					print("Press 1: to run any os(ENter the name of os):")
					print("Press 2: to see docker images")
					print("Press 3: to know docker commands")
					print("Press 4: to know about a particular docker commands")
					print("Press 5: to exit")
					print("Enter Your Choice : " , end="")
					ch1 = input()
					print(ch1)
					if int(ch1) == 1:
						oss=input("Enter the name of OS Which you want to run:")
						os.system(f"docker run -it {oss}")
						input()
					elif int(ch1) == 2:
						os.system("docker images")
						input()
					   
					elif int(ch1) == 3:
						os.system("docker --help")
						input()
								   
					elif int(ch1) == 4:
						name=input("Enter the command that you want to know about:")
					
						cmd="docker "+name+" --help"
						os.system(cmd)
						input()
					elif int(ch1)== 5:
						break
						    
                
			elif int(ch) == 8:
                 #       os.system("ssh {0} yum install -y yum-utils device-mapper-persistent-data lvm2".format(remoteIP))
                       # os.system("sudo yum config-manager --add-repo=https://download.docker.com/linux/centos/7/x86_64/stable/")
				os.system("sudo yum install docker-ce --nobest -y")
				os.system("systemctl start docker")
				os.system("systemctl enable docker")  
				
			                     
			elif int(ch) == 9:
				print("can you please tell me the dir name: " , end="")
				create_dir = input()
				os.system("mkdir {0} ".format(create_dir))
			elif int(ch) == 10:
				while True:
					h=input("""
					press 1: TO start Namenode	
					press 2: To start Datanode
					press 3: TO exit			
					""")
					if int(h)== 1:
						os.system("hadoop-daemon.sh start namenode")
					elif int(h)==2:
						os.system("hadoop-daemon.sh start datanode")
					elif int(h)==3:
						break
				
			elif int(ch) == 11:	
				while True:
					os.system("clear")
					print("Make sure you have established a connection to NameNode")
					print("""
					Press 1: To upload an existing file 
					Press 2: To create a new file and upload
					Press 3: To check files in hadoop cluster
					Press 4: To remove files in hadoop cluster
					Press 5:To exit
					""")
					choice=int(input("Enter your choice:"))
					if choice==1:
						file=input("Enter name of the file with extension:")
						cmd="hadoop fs -put "+file+" /"
						os.system(cmd)
						print("File uploaded")
						input()
					elif choice==2:
						file=input("Enter name of the file with extension :")
						
						vi="vi "+file
						os.system(vi)
						print("Now uploading")
						cmd="hadoop fs -put "+file+" /"
						os.system(cmd)
						print("Done")
						input()
					elif choice==3:
						os.system("hadoop fs -ls /")
						input()
					elif choice==4:
						file=input("Enter name of the file with extension:")
					
						cmd="hadoop fs -rm "+" /"+file                    
						os.system(cmd)
						input()
					elif choice==5:
						break
					else:
						print("option not supported")

			elif int(ch) == 12:
				os.system("fdisk -l")
			elif int(ch) == 13:
				n=int(input("How many disk how want contribute?:"))
				for i in range(n):
					p=input("Enter the first disk name:")
					os.system(f"pvcreate {p}")
			elif int(ch) == 14:
				v=input("Enter the vg name")
				p1=input("Enter the first pv name:")
				p2=input("Enter the seconf pv name:")
				os.system(f"vgcreate {v} {p1} {p2}")
			elif int(ch) == 15:
				print("""
				ENter the
				1:pv display
				2:vg display """)
				d=input()
		
				if d=="1":
					v1=input("Enter the pv name:")
					os.system(f"pvdisplay {v1}")
				elif d=="2":
					vg1=input("Enter the vg name:")
					os.system(f"vgdisplay {vg1}")	
			elif int(ch) == 16:
				pr=input("Enter the size of for partion(ex:3G or 5G):")
				pn=input("Enter the name of partion for creation:")
				pg=input("Enter the vg name:")
				os.system(f"lvcreate --size {pr} --name {pn} {pg}")
				print("",end="\n\n")
				os.system("mkfs.ext4 /dev/{pg}/{mylv1}")
				mu=input("Enter the of folder for mount:")
				os.system(f"mkdir S/{mu}")
				os.system(f"mount /dev/{pg}/{pn} /{mu}")
				os.system("tput setaf 2")# 2 for green
				print("===>Succesfully created partion<===")
				os.system("tput setaf 7")
			elif int(ch) == 17:
				vgname=input("Enter the vg name:")
				lvname=input("Enter the lv name:")
				os.system(f"lvdisplay {vgname}/{lvname}")
			elif int(ch) ==18:
				exit()
			
			else:
				print("option not supported")

			input("Enter to continue....")
			os.system("clear")


		elif location == "remote":
			if int(ch) == 1:
				os.system("ssh {0} date".format(remoteIP))
			elif int(ch) == 2:
				os.system("ssh  {0} cal".format(remoteIP))
			elif int(ch) == 3:
				os.system("ssh -X {0} firefox".format(remoteIP))
			elif int(ch) == 4:
				os.system("ssh {0} yum install httpd".format(remoteIP))
				os.system("ssh {0} systemctl start httpd".format(remoteIP))
			elif int(ch) == 5:
				print("can you please tell user name: " , end='')
				create_user = input()
				os.system("ssh {0} useradd {1}".format(remoteIP, create_user))
			elif int(ch) == 6:
				print("ssh {0} sudo please tell user name you want to delete: ".format(delete_user) , end='')
				delete_user = input()
				os.system("userdel {}".format(delete_user))
			elif int(ch) == 7:
				os.system("ssh {0} date".format(remoteIP))
			elif int(ch) == 8:
						    #os.system("ssh {0} sudo yum config-manager --add-repo=https://download.docker.com/linux/centos/7/x86_64/stable/".format(remoteIP))
				os.system("ssh {0} sudo yum install docker-ce --nobest ".format(remoteIP))
				os.system("ssh {0} sudo systemctl start docker".format(remoteIP))
				os.system("ssh {0} sudo systemctl enable docker".format(remoteIP))
				print("Option not supported")
			elif int(ch) == 9:
				print("can you please tell me the dir name: " , end="")
				create_dir = input()
				os.system("mkdir {0} ".format(create_dir))
			elif int(ch) == 12:
				os.system("ssh {0} fdisk -l".format(remoteIP))
			elif int(ch) == 13:
				n=int(input("How many disk how want contribute?:"))
				for i in range(n):
					p=input("Enter the first disk name:")
					os.system(f"ssh {remoteIP} pvcreate {p}")
			elif int(ch) == 14:
				v=input("Enter the vg name")
				p1=input("Enter the first pv name:")
				p2=input("Enter the seconf pv name:")
				os.system(f"ssh {remoteIP} vgcreate {v} {p1} {p2}")
			elif int(ch) == 15:
				print("""
				ENter the
				1:pv display
				2:vg display """)
				d=input()
		
				if d=="1":
					v1=input("Enter the pv name:")
					os.system(f"ssh {remoteIP} pvdisplay {v1}")
				elif d=="2":
					vg1=input("Enter the vg name:")
					os.system(f"ssh {remoteIP} vgdisplay {vg1}")
			elif int(ch) == 16:
				pr=input("Enter the size of for partion(ex:3G or 5G):")
				pn=input("Enter the name of partion for creation:")
				pg=input("Enter the vg name:")
				os.system(f"ssh {remoteIP} lvcreate --size {pr} --name {pn} {pg}")
				print("",end="\n\n")
				os.system(f"ssh {remoteIP} mkfs.ext4 /dev/{pg}/{mylv1}")
				mu=input("Enter the of folder for mount:")
				os.system(f"ssh {remoteIP} mkdir /{mu}")
				os.system(f"ssh {remoteIP} mount /dev/{pg}/{pn} /{mu}")
				os.system(f"ssh {remoteIP} tput setaf 2")# 2 for green
				print("===>Succesfully created partion<===")
				os.system(f"ssh {remoteIP} tput setaf 7")
			elif int(ch) == 17:
				vgname=input("Enter the vg name:")
				lvname=input("Enter the lv name:")
				os.system(f"ssh {remoteIP} lvdisplay {vgname}/{lvname}")
			elif int(ch) == 18:
				os.system("ssh {0} exit".format(remoteIP))


			else:
				print("location not supported")
