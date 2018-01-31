*This is a tough problem. If you are stuck, please ask an instructor for help.*

If you're named Danny Kyung or Matthew Emes, it opens up the possibility of justifying your use of usernames such as [dank](https://github.com/dank) or [memes](https://github.com/memes).
Your task is to find the longest word such that it satisfies the criteria - that is, it is a substring of the given string but not necessarily consecutively (we can call it a sparse substring). If there are multiple words of same maximum length, output all of them.
You may use the the [Enable word list](http://norvig.com/ngrams/enable1.txt), or some other reasonable English word list. Every word in your output must appear in your word list.
Formal Inputs & Outputs

#### Input description
```
One string.
```
#### Example Inputs
```
Donald Knuth
Alan Turing
Claude Shannon
```
#### Output description
```
A single word (output the lengthiest word/words in case of multiple words satisfying the criteria)
```
#### Example outputs
```
Donut (because **Don**ald k**nut**h)
Alanin, Anting
Cannon
```
Note : Your outputs may differ from these outputs depending on the word list you are using

#### Challenge Inputs
```
Ada Lovelace
Haskell Curry
**Your own name!**
```
