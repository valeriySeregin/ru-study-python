from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk), у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.
        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        rtn = "rating_kinopoisk"
        cntr = "country"
        delimiter = ","

        filtered_movies = filter(
            lambda movie: len(movie[cntr].split(delimiter)) >= 2, list_of_movies
        )
        ratings = map(lambda movie: movie[rtn], filtered_movies)
        filtered_ratings = filter(lambda rating: rating not in ["", "0"], ratings)
        ratings_as_floats = map(lambda rating: float(rating), filtered_ratings)
        floats_as_list = list(ratings_as_floats)

        return sum(floats_as_list) / len(floats_as_list)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению
        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        rtn = "rating_kinopoisk"
        name = "name"
        char_to_count = "и"

        movies_and_ratings = map(
            lambda movie: {rtn: float(movie[rtn]) if movie[rtn] != "" else 0, name: movie[name]},
            list_of_movies,
        )
        movies_by_rating = filter(lambda movie: movie[rtn] >= rating, movies_and_ratings)
        char_counts = map(lambda movie: movie[name].count(char_to_count), movies_by_rating)
        char_counts_as_list = list(char_counts)

        return sum(char_counts_as_list)
