import os
import platform
import time

def restart_laptop():
    # Determine the current operating system
    current_os = platform.system()
    
    # Print a message before restarting
    print("The laptop will restart in 10 seconds. Please save your work.")
    
    # Wait for 10 seconds before restarting
    time.sleep(10)
    
    if current_os == "Windows":
        # Restart command for Windows
        os.system("shutdown /r /t 0")
    elif current_os == "Linux" or current_os == "Darwin":
        # Restart command for Linux and macOS
        os.system("sudo shutdown -r now")
    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    restart_laptop()
