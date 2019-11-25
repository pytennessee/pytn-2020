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
### Python Execution (5m)

This will cover the basics of how Python source code is ran.
We will cover what is "byte compiling", what are "code objects" and how the byte code looks like.
Some examples of specific byte code, as well as the execution model, will be covered.

### The Frame Object (5m)

Python executes a "frame object".
We will cover what is a frame object, what it contains, and even how to analyze frame objects from within the Python interpreter.

### The Stack (5m)

Python evaluation is done on a virtual "stack machine".
We will introduce how the stack looks like, and what stack operations are supported.

### The Loop (5m)

The loop itself is a function called "PyEval_EvalFrameDefault".
It is divided into the prelude, and "the big switch": `switch(opcode)`.
The talk will show some snippets from the big switch, and relate them to the byte codes shown earlier.

Then we will talk about the things done in the prelude: the period-protection optimization, and how GIL release and signal handling are done.

### The "Predict" Optimization (5m)

Many times, operations come in pairs: for example, comparison and jump correpond to `if x == y`.
We will talk about how this is used to optimize execution, and when the optimization is disabled.

## Summary (5m)
Cover specific action-items:
understanding how performant Python will be.
A few examples of mindful optimization.

    
