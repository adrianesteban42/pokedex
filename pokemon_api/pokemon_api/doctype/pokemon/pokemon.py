# Copyright (c) 2024, Adrian Martinez and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from controllers.controlador import update_pokemon_from_api



class Pokemon(WebsiteGenerator):
	
	def get_list_context(context):
		update_pokemon_from_api()