
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

def see_movies(movies_list):
    print(movies_list)

def find_movie_by_attribute():
  find_property = input("what property you want to check ? ")
  find_property_value = input("what value are you looking for ? ")

  found_movies = []

  for movie in movie_list:
    if movie[find_property] == find_property_value:
      found_movies.append(movie)
  see_movies(found_movies) 

def user_choice():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")
    while user_input != 'q':
        if user_input == 'a':
            add_movies()
        elif user_input == 'l':
            see_movies(movie_list)
        elif user_input == 'f':
            movie = find_movie_by_attribute()
            print(movie or 'No movies found.')
        else:
            print('Unknown command-please try again.')
        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

user_choice()