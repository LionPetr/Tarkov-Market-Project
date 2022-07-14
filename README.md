# Tarkov-Market-Project
project1 file: using a specific item in the tarkov market webpage "https://tarkov-market.com/" the code performs multiple things:
- extracts the html
- checks if the item is a "flea" item which means it has the information that we need. If an item isnt a "flea" item it cant be used for the project 
- if item is a "flea" item the code finds 2 places where it says "24 hours:" in the html extracted from the webpage and using a certain displacement it finds the numbers that
we need such as price and percentage change each with their own displacement (amount of characters needed to move from the index of "24 hours")

this file returns a simple output printing the item name which is the last part of the item's url without the "_" and then prints out the statistics of the item that it pulled
or prints "Item can't be sold on flea" if the item doesn't pass the flea check. works by itself and to test different items you need to go to the tarkov market webpage and 
open one of the items there where the url follows this order "https://tarkov-market.com/item/" followed by the specific item specified. Then you need to copy the url and 
paste it in the url place in the code. 


test file is a program meant to interact with the "https://tarkov-market.com/tag/x" urls where x is a specific tag which has multiple items in it. The file pulls all the 
urls from the website and organizes them in an excel document named "excel work edited.xlsx" with the urls in one column and the names in another column. 
(needs a excel file named "excel work.xlsx" to work) to change the url that it should be working with you need to make sure the url is a "https://tarkov-market.com/tag/x" 
format and then paste it in the url place in the code. 
