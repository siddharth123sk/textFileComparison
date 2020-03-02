file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")
file3 = open("file3.txt", "a")
# file1.seek(0,0)
# file2.seek(0,0)
list1 = file1.readlines()
list2 = file2.readlines()
for i in list1:
    for j in list2:
        if i == j:
            file3.write("FILE 1:",i)
            file3.write("FILE 2:",j)