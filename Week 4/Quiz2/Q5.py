def group_list(group, users):
  members = group + str(": ")
  for user in users:
    if user == users[-1]:
      members += user
    else:
      members += user + str(", ")
  
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"