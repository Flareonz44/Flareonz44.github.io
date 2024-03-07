---
layout: post
title: "Skyfend Blader: The Anti-Drone Halo-like Gun"
author: Flareonz44
tags: [cybersec, electronics]
metadesc: "This brand-new device will kill your unauthorized drone on the fly, literally."
---
![Skyfend](/images/2024-1-24-about-skyfend/banner.webp)

***All content shown in this post is exclusively for educational purposes. I'm not responsible for the use you make of the information shown here.***

## What is exactly Skyfend Blader?

I'm sure this video footage will show off what this new device can really do.

> update: the video was removed, so I saved a snapshot of the official site for future generations, [here is the link](https://web.archive.org/web/20240307043537/https://www.skyfend.com/product/skyfend-blader/)

After watching the video, we can begin analyzing it from a cybersecurity point-of-view.

## Objectives of this Device

The purpose of this device is essentially to safeguard a secure area from drone attacks. Nowadays, drones are gaining popularity and becoming more accessible. This technology can be employed for both positive and negative purposes. Therefore, this device serves as a countermeasure against drones with malicious intent. We've watched similar scenarios in action movies where drones are utilized for spying on people's privacy or planning various attacks. It's not surprising that someone developed this tool to combat potentially harmful drone activities like those.

## Bypassing Skyfend Blader

After analyzing some videos found on YouTube where people demonstrated the use of this device, I have a better idea of how it actually works and how it could be bypassed.

Firstly, the device employs a method to detect drones in the 2 km surroundings, and there's only one way to achieve this: RC signal detection. So, from what I observed in various videos, this device comes equipped with a database containing most of the well-known drone communication protocols available on the market. Essentially, it can detect any of those drones purchased on platforms like eBay or Amazon.

This makes even more sense because the Skyfend Blader can be updated with newer firmware versions. Therefore, each time a new drone with a brand-new communication protocol emerges, it will be added to the database, and a corresponding firmware update will be made available for download.

So, after reading this, can you start figuring out a way to bypass them, right?

The simplest way to do this is by implementing your own drone communication protocol. You can base it on any already existing protocol and start from there. Let's put it into an example.

### Example

The Blader can interrupt any kind of communication with the drone, from the RC to the GPS system, making your drone unable to return.

#### RC Communication


If you use a well-known communication protocol, you are in trouble. Perhaps you can still use the same operating frequencies but make some changes to the protocol itself. First of all, encrypt all kinds of commands being sent to the drone with a mix of different algorithms. For instance, start with AES-256 and then use Twofish or Blowfish. Also, ensure that the message always starts with a phrase like "\_UNBREAKABLE\_". This way, if the signal is interrupted, and new commands are received (from the Blader trying to land or crash your drone), the incoming message cannot be understood by your drone featuring your custom protocol. Therefore, as the starting phrase is not present, the drone will raise an alarm and switch into "escape mode."

#### GPS system

So, now your drone is in "escape mode," and you can use another kind of communication to connect back to the drone (say LoRa or something similar), or you can set up another sophisticated system.

You can create an offline "virtual map" of the flight made by the drone by storing all the flight instructions received right before the initiation of the "escape mode." This way, the drone can retrace the path and eventually return to your location. You may argue that there are a lot of things to take into account, especially with strong winds, and you are right. But, if your system is well set up, the drone will get back to you in the best case, and in the worst case, it will return with an offset based on how the wind moved the drone.

You can even go beyond and set up a computer vision system for your drone to retrace the path, taking into account all the obstacles present in its surroundings.

At a certain point, your drone will be out of the detection range of the Blader, and you can safely reconnect to bring it back.

### A Phone Call will be enough

Now that your drone is safely back, you can start thinking about another way to control it while being invisible to the Blader. The best possible option is to use another wireless system, maybe RF on frequencies never used before, or, why not, a creative solution like making a phone call. However, instead of talking, you can send commands encoded in sound waves!

That phone call could still be detected, but not by the Skyfend Blader since it will never expect your drone to be controlled by a common phone call!

## Conclusion

So, after all, we can conclude that nothing, especially in cybersecurity, is 100% guaranteed to work. You just read a clear example of it. That's why we need to be always on alert, ready to act before it's too late. Also, we need to keep up to date with the latest technologies like drones, which could pose a real and significant threat to security if we don't know what we are dealing with.

See ya!