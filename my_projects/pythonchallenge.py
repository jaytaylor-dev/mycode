#!/usr/bin/env python3
backend_list= []
usr_info_list= []
name=input("What is your name?\n")
usr_info_list.append(name.capitalize)
backend_list.append(name)
age=int(input("What is your age?\n"))
usr_info_list.append(age)
backend_list.append(age)
favorite_movie=input("Finally, what is your favorite movie?\n")
usr_info_list.append(favorite_movie)
backend_list.append(favorite_movie)
genre= input("What is the movie's genre?\n")
backend_list.append(genre)

def get_my_list():
    return[backend_list];

(f"Hello, {usr_info_list[0]}  it seems like you are {usr_info_list[1]} and your favorite movie is {usr_info_list[2]}")
print(backend_list)
