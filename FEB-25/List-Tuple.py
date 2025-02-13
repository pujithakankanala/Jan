list=["dev-sev", "qa-server","pre-prod","prod"]
list.sort()

new_list=[s.upper() for s in list]
list1=[s.lower() for s in list]
print(new_list)
print(list1)