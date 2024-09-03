import subprocess

def terraform_run(command):
	process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
	# return process.stdout.decode()
	# subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
	print(process.stdout.decode())

directory = "/Users/yesh/Documents/LocalDisk-D/DevOps_with_shubam/Python_for_DevOps/September_1-2024/python_workshop_practice/terra-automate/Wanderlust-Mega-Project/terraform"
# command = f"terraform -chdir={directory} init"
# command = f"terraform -chdir={directory} plan"
# command = f"terraform -chdir={directory} apply -auto-approve"
command = f"terraform -chdir={directory} destroy -auto-approve"

# print(command)
terraform_run(command)