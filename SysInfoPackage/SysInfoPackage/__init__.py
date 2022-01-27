import os
import socket  
import platform

def sysInfo():

    hostname = socket.gethostname()   
    IPAddr = socket.gethostbyname(hostname)   
    print("Your Computer Name is:" + hostname)   
    print("Your Computer IP Address is:" + IPAddr)  
    print("The number of CPUs is " + str(os.cpu_count()))
    print("Name of the operating system:",os.name)
    print("\nName of the OS system:",platform.system())
    print("\nVersion of the operating system:",platform.release())


sysInfo()
