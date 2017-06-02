import fresh_tomatoes
import media

joe_dirt = media.Movie("Joe Dirt",
                       "Dude rocking a sweet mullet goes on a kickass adventure searching for his family",
                       "https://upload.wikimedia.org/wikipedia/en/6/69/Joe_dirt.jpg",
                       "https://www.youtube.com/watch?v=bfQu_ma0kls")
#print(joe_dirt.storyline)
step_brothers = media.Movie("Step Brothers",
                           "Don't you otuch my drumset!",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/d/d9/StepbrothersMP08.jpg/220px-StepbrothersMP08.jpg",
                           "https://www.youtube.com/watch?v=qb2Q0rMeeac")
#print(step_brothers.show_trailer)
#step_brothers.show_trailer()
jurassic_park = media.Movie("Jurassic Park",
                            "T Rex is coming!",
                            "https://upload.wikimedia.org/wikipedia/en/9/96/Jurassic_Park_logo.jpg",
                            "https://www.youtube.com/watch?v=f5C7dqrAItM")
happy_gilmore = media.Movie("Happy Gilmore",
                            "Hockey player turned golf pro wins his grandmas house back",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Happygilmoreposter.jpg/220px-Happygilmoreposter.jpg",
                            "https://www.youtube.com/watch?v=88H_d7G3m98")
moneyball = media.Movie("Moneyball",
                        "Billy Bean changes the way baseball is managed",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Moneyballsbn.jpg/220px-Moneyballsbn.jpg",
                        "https://www.youtube.com/watch?v=Bj20TKaRgN8")
sandlot = media.Movie("Sandlot",
                      "Bambi? That wimpy deer?",
                      "https://upload.wikimedia.org/wikipedia/en/d/d4/Sandlot_poster.jpg",
                      "https://www.youtube.com/watch?v=sOTqHBzR9xw")
movies = [joe_dirt, step_brothers, jurassic_park, happy_gilmore, moneyball, sandlot]
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
