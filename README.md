# The XHR HAR file api inspector
This name is pretty bad!

## Background 

If you are interesting in understanding an application you are using, it is often helpful to extract the URLs of the file to see how data is called. Being able to see these data calls behind the scene can help you understand the site better as well as be better informed with how to use the API.

## Example
For example, if you were to view a sample site like this: www.fast.com, you would see the results in your browser.

If however, you view the source in inspection mode,  you could see all of the data calls underneath the covers and embedded in the webpage to include:


* https://fast.com/app-9a70ea.js
* http://fast.com/
* https://fast.com/
* https://fast.com/assets/fonts/fonts/oc-webfont.ttf?mv454s
* https://api.fast.com/netflix/speedtest?https=true&token=YXNkZmFzZGxmbnNkYWZoYXNkZmhrYWxm&urlCount=5
* https://ipv4-c239-atl001-ix.1.oca.nflxvideo.net/speedtest/range/0-26214400?c=us&n=33657&v=3&e=1517807923&t=iZQ_W8ajF3uG3hBZw2VGxDnbBWc
* https://ipv4-c068-was001-ix.1.oca.nflxvideo.net/speedtest/range/0-26214400?c=us&n=33657&v=3&e=1517807923&t=eR5CEW8PQd2mbYizZSFyxWQTSIc
* https://ipv4-c068-was001-ix.1.oca.nflxvideo.net/speedtest/range/0-2048?c=us&n=33657&v=3&e=1517807923&t=eR5CEW8PQd2mbYizZSFyxWQTSIc
* https://fast.com/assets/fonts/oc-webfont.min.css
* https://ipv4-c239-atl001-ix.1.oca.nflxvideo.net/speedtest/range/0-2048?c=us&n=33657&v=3&e=1517807923&t=iZQ_W8ajF3uG3hBZw2VGxDnbBWc
* https://fast.com/assets/poweredby-865a3b.svg
* https://fast.com/app-54282a.css
* https://ipv4-c092-was001-ix.1.oca.nflxvideo.net/speedtest/range/0-2048?c=us&n=33657&v=3&e=1517807923&t=pMxQeRpucF5kptf7w9wVC8l4d2w
* https://fast.com/assets/new-logo-vert-37861c.svg
* https://ipv4-c092-was001-ix.1.oca.nflxvideo.net/speedtest/range/0-26214400?c=us&n=33657&v=3&e=1517807923&t=pMxQeRpucF5kptf7w9wVC8l4d2w

## Input

This is a project that simply reads URLs that are generated out of an HAR file, specifically focused on XHR URLs.  Simple view the file in inspection mode and extract the results as an HAR file.  To learn more about HAR files, check out this  
[link](https://blog.stackpath.com/glossary/har-file/).


# License Agreement

MIT License

Copyright (c) 2018 Terrance MacGregor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.