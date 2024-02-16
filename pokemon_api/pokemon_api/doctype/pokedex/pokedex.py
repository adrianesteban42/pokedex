import frappe
import requests
from frappe.website.website_generator import WebsiteGenerator

class Pokedex(WebsiteGenerator):
	
	pass


@frappe.whitelist(allow_guest=True)
def update_pokemon_from_api():
	frappe.errprint("entrando en metodo")
	url = 'https://pokeapi.co/api/v2/pokemon'
	response = requests.get(url)

	if response.status_code == 200:
		data = response.json()
		frappe.errprint(data)
		if data:
			for pokemon_data in data["results"]:
				pokemon_url = pokemon_data["url"]
				
				pokemon_name = pokemon_data["name"]
				doc = frappe.new_doc('Pokedex')
				doc.nombre_pokemon = pokemon_name
				doc.insert()