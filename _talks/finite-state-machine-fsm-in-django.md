---
title: "Finite State Machine (FSM) in Django"
layout: talk
body_class: talk
permalink: "talks/finite-state-machine-fsm-in-django"
about: 
abstract: "Our everyday life is full of workflows such as requesting time off from work. Many of these are actually Finite State Machines. Popular CMS tools have rich support for workflows, but now with django-fsm we can build quick, lightweight business workflows for our applications."
type: talk
expected_length: 30min
intended_audience: Intermediate
speakers: Calvin Hendryx-Parker
---

## Talk Description
Workflows are super powerful tools for automating business processes online. Our everyday life is full of workflows such as requesting time off from work. Many of these are actually Finite State Machines that move from state to state via transitions. Popular CMS’ such as Plone have rich support for workflows, but now with `django-fsm` we can build quick, lightweight business workflows for our applications. Plus, we have full audit logging and even build visualizations of our workflow to confirm with the business owners generated from the code.

# Talk Outline

## Overview

- Business rules:
    - Students submit a request for program change for review
    - Physicians submit a case study for review
    - Tax Payers submit personal property tax return forms for review
    - Users want to share information with only specific users
- Questions:
    - What is the status of the object?
    - Who should be allowed to action the item next?
    - Which transitions can the object go to next?
- Out of the box in Django, everything is public or private, depends on your views
- One way: encode into the model and your views the logic to handle this
    - How:
        - Make a checkbox to determine if an item should be public
        - Modify your views to view items based on the data
    - Issues:
        - Rules around transitions can’t be enforced (e.g. private > pending > published)
        - Managing rules per user will require additional code
            - You end up with spaghetti code!
        - And the code is so custom you can’t reuse it for another project
- A better way: workflows using FSM

## Workflows and Transitions

- Modeling real life
    - Graphviz
    - Draw.io
- States, Transitions, Variables
- Meet FSM…

## Getting Started with FSM

- Installation
- Code examples
- RapidScience case study in action
- Tips and Tricks

## Questions

    