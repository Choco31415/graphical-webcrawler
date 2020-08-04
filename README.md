# graphical-webcrawler
The first industrial graphic web crawler 
web_crawler2.py ================== Prototype idea to test out possbilities

sites.py        ================== algorthim for grabing weblinks off wikipedia, and crawling through weblinks

Algorthim description: start at wikipedia mainpage | mappedlist.append(all hrefs on this page entirely) | stagedlist.append(the main page weblink) 
                     | double verifiication double checks mappedlist and staged list   for any duplicates and matches. | matches will never be visited again and duplicates are made sure to be removed. | Rise and repeat to infinity. 
