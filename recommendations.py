# 	A dictionary of movie critics and their ratings of a small
#	set of movies.

critics = {'Lisa Rose':{'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
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


from math import sqrt


# 	Calculate Euclidean distance-based similarity score between two people.
#	Returns values from 0-1, with 0 being no absolutely no correlation / 
#	similarity, and 1 being perfect correlation / similarity.
def sim_distance(preferences, person_1, person_2):
	#	Get the list of shared items
	shared_items = {}
	for item in preferences[person_1]:
		if item in preferences[person_2]:
			shared_items[item] = 1


	#	If there are no common items, return 0.
	if len(shared_items) == 0:
		return 0


	#	Add the squares of all the differences.
	sum_of_squares=sum([pow(preferences[person_1][item]-
		preferences[person_2][item], 2)
		for item in preferences[person_1] if item in preferences[person_2]])


	#	Since we want all similarity scores to return greater values for
	#	greater similarity, need to invert sum_of_squares, which inherently
	#	gives smaller number numbers for greater similarity.  1 is added to the
	#	denominator to eliminate division by zero errors.
	return 1 / (1 + sum_of_squares)


#	Calculate Pearson correlation coefficient similarity score between
#	two people.  Returns values from -1 to 1, with -1 being perfect, but 
#	directly opposed, correlation / similarity, (i.e. if Person_1 loves
#	something, Person_2 will hate it, with that relationship being absolutely
#	dependable) 0 being no correlation, and 1 being perfect, (and in agreement)
#	correlation / similarity.
def sim_pearson(preferences, person_1, person_2):
	#	Get the list of shared items
	shared_items = {}
	for item in preferences[person_1]:
		if item in preferences[person_2]:
			shared_items[item] = 1


	#	If there are no common items, return 0.
	if len(shared_items) == 0:
		return 0


	#	Add up all the preferences.
	sum1 = sum([preferences[person_1][item] for item in shared_items])
	sum2 = sum([preferences[person_2][item] for item in shared_items])


	#	Sum up the squares.
	sum1_squared = sum([pow(preferences[person_1][item], 2)
		for item in shared_items])
	sum2_squared = sum([pow(preferences[person_2][item], 2) 
		for item in shared_items])


	#	Sum up the products.
	sum_product = sum([preferences[person_1][item] * preferences[person_2][item]
		for item in shared_items])

	#	Calculate Pearson score.
	pearson_numerator = sum_product - (sum1 * sum2 / len(shared_items))
	pearson_denominator = sqrt(
		(sum1_squared - pow(sum1, 2) / len(shared_items)) *
		(sum2_squared - pow(sum2, 2) / len(shared_items)))
	if pearson_denominator == 0:
		return 0
	pearson_score = pearson_numerator / pearson_denominator
	return pearson_score


#	Returns the best matches for person from the preferences dictionary.
def top_matches(preferences, person, n=5, similarity_metric = sim_pearson):
	scores = [(similarity_metric(preferences, person, 
		person_to_compare_against),	person_to_compare_against)
	for person_to_compare_against in preferences
		if person_to_compare_against != person]

	#	Sort the list, so that the highest results appear on top.
	scores.sort()
	scores.reverse()
	return scores[0:n]


#	Gets recommendations for a person by using a weighted average of every
#	other person's ratings.
def get_recommendations(preferences, person, similarity_metric = sim_pearson):
	totals = {}
	sum_of_similarities = {}
	for person_to_compare_against in preferences:
		#	Don't compare person to him/herself.
		if person_to_compare_against = person:
			continue
		similarity = similarity_metric(preferences, person, 
			person_to_compare_against)

		#	Ignore scores of 0 or lower
		if similarity <= 0:
			continue
		for item in preferences[person_to_compare_against]: