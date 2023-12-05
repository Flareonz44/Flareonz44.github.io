---
layout: post
title: "The Truman Network Attack: hacking a PosNet's reality."
author: Flareonz44
tags: [cybersec, coding, social-eng]
metadesc: "A aplication case of what I like to call the Truman Attack"
---

![Truman's reality](/images/2023-12-2-hacking-posnets/banner.webp)

***All content shown in this post is exclusively for educational purposes. I'm not responsible for the use you make of the information shown here.***

## A bit about The Truman Show

Do you remember Truman's life story? Let's do a quick recap.  
Truman is a person whose life is streamed 24/7 as a reality show to the entire world, but he never noticed this. His life was like anyone else's, despite the fact that his reality was entirely made up. Nothing was real for us, but for him, that fake reality was the only reality he knew, so for him, it was real. Until he started to connect the dots.

## The free burger

Now let's dive into this hypothetical situation, set up in our reality.  
We enter a fast-food chain to get one of those large and tasty combos. We head straight to the self-service touchscreen to choose our desired combo. We do so, and then the computer asks us to use our credit card to pay for the order. Right before that, we check our watch and proceed to pay. The ticket is printed, and we go to the delivery area to get our combo, ready to be eaten.  
But nothing is what it seems. In fact, we didn't check the time on our watch, and our bank account has the same amount of money as before the payment. How is it possible?

## The Truman Attack

What do the first story and the previous one have in common? Nothing, apparently.  
The Truman Attack (I coined the name; others may call it something else) consists of creating an entire fake reality for our target. In the burger story, the target is the PosNet that we use to pay. Essentially, we want the device to believe it is connecting to the real bank server while processing our transaction. But how?  
First of all, we need to make a network scan in the target's area. Since most PosNets are 'portable,' this means that they might be connected to a WiFi Access Point (though this is not the only communication protocol they support). Therefore, that AP should be on the list that scanning tools like `nmap` could provide. 
There are tons of WiFi attacks out there, but I particularly like one – the Deauth Attack. A Deauthentication attack is a kind of attack that disconnects all the devices on a network from the provided Access Point (AP). So, sit at a table in the restaurant, prepare your [DSTIKE](https://dstike.com/products/dstike-deauther-watch-v3s) (or use `aircrack-ng`), and wait for people to use the self-service system. Right before the payment moment, run the deauth on different APs until the customer at the touchscreen is taking more time than usual. That means you've found the correct AP to which the PosNet is connected.  
The next step is to set up an Access Point (AP) with an identical SSID as the PosNet's and launch the deauth attack on the original network (not yours – pay attention to the MAC addresses). Probably, someone will complain about it, and someone from the staff will come to solve the problem (in most cases). They will check the WiFi, and here we must be lucky for the staff member to connect to your network rather than the legit one. In general, people tend to choose the first option that matches the known network name, so to force our network to appear first, we must be closer to the device, as it will sort the list based on the strength of the signal. Or you can try to do it yourself at your own risk. Once it is successfully connected, our attack is almost ready.  
Almost.  
There's another crucial step that I haven't mentioned yet.    
Before all that, you must first set up a fake Bank server. This is the most difficult part since you must simulate all the communication with the PosNet. To do that, you must spend some time analyzing in-depth all the network traffic between the PosNet and the real server (I highly recommend getting yourself a PosNet to analyze securely at home, using Wireshark). There, find a vulnerability in the communication queries, perhaps a generic static successful payout response is enough.  
Using tools such as `dnsmasq` and `iptables`, you could redirect the network traffic from **auth.real-bank.com** that the PosNet requests to a specific port on your computer's localhost. Then, with some Python 3 code, set up a fake server that accepts any payout request and always returns a successful response. Back at the fast-food restaurant, you only have to deploy the attack.
But, where does the watch from the story fit in? Well, we don't want to be caught easily, so grab your Linux laptop with a big battery, make sure it's fully charged, and well packed in your backpack. Then, just use a smartwatch as a remote control to launch the servers, scripts, etc. (A Bluetooth connection and some Python might be enough to achieve this).

At this point, we've essentially created an entire reality for the PosNet, and since the device can't distinguish a real server from the simulated one, it's just like Truman.

## Beyond burgers

This attack is not only intended for payout systems. It could be used for anything, since the entire world these days is cloud-based. Every service could be vulnerable to this kind of attack unless we set up a robust protection system to prevent it.

## Prevention


Despite this attack being so complex that it is challenging to successfully deploy, there is still a possibility. Nowadays, systems are well-designed to prevent these types of attacks, making the chances very low. Nevertheless, establishing strong encrypted communication between the client and the server should be sufficient. Additionally, you can set up network verification to always ensure that the client is connected to a legitimate network, using MAC checking and creating dynamic authentication servers and keys.

## Conclusion

In a world where our lives increasingly depend on large and complex computing systems, our focus should be on enhancing the security of these systems. Most importantly, we must think outside the box and stay one step ahead of hackers, otherwise, they will prevail.

See ya!