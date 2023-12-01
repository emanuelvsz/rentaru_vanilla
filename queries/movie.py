import csv
import os

def get_movies():
    movie_filepath = 'db/movie.csv'
    with open(movie_filepath, newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=';')
        movies = [linha for linha in leitor_csv]
    return movies
    
def get_movie_by_id(movie_id):
    movie_filepath = 'db/movie.csv'
    with open(movie_filepath, newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=';')
        for linha in leitor_csv:
            if linha and linha[0] == str(movie_id):
                return linha
    return None

def update_availability(movie_id, new_status):
    movie_filepath = 'db/movie.csv'
    tempfile = 'db/temp_movie.csv'
    with open(movie_filepath, 'r', newline='', encoding='utf-8') as infile, \
        open(tempfile, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile, delimiter=';')
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for row in reader:
            if row['id'] == movie_id:
                row['avaiable'] = str(new_status).lower()
            writer.writerow(row)
    os.remove(movie_filepath)
    os.rename(tempfile, movie_filepath)