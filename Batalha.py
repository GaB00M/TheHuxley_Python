red_pokemons = []
blue_pokemons = []

for _ in range(6):
    nome = input()
    id_pokemon = int(input())
    ataque = int(input())
    vida = int(input())
    
    red_pokemons.append({
        "nome": nome,
        "id": id_pokemon,
        "ataque": ataque,
        "vida": vida
    })

for _ in range(6):
    nome = input()
    id_pokemon = int(input())
    ataque = int(input())
    vida = int(input())
    
    blue_pokemons.append({
        "nome": nome,
        "id": id_pokemon,
        "ataque": ataque,
        "vida": vida
    })

red_pokemons.sort(key=lambda x: (x["ataque"], -x["id"]), reverse=True)
pokemon_red = red_pokemons[0]

blue_pokemons.sort(key=lambda x: (x["ataque"], -x["id"]), reverse=True)
pokemon_blue = blue_pokemons[0]

if pokemon_red["ataque"] > pokemon_blue["ataque"]:
    vencedor = "Red"
elif pokemon_red["ataque"] < pokemon_blue["ataque"]:
    vencedor = "Blue"
else:
    vencedor = "Empate"

print("Pokemon do Red:", pokemon_red["nome"])
print("Pokemon do Blue:", pokemon_blue["nome"])
print("Vencedor:", vencedor)