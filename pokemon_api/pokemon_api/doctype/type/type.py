# Copyright (c) 2024, Adrian Martinez and contributors
# For license information, please see license.txt

import frappe
import requests
from frappe.website.website_generator import WebsiteGenerator


class type(WebsiteGenerator):
	pass

@frappe.whitelist(allow_guest=True)
def update_type_from_api():
	try:
		frappe.errprint("entrando en metodo")
		url = 'https://pokeapi.co/api/v2/type?limit=20'
		response = requests.get(url)

		if response.status_code == 200:
			data = response.json()
			frappe.errprint(data)
			if data:
				for type_data in data["results"]:
					existeType = frappe.get_cached_doc('type', filters={"name_type": type_data["name"]}, fields=["name"])
					if not existeType:
						doc = frappe.new_doc('type')
						doc.name_type = type_data["name"]
						doc.insert()
	except Exception as e:
		frappe.log_error(f'Error al obtener datos de la API de PokeAPI: {e}')