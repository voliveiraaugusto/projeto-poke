import requests

# URL base da PokeAPI
POKEAPI_BASE_URL = 'https://pokeapi.co/api/v2/'

# Função para obter o tipo de um Pokémon pelo nome
def obter_tipo_pokemon(nome):
    url = f'{POKEAPI_BASE_URL}pokemon-species/{nome.lower()}/'
    params = {'language': '9'}  # '9' é o código para português
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        tipo = None
        if isinstance(data['genera'], tuple):
            for entry in data['genera']:
                if entry['language']['name'] == 'pt':
                    tipo = entry['genus'].split()[-1]
                    break
        if tipo:
            return {"nome": nome, "tipo": tipo}
    return {"erro": "Pokémon não encontrado"}, 404

# Teste de conexão
def testar_conexao():
    nome_pokemon = 'charizard'  # Nome de um Pokémon existente
    resultado = obter_tipo_pokemon(nome_pokemon)
    if 'erro' in resultado:
        print(f"Erro ao obter o tipo do Pokémon {nome_pokemon}: {resultado['erro']}")
    else:
        print(f"Tipo do Pokémon {nome_pokemon}: {resultado['tipo']}")

if __name__ == '__main__':
    testar_conexao()
