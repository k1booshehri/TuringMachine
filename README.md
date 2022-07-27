## Project description (Theory of automata course, final project 2):
###Input
The first line of input is a binary string (consisting of 0's and 1's) which is the encoded string of a Turing machine. In the second line of the input, the integer nn comes, which represents the number of strings that should be tested on the machine as input. Then in each of the next nn lines, a coded string comes as input in each line, which must be tested on the implemented machine.
<br />
###Output
The output of the program contains exactly n lines, in each line, the test results of each input on the Turing machine are printed in order. If each entry is accepted, the word Accepted should be printed, otherwise, the word Rejected should be printed.
<br />
###important points
Consider the initial state code as 1.
The final state code is 1^{(number of states)}1
Consider the blank character code in bar 1.
It is guaranteed that an infinite loop does not occur in a given Turing machine.
<br />
###Example
#####Sample entry 1
<br />
101101011011001010110101
3
<br />
11011011
110111011
<br />
#####Sample output 1
Accepted
<br />
Accepted
<br />
Rejected
<br />

#####Sample input 2
101110110111101100101101111011011001101101101101100110111011011101100110111110111011010011101101110110100111011101110111010011101111010111101100111101101111011011001111010111110101
5
111011111011111111
1111101110111
1110111011111011111
<br />
111011111
<br />

#####Sample output 2
Rejected
<br />
Rejected
<br />
Accepted
<br />
Rejected
<br />
Accepted
