---
layout: post
title: "Vulnerabilities of the Scan & Go System"
author: Flareonz44
tags: [security, social-eng]
metadesc: "The Scan & Go system is widely used by Supermarket chains, but there are some vulnerabilities in it."
---

![digital scanner](/images/2023-5-2-vulnerabilities-scan-n-go/banner.png)

***All content shown in this post is exclusively for educational purposes. I'm not responsible for the use you make of the information shown here.***

## Introduction

This morning, I went to the supermarket to buy some snacks for tonight's movie night with friends. I was surprised at how long the checkout line was. There were around thirty people in the queue, and I had to wait for a minimum of forty minutes just to buy two snack bags and a coke.
I was at the snacks stand, when I noticed a significant price gap between the big and small packs of snacks. I decided to go for the larger pack, but I still felt like I was paying too much. As I was waiting to pay, I saw a couple using a new system called "Scan & Go" to pay for their items. It's a simple process where you scan your items, select your payment method, and pay. Easy right?
Since I had my credit card with me, I decided to try out this system too. I scanned my items and paid in less than five minutes.
On my way home, I realized how easy it would be for someone to cheat the system and pay less for their items.

## Attack pattern

Let's use a USB flash drive as an example. At the electronics stand, you check the prices for each one and you see this (prices are for reference only):

- 16 GB - $5
- 32 GB - $12
- 64 GB - $20

So, you grab a 16 GB drive and pay for it. When you get home, take out the information card that came with the product and carefully cut the barcode printed on it. Use some transparent tape to attach the barcode to your hand and leave a little gap on both sides. Then, go back to the store.

While you are carrying other products (like a chocolate bar or something inconspicuous), get a 64 GB flash drive and stick the first drive's barcode over the 64 GB one. Be aware of security cameras. Scan this modified product and immediately remove the stuck barcode. And you're done. If there's no one to check your payments, you've just gotten a 64 GB flash drive for only $5.

But even if there's someone checking your purchases, you still have a chance. The ticket will show something like "SNDSKDRIVE16ULTFIT", which corresponds to the 16 GB flash drive. Since the 64 GB version has a very similar name (like "SNDSKDRIVE64ULTFIT"), the person checking your purchases will likely only pay attention to the first letters to quickly check that you have a Sandisk flash drive, and then move on to your other products. If the checkout line is crowded, this verification will be faster, and therefore, you have a higher chance of bypassing the checkout.

If you still get caught, you can try blaming the scanning system. You can show the assistant all the products you bought, and since you removed the stuck barcode earlier, there is no evidence for them to incriminate you.

## Prevention

First, all supermarket chains that use the Scan & Go system or similar should thoroughly check each customer's purchase. As you read before, if the person is fast enough, it will be almost impossible to incriminate them, but at the very least, they should pay the correct price for the product.

## Final words

There is no system that is completely secure. However, I hope that the posts I've written will help someone to create or design a better system, or increase the security of existing ones. It only took me 15 minutes to think up an attack pattern, but this could cost millions to any company. Therefore, I strongly encourage companies to take necessary precautions to prevent fraud and protect their assets.