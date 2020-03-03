---
title: Homebrew Hacking
layout: talk
body_class: talk
permalink: talks/homebrew-hacking
about: 
abstract: "It's not hard to find an IoT device for every hobby. Part of the fun of being a maker/tinkerer is taking something apart and finding out how it works. The problem in general is fragmentation of information. Every \"pane of glass\" is narrow and doesnt work with other views/tech. Homebrewing is no different."
type: talk
expected_length: 30min
intended_audience: All
speakers: Marc Young
---

It's not hard to find an IoT device for every hobby.
Part of the fun of being a maker/tinkerer is taking something apart and finding out how it works.

The problem, however, is fragmentation of information.
Every "pane of glass" is narrow and doesnt work with other views/tech.

Homebrewing is no different.
In this talk I'll dive into how I took two devices that have nothing to do with each other and worked towards understanding their payloads in a way I can control.
The first is a bluetooth device that measures gravity of beer during fermentation (or the sugar measurements that let you know how fermentation is going)--called a hydrometer--and capturing them, parsing them, and moving them into a controlled dashboard (Datadog in this example).

The second will be a walk-through of how I use "hacking techniques" (DNS spoofing, man-in-the-middle, etc) to capture and try to understand the workflow of a smart-keg scale so that at some point we could remove the companies cloud-provider from the equation and control/submit that data to the same dashboard as our hydrometer.
