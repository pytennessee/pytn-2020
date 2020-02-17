---
title: About PyTennessee 2020 Game Night
body_class: game-night
layout: base
permalink: game-night
---

<div class="game-night-hero"> 
  <img src="{{ site.baseurl }}/static/img/{{ site.data.event.game_night.image }}" alt="A colorized shot of the Nashville skyline with the text {{ site.data.event.short_name }} Game Night Presented by Built">
</div>

## {{ site.data.event.name }} Game Night Information

Over the past 4 years, the {{ site.data.event.short_name }} Game Night has become a staple of {{ site.data.event.short_name }}.
It's been such a hit in the past, we're bringing it back for another year.
So if you're looking for something to do with other {{ site.data.event.short_abbreviation }} attendees, join us on **Saturday, March 7 from 6-9pm** for {{ site.data.event.full_abbreviation }} Game Night!

_Please note this is a ticketed event and only 100 tickets are made available._

[Meeple Mountain](https://www.meeplemountain.com/) will provide all the table top games, {{ site.data.event.short_name }} provide the food and drink, and [Built Technologies](https://www.getbuilt.com/) is hosting and sponsoring the whole thing.
The only thing left is you!
And in addition to providing table top games to play, Meeple Mountain will also have a few prizes to raffle off to the attendees.

So once you've had your fill of Python for the day, come to Built and enjoy some table top games, then head out to wherever the night takes you!

<div class="flex-container venue-info" markdown="1">

- ### {{ site.data.event.game_night.name }} Venue
{% for line in site.data.event.game_night.address %}- {{ line }}
{% endfor %}- {{ site.data.event.game_night.time }}

{{ site.data.event.game_night.map }}

</div>
