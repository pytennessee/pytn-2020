---
title: "Introduction To MicroPython"
layout: talk
body_class: talk
permalink: "talks/introduction-to-micropython"
about: 
abstract: "If you’ve ever wanted to get down to the bare metal your code is running on, come learn about the wonders of MicroPython, an implementation of CPython that makes embedded device development accessible to anyone with basic Python knowledge. Your next hobby project starts here!"
type: talk
expected_length: 30min
intended_audience: All
speakers: Sara Topic
---

## Talk Description
Description
===========
I envision the talk taking up 25 minutes, which leaves 5 minutes for questions. The sections vary in length and complexity so I've included an approximate minute count next to each section.

### 1. Why MicroPython Is Cool (3 minutes)
----------------------------------------

Most of us have a general idea of where our deployed code is running - either a physical server nearby, or more likely, a server farm we’ve never been to. But what if there was a way to get down to the bits with our code? We expect to be able to do this easily with certain programming languages, like C/C++, but the fact that we can do it in Python is surprising - Python is known for its backend server and data processing abilities, and conveniently abstracts out much of the low-level hardware design knowledge. 

Enter MicroPython, an implementation of Python 3 designed to run on microcontrollers. Of course, in real-world embedded systems you’d use one of the traditional languages, but MicroPython isn’t designed to save lives or track missiles, it’s just here to have a good time, which makes it the perfect tool for hobbyists and beginners because we can dig into the world of embedded systems without having to cobble together C code.

### 2. Hardware 101 (5 minutes total)

----------------------------------------

#### Hardware basics (2 minutes)
We’ll start by reviewing a few hardware basics, on a need-to-know basis for MicroPython development. A microcontroller is a small computer that lives on an Integrated Circuit (IC), more commonly referred to as a “chip” and is made up of several parts: 

* CPU - Processes the input it receives and performs the specified actions -- this is where our instruction set (based on the architecture) is defined 
* RAM - Provides storage for data we want to be able to store temporarily and perform I/O operations on quickly 
* Flash - Provides storage for data we want to save even when the microcontroller loses power, with slower I/O capabilities 
* Serial Bus Interface - Provides a capability for serial communication (read: sending data bit by bit). Examples of Serial Bus Interfaces you may have heard of include SPI and I2C
* I/O Ports - How the microcontroller connects to the rest of the world. Examples of input ports are buttons, switches, and sensors. Examples of output ports are LEDs and speakers.

#### Choosing Hardware (1 minute)

Now that we know the basics of hardware, we'll take a look at the specs for some microcontrollers that we could port MicroPython to. 


    | board | CPU | RAM (KB) | Flash (MB) | GPIO pins | 
    |---------|---------------------------------------------------|----------|------------|-----------| 
    | pyboard | 168 MHzCortex M4 CPU with hardware floating point | ~192 | ~1 | 31 | 
    | WiPy | Dual processor + WiFi radio System | 256 | 2 | 25 | 
    | ESP32 | Dual-core Tensilica LX6 microprocessor | 520 | 4 | 28 | 


#### First MicroPython Example

We’ll start with a basic example of turning on an LED, using the pyboard's `pyb` module.

    from pyb import LED 
    led = LED(1) # 1=red, 2=green, 3=yellow, 4=blue 
    led.on() 

Here's what some equlivalent code we might write in C++ and run on an Arduino (another microcontroller) would look like. While neither sample is very long, the python code (as we would expect) reads more intuitively and eliminates the need to compile and re-compile our code every time we make a change. 

    int ledPin = 13;                 // LED connected to digital pin 13
    
    void setup()
    {
        pinMode(ledPin, OUTPUT);      // sets the digital pin as output
    }

    void loop()
    {
        digitalWrite(ledPin, HIGH);   // sets the LED on
    }

### 3. Micropython v. CPython (7 minutes total)
----------------------------------

#### Development (3 minutes)

We've looked at some of the cool things we can do with MicroPython, now let's look at how it compares to CPython. 

*    MicroPython is an implementation of Python 3.4 and implements some features of 3.5. When MicroPython does differ from CPython, it's most likely because it was optimized for memory usage (remember there's only about a few hundred KBs of RAM on any of the devices we might run MicroPython on)  
*    One feature that MicroPython does not support is user-defined attributes for builtin exceptions, so something like 

    e = Exception()
    e.x = 0
    print(e.x)

