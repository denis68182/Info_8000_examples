
#How to make it?

import time
import  os

num_files = len(os.listdir("data"))   #list number of  files/folders in the data folder
num_files2 = len(os.listdir("src"))
file = open("res/myfile.txt","w")
file.write(f"The program was just run at {time.ctime()}\n")
file.write(" Lets make it in TZ. You will enjoy Mountain Kilimanjaro.\n")
file.write("Dont forget to visit MOrogoro, Bigwa Stenda.\n")
file.write(f"There are {num_files} in the data folder\n")
file.write(f"There are {num_files2} in the source/program code folder \n")
file.write("Good")
file.close()
