##create and write to a file using try and finally
# file = open("order.txt","w")
# try:
#     file.write("Masala chai - 2  cups")
# finally:
#     file.close()


#another way using with statement
with open("order.txt","w") as file:
    file.write("Masala chai - 2  cups\n")