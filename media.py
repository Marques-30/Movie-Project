class Movie ():
	#rating value of movies
	VALID_RATING = ["G", "PG", "PG-13", "R"]
	# layout for how movie details are found from enterianment_center 
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube