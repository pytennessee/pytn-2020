---
title: "Everyday Design Patterns: Facade Pattern"
layout: talk
body_class: talk
permalink: "talks/everyday-design-patterns-facade-pattern"
about: 
abstract: "Developers spend lots of time writing code to integrate third-party packages and APIs into our project. We spend additional time updating systems when our dependencies change. This talk will demonstrate HOWTO leverage the Facade Pattern to hide complexity and isolate the impact of changes."
type: talk
expected_length: 30min
intended_audience: All
speakers: Aly Sivji
---

## Talk Description
Whether we realize it or not, we are making software design decisions when we integrate third-party libraries and APIs into our codebase. Directly integrating dependencies into business logic results in code that is brittle and difficult to modify. Changes made to upstream packages require us to update integration code across the project.

This talk will demonstrate how to use Object-Oriented programming principles, specifically abstraction and encapsulation, to isolate the impact of upstream changes. The material will be presented in the context of modifying code to handle an API version upgrade: we will walk through the initial implementation, discuss its limitations, and investigate how the Facade Pattern can improve software design.

The session is geared towards developers of all levels looking for a friendlier approach to Design Patterns. By applying the principles outlined in this talk, you will be able to utilize the Facade pattern to write robust code that is easier to maintain.

### Outline

- Introduction to topic and speaker (2 minutes)
- Design Patterns Introduction (3 minutes)
    - What are design patterns?
    - Benefits of patterns
    - Types of Patterns: Creational, Structural, Behavioral
- Case Study: Interacting with APIs (6 minutes)
    - Introduce problem -- downloading data from 3rd party API
    - Walk thru initial solution (direct integration)
    - API changes...!!! Changing our code is painful!
    - Aside: tests are complicated to write
- Object-Oriented Programming (OOP) (6 minutes)
    - High-level intro
    - Principles of OOP
    - Dive into encapsulation and abstraction
    - Encapsulation and abstraction in Python
- Case Study Revisited: Facade Pattern (10 minutes)
    - Adding a layer between the API and implementation enables changes to be isolated
    - Walk through the process of changing code to support new API
    - Show how facade pattern simplifies testing with fakes
    - Other examples of Facade pattern in practice: wrap Python libraries
- Closing (3 minutes)
    - Benefits of Design Patterns
    - Program to an interface, not an implementation
    - Don't get too hung up on diagrams and terminology
    - Focus on understanding the problem you are trying to solve
    