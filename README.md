# Quine-McKlusky

ABSTRACT

The object of solving the problem of minimizing the Boolean function in this work is a block diagram with repetition, what is the truth table of the given function. This allows to leave the minimization principle within the function calculation protocol and, thus, dispense with auxiliary objects like algebraic expressions, Karnaugh map, Veitch diagram, acyclic graph, etc. 

The algebraic transformations of conjunctors are limited to the verbal form of information, they require active decoding, processing and the addition of algebraic data, therefore, as the number of variable variables increases and the resource of such minimization method is quickly exhausted. In turn, the mathematical apparatus of the combinatorial block diagram with repetition gives more information about the orthogonality, contiguity, and uniqueness of truth table blocks, so the application of such a minimization system of the Boolean function is more efficient. Equivalent transformations by graphic images, in their properties, have a large information capacity, capable of effectively replacing verbal procedures of algebraic transformations. The increased information capacity of the combinatorial method makes it possible to carry out manual minimization of 4, 5-bit Boolean functions quite easily. Using a block diagram with repetition in tasks of minimizing Boolean function is more advantageous in comparison with analogues for the following factors: – lower cost of development and implementation, since the principle of minimization of the method remains within the truth table of this function and does not require other auxiliary objects; – increasing the performance of the manual minimization procedure for 4-, 5-bit functions and increasing the performance of automated minimization with a greater number of variable functions, in particular due to the fact that several search options give the same minimum function. 

The combinatorial method for minimizing Boolean functions can find practical application in the development of electronic computer systems, because: – DNF minimization is one of the multiextremal logical-combinatorial problems, the solution of which is, in particular, the combinatorial device of block-schemes with repetition; – expands the possibilities of Boolean functions minimization technology for their application in information technology; – improves the algebraic method of minimizing the Boolean function due to the tabular organization of the method and the introduction of the device of figurative numeration; – the minimum function can be obtained by several search options that reduces the complexity of the search algorithm, and is the rationale for developing a corresponding function minimization protocol.
 
 
 Karnaugh map method or K-map method is the pictorial representation of the Boolean equations and Boolean manipulations are used to reduce the complexity in solving them. These can be considered as a special or extended version of the ‘Truth table’.
Karnaugh map can be explained as “An array containing 2k cells in a grid like format, where k is the number of variables in the Boolean expression that is to be reduced or optimized”. As it is evaluated from the truth table method, each cell in the K-map will represent a single row of the truth table and a cell is represented by a square.
The cells in the k-map are arranged in such a way that there are conjunctions, which differ in a single variable, and are assigned in adjacent rows. The K-map method supports the elimination of potential race conditions and permits the rapid identification.
By using Karnaugh map technique, we can reduce the Boolean expression containing any number of variables, such as 2-variable Boolean expression, 3-variable Boolean expression, 4-variable Boolean expression and even 7-variable Boolean expressions, which are complex to solve by using regular Boolean theorems and laws.
The problems and shortcomings of the known methods for minimizing Boolean functions are associated with a rapid growth in the amount of computation, which results in an increase in the number of computational operations, and, consequently, in the increase in the number of variables of the logical function.

Simplification of Boolean expression is a practical tool to optimize programing algorithms and circuits. Several techniques have been introduced to perform the minimization, including Boolean algebra (BA), Karnaugh Map (K-Map) and QM. Minimization using BA requires high algebraic manipulation skills and will become more and more complicated when the number of terms increases. K-Map is a diagrammatic technique based on a special form of Venn diagram. It is easier to use than BA but usually it is used to handle Boolean expressions with no more than six variables. When the number of variables exceeds six, the complexity of the map is exponentially enhanced and it becomes more and more cumbersome. Functionally identical to K-Map, QM method is more executable when dealing with larger numbers of variables and is easier to be mechanized and run on a computer.

 
 
 Quine McKlusky is a method to minimize boolean functions which are mathematical functions that output either "true" or "false".

 The algorithm takes as input a truth table that lists the output of a boolean function for every possible combination of inputs, and outputs a simplified version of the function that is equivalents to the original function but has fewer terms.

The Quine-McCluskey algorithm can be applied to both digital circuits and logical expressions, and is an efficient method for minimizing Boolean functions.

Here is a overview of the steps involved in the Quine-McCluskey algorithm:

1. Group terms: The terms in the truth table are grouped based on the number of "1"s they contain.

2. Compare terms: Each pair of terms in the same group is compared to see if they differ by only one bit. If two terms differ by only one bit, they are combined into a single term.

3. Repeat: The process of comparing and combining terms is repeated until no more terms can be combined. The resulting terms are called prime implicants.

4. Select prime implicants: A chart is created where each row represents a prime implicant and each column represents a term in the truth table. The chart is used to determine which prime implicants are necessary to cover all the terms in the truth table.

5. Express result: The result is expressed as a sum of products using the selected prime implicants.

6. Simplify: The result is simplified using Boolean algebra laws, if possible.

