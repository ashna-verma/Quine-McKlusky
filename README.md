# Quene-McKlusky
 
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

