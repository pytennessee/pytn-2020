---
title: "How To Host A Podcast For 25 Cents A Month"
layout: talk
body_class: talk
permalink: "talks/how-to-host-a-podcast-for-25-cents-a-month"
about: 
abstract: "When I decided to host a podcast, it was all new to me, so I did everything manually. Then I remembered I was a Python engineer. This talk is a practical guide of how to host your own podcast using Python and AWS to save money, time and own your listener data."
type: talk
expected_length: 30min
intended_audience: All
speakers: Michelle Brenner
---

## Talk Description
Want to host a podcast, but didn’t know where to start? I have the answers!! Last year I launched From The Source, where I interview unsung people in tech with amazing stories. Hosting involves 3 major components; an XML file with episode details, mp3 storage, and metrics on your listeners. In this talk, I’ll go over all the AWS tools and Python scripts I used so I could own my data and not incur hefty hosting fees. 

During this talk, I will be creating a fresh podcast from scratch, with only a few pre-prepared items like any good cooking show. Together we’ll upload the MP3 file to S3 and then create an XML file for the RSS feed and upload that as well. You can then pull the RSS feed onto your phone using any podcast app and download the episode. After we download the episode, we can parse the S3 logs using Athena to see who has been listening. And finally, I’ll show you a bonus script that helps with the worst part of hosting a podcast, editing. 

At the end of the talk, all you’ll need to worry about is which story you want to tell on your own podcast.
    