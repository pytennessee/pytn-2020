---
title: Hotel Information
body_class: hotel
layout: base
permalink: hotel-info
---

## {{ site.data.event.name }} Hotel Information

{{ site.data.event.hotel.description }}

<div class="flex-container hotel-info" markdown="1">

- ### {{ site.data.event.hotel.name }}
{% for line in site.data.event.hotel.address %}- {{ line }}
{% endfor %}- {{site.data.event.hotel.phone}}
- *Make your reservation*: <{{ site.data.event.hotel.url }}>

</div>

{{ site.data.event.hotel.map }}
