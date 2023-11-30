import csv

def get_movies():
    movie_filepath = 'db/movie.csv'
    with open(movie_filepath, newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            if leitor_csv.line_num == 1:
                break
            print(list(linha.values()))