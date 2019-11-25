---
title: "Ruthless Testing with Hypothesis"
layout: talk
body_class: talk
permalink: "talks/ruthless-testing-with-hypothesis"
about: 
abstract: "Let's face it: unit tests with only a few static cases are superficial at best. With Hypothesis, make your tests exhaustive and trustworthy! Explore the power of property-based testing, go beyond 100% coverage, and find the edge cases you haven't thought of."
type: talk
expected_length: 40min
intended_audience: Intermediate
speakers: Xavier Villaneau
---

## Talk Description
_Hypothesis_ is a Python testing library that specializes in generating wildly random input data for tests, in the hope of finding odd bugs. It additionally provides the tooling and the environment to make that testing easy and powerful.

This talk is for intermediate (or advanced) Python users who struggle to implement tests that feel thorough enough. I will be demonstrating what Hypothesis is capable of using a few examples, then go more into the details of its usage. Finally, I will show some of its other features.

## Part 1 — Introduction by Example

The first part of the talk is the longest, and its purpose is to hook in the audience. It does so by showing them a simple and seemingly harmless piece of code, and how Hypothesis finds some gnarly bugs in it:

    def extract_id(str_id: str) -> int:
        if str_id[0] == 'c' and str_id[1:].isdigit():
            return int(str_id[1:])
        return -1

The first few examples present the fundamental elements of an Hypothesis test: the `@given` decorator, strategies, and the `assume` function. Captured test output is used to demonstrate that Hypothesis uses many random values for its test input. These first tests do not fail, but they are useful to discuss the core ideas of the library.

The next examples are tests that fail, which means that we've found bugs! The first illustrates an edge-case bug (a crash on inputting the empty string). Interestingly, we found that edge case without writing an explicit test for it: Hypothesis automatically tested the empty string as part of its strategy system. 

The second failing example shows a much more obscure bug, this time a Unicode classification quirk. If we had used manual testing only, we would have unlikely found this bug. It's a good demonstration of how powerful the random data generation of Hypothesis is.

## Part 2 — The Hypothesis Manual, Abridged

This part summarizes the learning from the previous, albeit more formally. It lists the common API elements of Hypothesis and a few new ones.

I then go in the details of how Hypothesis handles test failure. In particular, I examine the _shrinking_ feature, where Hypothesis automatically tries to find the simplest failing case on failure. And I show how Hypothesis makes it easy to reproduce or ignore failing tests, even when randomness is involved.

Finally, I give some advice on how to write property-based tests. Such as how essential it is to write tests that have no side-effects! I also show some useful patterns to remember, such as invariant properties.

## Part 3 — Strategic Overview

This section is a straightforward overview of the tools for generating data provided by Hypothesis, known as _strategies_. In order, I show:

1. how to produce simple data types, such as numbers or strings;
2. how to make collections of objects, such as lists or dictionaries;
3. how to build more complex objects, like instantiating a class or a dataclass (automatically in some cases!);
4. how to create custom strategies with more complicated behavior;
5. if time allows it, how to make recursive strategies!

## Part 4 — The Bonus Features

This last and short section shows some of the other features of Hypothesis: Django support, pytest support, profiles, and stateful testing. The later is a broad topic and could be made into talk of its own, so I only give it a one-minute overview.

## Conclusion

I conclude by summarizing the strengths and features of Hypothesis. I also put it in the context of other forms of testing. I like to close the talk with the thought that Hypothesis is not a silver bullet that will replace all other tests, but a useful tool that shines at testing some particular pieces of software.

