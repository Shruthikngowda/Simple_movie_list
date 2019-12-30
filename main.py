
movie_list = []


def add_movies():
  print("Adding a movie")
  print("Please enter movie details")
  movie_name = input("Enter the movie name ")
  movie_year = input("Enter the movie released year")
  movie_director = input("Enter the movie director's name ")

  sample_dict = {}
  sample_dict["name"] = movie_name
  sample_dict["year"] = movie_year
  sample_dict["director"] = movie_director
  movie_list.append(sample_dict)

def see_movies():
  print("The movies list is as follows ")
  for x in movie_list:
    print(x)

def find_movie_by_attribute(attribute):
  




add_movies()
see_movies()