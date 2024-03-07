from flask import Flask, jsonify
import random

app = Flask(__name__)

# Dados simulados dos tipos de Pokémon
pokemon_types = {
    'fire': ['Charmander', 'Vulpix', 'Growlithe'],
    'water': ['Squirtle', 'Psyduck', 'Magikarp'],
    'grass': ['Bulbasaur', 'Oddish', 'Bellsprout'],
    'electric': ['Pikachu', 'Voltorb', 'Electabuzz'],
    'normal': ['Rattata', 'Meowth', 'Eevee']
}

# Função para obter o tipo de um Pokémon pelo nome
def get_pokemon_type(name):
    for type_name, pokemon_list in pokemon_types.items():
        if name in pokemon_list:
            return type_name
    return None

# Função para obter um Pokémon aleatório de um tipo específico
def get_random_pokemon_by_type(type):
    pokemon_list = pokemon_types.get(type, [])
    if pokemon_list:
        return random.choice(pokemon_list)
    return None

# Função para obter o Pokémon com o nome mais longo de um determinado tipo
def get_longest_name_pokemon_by_type(type):
    pokemon_list = pokemon_types.get(type, [])
    if pokemon_list:
        longest_name_pokemon = max(pokemon_list, key=len)
        return longest_name_pokemon
    return None

# Função para obter um Pokémon aleatório com letras específicas no nome e do tipo mais forte com base no clima
def get_random_pokemon_by_letter_and_weather(temperature):
    if temperature >= 30:
        weather_type = 'fire'
    elif temperature >= 20:
        weather_type = 'grass'
    elif temperature >= 10:
        weather_type = 'normal'
    elif temperature >= 0:
        weather_type = 'water'
    else:
        weather_type = 'ice'
    
    pokemon_list = pokemon_types.get(weather_type, [])
    filtered_pokemon = [p for p in pokemon_list if any(letter in p for letter in ['I', 'A', 'M'])]
    if filtered_pokemon:
        return random.choice(filtered_pokemon)
    return None

# Endpoint para obter o tipo de um Pokémon pelo nome
@app.route('/pokemon/type/<name>', methods=['GET'])
def get_pokemon_type_endpoint(name):
    """
    Endpoint para obter o tipo de um Pokémon pelo nome.
    URL completa: http://127.0.0.1:5000/pokemon/type/<name>
    """
    pokemon_type = get_pokemon_type(name)
    if pokemon_type:
        return jsonify({'name': name, 'type': pokemon_type}), 200
    else:
        return jsonify({'error': 'Pokemon not found!'}), 404

# Endpoint para obter um Pokémon aleatório de um tipo específico
@app.route('/pokemon/random/<type>', methods=['GET'])
def get_random_pokemon_by_type_endpoint(type):
    """
    Endpoint para obter um Pokémon aleatório de um tipo específico.
    URL completa: http://127.0.0.1:5000/pokemon/random/<type>
    """
    pokemon = get_random_pokemon_by_type(type)
    if pokemon:
        return jsonify({'type': type, 'pokemon': pokemon}), 200
    else:
        return jsonify({'error': 'Type not found!'}), 404

# Endpoint para obter o Pokémon com o nome mais longo de um determinado tipo
@app.route('/pokemon/longest_name/<type>', methods=['GET'])
def get_longest_name_pokemon_by_type_endpoint(type):
    """
    Endpoint para obter o Pokémon com o nome mais longo de um determinado tipo.
    URL completa: http://127.0.0.1:5000/pokemon/longest_name/<type>
    """
    pokemon = get_longest_name_pokemon_by_type(type)
    if pokemon:
        return jsonify({'type': type, 'longest_name_pokemon': pokemon}), 200
    else:
        return jsonify({'error': 'Type not found!'}), 404

# Endpoint para obter um Pokémon aleatório com letras específicas no nome e do tipo mais forte com base no clima
@app.route('/pokemon/letter_and_weather/<int:temperature>', methods=['GET'])
def get_random_pokemon_by_letter_and_weather_endpoint(temperature):
    """
    Endpoint para obter um Pokémon aleatório com letras específicas no nome e do tipo mais forte com base no clima.
    URL completa: http://127.0.0.1:5000/pokemon/letter_and_weather/<temperature>
    """
    pokemon = get_random_pokemon_by_letter_and_weather(temperature)
    if pokemon:
        return jsonify({'temperature': temperature, 'pokemon': pokemon}), 200
    else:
        return jsonify({'error': 'No Pokémon found with specified criteria!'}), 404

if __name__ == '__main__':
    app.run(debug=True)
