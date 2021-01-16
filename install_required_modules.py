import os, platform
print("Internet Connection is required. Atfirst confirm connection and then press 'Enter key'.")
input("Start Process? ")
print("Don't worry. System will automatically download all the required modules...")

os.system("pip install flask")
os.system("pip3 install flask")

os.system("pip install bs4")
os.system("pip3 install bs4")


os.system("pip install requests")
os.system("pip3 install requests")

print("Task Completed. Now run the main.py. You can also run it here. Or quit the window to exit.")
input("run 'main.py'? ")
if platform.system() == "Windows":
	print("Windows detected.")
	os.system("python main.py")

if platform.system() == "Linux":
	print("Linux detected.")
	os.system("python3 main.py")




