
#example 1
def is_good_movie(movie):
    if movie["imdb"] > 5.5:
        return True
    return False
#example 2
def movies_above_5_5(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

good_movies = movies_above_5_5(movies)
for movie in good_movies:
    print(movie["name"])
#example 3

    def movies_by_category(movies, category_name):
      return [movie for movie in movies if movie["category"] == category_name]
romance_movies = movies_by_category(movies, "Romance")
for movie in romance_movies:
    print(movie["name"])
#example 4

    def average_imdb_score(movies):
        total_score = sum(movie["imdb"] for movie in movies)
        return total_score / len(movies) if len(movies) > 0 else 0
average_score = average_imdb_score(movies)
print(f"Average IMDB score: {average_score}")

# example 5
def average_imdb_score_by_category(movies, category_name):
    filtered_movies = [movie for movie in movies if movie["category"] == category_name]
    if len(filtered_movies) > 0:
        total_score = sum(movie["imdb"] for movie in filtered_movies)
        return total_score / len(filtered_movies)
    else:
        return 0
    
average_score_romance = average_imdb_score_by_category(movies, "Romance")
print(f"Average IMDB score for Romance movies: {average_score_romance}")