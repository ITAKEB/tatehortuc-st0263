from mrjob.job import MRJob


class MoviesDataAnalityc(MRJob):

    def mapper(self, _, line):
        user = line.split(',')[0]
        movie = line.split(',')[1]
        rating = line.split(',')[2]
        genre = line.split(',')[3]
        date = line.split(',')[4]

        if user != "User" and movie != "Movie" and rating != "Rating" and genre != "Genre" and date != "Date":
            yield f'{user} movies-user', int(rating)
            yield 'movies-maxmin-day', date
            yield f'{movie} users-per-movie', [user, int(rating)]
            yield 'wandb-rating-day', [date, int(rating)]
            yield f'{genre} wandb-moview-by-genre', [movie, int(rating)]

    def reducer(self, key, values):
        count = 0
        total = 0

        if key.__contains__('movies-user'):
            user = key.split(" ")[0]
            for rating in values:
                total += rating
                count += 1

            average = total / count
            yield user, f"movies: {count}, rating-avg:{average}"

        if key.__contains__('movies-maxmin-day'):
            dates = {}
            for date in values:
                try:
                    dates[date] = dates[date] + 1
                except Exception:
                    dates[date] = 0
                    dates[date] = dates[date] + 1

            max_day = max(dates.items(), key=lambda x: (x[1]))
            yield "movies-max-day", max_day
            min_day = min(dates.items(), key=lambda x: (x[1]))
            yield "movies-min-day", min_day

        if key.__contains__('users-per-movie'):
            movie = key.split(" ")[0]
            for value in values:
                total += value[1]
                count += 1

            average = total / count

            yield movie, f"users: {count}, rating-avg:{average}"

        if key.__contains__('wandb-rating-day'):
            dates = {}
            ratings = {}
            for value in values:
                try:
                    dates[value[0]] = dates[value[0]] + 1
                    ratings[value[0]] = ratings[value[0]] + value[1]
                except Exception:
                    dates[value[0]] = 0
                    ratings[value[0]] = 0
                    dates[value[0]] = dates[value[0]] + 1
                    ratings[value[0]] = ratings[value[0]] + value[1]

            for date in dates:
                count = dates[date]
                ratings_sum = ratings[date]
                dates[date] = ratings_sum / count

            max_day = max(dates.items(), key=lambda x: (x[1]))
            yield "movies-max-day:", max_day
            min_day = min(dates.items(), key=lambda x: (x[1]))
            yield "movies-min-day:", min_day

        if key.__contains__('wandb-moview-by-genre'):
            genre = key.split(" ")[0]
            movies = {}
            ratings = {}
            for value in values:
                try:
                    movies[value[0]] = movies[value[0]] + 1
                    ratings[value[0]] = ratings[value[0]] + value[1]
                except Exception:
                    movies[value[0]] = 0
                    ratings[value[0]] = 0
                    movies[value[0]] = movies[value[0]] + 1
                    ratings[value[0]] = ratings[value[0]] + value[1]

            for movie in movies:
                count = movies[movie]
                ratings_sum = ratings[movie]
                movies[movie] = ratings_sum / count

            best_movie = max(movies.items(), key=lambda x: (x[1]))
            yield genre, f"best-movie: {best_movie}"
            worst_movie = min(movies.items(), key=lambda x: (x[1]))
            yield genre, f"worst-movie: {worst_movie}"


if __name__ == '__main__':
    MoviesDataAnalityc.run()
