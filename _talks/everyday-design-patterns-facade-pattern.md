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

