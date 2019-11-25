---
title: "How to Stop Worrying by using Transactions and Exceptions"
layout: talk
body_class: talk
permalink: "talks/how-to-stop-worrying-by-using-transactions-and-exceptions"
about: 
abstract: "We've all got that crazy set of database updates that need to land successfully in four tables, but what do we do when they fail? Join me as I toss aside the deep theory and step into the dark and very real world of transactions, exceptions and debugging SQL."
type: talk
expected_length: 30min
intended_audience: All
speakers: Jason Myers
---

## Talk Description
Learning to use transactions can greatly help to coordinate database work so that you can ensure that distributed updates are fully successful and rollback when they fail. Often this is surrounded by a bunch of theory, and you're not exposed to debugging and handling these exceptions. We'll explore nested transactions, graceful fallbacks, and SQL debugging in PostgreSQL. While we'll be focusing mostly on SQL, we'll also take a look at how you can coordinate these techniques with Python and distributed services as well.
    