would not be supported.

*    Another difference and potential _gotcha_ is that imported modules that failed to load still get registered as loaded, because module handling is more efficient when it isn't wrapped in exception handling. For the example code 
  
    import sys
    try:
        from modules import foo
    except NameError as e:
        print(e)

    try:
        from modules import foo
        print('Should not get here')
    except NameError as e:
        print(e)

MicroPython will output

    foo
    name 'xxx' isn't defined
    Should not get here

Luckily, MicroPython docs do a good job of providing workarounds to omitted features, so they shouldn't limit development. 

#### Compiling & Porting (4 minutes)

In my opinion, the coolest difference between CPython and MicroPython is the way they are compiled and ported. MicroPython's features include a native emitter that targets machine code directly rather than the bytecode virtual machine. Why is this so cool? Well, normally Python code is converted to bytecode (you may have noticed `.pyc` files that get generated when you run Python code, these are the bytecode instructions that will get executed by the virtual machine when your code runs). The same python `.py` file will always generate the same `.pyc` file content, regardless of the architecture it is run on. The bytecode then needs to be interpreted to machine code - which is dependent on the architecture you are running. This is why we say that Python is "interpreted" because it has already been compiled and now it has to be interpreted to machine code.

On the other hand, in MicroPython, we know which hardware we are targeting before we start writing any code -- so no interpreting is necessary and can go straight from python code to machine code. That’s what we mean when we say we are running code on "bare metal!" 

### 4. pyboard Libraries (5 minutes total)

----------------------------------------

#### Setting Up (1 minute) 


We'll now demonstrate some more examples of the pyboard in action. I will make it clear that a pyboard is just one of the options available for running MicroPython, and that any of these examples could be ported to a different microcontroller with minimal effort. 

I'll begin with a short screencap video showing the process of booting a pyboard on Mac (basically, just opening the `PYBFLASH` folder and opening `main.py` for editing). I'll also show how to get a REPL prompt in a terminal window, which will allow us to see the output of any `print` statements in our script.

For the following examples I'll show a code sample (just a few lines, enough to be visible on screen) alongside a video of the code running on a pyboard.
 

#### Accelerometer example (1 minute)


    accel = pyb.Accel()
    light = pyb.LED(3)
    SENSITIVITY = 3
    
    while True:
        x = accel.x()
        if abs(x) > SENSITIVITY:
            light.on()
        else:
            light.off()

        pyb.delay(100)

I'll explain what an accelerometer is (a device that can detect the angle and motion of the board), and why the `SENSITIVITY` variable is necessary (the  accelerometer is very sensitive).


#### Touch Detection and LCD screen example (1 minute)


At this point I'll introduce the LCD160CR display, a component that attaches to the pyboard. MicroPython provides an LCD160CR library that makes interfacing with the display simple. 

    import time
    import pyb
    import lcd160cr

    lcd = lcd160cr.LCD160CR('X')
    lcd.set_text_color(lcd.rgb(255,255,255), lcd.rgb(0,0,0))
    lcd.set_font(0,2,1,0,0)
    prev_touch = False
    while True:
        curr_touch = lcd.is_touched()
        if (curr_touch != prev_touch):
            lcd.erase()
            lcd.set_pos(10,10)
            if (curr_touch):
                lcd.write("Touch!"")
            else:
                lcd.write("No touch!")
        sleep(0.1)

This example program will display a message based on whether or not the screen is touched. We track the previous state because otherwise we would have to clear and write to the screen in every iteration of the loop, which would show a flash on the screen when the message hasn't changed.  I'll briefly explain how the `lcd` library functions make setting font simple and the video will demonstrate how responsive the screen is to touch. 


#### Tic-Tac-Toe example (2 minutes) 


 I'll show a demo of a tic-tac-toe game I wrote for the pyboard (example video [here](https://vimeo.com/306583799)). The source code for this project was about 200 lines so I won't go into detail but will give an overview of how the flow control breaks down and struggles I had in creating it (like detecting touch and drawing the letters with the few pixels I had to work with).
 

### 5. Conclusion (5 minutes) 


We'll reiterate that MicroPython gives Python developers the unique ability to run their code on bare metal and explore embedded device development, without having to learn a hardware description language or mess around in C, leaving five minutes to take questions
    