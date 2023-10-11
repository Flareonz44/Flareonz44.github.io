---
layout: post
title: "An engine for Beyonder: Mars Research"
author: Flareonz44
tags: [3d, BeyonderMR, coding, portfolio, videogames]
metadesc: "A little timeline showing all the game engines I used before for my game Beyonder: Mars Research"
---

![game landscape](/images/2023-6-28-an-engine-for-beyonder-mars-research/banner.png)

This is \*hopefully\* the last engine switch for my game, Beyonder: Mars Research. Let's go back in time and let me tell you about all the changes this game has undergone. The original idea was to create a 2.5D game with some sort of procedural generation. How did it end up as a 3D, almost-infinite game?

## Game Maker Studio
### 2.5D

<img src="/images/2023-6-28-an-engine-for-beyonder-mars-research/1.png"
     alt="2.5D game"
     width="30%"
     style="float: right; margin-right: 10px;"
     class="responsive-image"/>

After I released [my first game](https://windfallgamestudio.itch.io/kuzgakais-dungeon) made with Game Maker Studio, I was completely set on using the same engine for my next game since I got used to it. I drew inspiration from [The Martian](https://www.imdb.com/title/tt3659388/) starring Matt Damon, and my plan was to create a top-down game centered around exploration and resource gathering, maybe with an engaging backstory. At first, the game appeared quite promising. I even implemented a basic sun shadow system. However, there was a major issue. Technically, the game was infinite but not linear. Whenever you reached the right side of the map, you would be 'teleported' to another chunk, causing a temporary pause in the game. The problem was that all the chunks were random, yet they ended up being nearly identical most of the time. It became monotonous within just five minutes, and I desired a more immersive experience.

### 3D

<img src="/images/2023-6-28-an-engine-for-beyonder-mars-research/2.png"
     alt="3D game"
     width="30%"
     style="float: right; margin-right: 10px;"
     class="responsive-image"/>

"No way, 3D is the best option," I said. While Game Maker Studio 1.4 technically supports 3D, it only allows simple shapes and lacks the capability for complex things. I decided to give it a try, but it required long hours research to understand how to make it work. Texturing and model loading caused me some headaches. Moreover, collision detection was a complete nightmare to figure out.
Despite these difficulties, the limitation to just one chunk persisted. Since my coding skills were still in the early stages of development, some techniques like dynamic chunk loading and generation seemed like Greek to me. Eventually, I decided to abandon Game Maker Studio.

## Interlude

I decided to stick with 3D, but finding the perfect engine was quite a challenge. I didn't want to go for Unity or Unreal because they're pretty heavy-duty (I mean, will a Core 2 Duo support UE5? ). My game dev philosophy is about creating games that everyone can enjoy, regardless of their computer specs. So, I was looking for something lightweight and easy to use. I gave CopperCube, UE2, Construct, Cocos, and Tree.js a shot, but none of them convince me. Until I discovered Panda3D.

## Panda3D

<img src="/images/2023-6-28-an-engine-for-beyonder-mars-research/3.png"
     alt="3D game with panda"
     width="30%"
     style="float: right; margin-right: 10px;"
     class="responsive-image"/>

Panda is almost perfect. It has bindings for Python 3, and that is awesome. I learned programming with Python, and the idea of making games with it really caught my attention. After some attempts, I managed to display basic shapes, and after a week, I decided to start the development of a game. I used this engine for about 8 months, and to be honest, it is very powerful. You can do thousands of things in 2D and even 3D. It's an incredible game-making engine, and it is very easy to use. It includes some basic lighting and physics simulation with Bullet, and its node-based organization is very useful to understand how the engine and objects are organized inside the game.
However, there's one problem: speed. Python is an interpreted language, and therefore, it is slower compared to C or C++. Due to this limitation, I made the decision to drop Panda3D. Just to give you an idea, generating one chunk took 3 seconds. Initially, I had to generate about 88 chunks, and then 15 each time you walked some meters. The most efficient way to complete the generation was to run each chunk generation in a different thread. Using this method, generating 88 chunks took 7 seconds on a Ryzen 5 and about 17 seconds on a Core 2 Duo. The main issue here is that rendering time highly depends on the computer's performance, which goes against my philosophy.
After some research, I discovered what I believe to be the best library for me: Raylib.

## Raylib

<img src="/images/2023-6-28-an-engine-for-beyonder-mars-research/4.png"
     alt="3d game with raylib"
     width="30%"
     style="float: right; margin-right: 10px;"
     class="responsive-image"/>

Something that I complained about in previous C/C++ engines is that the installation and setup process was very difficult, but this is not a problem with Raylib. It provides an installer, but the installation process is simply placing the Raylib folder in your main drive directory (e.g. C:), setting up some variables and that's all! I started the porting process about two weeks ago, and I have to say that I feel very comfortable with it. It's super easy-going. Although I had to make some conversions from Python to the C coding style, everything else was pretty straightforward. At the time of writing, I have successfully finished the terrain generation and dynamic chunk loading.
The only thing that I missed from Panda3D is the built-in collision detection system, something that Raylib lacks. But that's okay because it forced me to learn and read some online blogs to find an efficient collision detection system. I'll talk about that in the next post, so stay tuned!

## Next steps

As I mentioned before, I have to create my own collision detection engine and then implement it in the game. Additionally, I need to reorganize the noise layers for the terrain to improve its appearance. Porting the UI elements will be challenging, but hang on! It's Wednesday morning, and I need to refill my coffee mug. See you later!