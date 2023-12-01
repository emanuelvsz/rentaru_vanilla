import csv

def insert_into_rent(rent):
    rent_filepath = 'db/rent.csv'
    with open(rent_filepath, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['user_id', 'movie_id', 'rented_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        if csvfile.tell() == 0:
            writer.writeheader()
        rent.rented_at = rent.rented_at.strftime('%Y-%m-%d')
        writer.writerow({
            'user_id': rent.user_id,
            'movie_id': rent.movie_id,
            'rented_at': rent.rented_at
        })
        