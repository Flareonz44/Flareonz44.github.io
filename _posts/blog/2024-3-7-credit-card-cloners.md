---
layout: post
title: "Credit Card Cloners [with NFC]"
author: Flareonz44
tags: [cybersec, electronics]
metadesc: "Another way your credit card could be cloned by criminals"
---
![Cards](/images/2024-3-7-credit-card-cloners/banner.webp)

***All content shown in this post is exclusively for educational purposes. I'm not responsible for the use you make of the information shown here.***

Today I went to the local vegetable market to buy some tomatoes and onions for a salad. Everything was going as usual until the guy (who I'm pretty sure is the owner of the store) told me the POS system was not working. I was about to say something, but he beat me to it, saying that he would use his phone to process the payment. I said 'ok' because I was curious about what he would do next.  
He grabbed my card and held it close to his phone (at this point, I figure out he was using NFC). He input the amount and proceeded. Just for security reasons, he showed me the successful payment screen and then I left with my tomatoes.

## The Attack

Don't panic! Nothing bad has happened (at least as of now), but as an ethical hacker, I always have to consider all possible scenarios, and I just imagined that this man could have installed an app for NFC data dumping or something similar. If that's the case, I'm in trouble (along with all his other customers).  
It's a perfect crime because if the dumping app is silent enough, it could run as a quiet background service, and no one will notice it. There's no point in quickly checking for open apps or notification logs, especially when you're just paying for your vegetables. You're also unlikely to take the time to scan the entire phone's storage for the dump file.  
He could then sell that card information, and things could easily get out of control.

## Prevention


In IT, when we talk about dealing with vulnerabilities, we tend to divide solutions into two groups:

- patches
- workarounds

The first ones are basically software updates that make the system no longer vulnerable to that attack, and the second one is a quick solution to the problem, an alternative to being vulnerable until the patch is implemented.  
In our case, there's no patch, no solution to this, because it's practically impossible to detect it. Therefore, I'll give you two workarounds:

- Never give your credit card information and AVOID using this payment solution.

- If the POS system is not working, ask if you could transfer money or pay via QR code.

## Conclusion

As of today, there's no other way to prevent this particular case, so it's better to keep the workaround in mind. Despite NFC being a fascinating technology, we must be aware of these kinds of attacks, as they directly affect us, so

Moral?

![trust no one!](/images/2024-3-7-credit-card-cloners/moral.webp)

Cheers!