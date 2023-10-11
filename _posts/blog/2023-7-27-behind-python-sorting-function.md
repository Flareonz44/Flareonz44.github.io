---
layout: post
title: "Back to the roots: Behind Python's sorting function"
author: Flareonz44
tags: [algorithm, c, coding, portfolio, python, tutorial]
metadesc: Let's dive into the deep lines of Python's built-in functions and let's made our own implementation.
---

![algorithm](/images/2023-7-27-behind-python-sorting-function/image.png)

Some days ago, I applied for a position as a C programmer. The next day, I received an e-mail from the company's recruitment team. The recruiter asked me to create a program in C that takes two parameters: an input file and an output file. The program must open the input file (which is a .txt file containing a random text paragraph) and then sort all the words inside alphabetically using linked lists. In the e-mail, the writer also provided a sample text for input and output as an example. 'Super easy task', I said. I was completely wrong.

## Python approach

After more than 4 years of using Python, I get used to tackling any programming problem with it, and then porting the logic to the desired language or framework. I thought the problem could be easily solved, mainly because of the high-level nature of Python and because sorting is a super common feature that almost any program includes.
I sketched out the entire program, and it only took 40 lines of code. Now it was time to port it to C. The problem was that the whole essence of the program relies on Python's sort() function. I was pretty sure that C does not include a built-in sort() function, and therefore, it was time to create my own sorting algorithm from scratch.

## The challenge

The first thing I did was obviously Google. There must be someone out there who made a post about this. But surprisingly, after 2 hours of research, I found nothing. Some Stack Overflow questions related to this, but that was all, and the answers were based on a Wikipedia page :/ So, the next step was to start sketching something to begin with. Personally, whenever I encounter challenges like this that require designing an algorithm, I always start by solving it on my own with a pencil and a sheet of paper. So I did that. I sorted some words by hand and then took a moment to analyze, step by step, all the 'instructions' I followed to solve the task. I came up with comparing two words letter by letter until I found the right place for each one. That was the key. Probably, a very skilled programmer will say that my own implementation of the sorting function is not the most efficient, but the idea was not to pursue performance, just to learn how the masked sort() function could work.

Before this key idea, I was thinking of creating a recursive function that split each word into a tree-like hierarchy group, but it was a bit difficult to implement. I believe that group-based approach could work for a large word database, but I'm not sure because it would need a lot of memory and CPU resources. In any case, I stuck with the first idea I mentioned.

The main logic of the algorithm relies on a function called 'goes_first(str1, str2)'. That function will return 0 (false) if str1 goes before str2 or 1 (true) if str2 goes before str1. But how does the code know which word goes first? Easy. It iterates over each letter of the shortest string (if you iterate over the last letter of the longer word, you could run into an out-of-index error when accessing the index 5 of 'apple'). If both letters are equal, it continues. If they are different, then it returns the string with the lower ASCII value (A/65 goes before G/71). That's all. The code returns the corresponding value, and the calling function just rearranges the list based on the 'goes_first' function's answer.

## Improvements

I tested the code with the sample the recruiter provided, but I found that my approach was case-sensitive. Therefore, 'Z' goes before 'a' due to the ASCII index. I easily solved the problem with an ugly 'toLowerCase()' function as follows:

```c
for (int i = 0; i < strlen(str); i++){
    char st1 = (str[i]>='A'&&str[i]<='Z')?str[i]+32:str[i];
    //...
}
```

Basically, if the character is in the range of capital letters, it will be offset by 32, which is the gap between capital and lowercase characters in ASCII, and then it will continue with the comparison logic.

However, there was still one problem: my code puts 'activity' before 'act'. Although it is still correct because they start exactly the same, it is better to put 'act' first, as it has fewer letters than 'activity'. So I made a simple patch: if we are at the end character of the shortest string and we get the same letters (e.g., 't' from 'act' equals the first 't' from 'activity'), the code will return the shortest word no matter what.

And now, the implementation is finally done (after 4 hours of coding).
Here you have the github repo to check it out: [github.com/Flareonz44/TXT-Word-Sorter](https://github.com/Flareonz44/TXT-Word-Sorter)

## Final thoughts

I liked this challenge, mainly because it made me think about these kinds of functions that are hidden from the day-to-day Python programmer. And I think that, probably, that's the best advantage of Python: you don't have to code this kind of function; you just call it with sort(), and that's all. You gain a lot of time, and your productivity increases exponentially. But, from time to time, it's worth going back to the roots, just to have fun and learn a lot.