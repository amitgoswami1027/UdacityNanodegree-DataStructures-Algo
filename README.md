
# Algorithm Design - My Notes

# https://github.com/binhnguyennus/awesome-scalability#architecture




## GRAPH THEORY AND CONCEPTS



### According to the GARTNER, Graph analysis is possibly single most effective competative differentator for orgnizations pursuing data drivenoperations and decisions after the design for data capture. 

### Google Knowledge Graph - things not Strings.

### GRAPH Technologies - GRAPH Promote Cross Domain Solutions
* Graph Database
* Graph Analytics
* Graph Visualizations
* Graph Discovery


### LINKS
* https://neo4j.com/blog/native-vs-non-native-graph-technology/
* http://graph500.org/

# graph-training

The documentation site is [here](https://github.optum.com/pages/ATC/graph-training/)
Materials for graph training courses.
See README for each individual course for instructions on running environments and loading data.

The Artifactory that we used for the graph training courses:

https://repo1.uhc.com/artifactory/webapp/#/artifacts/browse/tree/General/docker/graphtraining

Please see Dan McCreary if you have any questions.

- Dan





























## IMPORTANT LINKS
* http://algorist.com/algorist.html
* http://162.243.213.31/2012/11/27/100-most-useful-theorems-and-ideas-in-mathematics/
* Algorithm Reference : https://www.baeldung.com




# Algorithms Design Reference

### My Algo Design by Steven Skiena Notes: 
Java Collections:
https://beginnersbook.com/2013/12/hashset-class-in-java-with-example/

## Efficiency Reference

Dictionary Operation | Unsorted Array | Sorted Array
--- | --- | ---
Search(L, k) | O(n) | O(logn)
Insert(L, * x) | O(1) | O(n)
Delete(L, * x) | O(1)$ | O(n)
Successor(L, * x) | O(n) | O(1)
Predecessor(L, * x) | O(n) | O(1)
Min(L) | O(n) | O(1)
Max(L) | O(n) | O(1)

_$ Deletion can be quickened by filling in the hole with A[n] and decrement n_

Dictionary Operation | Singly Unsorted | Double Unsorted | Singly Sorted | Double Sorted
--- | --- | --- | --- | ---
Search(L, k) | O(n) | O(n) | O(n) | O(n)
Insert(L, * x) | O(1) | O(1) | O(n) | O(n)
Delete(L, * x) | O(n) | O(1) | O(n) | O(1)
Successor(L, * x) | O(n) | O(n) | O(1) | O(1)
Predecessor(L, * x) | O(n) | O(n) | O(n) | O(1)
Min(L) | O(n) | O(n) | O(1) | O(1)
Max(L) | O(n) | O(n) | O(1) | O(1)

Find Min | Unsorted Array | Sorted Array | Balanced Tree
--- | --- | --- | ---
Insert(Q, * x) | O(1) | O(n) | O(logn)
FindMin(Q) | O(1) | O(1) | O(1)
DeleteMin(Q) | O(n) | O(1) | O(logn)

## Sort
- Heap Sort ![n log n][n_lg_n]
- Merge Sort ![n log n][n_lg_n]
- Quick Sort (worst case n^2, _random_ case ![n log n][n_lg_n] with high probability)


## Learning Resources

The learning resources are divided into 4 categories: [Courses](#Courses), [Books](#Books), [Training Sites](#Training-Sites), [Other Resources](#Other-Resources).


### Courses

Collection of free courses from one of the best CS universities.

1. Standford University
    - [Algorithms Specialization (Coursera)](https://www.coursera.org/specializations/algorithms)
        * [Divide and Conquer, Sorting and Searching, and Randomized Algorithms](https://www.coursera.org/learn/algorithms-divide-conquer)
        * [Graph Search, Shortest Paths, and Data Structures](https://www.coursera.org/learn/algorithms-graphs-data-structures)
        * [Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming](https://www.coursera.org/learn/algorithms-greedy)
        * [Shortest Paths Revisited, NP-Complete Problems and What To Do About Them](https://www.coursera.org/learn/algorithms-npcomplete)
    - [Introduction to Programming Contests - CS 97SI](http://web.stanford.edu/class/cs97si/)

2.  Princeton University
    - [Algorithms Part 1 - Coursera](https://www.coursera.org/learn/algorithms-part1)
    - [Algorithms Part 2 - Coursera](https://www.coursera.org/learn/algorithms-part2)

3. UC San Diego
    - [Data Structures and Algorithms Specialization (Coursera)](https://www.coursera.org/specializations/data-structures-algorithms)
        * [Algorithmic Toolbox](https://www.coursera.org/learn/algorithmic-toolbox)
        * [Data Structures](https://www.coursera.org/learn/data-structures)
        * [Algorithms on Graphs](https://www.coursera.org/learn/algorithms-on-graphs)
        * [Algorithms on Strings](https://www.coursera.org/learn/algorithms-on-strings)
        * [Advanced Algorithms and Complexity](https://www.coursera.org/learn/advanced-algorithms-and-complexity)
    - [edX](https://www.edx.org/school/uc-san-diegox)
        * [Data Structures Fundamentals](https://www.edx.org/course/data-structures-fundamentals)
        * [Algorithmic Design and Techniques](https://www.edx.org/course/algorithmic-design-and-techniques)
        * [Graph Algorithms](https://www.edx.org/course/graph-algorithms)

4. MIT University
    - [Introduction to algorithms 2005](https://www.youtube.com/playlist?list=PL8B24C31197EC371C) - *[Official MIT page with resources](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/)*. Note: this course is the old 6.046J course (the new name is ***Design and analysis of algorithms***, you can find it below).
    - [Introduction to algorithms 2011 - 6.006](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb) - *[Official MIT page with resources](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/)*
    - [Design and analysis of algorithms - 6.046J](https://www.youtube.com/playlist?list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp) - *[Official MIT page with resources](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015/index.htm)*
    - [Advanced Data Structures - 6.851](https://www.youtube.com/playlist?list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf) - *[Official MIT page with resources](http://courses.csail.mit.edu/6.851/spring14/lectures/)*
    - [Advanced Algorithms 2016 - 6.854](https://www.youtube.com/playlist?list=PL6ogFv-ieghdoGKGg2Bik3Gl1glBTEu8c) - *[Official MIT page with resources](http://people.csail.mit.edu/moitra/854.html)*
    - [Programming for the Puzzled 2018 - 6.S095](https://www.youtube.com/playlist?list=PLUl4u3cNGP62QumaaZtCCjkID-NgqrleA) - *[Official MIT page with resources](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s095-programming-for-the-puzzled-january-iap-2018/)*

5. Harvard University
    - [Advanced algorithms - CS224](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uP4rJgf5ayhHWgw7akUWSf)

6. UC Berkeley
    - [Data Structures - CS61B](https://inst.eecs.berkeley.edu/~cs61b/archives.html)
    - [Efficient Algorithms and Intractable Problems - CS170](https://cs170.org/) - *[YouTube videos](https://www.youtube.com/playlist?list=PLkFD6_40KJIx8lWWbE-Uk069aZ1R-W-VU)*


### Books

Several books that have made an impression on me:

1. [Grokking Algorithms by Aditya Bhargava](https://www.goodreads.com/book/show/22847284-grokking-algorithms-an-illustrated-guide-for-programmers-and-other-curio) - **The best** book for complete beginners in algorithms! I wish this book existed when I started learning algorithms.
2. [Introduction to Algorithms by CLRS](https://www.goodreads.com/book/show/6752187-introduction-to-algorithms) - This book is called "bible textbook of algorithms" by many programmers.
3. [Algorithms by Robert Sedgewick & Kevin Wayne](https://www.goodreads.com/book/show/10803540-algorithms) - These authors are instructors of the previously mentioned coursera courses: [Algorithms Part 1](https://www.coursera.org/learn/algorithms-part1) and [Algorithms Part 2](https://www.coursera.org/learn/algorithms-part2). Also this book has excellent and free [site](http://algs4.cs.princeton.edu) with exercises, presentations, and examples.
4. [The Algorithm Design Manual by Steven Skiena](https://www.goodreads.com/book/show/425208.The_Algorithm_Design_Manual) - The book describes many advanced topics and algorithms and it focuses on real life practical examples. This book has one of the best [site](http://www.algorist.com) with resources ([solutions](http://www.algorist.com/algowiki/index.php/The_Algorithms_Design_Manual_(Second_Edition)), [algorithms and data structures](http://www.algorist.com/algorist.html), [python implementations](http://www.algorist.com/languages/Python.html)).
5. [Algorithms by S. Dasgupta, C. Papadimitriou, and U. Vazirani](https://www.goodreads.com/book/show/138563.Algorithms) - This book is an official book for algorithms and data structures classes in several famous universities.
6. [Competitive Programming 3 by Steven Halim & Felix Halim](https://www.goodreads.com/book/show/22820968-competitive-programming-3) - A great book that prepares you for competitive programming (not for complete beginners). You can learn many things and tricks about competitive programming. *But if your goal is to prepare for competitive programming then choose a faster language than Python, **C/C++** (or Java, it's faster than Python but not like C/C++).*
7. [Cracking the Coding Interview by Gayle Laakmann McDowell](https://www.goodreads.com/book/show/29350585-cracking-the-coding-interview) - A bit different from the previous books. Prepares you for coding interviews using great coding problems.


### Training Sites

If the problems from [LeetCode](https://leetcode.com/) are not enough and you need more problems like those, you can find much more on these platforms:

- [HackerRank](http://hackerrank.com/)
- [CodeChef](http://codechef.com/)
- [HackerEarth](http://hackerearth.com/)
- [CodeForces](http://codeforces.com/)
- [Topcoder](http://topcoder.com/)
- [Project Euler](https://projecteuler.net/)
- [SPOJ](http://www.spoj.com/)
- [A2OJ](https://a2oj.com/)
- [PEG](https://wcipeg.com/)
- [Online Judge](https://onlinejudge.org/)
- [E-Olymp](https://www.e-olymp.com/en/)
- [VJudge](https://vjudge.net/)
- [DMOJ](https://dmoj.ca/)
- [USA CO](http://www.usaco.org/)
- [Rosetta Code](http://rosettacode.org/)
- [AtCoder](https://atcoder.jp/)
- [Russian Code Cup](https://www.russiancodecup.ru/en/)
- [LintCode](http://www.lintcode.com/en/)
- [Kattis](https://www.kattis.com/developers)
- [CodeAbbey](http://codeabbey.com/)
- [CS Academy](https://csacademy.com/)
- [Advent of Code](https://adventofcode.com/)
- [Exercism](https://exercism.io/)
- [CodeFu](https://codefu.mk/)
- [Mendo](https://mendo.mk/Welcome.do)
- [Z-Training](http://www.codah.club/)
- [Codewars](http://www.codewars.com/)
- [Wolfram Challenges](https://challenges.wolfram.com/)
- [Google's Coding Competitions](https://codingcompetitions.withgoogle.com/)
- [Cyber-dojo](https://cyber-dojo.org/)
- [CodingBat](http://codingbat.com/)
- [CodeKata](http://codekata.com/)
- [BinarySearch](https://binarysearch.io/)
- [Daily Coding Problem](https://www.dailycodingproblem.com/)
- [Daily Interview Pro](http://dailyinterviewpro.com/)
- [Codility](https://codility.com/)
- [CoderByte](https://coderbyte.com/)
- [AlgoExpert](https://www.algoexpert.io/)
- [Edabit](https://edabit.com/)
- [DevPost](https://devpost.com/)
- [Brilliant](http://brilliant.org/)
- [Codingame](https://www.codingame.com/)
- [CheckiO](http://www.checkio.org/)
- [FightCode](http://fightcodegame.com/)
- [Kaggle](http://kaggle.com/)
- [Rosalind](http://rosalind.info/problems/locations/)


### Other Resources

1. [Geeks For Geeks](https://www.geeksforgeeks.org/) - The site which **all** interested in algorithms (no matter if beginners or experts) should know! [YouTube channel](https://www.youtube.com/channel/UC0RhatS1pyxInC00YKjjBqQ) with many useful videos.
2. [The Algorithms - Python](https://github.com/TheAlgorithms/Python) - Great GitHub repo with many algorithms written in Python ([Link](https://github.com/TheAlgorithms) from the same repo written in other programming languages).
3. [CP Algorithms](http://cp-algorithms.com/) - Great page with excellent explanations for various algorithms.
4. [USFCA Visualization Tool](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html) - Great tool for visualizing data structures and algorithms, created by the University of San Francisco.
5. [VisuAlgo](https://visualgo.net/en) - Another great tool for visualizing data structures and algorithms through animation.
6. [Google - Intro to Data Structures and Algorithms](https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513) - Free course on Udacity offered by Google.
7. [Microsoft - Algorithms and Data Structures](https://www.edx.org/course/algorithms-and-data-structures) - Free course on edX offered by Microsoft (maybe these 2 resources, from Google and Microsoft, should belong in the [Courses](#Courses) section).
8. [HackerEarth - Tutorials and Practice](https://www.hackerearth.com/practice/) - Practice problems and learn about many algorithms and data structures needed for competitive programming.
9. [KhanAcademy - Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms) - Good explanations for some basic algorithms.
10. [Tutorialspoint - Data Structures and Algorithms](https://www.tutorialspoint.com/data_structures_algorithms/index.htm) - Another platform with good explanations, also Tutorialspoint has free tutorials for almost everything related to CS!
11. [hackr.io - Data Structures and Algorithms Tutorials and Courses](https://hackr.io/tutorials/learn-data-structures-algorithms) - Big collection of tutorials and courses.
12. YouTube playlists with tutorials:
    - [Data Structures by mycodeschool](https://www.youtube.com/playlist?list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [Data Structures by HackerRank](https://www.youtube.com/playlist?list=PLI1t_8YX-Apv-UiRlnZwqqrRT8D1RhriX)
    - [Algorithms by HackerRank](https://www.youtube.com/playlist?list=PLI1t_8YX-ApvMthLj56t1Rf-Buio5Y8KL)
