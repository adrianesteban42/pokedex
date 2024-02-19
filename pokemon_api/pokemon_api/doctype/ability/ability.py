# Copyright (c) 2024, Adrian Martinez and contributors
# For license information, please see license.txt

import frappe
import requests
from frappe.website.website_generator import WebsiteGenerator


class Ability(WebsiteGenerator):
	pass

@frappe.whitelist(allow_guest=True)
def update_ability_from_api():
	try:
		frappe.errprint("entrando en metodo")
		url = 'https://pokeapi.co/api/v2/ability?limit=367'
		response = requests.get(url)

		if response.status_code == 200:
			data = response.json()
			frappe.errprint(data)
			if data:
				for ability_data in data["results"]:
					ability_url = ability_data["url"]
					existeAbility = frappe.get_cached_doc('Ability', filters={"name_ability": ability_data["name"]}, fields=["name"])
					if not existeAbility:
						doc = frappe.new_doc('Ability')
						doc.name_ability = ability_data["name"]
						response = requests.get(ability_url)
						if response.status_code == 200:
							data = response.json()
							for effects in data["effect_entries"]:
								if effects['language']['name'] == 'en':
									doc.effect = effects["effect"]
						doc.insert()
	except Exception as e:
		frappe.log_error(f'Error al obtener datos de la API de PokeAPI: {e}')
		
