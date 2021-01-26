
# Udacity DS & Algo Nanodegree - Project01

### About the Project data
* The text data (text.csv) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).
* The call data (call.csv) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)
*  There are three different kinds of telephone numbers, each with a different format:
   * Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".
   * Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
   * Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".

## Step 2 - Implement the Code
* Complete the five tasks (Task0.py, Task1.py, ...,Task4.py). Do not change the data or instructions, simply add your code below what has been provided. Include all the code that you need for each task in that file. 
* In Tasks 3 and 4, you can use in-built methods sorted() or list.sort() for sorting which are the implementation of Timsort and Samplesort, respectively. Both these sorting methods have a worst-case time-complexity of O(n log n). Check the below links to learn more about these methods:
  * How to use the above methods - https://docs.python.org/3/howto/sorting.html
  * Complexity analysis of Timsort and Samplesort - http://svn.python.org/projects/python/trunk/Objects/listsort.txt

The solution outputs for each file should be the print statements described in the instructions. Feel free to use other print statements during the development process, but remember to remove them for submission - the submitted files should print only the solution outputs.

## Step 3 - Calculate Big O
Once you have completed your solution for each problem, perform a run time analysis (Worst Case Big-O Notation) of your solution. Document this for each problem and include this in your submission.

* Time Complexity : How effecient our algorithm is w.r.t the the time it take to do the computation
* Space Complexity : When we refer to space complexity, we are talking about how efficient our algorithm is in terms of memory usage.

### TASK0: In this task we need to find the first record of texts and the last record of calls? We are making use of the Sorted() function which make use of the Timesort algorithm internally, which has the complexity in terms of O notation is O(nlogn). So the overall complexity of this particular task would be O(nlogn)
### TASK1: In this task we are iterating through texts and calls list and then making use of union to merge the two list. Union operation will have the complexity of O(len(s1) + len(s2)) ~ O(n) while iterating through the lists can also be done in O(n). So ovrall complexity would be for task-1 would be O(n).  
### TASK2:To find the telephone number that spent the longest time on the phon during the period, we need to sort the list on particular parameter. We are using Sorted() which takes o(n log n) time. So overall time complexity of this particular task2 would be O(n long n) 
### TASK3:get_prefixes(phonenumber) function takes O(n) time. Fetching all the Phone Number prefixes and store in the "called_codes" list also takes O(n) time. Sort() internal python fuction takes o(n logn) time. SO overall o(n) + o(n) + o(n logn ) ~ o(n) time.
### TASK4:Iterating thought calls list takes o(n) time. Difference function takes O(min(len(s), len(t)). So overall it would take o(n).

## Step 4 - Check again Rubric and Submit
Use the rubric to check your work before submission. A Udacity Reviewer will give feedback on your work based on this rubric and will leave helpful comments on your code.

## Important Links
* https://docs.python.org/3/howto/sorting.html
* http://svn.python.org/projects/python/trunk/Objects/listsort.txt
* https://www.protechtraining.com/blog/post/python-for-beginners-reading-manipulating-csv-files-737

