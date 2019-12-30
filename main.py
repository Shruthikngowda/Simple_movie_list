
movie_list = []


def add_movies():
  print("Adding a movie")
  print("Please enter movie details")
  movie_name = input("Enter the movie name ")
  movie_year = int(input("Enter the movie released year"))
  movie_director = input("Enter the movie director's name ")

  movie_list.append(
    {
      'name': movie_name,
      'year': movie_year,
      'director': movie_director
    }
  )

def see_movies():
    print(movie_list)

def find_movie_by_attribute():
  find_property = input("what property you want to check ? ")
  find_property_value = input("what value are you looking for ? ")

  found_movies = []

  for movie in movie_list:
    if movie[find_property] == find_property_value:
      found_movies.append(found_movies)
    
  return found_movies



add_movies()
see_movies()
find_movie_by_attribute()