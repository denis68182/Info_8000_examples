
#How to make it?

import time
import  os

num_files = len(os.listdir("data"))   #data  is the data folder now will appear in the fille  git folders to be commited after having data (number of files)
file = open("res/myfile.txt","w")
file.write(f"The program was just run at {time.ctime()}\n")
file.write(" Lets make it in TZ. You will enjoy Mountain Kilimanjaro. \n")
file.write("Dont forget to visit MOrogoro, Bigwa Stenda. \n")
file.write(f"There are {num_files} in the data folder")
file.close()
