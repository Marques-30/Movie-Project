import fresh_tomatoes #link to fresh_tomatoes
import media #link to media

pulp_fiction = media.Movie("Pulp Fiction", #movie title
							"""The lives of two mob hit men, a boxer, a gangster's wife,
							and a pair of diner bandits intertwine in four tales of 
							violence and redemption.""", #plot summary
							"""http://www.teclasap.com.br/wp-content/uploads/2013/06/
							pulp_fiction.jpg""", #poster
							"https://www.youtube.com/watch?v=dZWPL9deY7I") #trailer

The_Dark_Knight = media.Movie("The Dark Knight", #movie title
							"""When the menace known as the Joker wreaks havoc and 
							chaos on the people of Gotham, the caped crusader must 
							come to terms with one of the greatest psychological 
							tests of his ability to fight injustice.""", #plot summary
							"""https://rvivekshanmugam.files.wordpress.com/2008/07/
							the_dark_knight_poster1.jpg""", #poster
							"https://www.youtube.com/watch?v=yrJL5JxEYIw") #trailer

Seven_Psychopaths = media.Movie("Seven Psychopaths", #movie title
								"""A struggling screenwriter inadvertently becomes 
								entangled in the Los Angeles criminal underworld 
								after his oddball friends kidnap a gangster's beloved 
								Shih Tzu.""", #plot summary
								"""http://ia.media-imdb.com/images/M/MV5BMTgwMzUxMjc0M1
								5BMl5BanBnXkFtZTcwMzQ2MjYyOA@@._V1_SX640_SY720_.jpg""", #poster
								"https://www.youtube.com/watch?v=8WGqz5xjlk8") #trailer

Battle_Royale= media.Movie("Battle Royale", #movie title
							"""In the future, the Japanese government captures 
							a class of ninth-grade students and forces them to 
							kill each other under the revolutionary
							 'Battle Royale' act.""", #plot summary
							"""http://chicagocinemasociety.org/wp-content/
							uploads/2012/04/BattleRoyaleBluRay.jpg""", #poster
							"https://www.youtube.com/watch?v=N0p1t-dC7Ko") #trailer

Dope = media.Movie("Dope", #movie title
					"""Life changes for Malcolm, a geek who's surviving
					 life in a tough neighborhood, after a chance invitation 
					 to an underground party leads him and his friends 
					into a Los Angeles adventure.""", #plot summary
					"""http://verastic.com/site/wp-content/uploads/
					2015/06/DOPE-Movie.jpg""", #poster
					"https://www.youtube.com/watch?v=L41xwM8tIRQ") #trailer

kingsman_the_secret_service= media.Movie("kingsman The Secret Service", #movie title
			"""A spy organization recruits an unrefined, but 
			promising street kid into the agency's ultra-competitive 
			training program, just as a global threat emerges 
			from a twisted tech genius.""", #plot summary
			"""https://upload.wikimedia.org/wikipedia/en/8/8b/
			Kingsman_The_Secret_Service_poster.jpg""", #poster
			"https://www.youtube.com/watch?v=kl8F-8tR8to") #trailer

movies = [pulp_fiction, The_Dark_Knight, Seven_Psychopaths, Battle_Royale, Dope, kingsman_the_secret_service]
fresh_tomatoes.open_movies_page(movies) # open in fresh_tomatoes