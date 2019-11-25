---
title: "Multiply your Testing Effectiveness with Parameterized Testing"
layout: talk
body_class: talk
permalink: "talks/multiply-your-testing-effectiveness-with-parameterized-testing"
about: 
abstract: "Parametrization is one of the superpowers of pytest. It allows you to cover a huge number of test cases with a single test function. This speeds up test writing and makes test maintenance easier. This talk is a medium depth dive into pytest parametrization, with techniques you can use right away."
type: talk
expected_length: 30min
intended_audience: All
speakers: Brian Okken
---

## Talk Description
There are many reasons I want to give this talk:

* parametrization makes test suites easier to maintain
* it's under-utilized
* there are many ways to do it, but people often learn one way and stop there
* it seems advanced, but it's not, really.

Code examples and discussion take up most of the rest of the talk.
These are all simple transitions from one form to another, but leaving up
the code and going kinda slow through each stage makes it easier to digest.


Outline:

* Value of tests. (3 min)
   * Importance of automated test suites in the context of a version control driven Continuous Integration pipeline.
   * There seems to often be this desire for a "why should I care about testing" portion for testing talks. 
   * This will be short, as it's not the focus of the talk.

* Starting test (3 min)
    * Simple tracer bullet style single test case test function
    * Reasons for starting with a tracer bullet test.
    * show a pre-canned demo run of test flow.
* Splitting off setup and teardown (4 min)
    * Simplify the test by pushing setup and teardown into fixtures.
    * Will necessitate a brief explanation of fixtures. But that's not the focus of the talk, so I'll include links to further info.  
    * show a pre-canned demo run of test flow.
* Same test case as a parametrized test (3 min)
    * discuss the syntax and mechanics
    * show a pre-canned demo run of test flow.
* Add more test cases (3 min)
    * show a pre-canned demo run of test flow.
    * discuss mechanics more 
    * talk about test case selection
* Fixture parametrization (4 min)
    * move the parametrization to a fixture
    * discuss syntax and mechanics
    * when would you use this over function parametrization
* pytest_generate_tests (4 min)
    * move the parametrization to pytest_generate_tests
    * discuss syntax and mechanics
    * when would you use this over others
    * warn people about the limitations
* review (4 min)
    * different methods covered
    * when they are run
    * reasons to use one over the others
* resources for further exploration (2 min)
    * will just leave this up at end of talk as part of thank you slide

    