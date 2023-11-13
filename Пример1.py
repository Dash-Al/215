#!/usr/bin/envpython3
# -*- coding: utf-8 -*-
# open the file2.txt in append mode. Create a new file if no such file exists.
if __name__ == "__main__":
fileptr = open("file2.txt", "w")
   # appending the content to the file
fileptr.write(
      "Python is the modern day language. It makes things so simple.\n"
      "It is the fastest-growing programing language"
)
   # closing the opened the file
fileptr.close()
