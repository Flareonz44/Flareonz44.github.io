---
layout: post
title: "COD4MW Cheat: A Reverse Engineering Adventure"
author: Flareonz44
tags: [reveng, hacking]
type: project
metadesc: How I made a esp-cheat for Call of Duty 4 Modern Warfare in C++
---

## About game cheats

If you enjoy playing online games, you've probably heard about cheaters. People tend to have a negative perception of them, and they're somewhat right. Cheats can ruin the online gaming experience, but they can also be an interesting way to learn about reverse engineering.

For those who have never heard of cheats, here's a brief summary. Think about first-person shooters like Fortnite, Counter-Strike, or Valorant. These games are highly competitive, requiring quick reflexes and strategic thinking to outsmart other players and win the round. For example, if you're hiding, waiting for an opponent to come around a corner so you can take them by surprise, you have a plan. It works because the other player can't see you behind the wall. But what if they could? Your plan would be foiled, and you'd be killed before you could react. Essentially, a game cheat allows you to not only see through walls but also shoot instantly, make auto-headshots, gain extra experience, find better loot, and much more. The possibilities are limitless.

## How it works

Here is a video using the cheat I made:

<iframe src="https://drive.google.com/file/d/179xpsCqiiAdhf9w8YimZ-chZsu33zzBX/preview" width="640" height="360" allow="autoplay"></iframe>

I'm going to talk about ESP cheats, short for **E**xtra**S**ensorial **P**erception. As the name suggests, it's a cheat that allows you to perceive the positions of other players on the map, enabling you to predict their movements easily. But how does it work?

To play the game, your computer must create a virtual world where each object is placed. These objects are rendered on the screen following Euclidean geometry and the principles of perspective world projection. This means the virtual world behaves like the real one, with objects appearing from the farthest to the nearest, making distant objects more likely to be obscured, for example, by a wall in front of them. Each of these objects stores information in your computer's RAM memory, holding variables like position, rotation, texture, animation, color, and more.

In games, each player should be displayed on the screen based on their distance relative to the main player's camera. To do this, there must be a set of variables holding the players' data. This is where cheats come into play. The cheat reads the RAM memory, looking for player data, retrieves their positions, and displays them on the screen, making it easy for the user to track their movements.

But that's just an overview because cheats involve reverse engineering, mathematical calculations, and a lot of time. To retrieve the data, you first need to manually study and analyze the game's memory. Tools like [Cheat Engine](https://cheatengine.org/) can make this task faster. You must think like the game's developer and reverse-engineer the game's structure. If I were the developer, I'd likely organize all the game entities (players, dynamic objects, animals, etc.) into one list for easy retrieval. Inside memory, a list consists of all the data one after another, and if they follow a logical structure (for example, the position represented by X, Y, and Z variables), it becomes easier to access them. There's also a tool called [ReClass.NET](https://github.com/ReClassNET/ReClass.NET) that help me a lot with the dynamic memory analysis.

Once you've organized the data for easy access, you can write basic memory read/write functions in C++ to perform the data gathering. After that, you can proceed with creating the cheat's interface. I kept mine simple since it was for personal use. I used DirectX9 to draw lines, text, and menus in a png-like window that places over the game window, like and overlay. However, it's not that straightforward. You need to consider perspective, so you must first gather crucial information, such as the camera position, scaling, aspect ratio, and the Transformation Matrix, which, through mathematical calculations, from memory, so you can determine the screen position of any object within the 3D world.

With all this in place, you're ready to compile and launch your cheat to test it.

I know it's easier said than done. I spent at least 26 hours trying to understand how the 3D engine works. But in the end, it was worth it. I learned a lot about software reverse engineering, Windows security, and its architecture (x86 assembler really tested my limits).

## how to use it

Just run it, and use the [Insert] key to open up the menu and set it up as you want. You can find the compiled versions inside the build directory, but if you prefer you can build it yourself. I used Visual Studio 2015.

Here's a link to the [GitHub repo](https://github.com/Flareonz44/COD4MW-ESP-Cheat) of the sln project.

Cheers!