---
title: About the Venue
body_class: venue
layout: base
permalink: venue
---

<div class="venue-hero">
  <img src="{{ site.baseurl }}/static/img/venue.jpg" alt="A view from just outside the front door, looking at the venue parking lot">
</div>

## {{ site.data.event.name }} Venue Information

The {{ site.data.event.venue.name }} has played host to {{ site.data.event.short_name }} since
the beginning, and we're excited to return to the NSL again this year!

{{ site.data.event.venue.description }}

<div class="flex-container venue-info" markdown="1">

- ### {{ site.data.event.venue.name }}
{% for line in site.data.event.venue.address %}- {{ line }}
{% endfor %}- <{{ site.data.event.venue.url }}>

{{ site.data.event.venue.map }}

</div>
