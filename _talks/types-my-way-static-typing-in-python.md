---
title: "Types my way: Static typing in Python"
layout: talk
body_class: talk
permalink: "talks/types-my-way-static-typing-in-python"
about: 
abstract: "For some time, there has been significant discussion in the Python community about the use of static typing. There are now options for developers who enjoy strongly typed languages but also enjoy the flexibility of duck typing in Python. Please join me as we explore Mypy, type hints and annotations."
type: talk
expected_length: 30min
intended_audience: Intermediate
speakers: Joe Cabrera
---

## Talk Description
All programming languages include a type system that formalizes the category of objects it can work with and Python is no different. While many developers enjoy the flexibility of duck typing, it can lead to guessing types at runtime. Static typing helps document your code, improves linting and aids in building cleaner architectures. Though runtime type checking most likely will never be natively supported in Python, there are third party tools such as type checkers, linters and IDEs that do support it.

This talk will show the basics of type hints and annotations and delve into the use of Mypy as a type checker. Since many times you cannot add type hints unilaterally to an entire codebase, I’ll also introduce the concept of gradual typing. Finally, we will look at some of the trade-offs of static type checking and discuss the future of static typing in the Python language.

    