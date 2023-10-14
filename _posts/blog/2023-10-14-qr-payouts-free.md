---
layout: post
title: "QR Payouts for free through Social Engineering"
author: Flareonz44
tags: [cybersec, coding, social-eng]
metadesc: "How easily you could bypass any QR Payout like Mercado Pago's one using social engineering"
---

***All content shown in this post is exclusively for educational purposes. I'm not responsible for the use you make of the information shown here.***

![phone and qr payout](/images/2023-10-12-qr-payouts-free/banner.webp)

## Overview

Last Monday, I went to the drugstore to get a Coke and some snacks. I grabbed the Coke from the fridge and a bag of snacks from the shelves. I went straight to pay for them. Since I didn't have my credit card with me, I asked the cashier if they accept "Mercado Pago" (it's an e-wallet like PayPal), and she said, 'Yeah, scan the QR below, please.' I did that, entered the total due, and pressed 'confirm.' I showed my screen to her to confirm that the payment was successfully completed, and then I headed back home.

## Attacking

### How payout works

There are several ways you can set up a QR payout system. One of these methods involves generating a static QR code that links to the owner's account ID, and you must make a money transfer to that account. However, there's a significant issue with this approach. In the case of our drugstore, the account ID belongs to the store owner. Therefore, when you complete the transaction, the shop employee has no means of verifying the operation except by relying on the success screen displayed on your phone. They can't access the manager's account transaction history. This is where our exploit comes into play.

### Let's dive in

Grab any Android App IDE you like, a screenshot of the "success screen" from your e-wallet, and any necessary resources. For example, Mercado Pago's success screen may also include a particular sound effect when the payout is completed, so I obtained an MP3 with that sound. Create a simple app that displays the success screen when executed.

You may also include some features to make the hack more believable. In my case, Mercado Pago also displays the name of the account owner and the amount transferred. You can either create an API request to automatically retrieve the account name from the QR code or use a text input method. You can determine the owner's account name from the main app before making the payment and input the name in your app to be displayed. Do the same input box for the money display. After that, compile everything into an .apk file and install it on your phone.

The next time you visit the store, run your malicious app, and you're done – enjoy your free coke and chips.

## Protect your shop

The simplest way to protect yourself from this attack is to set up a proper QR payout. Create a temporary QR payout  link (unique for each purchase) that must be validated before printing a receipt. This way, the store employee can verify that the money transaction was successfully completed before allowing you to leave with your goods.

## Conclusion

These days, QR codes are very popular, and along with their popularity comes some risks that we must be aware of and make the proper decisions to prevent any scams. I hope this article helps you understand one of these risks.

Until next post, take care!