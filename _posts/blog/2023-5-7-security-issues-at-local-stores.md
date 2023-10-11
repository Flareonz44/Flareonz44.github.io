---
layout: post
title: "Security issues at local stores"
author: Flareonz44
tags: [cybersec, social-eng, electronics]
metadesc: How a Mouse Jack Attack could seriously compromise a local store.
---

![pharmacy picture](/images/2023-5-7-security-issues-at-local-stores/banner.png)

***All content shown in this post is exclusively for educational purposes. I'm not responsible for the use you make of the information shown here.***

Yesterday, I walked three streets over to the pharmacy to buy some shampoo, as it was cheaper there than at the supermarket. I only bought the shampoo, and when the cashier told me the total price, I noticed that it didn't match the price on the shelf. I brought this to the cashier's attention, and she advised me to speak with the manager. After checking it, he told me I was right. The manager promptly went to the nearby computer, located between two shelves, and logged into the management program with his user and password in front of me. He scanned the product, corrected the price using the wireless keyboard, and instructed me to pay at the checkout counter.
There, I ask the cashier if now the price was the correct one, and she said "Yes", with a smile on her face. I left the pharmacy, worried about how easy it would be to access their computers and eventually modify prices as I want.

## Attack pattern

Nowadays, wires in desktop computers look unsightly. Whether you care about the aesthetics of your computer or are simply bothered by cables, a wireless keyboard is the best option. It's easy to set up and doesn't cause any compatibility issues.
However, many wireless keyboards use non-standardized technology. Manufacturers often rely on chips such as nRF24L, which enable wireless radio communication. These chips are usually built into wireless adapters and function as radio receivers, capturing signals sent through specific channels and telling the computer which keys you have pressed.
By using an nRF module, a dev board, a battery, and a power amplifier (PA), you could easily carry out a Mouse Jack attack. Pretend to be browsing in a pharmacy, approach to the target computer, and hit the board reset button. Within seconds, the computer would be compromised, as the nRF module would behave like a legitimate keyboard, and start sending keyboard inputs that will be accepted by the adapter. The security cameras wouldn't notice anything.
You could also set up a Python 3 server and open a port on your home router to the world. Run a command on the target computer that downloads an executable from the home server and quietly installs it. Once this is done, you could establish a reverse shell, take control of the computer, and log in to the management program to make any desired changes.

## Prevention

As you can see, I'm not a black hat with years of experience, but I was still able to figure out how to carry out this attack. Now, imagine what a skilled guy could do. This type of attack can compromise the entire economy of local stores, so taking action to prevent it's necessary.
While computer systems tend to be secure, the main vulnerability is often people. For example, if the manager hadn't covered the keyboard while typing, I wouldn't have been able to see their username and password. Furthermore, placing a computer in plain view with the necessary credentials to make changes to the price database is highly risky.
In addition, while wireless devices may look sleek and modern, they are not as secure as traditional wired keyboards. Using a wired keyboard is a thousand times more secure. Until next time!