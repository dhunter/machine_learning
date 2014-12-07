# 	A dictionary of movie critics and their ratings of a small
#	set of movies.

critics={'Lisa Rose':{'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
		'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
		'The Night Listener': 3.0},
	'Gene Seymour':{'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
		'Just My Luck': 1.5, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5,
		'The Night Listener': 3.0},
	'Michael Phillips':{'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
		'Superman Returns': 3.5, 'The Night Listener': 4.0},
	'Claudia Puig':{'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
		'Superman Returns': 4.0, 'You, Me and Dupree': 2.5,
		'The Night Listener': 4.5},
	'Mick LaSalle':{'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
		'Just My Luck': 2.0, 'Superman Returns': 3.0, 'You, Me and Dupree': 2.0,
		'The Night Listener': 3.0},
	'Jack Matthews':{'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
		'Superman Returns': 5.0, 'You, Me and Dupree': 3.5,
		'The Night Listener': 3.0},
	'toby':{'Snakes on a Plane': 4.5, 'Superman Returns': 4.0,
		'You, Me and Dupree': 1.0}}


# 	Calculate distance-based similarity score between two people.
from math import sqrt
def sim_distance(preferences,person_1,person_2):
	#	Get the list of shared items
	shared_items={}
	for item in preferences[person_1]:
		if item in preferences[person_2]:
			shared_items[item]=1

	#	If there are no common items, return 0.
	if len(shared_items)==0: return 0

	#	Add the squares of all the differences.
	sum_of_squares=sum([pow(preferences[person_1][item]-
		preferences[person_2][item],2)
		for item in preferences[person_1] if item in preferences[person_2]])

	return 1/(1+sum_of_squares)