import os
import datetime

command = "df -h" # disk
command = "uptime" # load avg
command = "date" # date

def check_cpu(command):
	print(os.system(command))

def show_date():
	return datetime.datetime.today()

toady = show_date()
print(toady)

# check_cpu("df -h")

# check_date("date")

# uptime("uptime")

# check_ram("sysctl hw.memsize")