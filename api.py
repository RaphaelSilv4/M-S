'''import requests

 #Sua chave de API do TMDb
API_KEY = 'TMDB_KEY'

 #URL base da API do TMDb
base_url = 'https://api.themoviedb.org/3'

 #Endpoint para buscar informações de um filme específico por ID
movie_id = 550  # Exemplo de ID do filme "Fight Club"
endpoint = f'{base_url}/movie/{movie_id}?api_key={API_KEY}'

 #Fazendo a requisição GET para obter os detalhes do filme
response = requests.get(endpoint)
if response.status_code == 200:
    movie_data = response.json()
    print(movie_data)
else:
    print('Falha ao obter dados do filme.')'''
