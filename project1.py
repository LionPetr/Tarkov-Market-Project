# project1

from urllib.request import urlopen
import re

def extractHtml(url):
   
    page = urlopen(url)
    html_source = page.read()
    html = html_source.decode("utf-8")
    return html

## pull the correct numbers from the html code
def figureOutStats(startValue, displacment):
    fullPrice = html[startValue + displacment[0] : startValue + displacment[1]]
    x = fullPrice.index(displacment[2])
    numPrice = fullPrice[: x]
    return(numPrice)

## check if item is currently available on flea    
def fleaCheck(url, startValue, displacement):
    html = extractHtml(url)
    fullPrice = html[startValue + displacement[0] : startValue + displacement[1]]
    check = fullPrice.find(displacement[2])
    if check == -1:
        return False
    else:
        return True

## used html
url = "https://tarkov-market.com/item/hk417_7.62x51_16.5_inch_barrel"

priceDisplacement = [58, 90, "₽"] ## the amount of spaces betweeen 24 hours and the actual price
percentDisplacement = [70, 90, "%"] ## the amount of spaces between 24 hours and the actual precrentage
html = extractHtml(url)
averagePricePlace = html.find("24 hours:")
averagePercentPlace = html.find("24 hours:", averagePricePlace + 10)

## print starting text 
tag = url[31:]
name = tag.replace("_", " ")
print("checking the price of " + name)

## make sure the item is on the flea and then get its price
if fleaCheck(url, averagePricePlace, priceDisplacement):
    test = figureOutStats(averagePricePlace, priceDisplacement)
    print(test)
    test = figureOutStats(averagePercentPlace, percentDisplacement)
    print(test.replace(" ", ""))
else:
    print("Item can't be sold on flea")




    
        
    







