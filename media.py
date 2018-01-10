import webbrowser


class Movie():
    """ This class provides a way to store movie related information
        to eventually be fed into fresh_tomatoes.py """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  # Constant movie ratings

    def __init__(
                self,
                movie_title,
                movie_storyline,
                poster_image,
                trailer_youtube
                ):
        """ This function generates the Movie class object
        and instance variables for each argument,
        which store movie related information """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Function to open trailer URLs in browser """
        webbrowser.open(self.trailer_youtube_url)
