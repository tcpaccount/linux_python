'''
To secure his messages, Julius uses a word-by-word progressive variant of the Caesar cipher: for each word in the message, he shifts each letter in the alphabet by as many ranks as the number of characters that the word contains. For each letter, if we need to go beyond "Z", we wrap around to "A".

For example, the message
CLASH OF CODE
becomes
HQFXM QH GSHI


(each letter of "CLASH" is shifted by 5 ranks, each letter of "OF" is shifted by 2 ranks...).

You receive an instruction (DECODE or ENCODE) on the first line and the message to process on the second.
Input
Line 1: The text instruction indicating whether to encode the message (if instruction = ENCODE) or decode it (if instruction = DECODE).
Line 2: The text message indicating the message you have to encode or decode (words are separated by spaces and each character is a capital letter)).
Output
A line containing the encoded or decoded message (depending on the instruction variable received).
Constraints
message contains only uppercase letters and spaces.
Example
Input
ENCODE
ABACUS

Output
GHGIAY


___________________
ENCODE
ABACUS

Output
GHGIAY
___________________
ENCODE
YES I KNOW

Output
BHV J ORSA
___________________
DECODE
FXWMNAODU

Output
WONDERFUL
___________________
DECODE
J XKGRRE PMOI HTIJX

Output
I REALLY LIKE CODES
___________________

'''


import sys
import math
import string


instruction = input()
message = input()

