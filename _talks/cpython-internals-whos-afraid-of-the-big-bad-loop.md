---
title: "CPython Internals: Who's Afraid of the Big Bad Loop?"
layout: talk
body_class: talk
permalink: "talks/cpython-internals-whos-afraid-of-the-big-bad-loop"
about: 
abstract: "The heart of the CPython implementation is the so-called \"ceval\" loop. This is the loop that runs the Python bytecode. The talk will explain the basics of the CPython execution model, and then cover the details of how the eval loop is written, as well as some of the interesting optimizations it has."
type: talk
expected_length: 30min
intended_audience: All
speakers: Moshe Zadka
---

## Talk Description

The talk will cover the internals of the CPython so-called "ceval" loop:
how the reference implementation of Python,
commonly called "CPython",
evaluates the Python code we love to write.

In order to properly understand the loop,
we will build some background on the Python execution models:
the structure of byte code,
what is a stack virtual machine,
and what are execution frames.

Then we will delve into a series of white lies:
the source code that is *not* the source code of the ceval loop,
but would have been if performance optimizations would not have made it hard to read.
How does the big switch work?
How does signal handling work?
What about the boogey man we tell all little kids about,
the Global Interpreter lock?
    
