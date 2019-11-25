---
title: "Optimizing Your Machine Learning Model For Production"
layout: talk
body_class: talk
permalink: "talks/optimizing-your-machine-learning-model-for-production"
about: 
abstract: "This talk will cover how to optimize your machine learning model for production. Learn the tradeoffs between choosing models for accuracy versus performance and how to optimize post training by adopting software engineering best practices."
type: talk
expected_length: 40min
intended_audience: Intermediate
speakers: Stephanie Kim
---

## Talk Description
From choosing your machine learning model to deciding how to process the data you'll make inferences on, there are many places in your data science pipeline where you can optimize for performance. Sometimes you'll have to make trade-offs between accuracy and performance, while other areas you can optimize are outside of the model and utilize software engineering best practices.

While there is an overwhelming amount of information about how to optimize your machine learning model for accuracy, figuring out performance gains in regards to speed is harder to find, but just as important.  

When it comes to model selection, sometimes choosing a pre-trained optimized model is the best solution, especially when deploying your model on edge devices where performance matters the most. While in other use cases, you might need to balance performance for the highest accuracy you can achieve. This is where the optimizations for performance come down to software engineering best practices and cutting edge ideas developing faster neural nets.

The tradeoff is up to you and your use case, but there are many tricks you can use across the board: 
* Utilizing concurrent code practices when and where it makes sense
* Getting out of the habit of using data frames
* Caching serialized models for faster loading
* Understanding when it makes sense to use GPU's versus CPU's
* What is an ablation study and can it help you produce a faster model?

We'll cover these and other tips and tricks so you'll walk away understanding how you can make your machine learning models faster in production for various use cases.
    