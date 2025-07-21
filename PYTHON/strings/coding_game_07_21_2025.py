'''
In the spirit of particles and anti-particles, let's define characters and anti-characters as lowercase and uppercase characters respectively. As we all know particles meeting anti-particles annihilates each other and produce energy. In a string, an anti-character annihilates a character if they are adjacent and are the same letter in opposite cases (e.g., a and A), releasing 1 unit of energy in the process.

baACCcB → b(aA)C(Cc)B → bCB + 2 energy units

Given a string of characters, annihilate characters until a stable string is reached and record the energy released. A stable string is a string where no annihilation can occur.
Input
One line:
string s consisting of only letters in the ASCII alphabet, i.e., A-Z and a-z .
Output
Line 1: The remaining string after annihilation
Line 2: Units of energy released
Constraints
1 <= Length of s <= 255
Example
Input

aAaAa

Output

a
2


_______________________________


aABbEeeEFfAa


6

_______________________________


heAbCDeFfEdcBallo

hello
6


_______________________________


AAAbaaa

AAAbaaa
0


_______________________________


REaABCbBcDdbeFfEsSeR

RR
9


_______________________________


cbbbbcBAcbBCcBBAABAcbBaABacBbccbbaABBaCbbABbaBcCcAbAaBBBacbBCBCbCaCAacaAcAbbBAaAbaBacCbAaBAcAAaACCbAaCCcBbcaBacAccBaBBAAacAbbAabcababbcBAAcAAAbbABcAccccccCBCACbbbCabABCAaBCCAACCCbaCaCcabaAacCaccABacAcCbbCBaAbcBBCbBacaCBcaaaaABACcBaABABbCcCAcaAbBCacccbBBCc

cbbbbcBAcBBAABAcBacccaCbcABBaBCbCacAbAbaBcAACCbaBacAccBaBBAcAbbbcababbcBAAcAAAbbABcAcccccBCACbbbCabABCBCCAACCCbaCaabaaccABacACacaCBcaaaBABBAccB
56


_______________________________

_______________________________

_______________________________




'''
s = input()


