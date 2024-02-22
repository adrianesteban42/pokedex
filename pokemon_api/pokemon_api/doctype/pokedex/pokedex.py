import frappe
import requests
from frappe.website.website_generator import WebsiteGenerator

class Pokedex(WebsiteGenerator):
	
	pass

# metodo para cargar los pokemon de la api
@frappe.whitelist(allow_guest=True)
def update_pokemon_from_api():
	try:
		url = 'https://pokeapi.co/api/v2/pokemon'
		response = requests.get(url)

		if response.status_code == 200:
			data = response.json()

			if data:

				for pokemon_data in data["results"]:
					pokemon_url = pokemon_data["url"]
					# existePokemon = frappe.get_cached_doc("Pokedex", filters={"name_pokemon": pokemon_data["name"]})
					# frappe.errprint(existePokemon)
					# if not existePokemon:
					response = requests.get(pokemon_url)					

					if response.status_code == 200:
						pokemon = response.json()
						frappe.errprint(pokemon["name"])
						doc = frappe.new_doc('Pokedex')
						frappe.errprint(pokemon["name"])
						doc.name_pokemon = pokemon["name"]

						# abilities = [{"ability": ability["ability"]["name"]} for ability in pokemon["abilities"]]
						# doc.extend("ability", abilities)

						abilities = []
						for ability in pokemon["abilities"]:
							ability_name = ability["ability"]["name"]
							ability_doc = frappe.get_doc("Ability", {"name": ability_name})
							
						doc.ability = abilities

						# types = [{"type": type["type"]["name"]} for type in pokemon["types"]]
						# doc.extend("type", types)

						doc.insert()
					else:
						frappe.errprint("no entro")
	except Exception as e:
		frappe.log_error(f'Error al obtener datos de la API de PokeAPI: {e}')