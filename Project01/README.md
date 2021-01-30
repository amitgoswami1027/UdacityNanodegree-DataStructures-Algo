
# Project01

## Review Comments Implementation (For my reference)
* 1. Your code should be well-structured and readable. -[Done]
      * Here are some formatting errors in the codes; check the clarification for each code.
      * Sorted has worsened the efficiency of the code. With simple indexing, the time is O(1), i.e., constant time, but with indexing is log-linear time, i.e., O(n logn).
      * No need to sort as the lists are already sorted.
* 2. Print only the solution outputs. Feel free to use other print statements during the development process, but remember to remove them for submission.- [Done]
      * The output for task 1; there is a syntax error, for task 2, the duration is incorrect, for task 3; codes and the percentage are incorrect and there are two extra print 
        statements, and for task 4, the numbers are incorrect.
* 3. Task 1 - The script correctly prints number of distinct telephone numbers in the dataset. [Done]
      * Instead of starting with lists then converting them to sets, you may start directly with sets.
* 4. Task 2 - The script correctly prints the telephone number that spent the longest time on the phone and the total time in seconds they spend on phone call. [Done]
      * The duration is incorrect.
      * Suggestions : Create a dictionary where the numbers are keys and length as values then use the function in this article to add up the time for the same number.
* 5. Task 3- The script correctly prints the telephone codes called by fixed-line numbers in Bangalore and the percentage of calls from fixed lines in Bangalore that are to fixed lines in Bangalore. [Done]
      * The output is incorrecct.
      * PART-A: Task instructions for numbers starting with 7, 8, or 9, the code must fetch the first four digits, [1:5] is incorrect.
      * PART-B: According to the task rules, we need to get the count of numbers in record[0] starting with (080), this the first number we need to calculate the percentage, 
        then the second number is the count of record[1] starts with '(080)' when record[0] is also starting with (080).
* 6. Task 4- The script correctly prints the list of numbers that could be telemarketers. [Done]
      * Output is incorrect.
      * telemarketers = callers - called - texters - texted. Telemarketers sent a call but never received a call, sent a text, or received a text.
* 7. Readme Review [Done]
      * Note that you have used sorting for tasks 0, 2, 3, and 4, all currently have O(n logn).
      * O(n logn) > O(n) > O(1) in time complexity, so while analyzing for the worst-case time notation, if the code has O(n) function and O(n logn) function, then the overall 
        worst case is O(n logn). [Thanks for explaination, noted]
      * Student provides a text file accurately explaining their run time analysis (Worst-Case Big-O Notation) for each solution they produced. 

## Complexity Analysis
* TASK0: In this task we need to find the first record of texts and the last record of calls? Overall complexity is O(1) i.e constant time.
* TASK1: In this task we are iterating through texts and calls list and then making use of union to merge the two list. Union operation will have the complexity of O(len(s1) + len(s2)) ~ O(n) while iterating through the lists can also be done in O(n). So ovrall complexity would be for task-1 would be O(n).  
* TASK2:To find the telephone number that spent the longest time on the phon during the period, we need to iterate through the list So overall time complexity of this particular task2 would be linear i.e O(n) 
* TASK3:get_prefixes(phonenumber) function takes O(n) time. Fetching all the Phone Number prefixes and store in the "called_codes" list also takes O(n) time. Sort() internal python fuction takes o(n logn) time. SO overall o(n) + o(n) + o(n logn ) ~ o(n logn) time.
* TASK4:Iterating thought calls list takes o(n) time. Difference function takes O(min(len(s), len(t)) and also used sort - O(n log n). So overall it would take o(n log n).

## Project Details
### Step 1 - About the Project data
* The text data (text.csv) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).
* The call data (call.csv) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)
*  There are three different kinds of telephone numbers, each with a different format:
   * Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".
   * Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
   * Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".

### Step 2 - Implement the Code
* Complete the five tasks (Task0.py, Task1.py, ...,Task4.py). Do not change the data or instructions, simply add your code below what has been provided. Include all the code that you need for each task in that file. 
* In Tasks 3 and 4, you can use in-built methods sorted() or list.sort() for sorting which are the implementation of Timsort and Samplesort, respectively. Both these sorting methods have a worst-case time-complexity of O(n log n). Check the below links to learn more about these methods:
  * How to use the above methods - https://docs.python.org/3/howto/sorting.html
  * Complexity analysis of Timsort and Samplesort - http://svn.python.org/projects/python/trunk/Objects/listsort.txt

The solution outputs for each file should be the print statements described in the instructions. Feel free to use other print statements during the development process, but remember to remove them for submission - the submitted files should print only the solution outputs.

### Step 3 - Calculate Big O
Once you have completed your solution for each problem, perform a run time analysis (Worst Case Big-O Notation) of your solution. Document this for each problem and include this in your submission.

### Step 4 - Check again Rubric and Submit
Use the rubric to check your work before submission. A Udacity Reviewer will give feedback on your work based on this rubric and will leave helpful comments on your code.

## Important Links
* https://docs.python.org/3/howto/sorting.html
* http://svn.python.org/projects/python/trunk/Objects/listsort.txt
* https://www.protechtraining.com/blog/post/python-for-beginners-reading-manipulating-csv-files-737
* [Lexigraphic Sort]youtube.com/watch?v=goUlyp4rwiU
* https://docs.python.org/3/howto/sorting.html
* http://svn.python.org/projects/python/trunk/Objects/listsort.txt
* https://www.protechtraining.com/blog/post/python-for-beginners-reading-manipulating-csv-files-737
* https://www.programiz.com/python-programming/set
* https://www.edureka.co/blog/hash-tables-and-hashmaps-in-python/
* https://www.geeksforgeeks.org/python-sum-list-of-dictionaries-with-same-key/

