
exemple_search_params='{\n  "checkin": "2023-11-05",\n  "checkout": "2023-11-07",\n  "group_adults": 3,\n  "no_rooms": 2,\n  "group_children": 2,\n  "age": [5, 7],\n  "price": "none",\n  "city": "Cairo",\n  "country": "Egypt",\n  "class": "5"\n}'


#Note you can use print(BeautifulSoup(Hotel_descritpion, "html.parser").prettify()) to see the html code
exemple_hotel_div_content = '<div class="c066246e13 d8aec464ca" data-testid="property-card-container"><div class="a5922b8ca1"><div class="e952b01718 a3f1b35606"><a aria-hidden="true" data-testid="property-card-desktop-single-image" href="https://www.booking.com/hotel/eg/the-muse-inn.en-gb.html?aid=304142&amp;label=gen173nr-1FCAQoggJCEnNlYXJjaF9jYWlybyxlZ3lwdEgJWARojAGIAQGYAQm4ARnIAQzYAQHoAQH4AQOIAgGoAgO4AriLiqoGwAIB0gIkYWZjNmM0ZmMtZTljMC00YmU4LWJlMWItMjJjOTAzMTgzMDJl2AIF4AIB&amp;ucfs=1&amp;arphpl=1&amp;checkin=2023-11-01&amp;checkout=2023-11-07&amp;group_adults=3&amp;req_adults=3&amp;no_rooms=2&amp;group_children=2&amp;req_children=2&amp;age=5&amp;req_age=5&amp;age=7&amp;req_age=7&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;nflt=class%3D5-star&amp;srpvid=8783785c232b0013&amp;srepoch=1698858433&amp;all_sr_blocks=1090878511_381972553_0_0_0%2C1090878508_381972553_0_0_0&amp;highlighted_blocks=1090878511_381972553_0_0_0%2C1090878508_381972553_0_0_0&amp;matching_block_id=1090878511_381972553_0_0_0&amp;sr_pri_blocks=1090878511_381972553_0_0_0__34560%2C1090878508_381972553_0_0_0__21600&amp;from=searchresults#hotelTmpl" rel="noopener noreferrer" tabindex="-1" target="_blank"><img alt="The Muse Inn" class="f9671d49b1" data-testid="image" height="248" src="https://cf.bstatic.com/xdata/images/hotel/square600/499451951.webp?k=b28be351c0ee215e39d4575d414ba02ddaf443db454473d81975188ba7c22677&amp;o=" width="248"/></a><div class="f9039b381b" data-testid="wishlist-icon" role="none"><span class=""><span class="f419a93f12"><button aria-expanded="false" class="fad65e569f" data-testid="wishlist-button" type="button"><div class="aca0ade214 aaf30230d9 c2931f4182 a6623c6f96"><span aria-hidden="true" class="fcd9eec8fb e4b4726df8 d24fc26e73" data-testid="wishlist-icon"><svg height="1em" viewbox="0 0 128 128" width="1em"><path d="M64 112a3.6 3.6 0 0 1-2-.5 138.8 138.8 0 0 1-44.2-38c-10-14.4-10.6-26-9.4-33.2a29 29 0 0 1 22.9-23.7c11.9-2.4 24 2.5 32.7 13a33.7 33.7 0 0 1 32.7-13 29 29 0 0 1 22.8 23.7c1.3 7.2.6 18.8-9.3 33.3-9.1 13.1-24 25.9-44.2 37.9a3.6 3.6 0 0 1-2 .5z"></path></svg></span></div></button></span></span></div></div></div><div class="c1edfbabcb"><div class="aca0ade214 aaf30230d9 cd2e7d62b0 b0db0e8ada"><div class=""><div class="aca0ade214 c9835feea9 c2931f4182 d79e71457a f02fdbd759"><div class="aaee4e7cd3 e7a57abb1e"><div class="aca0ade214 a5f1aae5b2 cd2e7d62b0"><div><div class="d6767e681c"><h3 class="aab71f8e4e"><a class="a78ca197d0" data-testid="title-link" href="https://www.booking.com/hotel/eg/the-muse-inn.en-gb.html?aid=304142&amp;label=gen173nr-1FCAQoggJCEnNlYXJjaF9jYWlybyxlZ3lwdEgJWARojAGIAQGYAQm4ARnIAQzYAQHoAQH4AQOIAgGoAgO4AriLiqoGwAIB0gIkYWZjNmM0ZmMtZTljMC00YmU4LWJlMWItMjJjOTAzMTgzMDJl2AIF4AIB&amp;ucfs=1&amp;arphpl=1&amp;checkin=2023-11-01&amp;checkout=2023-11-07&amp;group_adults=3&amp;req_adults=3&amp;no_rooms=2&amp;group_children=2&amp;req_children=2&amp;age=5&amp;req_age=5&amp;age=7&amp;req_age=7&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;nflt=class%3D5-star&amp;srpvid=8783785c232b0013&amp;srepoch=1698858433&amp;all_sr_blocks=1090878511_381972553_0_0_0%2C1090878508_381972553_0_0_0&amp;highlighted_blocks=1090878511_381972553_0_0_0%2C1090878508_381972553_0_0_0&amp;matching_block_id=1090878511_381972553_0_0_0&amp;sr_pri_blocks=1090878511_381972553_0_0_0__34560%2C1090878508_381972553_0_0_0__21600&amp;from=searchresults#hotelTmpl" rel="noopener noreferrer" target="_blank"><div class="f6431b446c a15b38c233" data-testid="title">The Muse Inn</div><div class="ac4a7896c7">Opens in new window</div></a></h3><div class="d8c86a593f"><span class="f419a93f12"><div aria-expanded="false" aria-label="3 out of 5" class="b3f3c831be" tabindex="0"><div aria-hidden="true" class="a455730030" data-testid="rating-stars" role="img"><span aria-hidden="true" class="fcd9eec8fb d31eda6efc c25361c37f"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M23.555 8.729a1.505 1.505 0 0 0-1.406-.98h-6.087a.5.5 0 0 1-.472-.334l-2.185-6.193a1.5 1.5 0 0 0-2.81 0l-.005.016-2.18 6.177a.5.5 0 0 1-.471.334H1.85A1.5 1.5 0 0 0 .887 10.4l5.184 4.3a.5.5 0 0 1 .155.543l-2.178 6.531a1.5 1.5 0 0 0 2.31 1.684l5.346-3.92a.5.5 0 0 1 .591 0l5.344 3.919a1.5 1.5 0 0 0 2.312-1.683l-2.178-6.535a.5.5 0 0 1 .155-.543l5.194-4.306a1.5 1.5 0 0 0 .433-1.661z"></path></svg></span><span aria-hidden="true" class="fcd9eec8fb d31eda6efc c25361c37f"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M23.555 8.729a1.505 1.505 0 0 0-1.406-.98h-6.087a.5.5 0 0 1-.472-.334l-2.185-6.193a1.5 1.5 0 0 0-2.81 0l-.005.016-2.18 6.177a.5.5 0 0 1-.471.334H1.85A1.5 1.5 0 0 0 .887 10.4l5.184 4.3a.5.5 0 0 1 .155.543l-2.178 6.531a1.5 1.5 0 0 0 2.31 1.684l5.346-3.92a.5.5 0 0 1 .591 0l5.344 3.919a1.5 1.5 0 0 0 2.312-1.683l-2.178-6.535a.5.5 0 0 1 .155-.543l5.194-4.306a1.5 1.5 0 0 0 .433-1.661z"></path></svg></span><span aria-hidden="true" class="fcd9eec8fb d31eda6efc c25361c37f"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M23.555 8.729a1.505 1.505 0 0 0-1.406-.98h-6.087a.5.5 0 0 1-.472-.334l-2.185-6.193a1.5 1.5 0 0 0-2.81 0l-.005.016-2.18 6.177a.5.5 0 0 1-.471.334H1.85A1.5 1.5 0 0 0 .887 10.4l5.184 4.3a.5.5 0 0 1 .155.543l-2.178 6.531a1.5 1.5 0 0 0 2.31 1.684l5.346-3.92a.5.5 0 0 1 .591 0l5.344 3.919a1.5 1.5 0 0 0 2.312-1.683l-2.178-6.535a.5.5 0 0 1 .155-.543l5.194-4.306a1.5 1.5 0 0 0 .433-1.661z"></path></svg></span></div></div></span></div><span class="f419a93f12"><span aria-expanded="false" data-testid="preferred-badge" role="button" tabindex="0"><span aria-label="This property is part of our Preferred Partner Programme. It is committed to providing commendable service and good value. It will pay us a higher commission if you make a booking." class="fcd9eec8fb c2a6770498 c2cc050fb8 e410954d4b" role="img"><svg height="1em" viewbox="0 0 128 128" width="1em"><path d="M112 8H16a8 8 0 0 0-8 8v96a8 8 0 0 0 8 8h96a8 8 0 0 0 8-8V16a8 8 0 0 0-8-8zM48 96H24V58h24zm56-25a8.7 8.7 0 0 1-2 6 8.9 8.9 0 0 1 1 4 6.9 6.9 0 0 1-5 7c-.5 4-4.8 8-9 8H56V58l10.3-23.3a5.4 5.4 0 0 1 10.1 2.7 10.3 10.3 0 0 1-.6 2.7L72 52h23c4.5 0 9 3.5 9 8a9.2 9.2 0 0 1-2 5.3 7.5 7.5 0 0 1 2 5.7z"></path></svg></span></span></span></div></div><div><div class="abf093bdfe ecc6a9ed89"><a class="a83ed08757 f88a5204c2 a1ae279108 b98133fb50" href="https://www.booking.com/hotel/eg/the-muse-inn.en-gb.html?aid=304142&amp;label=gen173nr-1FCAQoggJCEnNlYXJjaF9jYWlybyxlZ3lwdEgJWARojAGIAQGYAQm4ARnIAQzYAQHoAQH4AQOIAgGoAgO4AriLiqoGwAIB0gIkYWZjNmM0ZmMtZTljMC00YmU4LWJlMWItMjJjOTAzMTgzMDJl2AIF4AIB&amp;ucfs=1&amp;arphpl=1&amp;checkin=2023-11-01&amp;checkout=2023-11-07&amp;group_adults=3&amp;req_adults=3&amp;no_rooms=2&amp;group_children=2&amp;req_children=2&amp;age=5&amp;req_age=5&amp;age=7&amp;req_age=7&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;nflt=class%3D5-star&amp;srpvid=8783785c232b0013&amp;srepoch=1698858433&amp;all_sr_blocks=1090878511_381972553_0_0_0%2C1090878508_381972553_0_0_0&amp;highlighted_blocks=1090878511_381972553_0_0_0%2C1090878508_381972553_0_0_0&amp;matching_block_id=1090878511_381972553_0_0_0&amp;sr_pri_blocks=1090878511_381972553_0_0_0__34560%2C1090878508_381972553_0_0_0__21600&amp;from=searchresults&amp;map=1" rel="noopener noreferrer" target="_blank"><span><span class="aee5343fdb def9bc142a" data-testid="address">Giza, Cairo</span><span class="aee5343fdb def9bc142a">Show on map</span></span></a><span class="aee5343fdb"><span class="f419a93f12"><span aria-expanded="false" data-testid="distance">11.4 km from centre</span></span></span></div></div></div></div><div class=""><div class="aca0ade214 ebac6e22e9 cd2e7d62b0 a0ff1335a1"><div class=""><div class="aca0ade214 a5f1aae5b2 cd2e7d62b0"><a class="a83ed08757 f88a5204c2 c057617e1a b98133fb50" data-testid="review-score-link" href="https://www.booking.com/hotel/eg/the-muse-inn.en-gb.html?aid=304142&amp;label=gen173nr-1FCAQoggJCEnNlYXJjaF9jYWlybyxlZ3lwdEgJWARojAGIAQGYAQm4ARnIAQzYAQHoAQH4AQOIAgGoAgO4AriLiqoGwAIB0gIkYWZjNmM0ZmMtZTljMC00YmU4LWJlMWItMjJjOTAzMTgzMDJl2AIF4AIB&amp;ucfs=1&amp;arphpl=1&amp;checkin=2023-11-01&amp;checkout=2023-11-07&amp;group_adults=3&amp;req_adults=3&amp;no_rooms=2&amp;group_children=2&amp;req_children=2&amp;age=5&amp;req_age=5&amp;age=7&amp;req_age=7&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;nflt=class%3D5-star&amp;srpvid=8783785c232b0013&amp;srepoch=1698858433&amp;all_sr_blocks=1090878511_381972553_0_0_0%2C1090878508_381972553_0_0_0&amp;highlighted_blocks=1090878511_381972553_0_0_0%2C1090878508_381972553_0_0_0&amp;matching_block_id=1090878511_381972553_0_0_0&amp;sr_pri_blocks=1090878511_381972553_0_0_0__34560%2C1090878508_381972553_0_0_0__21600&amp;from=searchresults#hotelTmpl" rel="noopener noreferrer" target="_blank"><span><div class="aca0ade214 aaf30230d9 e1ffac4e41 e7d9f93f4d d79e71457a d5fd510f01 dc7f26e57f" data-testid="review-score"><div aria-label="Scored 9.6 " class="a3b8729ab1 d86cee9b25">9.6</div><div class="aaee4e7cd3 e7a57abb1e a29749fd9f"><div aria-label="Exceptional" class="a3b8729ab1 e6208ee469 cb2cbb3ccb">Exceptional </div><div class="abf093bdfe f45d8e4c32 d935416c47">18 reviews</div></div></div></span></a><div><a aria-label="Location: Scored 9.6 " class="a83ed08757 f88a5204c2 b98133fb50" data-testid="secondary-review-score-link" href="https://www.booking.com/hotel/eg/the-muse-inn.en-gb.html?aid=304142&amp;label=gen173nr-1FCAQoggJCEnNlYXJjaF9jYWlybyxlZ3lwdEgJWARojAGIAQGYAQm4ARnIAQzYAQHoAQH4AQOIAgGoAgO4AriLiqoGwAIB0gIkYWZjNmM0ZmMtZTljMC00YmU4LWJlMWItMjJjOTAzMTgzMDJl2AIF4AIB&amp;ucfs=1&amp;arphpl=1&amp;checkin=2023-11-01&amp;checkout=2023-11-07&amp;group_adults=3&amp;req_adults=3&amp;no_rooms=2&amp;group_children=2&amp;req_children=2&amp;age=5&amp;req_age=5&amp;age=7&amp;req_age=7&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;nflt=class%3D5-star&amp;srpvid=8783785c232b0013&amp;srepoch=1698858433&amp;all_sr_blocks=1090878511_381972553_0_0_0%2C1090878508_381972553_0_0_0&amp;highlighted_blocks=1090878511_381972553_0_0_0%2C1090878508_381972553_0_0_0&amp;matching_block_id=1090878511_381972553_0_0_0&amp;sr_pri_blocks=1090878511_381972553_0_0_0__34560%2C1090878508_381972553_0_0_0__21600&amp;from=searchresults#hotelTmpl" rel="noopener noreferrer" target="_blank"><span><span class="a3332d346a">Location 9.6</span></span></a></div><span class="abf093bdfe c147fc6dd1 d8d1f2a629"><span class="b30f8eb2d6">New to Booking.com</span></span></div></div></div></div></div></div><div><div class="da455a9bcf"><span class="f419a93f12"><span aria-expanded="false" aria-label="Late Escape Deal. You’re getting a reduced rate because this property is offering a discount on stays between 1 October 2023 and 3 January 2024.." class="abf093bdfe c147fc6dd1 d18b4a6026" data-testid="property-card-deal" tabindex="0"><span class="b30f8eb2d6">Late Escape Deal</span></span></span></div></div><div class="b1037148f8" data-testid="availability-group"><div class="c19beea015"><div class="ccdd44706b" data-testid="recommended-units"><span class="abf093bdfe c147fc6dd1 a5f389215e d516b1d73e"><span class="b30f8eb2d6">Recommended for your group</span></span><div class="ccbf515d6e d4744bc240 c23ed9b97e f666522354" role="none" tabindex="0"><div class="a3d07576c6"><span class="affdc0966d">1×</span></div><div class="c59cd18527"><h4 class="abf093bdfe e8f7c070a7" role="link" tabindex="0">Deluxe Double Room</h4><ul class="ba51609c35"><li class="a6a38de85e"><div class="fc367255e6"><div class="abf093bdfe">1 extra-large double bed</div></div></li></ul></div></div><div class="ccbf515d6e d4744bc240 c23ed9b97e f666522354" role="none" tabindex="0"><div class="a3d07576c6"><span class="affdc0966d">1×</span></div><div class="c59cd18527"><h4 class="abf093bdfe e8f7c070a7" role="link" tabindex="0">Family Room</h4><ul class="ba51609c35"><li class="a6a38de85e"><div class="fc367255e6"><div class="abf093bdfe">2 extra-large double beds</div></div></li></ul></div></div></div></div><div class="a4b53081e1"><div class="aca0ade214 aaf30230d9 cd2e7d62b0 fdccaff19b" data-testid="availability-rate-wrapper"><div class="c5ca594cb1 f19ed67e4b" data-testid="availability-rate-information"><div class="abf093bdfe f45d8e4c32" data-testid="price-for-x-nights">6 nights, 3 adults, 2 children</div><span class="f419a93f12"><div aria-expanded="false"><span aria-hidden="true" class="c73ff05531 e84eb96b1f">MAD 7,232</span><div class="e84eb96b1f a661120d62"><span aria-hidden="true" class="f6431b446c fbfd7c1165 e84eb96b1f" data-testid="price-and-discounted-price">MAD 5,786</span><span aria-hidden="true" class="fcd9eec8fb db5f35ed74 bf9a32efa5 c696a7d242"><svg viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M14.25 15.75h-.75a.75.75 0 0 1-.75-.75v-3.75a1.5 1.5 0 0 0-1.5-1.5h-.75a.75.75 0 0 0 0 1.5h.75V15a2.25 2.25 0 0 0 2.25 2.25h.75a.75.75 0 0 0 0-1.5zM11.625 6a1.125 1.125 0 1 0 0 2.25 1.125 1.125 0 0 0 0-2.25.75.75 0 0 0 0 1.5.375.375 0 1 1 0-.75.375.375 0 0 1 0 .75.75.75 0 0 0 0-1.5zM22.5 12c0 5.799-4.701 10.5-10.5 10.5S1.5 17.799 1.5 12 6.201 1.5 12 1.5 22.5 6.201 22.5 12zm1.5 0c0-6.627-5.373-12-12-12S0 5.373 0 12s5.373 12 12 12 12-5.373 12-12z"></path></svg></span></div></div></span><div class="ac4a7896c7">Original price MAD 7,232. Current price MAD 5,786.</div><div class="abf093bdfe f45d8e4c32" data-testid="taxes-and-charges">+MAD 868 taxes and charges</div></div><div class="da8b337763" data-testid="availability-cta"><a class="a83ed08757 c21c56c305 a4c1805887 d691166b09 ab98298258 deab83296e c082d89982 ff33faec5f" data-testid="availability-cta-btn" href="https://www.booking.com/hotel/eg/the-muse-inn.en-gb.html?aid=304142&amp;label=gen173nr-1FCAQoggJCEnNlYXJjaF9jYWlybyxlZ3lwdEgJWARojAGIAQGYAQm4ARnIAQzYAQHoAQH4AQOIAgGoAgO4AriLiqoGwAIB0gIkYWZjNmM0ZmMtZTljMC00YmU4LWJlMWItMjJjOTAzMTgzMDJl2AIF4AIB&amp;ucfs=1&amp;arphpl=1&amp;checkin=2023-11-01&amp;checkout=2023-11-07&amp;group_adults=3&amp;req_adults=3&amp;no_rooms=2&amp;group_children=2&amp;req_children=2&amp;age=5&amp;req_age=5&amp;age=7&amp;req_age=7&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;nflt=class%3D5-star&amp;srpvid=8783785c232b0013&amp;srepoch=1698858433&amp;all_sr_blocks=1090878511_381972553_0_0_0%2C1090878508_381972553_0_0_0&amp;highlighted_blocks=1090878511_381972553_0_0_0%2C1090878508_381972553_0_0_0&amp;matching_block_id=1090878511_381972553_0_0_0&amp;sr_pri_blocks=1090878511_381972553_0_0_0__34560%2C1090878508_381972553_0_0_0__21600&amp;from=searchresults#hotelTmpl" target="_blank"><span class="e4adce92df">See availability</span><span class="eedba9e88a d7eef963fa"><span aria-hidden="true" class="fcd9eec8fb bf9a32efa5"><span aria-hidden="true" class="fcd9eec8fb bf9a32efa5" data-testid="availability-cta-icon"><svg data-rtl-flip="true" viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M8.91289 19.2361C9.03226 19.2367 9.15054 19.2134 9.2608 19.1676C9.37105 19.1219 9.47105 19.0546 9.55493 18.9696L15.612 12.9125C15.7367 12.7891 15.8353 12.6418 15.9018 12.4795C15.9684 12.3172 16.0017 12.1431 15.9997 11.9676C16.0075 11.6171 15.877 11.2776 15.6362 11.0227L9.57916 4.96566C9.40881 4.79552 9.17788 4.69995 8.93711 4.69995C8.69634 4.69995 8.46542 4.79552 8.29506 4.96566C8.20935 5.04918 8.14122 5.14902 8.09471 5.25929C8.04819 5.36957 8.02423 5.48803 8.02423 5.60771C8.02423 5.72739 8.04819 5.84586 8.09471 5.95613C8.14122 6.0664 8.20935 6.16624 8.29506 6.24976L13.9887 11.9676L8.27084 17.6855C8.18512 17.769 8.117 17.8689 8.07048 17.9792C8.02396 18.0894 8 18.2079 8 18.3276C8 18.4473 8.02396 18.5657 8.07048 18.676C8.117 18.7863 8.18512 18.8861 8.27084 18.9696C8.3543 19.0551 8.45423 19.1228 8.56458 19.1686C8.67493 19.2144 8.79341 19.2374 8.91289 19.2361Z"></path></svg></span></span></span></a></div></div></div></div></div></div></div>'
