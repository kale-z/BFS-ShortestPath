# Shortest Path by BFS
In this exercise, a provided input of a grid with some obstacles as shown in the below screenshot. The goal is to write a Python function that finds the shortest walking distance from top-left corner (S: start) to the bottom-left corner (T: target) of the grid. The applied algorithm was Breadth-First Search (BFS) algorithm. 

<br>


## Explanation
Grid is represented as a two-dimensional array (list) where **0** represents ‘no obstacle’ and **1** represents ‘obstacle’ at the corresponding location.

<img style="max-width: 100%;height: 200px;" src="/screenshots/FullGrid.png" alt>

For the example grid above, the array representation is as follows:
<pre>
  G = [[0,1,0,1,0,0], [0,1,0,0,0,0], [0,0,0,0,1,0], [0,0,0,1,1,0]]
</pre>

If the number of rows in the grid is **n** and the number of columns is **m**, the starting point is (0,0) and the target is (n-1, m-1). In this example, the start from (0,0) and want to react to (3,5). We can only move to left, right, up and down as long as there is no obstacle and we don’t move outside of the grid as we can see in the following example.

<img style="max-width: 100%;height: 180px;" src="/screenshots/GridMovements.png" alt>

<br>

## Methodology

<pre>
<i>Input</i>: Two-dimensional array (G) that represents the grid.
<i>Output</i>: Print the minimum number of steps needed to go from S to T and the actual path. 
<b><i>If there is no valid path, report it as well (Minimum Steps: 0, Path: No Valid Path)</i></b>
</pre>

For the example above, a possible output is:
<pre>
Minimum Steps: 10
Path: (0,0)&rarr;(1,0)&rarr;(2,0)&rarr;(2,1)&rarr;(2,2)&rarr;(2,3)&rarr;(1,3)&rarr;(1,4)&rarr;(1,5)&rarr;(2,5) &rarr;(3,5)
</pre>

<br>

## Usage
<ol>
  <li>Inside the script, the first line is a nested list which represents the grid.</li>
  <li>There are two functions: 
    <ul>
      <li><code>Graph</code>: which prints the grid graph as Adjacency List as shown in screenshots</li>        
      <li><code>BFS</code>: which applies the Breadth-First Search (BFS) algorithm and returns the results </li>
    </ul>
  <li>The first line of the BFS function indicating the start and end points consecutively</li>
</ol>

<br>

## Screenshots
<em>Adjacency List Representation of the Output Graph</em>
   <br><br>
<img style="max-width: 100%;height: 350px;" src="/screenshots/AdjacencyList.png" alt>
