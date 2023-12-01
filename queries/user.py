import csv

def get_user_by_id(user_id):
    user_filepath = 'db/user.csv'
    with open(user_filepath, newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=';')
        for linha in leitor_csv:
            if linha and linha[0] == str(user_id):
                return linha
    return None

def buscar_filmes_alugados_por_usuario(user_id):
    rent_filepath = 'db/rent.csv'
    movies_filepath = 'db/movie.csv'
    rented_movies = []
    with open(rent_filepath, newline='', encoding='utf-8') as rent_file, \
        open(movies_filepath, newline='', encoding='utf-8') as movies_file:
        rent_reader = csv.DictReader(rent_file, delimiter=';')
        movies_reader = csv.DictReader(movies_file, delimiter=';')
        user_rentals = [rental for rental in rent_reader if rental['user_id'] == str(user_id)]
        for rental in user_rentals:
            movie_id = rental['movie_id']
            movie_data = next((movie for movie in movies_reader if movie['id'] == movie_id), None)
            if movie_data:
                rented_movies.append({
                    'id': movie_data['id'],
                    'title': movie_data['title'],
                    'price': movie_data['price'],
                    'rented_at': rental['rented_at']
                })
    return rented_movies