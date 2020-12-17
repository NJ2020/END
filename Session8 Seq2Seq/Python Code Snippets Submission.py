# write a python function to calculate factorial for user provided number and return the factorial

import math
if not n >= 0:
	raise ValueError("n must be >= 0")
if math.floor(n) != n:
	raise ValueError("n must be exact integer")
if n+1 == n:  # catch a value like 1e300
	raise OverflowError("n too large")
result = 1
factor = 2
while factor <= n:
	result *= factor
	factor += 1
return result

# Write a Python program to print the sample string : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"  in a specific format

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# Write a Python program to get the Python version you are using.

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

#Write a Python program to read each row from a given csv file and print a list of strings

import csv
with open('departments.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar='|')
 for row in data:
   print(', '.join(row))
   
#Write a Python program to read a given CSV file having tab delimiter

import csv
with open('countries.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter = '\t')
 for row in data:
   print(', '.join(row))
   
#Write a Python program to read a given CSV file as a list.

import csv
with open('employees.csv', newline='') as f:
   reader = csv.reader(f)
   data_list = list(reader)
print(data_list)

#Write a Python program to read a given CSV file as a dictionary

import csv
data = csv.DictReader(open("departments.csv"))
print("CSV file as a dictionary:\n")
for row in data:
   print(row)
   
#Write a Python program to read a given CSV files with initial spaces after a delimiter and remove those initial spaces

import csv
print("\nWith initial spaces after a delimiter:\n")
with open('departments.csv', 'r') as csvfile:
   data = csv.reader(csvfile, skipinitialspace=False)
   for row in data:
     print(', '.join(row))
print("\n\nWithout initial spaces after a delimiter:\n")
with open('departments.csv', 'r') as csvfile:
   data = csv.reader(csvfile, skipinitialspace=True)
   for row in data:
     print(', '.join(row))
     
#Write a Python program that reads a CSV file and remove initial spaces, quotes around each entry and the delimiter

import csv
csv.register_dialect('csv_dialect',
                    delimiter='|',
                    skipinitialspace=True,
                    quoting=csv.QUOTE_ALL)
with open('temp.csv', 'r') as csvfile:
   reader = csv.reader(csvfile, dialect='csv_dialect')
   for row in reader:
       print(row)
       
#Write a Python program to read specific columns of a given CSV file and print the content of the columns

import csv
with open('departments.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("ID Department Name")
 print("---------------------------------")
 for row in data:
   print(row['department_id'], row['department_name'])
   
#Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names

import csv
fields = []
rows = []
with open('departments.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar=',')
 # Following command skips the first row of the CSV file.
 fields = next(data)
 for row in data:
   print(', '.join(row))
print("\nTotal no. of rows: %d"%(data.line_num))
print('Field names are:')
print(', '.join(field for field in fields))

#Write a Python program to create an object for writing and iterate over the rows to print the values.

import csv
import sys
with open('temp.csv', 'wt') as f:
    writer = csv.writer(f)
    writer.writerow(('id1', 'id2', 'date'))
    for i in range(3):
        row = (
            i + 1,
            chr(ord('a') + i),
            '01/{:02d}/2019'.format(i + 1),)
        writer.writerow(row)
print(open('temp.csv', 'rt').read())

#Write a Python program to write a Python list of lists to a csv file. After writing the CSV file read the CSV file and display the content

import csv
data = [[10,'a1', 1], [12,'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]
with open("temp.csv", "w", newline="") as f:
   writer = csv.writer(f)
   writer.writerows(data)
with open('temp.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ')
 for row in data:
   print(', '.join(row))
   
#Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content

import csv
csv_columns = ['id','Column1', 'Column2', 'Column3', 'Column4', 'Column5']
dict_data = {'id':['1', '2', '3'],
    'Column1':[33, 25, 56],
    'Column2':[35, 30, 30],
    'Column3':[21, 40, 55],
    'Column4':[71, 25, 55],
    'Column5':[10, 10, 40], }
csv_file = "temp.csv"
try:
   with open(csv_file, 'w') as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
       writer.writeheader()
       for data in dict_data:
           writer.writerow(dict_data)
except IOError:
   print("I/O error")
data = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data:
   print(row)
   
   
#Write a Python program to find the title tags from a given html document

from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print("Title of the document:")
print(soup.find("title"))

#Write a Python program to retrieve all the paragraph tags from a given html document

from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print("All paragraph tags:")
print(soup.find_all("p"))

#Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.

from array import *
array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)
print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])

#Write a Python program to append a new item to the end of the array

from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Append 11 at the end of the array:")
array_num.append(11)
print("New array: "+str(array_num))
      
#Write a Python program to reverse the order of the items in the array.
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))

#Write a Python program to get the length in bytes of one array item in the internal representation
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Length in bytes of one array item: "+str(array_num.itemsize))
Sample Output:

#Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents and also find the size of the memory buffer in bytes.

from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))

#Write a Python program to get the number of occurrences of a specified element in an array

from array import *
array_num = array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(array_num))
print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))

#Write a Python program to append items from inerrable to the end of the array

from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
array_num.extend(array_num)
print("Extended array: "+str(array_num))

#Write a Python program to convert an array to an array of machine values and return the bytes representation.

from array import *
print("Bytes to String: ")
x = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
s = x.tobytes()
print(s)

#Write a Python program to append items from a specified list.

from array import *
num_list = [1, 2, 6, -8]
array_num = array('i', [])
print("Items in the list: " + str(num_list))
print("Append items from the list: ")
array_num.fromlist(num_list)
print("Items in the array: "+str(array_num))

#Write a Python program to insert a new item before the second element in an existing array.

from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Insert new value 4 before 3:")
array_num.insert(1, 4)
print("New array: "+str(array_num))

#Write a Python program to remove a specified item using the index from an array.

from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Remove the third item form the array:")
array_num.pop(2)
print("New array: "+str(array_num))

#Write a Python program to remove the first occurrence of a specified element from an array.

from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
print("Remove the first occurrence of 3 from the said array:")
array_num.remove(3)
print("New array: "+str(array_num))

#Write a Python program to convert an array to an ordinary list with the same items

from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
num_list = array_num.tolist()
print("Convert the said array to an ordinary list with the same items:")
print(num_list)

#Write a Python program to find whether a given array of integers contains any duplicate element. Return true if any value appears at least twice in the said array and return false if every element is distinct. 

def test_duplicate(array_nums):
    nums_set = set(array_nums)    
    return len(array_nums) != len(nums_set)     
print(test_duplicate([1,2,3,4,5]))
print(test_duplicate([1,2,3,4, 4]))
print(test_duplicate([1,1,2,2,3,3,4,4,5]))

#Write a Python program to find the first duplicate element in a given array of integers. Return -1 If there are no such elements
def find_first_duplicate(nums):
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate

print(find_first_duplicate([1, 2, 3, 4, 4, 5]))
print(find_first_duplicate([1, 2, 3, 4]))
print(find_first_duplicate([1, 1, 2, 3, 3, 2, 2]))

#Write a Python program to find a pair with highest product from a given array of integers.
def max_Product(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        print("No pairs exists") 
        return      
    # Initialize max product pair 
    x = arr[0]; y = arr[1] 

    # Traverse through every possible pair     
    for i in range(0, arr_len): 

        for j in range(i + 1, arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 

    return x,y    

nums = [1, 2, 3, 4, 7, 0, 8, 4] 
print("Original array:", nums)
print("Maximum product pair is:", max_Product(nums))

nums = [0, -1, -2, -4, 5, 0, -6] 
print("\nOriginal array:", nums)
print("Maximum product pair is:", max_Product(nums))
