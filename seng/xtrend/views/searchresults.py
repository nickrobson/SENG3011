# homepage.py
# SENG3011 - Cool Bananas
#
# Displays homepage with list of revisions of code

from django.template.loader import get_template
from django.http import HttpResponse
from django.http import QueryDict

from ...utils import SingletonView

from datetime import date, timedelta

from ..core import stocks, rating
from seng.server import cache


class SearchResultsView(SingletonView):
    
    def __init__(self):
        self.template = get_template('assets/xtrend/searchresults.html')
        
    def get(self, request):
        resultsJson = [];

        # for each ric:
        searchRics = request.GET.getlist('instrument_id')
        searchBuy = request.GET.get('buy')
        searchSell = request.GET.get('sell')
        searchRange = int(request.GET.get('range'))
        searchDays = request.GET.get('days')

        currentDate = date(2015, 12, 31)

        searchResults = []
        numResults = 0

        for ric in searchRics:
            ricRating = rating.get_rating(ric)
            lower_window = 10
            upper_window = 0
            stockJsonOutput = stocks.get(
                [ric],
                upper_window,
                lower_window,
                currentDate #doi
            )
            #print(stockJsonOutput)
            lastStock = stockJsonOutput[ric][-1]
            for stock in reversed(stockJsonOutput[ric]):
                if (stock.adjusted_close > 0):
                    lastStock = stock
                    break
            price = lastStock.adjusted_close
            if (((ricRating <= 0 and searchSell == "1")
                and (price > searchRange))
                or ((ricRating > 0 and searchBuy == "0")
                    and (price < searchRange))):
                print(price)
                currResult = {}
                currResult['instrument_id'] = ric
                currResult['sentiment'] = '{0:0.4f}'.format(ricRating)
                
                currResult['tradingAt'] = '{0:0.3f}'.format(lastStock.adjusted_close)
                currResult['lastReturn'] = '{0:0.3f}'.format(lastStock.return_value)
                currResult['ratingPercentage'] = '{0:0.1f}'.format((ricRating + 100) / 2)
                searchResults.append(currResult)
                numResults += 1

        self.content = self.template.render({
            'range': range(0, numResults),
            'searchResults': searchResults
        });

        return HttpResponse(self.content, content_type='text/html')

    
