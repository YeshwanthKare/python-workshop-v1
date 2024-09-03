import os # Importing a new library into your code

print(os.system("df -h")) # disk space in Linux or Mac
print(os.system('uptime')) # uptime and load average
print(os.system("sysctl hw.memsize")) # RAM size "sysctl hw.memsize" for Mac / "free -h" for Linux / "sysinfo" for Windows

