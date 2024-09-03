#list -> data structure which can hold multiple values of multiple type
#array -> data structure which can hold multiple values of same type
list_of_cloud = ["aws", "azure", "gcp", "digital ocean", "utho", "alibaba", "oracle"]

cloud = "aws"

# add a new cloud Salesforce

list_of_cloud.append("salesforce")

# add a new cloud Salesforce

list_of_cloud.append("IBM")

# insert into a position

list_of_cloud.insert(2, "Heroku")

# insert "HELLO Cloud" in 0th index


list_of_cloud.insert(0, "Hello Cloud")

print(list_of_cloud)


print(len(list_of_cloud))

for cloud in list_of_cloud:
	print(cloud)

for i in range(1,11):
	print(i)