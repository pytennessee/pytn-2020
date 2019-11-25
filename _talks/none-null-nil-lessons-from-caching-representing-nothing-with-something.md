---
title: "None, null, nil: lessons from caching & representing nothing with something"
layout: talk
body_class: talk
permalink: "talks/none-null-nil-lessons-from-caching-representing-nothing-with-something"
about: 
abstract: "`There are only two hard things in Computer Science: cache invalidation and naming things`. This talk is about the value of `nothing`. I will discuss the success of caching for app performance, but how at one point `nothing` took down production. Learn factors to consider when caching for APIs."
type: talk
expected_length: 30min
intended_audience: All
speakers: Felice Ho
---

## Talk Description
* Intro (1 min)

	- Speaker intro

	- Overview of talk: the topic, why, what you will learn

	- Inspiration for talk and goals

* The scenario: what, why, where, how of caching (6 min, 7 total)

	- What is a cache and cache invalidation

	- Why are we caching and how can it help you with app performance?

	- Where are are caching data and how can it be accessed?

	- How are we caching data?

* Factors to consider when caching data (6 min, 13 total)

	- API contract

	- API design: do we include null data

	- Options to store the data

		+ string, hash, hash fields (JSON via Redis pipelining and Lua)

		+ ReJSON - native JSON in Redis

	- How to invalidate / avoid stale data

		+ TTL, update process, null values, etc

* The problem with `nothing` (4 min, 17 total)

	- How nothing helps with cache invalidation

	- What is null?

	- Serialization of `nothing` is represented differently

		+ in Python, JSON, Lua, Redis

	+ ‘None’ is not same as None

* How did `nothing` take down production (2 min, 19 total)

* Lessons learned (2 min, 21 total)

* Wrap up / the value of `nothing` (2 min, 23 total)


**Audience Takeaways:**

* Learn about caching and how to handle the problem of cache invalidation

* Why null values can be important and how to handle when they are expressed differently (None, null, nil, etc)

* Learn how caching can help with app and database performance
    