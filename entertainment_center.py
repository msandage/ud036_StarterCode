import media
import fresh_tomatoes

#Generating Movie class objects based on media.py module Movie class
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

starship_troopers = media.Movie("Starship Troopers",
                                "Just trying to kill some bugs, sir",
                                "http://horrorfuel.com/wp-content/uploads/2016/11/stAR.jpg",
                                "https://www.youtube.com/watch?v=Y07I_KER5fE")

#Arrange Movie objects into list to be accepted by fresh_tomates.py module open movie page function
movies = [toy_story, avatar, starship_troopers] 

#Generates a website which accepts Movie class objects in an array/list and displays them in a grid
fresh_tomatoes.open_movies_page(movies) 
