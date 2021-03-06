# analysis.py
# SENG3011 - Cool Bananas
#
# Displays stock analysis for a particular RIC

import math

from django.template.loader import get_template
from django.http import HttpResponse, Http404

from datetime import date
from ..core import stocks

from ...core import mk
from ...core.constants import RIC_PATTERN
from ...server.models import NewsArticle
from ...utils import SingletonView
from ..core.rating import get_rating

def format_body(text):
    lines = text.split('\n    ')[:6]
    lines = map(lambda line: '<p>%s</p>' % line, lines)
    return '\n\n'.join(lines)

def get_polarity_image(polarity):
    if polarity > .1:
        return '/coolbananas/static/sentiment/arrow_up.svg'
    if polarity < -.1:
        return '/coolbananas/static/sentiment/arrow_down.svg'
    return '/coolbananas/static/sentiment/neutral.svg'

class RICAnalysisView(SingletonView):

    def __init__(self):
        self.template = get_template('assets/xtrend/analysis.html')

    def get(self, request, ric = None):
        if ric is None:
            raise Http404('You need to specify an instrument ID!')
        if not RIC_PATTERN.fullmatch(ric):
            raise Http404('Invalid instrument ID!')
        articles = NewsArticle.objects.filter(newsarticleric__ric = ric).order_by('time_stamp').reverse()[:50].all()
        if not len(articles):
            raise Http404('We have no analysis on %s, as there are no news articles.' % ric)
        articles = list(map(lambda article: {
                'headline': article.headline,
                'timestamp': article.time_stamp,
                'body': format_body(article.news_text),
                'uri': article.uri,
                'polarity': article.polarity,
                'polarity_image': get_polarity_image(article.polarity),
            }, articles))
        rating = get_rating(ric)
        extraSymbol = ''
        if rating >= 0:
            extraSymbol = '+'

        currentDate = date(2015, 12, 31)
        lower_window = 10
        upper_window = 0
        stockJsonOutput = stocks.get(
            [ric],
            upper_window,
            lower_window,
            currentDate #doi
        )

        lastStock = stockJsonOutput[ric][-1]
        for stock in reversed(stockJsonOutput[ric]):
            if (stock.adjusted_close > 0):
                lastStock = stock
                break

        content = self.template.render({
            'InstrumentID': ric,
            'ArticlesFirst': articles[::2],
            'ArticlesSecond': articles[1::2],
            'Rating': extraSymbol + str('{0:0.1f}'.format(rating)),
            'RatingPercentage': '{0:0.1f}'.format((rating + 100) / 2),
            'tradingAt': '{0:0.2f}'.format(lastStock.adjusted_close),
            'lastReturn': '{0:0.4f}'.format(lastStock.return_value)
        })
        return HttpResponse(content, content_type='text/html')

