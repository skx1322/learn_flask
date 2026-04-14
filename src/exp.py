import os 
# open file. open(location, mode)
# mode includes read (r), append (a), write (w) and create (x).
# there are also text (t) and (b)
my_text = open("./src/text.txt")

# read file
f = my_text.read()
print(f)

# close file
my_text.close()

# write file
my_text = open("./src/text.txt", "w") 
my_text.write("1. test more")
my_text.close()

# append file
my_text = open("./src/text.txt", "a") 
my_text.write("\n2. yeah")
my_text.close()

# create file
cre = open("data.txt", "x")
cre.close()

# delete file
os.remove("data.txt")

# check if file exist
def check(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("This file does not exist")

# close file
my_text.close()