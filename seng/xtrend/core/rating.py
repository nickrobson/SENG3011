# rating.py
# SENG3011 - Cool Bananas
#
# Functions for calculating ratings based on RICs.

from datetime import datetime, date

from .core import companyreturn
from ...server.cache import query

currentDate = date(2015, 12, 31)

def getRating(ric):
	return calculateRating(ric)

def calculateRating(ric):
	# The rating works by basing it as a percentage change over the past fortnight.
	# More recent changes will affect the rating more than previous changes.
	# The overall rating is based 60-40 between news ratings and stock prices when
	# the RIC has 5 or more articles in the past fortnight, otherwise it's based
	# 20-40.

	# TODO: Sanity checks.
	# TODO: Double check this works; this is just a theoretical model.

	relatedStocks = stingrayQuery((ric,), ("CM_Return", "AV_Return"), 14, 0, currentDate)
	relatedArticles = query((ric,), (), (date - datetime.timedelta(days = 14), date))


	# Step 1: calculate the rating based on stock prices..

	# Set up two variables: one will be the actual rating, and one will be the
	# magnitude of how much we're going up and down by.
	# We're looking at the past two weeks of stocks. Take their lows on each of
	# these dates and apply this formula to the total score (and the absolute of
	# this to the magnitude score).

	# (1 - (Price this day - Price yesterday)/ Price yesterday) / (Days since now + 1).

	# This value should be positive if the price when down, and negative if the price
	# went up. It is based on a percentage increase/decrease of the stock based on
	# the previous days. More recent dates are weighted stronger. The price yesterday
	# might not be available. It should be alright to replace that with the previous
	# entry if possible.

	# The total stock price score will be this:
	
	# Current rating / magnitude rating

	# What this does is that if a stock is consistently going up or down, then the
	# rating should be strong. If it remains stagnant, this should even out the
	# score to something middle ground.

	# If required, we'll divide this by a magic number just to scale everything, but
	# I think this works in theory.


	# Step 2: weigh the news articles.
	# This one works in a similar way as before. Basically, for each article,
	# apply this formula to two new variables.

	# (Polarity * (1 - Subjectivity)) / Days since now.

	# The subjectivity part might need to be changed. This is a basic check to see
	# whether the articles are writing positively or negatively. More recent articles
	# are more important, and will affect the score more.

	# Again, the same deal as before. If a company has all good or all bad articles,
	# they should see a much stronger rating than one wiithout one. We do the same
	# thing as before.

	# Current rating / magnitude rating	


	# Step 3: weigh the two scores appropriately.

	# If a company isn't getting that much news, it's hard to give an accurate rating
	# based on them. Instead, we weigh the news accordingly.

	# Total rating = Share rating * 0.4 + (clamp(1, 5, len(news articles)) * 0.4 + 0.2) * news rating

	# Basically, the share price will always be 40% of the total score. For the
	# news articles, if there's not a lot of articles, then the news score will
	# be lower. There's a minimum point: clearly if there's no news at all,
	# there won't be a rating. However, if there's one article, then we rank it
	# to at least 20% of the score. Two articles will be 30%, three 40%, four 50%,
	# and five or more will be the full 60%. Generally if a company is getting
	# lots of news articles, then the worth of each individual article is not as
	# important, and we want to see the larger assessment of them. This should
	# also give a decent rating towards less popular companies.

	
	# Once this is all implemented, return the proper value.
	return 0.0