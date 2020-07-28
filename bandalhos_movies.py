from imdb import IMDb
ia = IMDb()

print(ia.get_movie_infoset())
#the_matrix = ia.get_movie('0133093')
#print(the_matrix['director'])

movie = ia.get_movie('0094226')
print(movie)
#movie = ia.get_movie('0094226', info=['taglines','main'])
print(movie.infoset2keys)
#print(movie.current_info)
