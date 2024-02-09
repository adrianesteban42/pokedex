import frappe
import requests
import frappe
import requests
from frappe.utils.data import today
from frappe.utils import flt
from frappe import _

def update_pokemon_from_api():
    url = 'https://pokeapi.co/api/v2/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            for pokemon_data in data:
                pokemon = frappe.new_doc("Pokemon")
                pokemon.nombre_pokemon = pokemon_data["name"]
                pokemon.insert()
                frappe.db.commit()
        frappe.msgprint("Pokémon actualizados correctamente desde la API.")
    else:
        frappe.msgprint("Error al obtener los Pokémon de la API.")
