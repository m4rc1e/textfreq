=====
Text Frequency
=====

Description:
-----
A script to count the frequencies of the following in text:
•Words
•Letters
•Letter pairs
•Devanagari Conjuncts
•Bengali Conjuncts

Can handle non ascii files well. 1gb of data takes approximately 5-7 mins.

Installation:
-----
- pip or easy_install 'textfreq'

Usage:
-----
In Shell/Command-prompt: ``textfreq <INPUT.txt> <OUTPUT.txt> <Commands: -w (words), -p (pairs), -l (letters), -dc (Deva Conjuncts), -bc (Bangla Conjuncts)>``

Version History:
-----
***V0.100***
- Significantly improved speed
- Added Devanagari and Bengali Conjuncts finder

***V0.001***
- Added words, pairs and letter counts
