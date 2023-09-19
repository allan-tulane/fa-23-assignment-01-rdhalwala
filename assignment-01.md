

# CMPS 2200 Assignment 1

**Name:**__Raiya Dhalwala________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
.  Yes.
  2^n+1 = 2*2^n = c*2^n \in O(2^n)
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
.  No because 2^{2^n} grows much faster than 2^n, so it is not an element of O(2^n)
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  No because when you keep doing the derivative it ends upt with

1.01n^1.01/2logn = limit n --> infinity 1.01 *1.01 *n^1.01/2 = infinity.
Then according to the slides this would go in omega.
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  Yes, as I said in the problem above, once you take the limit, it goes to infinity which corresponds with omega.
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  When you derive sqrt(n), it is 1/(2sqrt(n))
The derivative of \mathrm{log} n)^3 is 3(logn)^2 * 1/nln(10)
Then you look at the ratio and simplify. I did a lot on paper but you get 1/2*3*logn^2*1/nln(10)
Move the constants out and get to 1/(logn^2* 1/sqrt(n))
So the limit is 0
When you look at the limit table in slide 1 this means that sqrt(n) does exist in O((\mathrm{log} n)^3)
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?
    No, in the last question we just showed how it is in O((\mathrm{log} n)^3), so it does not meet the requirements to be and element of Omega.
.  


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  
  This function is a recursive function because it calls itself within the function. It has a base case to determine if x is one. Otherwise it recursively calls x-1 and x-2 and then returns the sum of that. It will return the fibonacci sequence of those numbers.

.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  
  The work is O(n) and the span is O(n) because this is a linear algorithm.

.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   
  Partial credit? Got confused at end.

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
  The work of this algorithm is O(n log n) because it splits in two, but each time it works at constant work.
  The span is O(log n) because it is like lab last week with recursion and splitting in two.
.  
.  
.  
.  
.  
.  

  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  
This algorithm has a work of O(n) because the input is same as amt of threads
The span of this algorithm is O(log n) bc that is height of longest tree in recursion.
.  
.  
.  
.  
.  
.  
.  
.  

