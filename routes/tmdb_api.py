from flask import Blueprint, jsonify, request
import requests
from config.database import db

api_key = 'TMDB KEY'
tmdb_bp = Blueprint("tmdb_bp", __name__)


@tmdb_bp.route("/tmdb/logo", methods=["GET"])
def get_content_logo(content_type, content_id):
    if content_type == 'movie':
        url = f'https://api.themoviedb.org/3/movie/{content_id}?api_key={api_key}'
    elif content_type == 'tv':
        url = f'https://api.themoviedb.org/3/tv/{content_id}?api_key={api_key}'
    else:
        return jsonify({'error': 'Tipo de conteúdo inválido'}), 400

    response = requests.get(url)

    if response.status_code == 200:
        content_data = response.json()

        if 'logo_path' in content_data and content_data['logo_path']:
            base_url = 'https://image.tmdb.org/t/p/original'
            logo_url = f'{base_url}{content_data["logo_path"]}'
            return jsonify({'logo_url': logo_url})
        else:
            return jsonify({'error': 'Logo não encontrada'}), 404
    else:
        return jsonify({'error': 'Falha ao obter detalhes do conteúdo'}), 500


def get_content_details(content_type, content_id):
    if content_type == 'movie':
        url = f'https://api.themoviedb.org/3/movie/{content_id}?api_key={api_key}'
    elif content_type == 'tv':
        url = f'https://api.themoviedb.org/3/tv/{content_id}?api_key={api_key}'
    else:
        return jsonify({'error': 'Tipo de conteúdo inválido'}), 400

    response = requests.get(url)

    if response.status_code == 200:
        content_data = response.json()
        return jsonify(content_data)
    else:
        return jsonify({'error': 'Falha ao obter detalhes do conteúdo'}), 500


def get_popular_content(content_type):

    if content_type == 'movie':
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=pt-BR&page=1'
    elif content_type == 'tv':
        url = f'https://api.themoviedb.org/3/tv/popular?api_key={api_key}&language=pt-BR&page=1'
    else:
        return jsonify({'error': 'Tipo de conteúdo inválido'}), 400

    response = requests.get(url)

    if response.status_code == 200:
        popular_content_data = response.json()

        if 'results' in popular_content_data:
            return jsonify(popular_content_data['results'])
        else:
            return jsonify({'error': 'Nenhum conteúdo popular encontrado'}), 404
    else:
        return jsonify({'error': 'Falha ao obter conteúdo popular'}), 500
