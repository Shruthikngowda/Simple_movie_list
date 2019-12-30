
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

def find_movie_by_attribute(attribute):
  try:
    res = [ sub[attribute] for sub in movie_list ]
  except:
    print("Wrong attribute") 
  #print(res)




add_movies()
see_movies()
find_movie_by_attribute("reeee")