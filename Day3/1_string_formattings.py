# We can format strings in python by using f-strings

language = "Python"
message = f"I am learning {language}"
print(message)

tool1 = "Pen"
tool2 = "Pencil"
message = f"I have {tool1} and {tool2}"  # In python version 3.6 and later

# f-strings are introduced from python 3.6
message = "I have {} and {}".format(tool1, tool2) # In python version 3.2/3.3
print(message)

message = "I have {1} and {0}".format(tool1, tool2)
print(message)

message = "I have %s and %s" % (tool1, tool2) # In python version 3.0/3.2
print(message)