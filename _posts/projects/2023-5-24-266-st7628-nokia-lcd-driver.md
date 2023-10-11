---
layout: post
title: "ST7628 LCD driver library for ESP8266"
author: Flareonz44
tags: [electronics, coding]
metadesc: Use your old Nokia LCD Screen with your ESP8266.
---

Found the code on my [GitHub](https://github.com/Flareonz44/8266_ST7628-Nokia-LCD-Driver)!

## About

So one day, I found my old Nokia 1600, and sadly, it was no longer functional. I never knew why because the battery still worked (now powers a custom wireless mouse :P). However, I had a clever idea to a new project with my ESP8266.

I began searching the internet but found very little information, mainly because no one had thought of this before. The only person who had developed a library for interfacing with the device was [Tapia Flavio](https://github.com/kr4fty/ST7628-Nokia-1600-LCD-Library), but it was designed for Arduino, not ESP.

Initially, I considered creating my own version of the library. This led me to research how LCDs work and how to effectively communicate with them.

I discovered that these devices operate in a super interesting and somewhat complex way. Some use SPI communication, while others use I2C. These types of LCD screens often support both modes, resulting in 10 pins required for communication. Fortunately, I found that some devices only needed 4 or 6 pins to function. I searched for the datasheet of my particular LCD screen and found myself spending two hours trying to decipher 118 pages of pure digital electronics. Quite a challenge.

Although it was fascinating to understand how the device worked, I decided to go forward with a solution. I opted to port the Arduino code to ESP, which wasn't too difficult because the code was almost identical, requiring only a few modifications to make it compatible with ESP.

However, I realized that there was no way for me to physically test my code. Connecting the LCD to my ESP was impossible since I lacked the proper connector, and direct soldering wasn't an option. Anyway, I must say that I learned a lot during this journey.

## Wiring and procedure

![wiring diagram](/images/2023-5-24-266-st7628-nokia-lcd-driver/1.png)

It's not very difficult, just connect everything to the ESP, and it should work. Pay attention to the pins, especially when it comes to SPI, as you have the option to use either hardware SPI or software SPI, and a wiring error could result in undesired results.

Keep it real!