import shutil
import datetime
import os

def backup_files(source, destination):
	today = datetime.date.today()
	backup_file = os.path.join(destination, f"backup_{today}")
	shutil.make_archive(backup_file, "gztar", source)

source = "/Users/yesh/Documents/LocalDisk-D/DevOps_with_shubam/Python_for_DevOps/September_1-2024/python_workshop_practice"
destination = "/Users/yesh/Documents/LocalDisk-D/DevOps_with_shubam/Python_for_DevOps/September_1-2024/python_workshop_practice/backups"

backup_files(source, destination)