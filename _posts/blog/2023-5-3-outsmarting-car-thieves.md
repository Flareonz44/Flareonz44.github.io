---
layout: post
title: "Outsmarting car thieves"
author: Flareonz44
tags: [security, social-eng, electronics]
metadesc: "Car thefts are everywhere, but with there are some ways to outsmart them."
---

![man robbing a car](/images/2023-5-3-outsmarting-car-thieves/banner.png)

## Intro

Unfortunately, thefts are a frequent occurrence in most Latin American countries. Every day, the news reports show new videos of cars or valuable possessions being stolen by thieves. However, I recently came across an intriguing video that caught my attention and gave me an idea on how to outsmart these car thieves.

## Analyzing the video

So here is the video:

<video width="100%" height="315" controls>
  <source src="/images/2023-5-3-outsmarting-car-thieves/video.mp4" type="video/mp4">
</video>

As you can see in the video, the thieves' behavior is almost identical among them: they try to steal the car as quickly as possible, taking advantage of the victim's shock and leaving no time to react. By the time the owner tries to do something, the thieves are often gone. However, in this particular case, something went terribly wrong for the thieves: they didn't know how to start the engine, which prevented them from driving away with the car.
Most car models operate in a similar manner, making it easy for people to transfer their driving skills from one car to another. However, there are exceptions, such as this particular car, which requires additional steps to start the engine.
In the end, the thieves were caught by the police due to the difficulties they encountered with the car.

## Walkaround

After 1995, most car manufacturers implemented a new technology in car keys known as "transponder keys". They work similarly to RFID technology, as they contain a microchip that communicates with an antenna near the ignition switch. When the key is inserted into the ignition and turned on, the microchip receives power from the antenna's radio frequency field and sends its unique serial number back to the car's electronic board. If the serial number matches the one set by default, the engine can be started.
However, if the key or its serial number does not match, the car will not start.
If your key model has a separate microchip, you can modify it to extract the microchip and create an "access card" to start the car. This involves creating a socket near the switch and inserting the access card there whenever you want to start the car. This modification will prevent thieves from stealing your car, as they won't know about this previous step.
For key models that have a circuit board holding the RF chip, you can extract the entire circuit and keep the empty key. You can cover the circuit with opaque tape or a plastic or recycled metal case to protect it. Then, you just need to keep that PCB near the switch (again you can create a socket for it).
If you want to make something more elaborate, you can clone the serial number from the key with tools like Flipper Zero and use open-source boards to create a Bluetooth car locking system with your smartphone. The possibilities are endless.

## Final thoughts

Probably, this isn't the only solution to this problem, and it may not completely prevent car thefts. However, it could potentially help save your car from being stolen. I hope this post is useful to someone. Take care!