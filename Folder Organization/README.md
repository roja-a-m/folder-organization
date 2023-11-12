A web development project is being organized into several folders, and there are three rules that need to be followed:
Only one README file is allowed in each folder, and it cannot be the only file in the folder.
The number of CSS files and JS files can only exceed the number of the other file type by at most 1. Only a certain number of files are allowed in each folder.
Given the types of files and the folder capacity, what is the minimum number of folders needed to organize the project?
For example, let's say cssFiles = 2, jsFiles = 1, and readMeFiles = 2. The number of files in each folder cannot exceed capacity = 2. In this case, you would need a minimum of 3 folders. One possible solution is such: 1 CSS file and 1 README file, 1 CSS file and 1 README file, and 1 JS file. Therefore, the answer is 3.

Note: It is guaranteed that the answer always exists.

Function Description
Complete the function minFolders in the editor below. The function must return an integer denoting the minimum number of folders required to organize the project.

minFolders has the following parameter(s): 
cssFiles: an integer
jsFiles: an integer
readMeFiles: an integer
capacity: an integer

Constraints
0 ≤ cssFiles ≤ 105
0 ≤ jsFiles ≤ 105
0 ≤ readMeFiles ≤ 105 1 ≤ capacity ≤ 103


Sample Input For Custom Testing
5 0 2 2
Sample Output
5
Explanation
Here, there are 5 CSS files, 0 JS files, and 2 README files, where the maximum folder capacity is 2. The optimal solution requires 5 folders:
1. 1 CSS file and 1 README file 2. 1 CSS file and 1 README file 3. 1 CSS file
4. 1 CSS file
5. 1 CSS file
Therefore, the answer is 5.
