import frappe
import requests
from frappe.website.website_generator import WebsiteGenerator

class Pokedex(WebsiteGenerator):
	
	pass

# metodo para cargar los pokemon de la api
@frappe.whitelist(allow_guest=True)
def update_pokemon_from_api():
	frappe.errprint("entrando en metodo")
	url = 'https://pokeapi.co/api/v2/pokemon'
	response = requests.get(url)

	if response.status_code == 200:
		data = response.json()
		frappe.errprint(data)
		if data:
			# 
			for pokemon_data in data["results"]:
				pokemon_url = pokemon_data["url"]
				existeAbility = frappe.get_cached_doc('Ability', filters={"name_ability": pokemon_data["url"]}, fields=["name"])
				if not existeAbility:		
					doc = frappe.new_doc('Pokedex')
					doc.nombre_pokemon = pokemon_data["name"]
					for pokemon in pokemon_url["abilities"]:
						doc.ability = pokemon[""]
						 
						 
					doc.insert()