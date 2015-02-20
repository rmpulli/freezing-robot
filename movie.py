import fresh_tomatoes


class Movie:
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

# Some movies with title, poster image url and trailer url
mos = Movie('Man of Steel', 'http://oyster.ignimgs.com/wordpress/stg.ign.com/2012/12/Man-of-Steel-poster2-610x904.jpg',
            'https://www.youtube.com/watch?v=NlOF03DUoWc')
gotg = Movie('Guardians of the Galaxy',
             'http://cdn.screenrant.com/wp-content/uploads/Guardians-of-the-Galaxy-IMAX-poster-700x1024.jpg',
             'https://www.youtube.com/watch?v=d96cjJhvlMA')
vfv = Movie('V for Vendetta', 'http://content9.flixster.com/rtmovie/49/33/49339_gal.jpg',
            'https://www.youtube.com/watch?v=IHVzzxrPt1c')
pb = Movie('The Princess Bride', 'https://headinavice.files.wordpress.com/2013/01/the-princess-bride-movie-poster.jpg',
           'https://www.youtube.com/watch?v=O3CIXEAjcc8')
ti = Movie('The Incredibles',
           'http://img3.wikia.nocookie.net/__cb20100622151355/pixar/images/4/44/Movie_poster_the_incredibles.jpg',
           'https://www.youtube.com/watch?v=sZwWCrFNfzQ')

# Create content for page
fresh_tomatoes.create_movie_tiles_content([mos, gotg, vfv, pb, ti])

# Open the movies page
fresh_tomatoes.open_movies_page([mos, gotg, vfv, pb, ti])
