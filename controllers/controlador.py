import frappe
import requests
from frappe.utils.data import today
from frappe.utils import flt
from frappe import _

# def update_pokemon_from_api():
#     frappe.errprint("entrando en metodo")
#     url = 'https://pokeapi.co/api/v2/pokemon'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         frappe.errprint(data)
        # if data:
        #     for pokemon_data in data["results"]:
        #         pokemon_name = pokemon_data["name"]
        #         print("________________________________________________________________", pokemon_name)
                # create a new document
                # doc = frappe.new_doc('Pokedex')
                # doc.nombre_pokemon = pokemon_name
                # doc.insert()


    #             # Si no existe, crear una nueva instancia
    #             if not pokemon:
    #                 pokemon = frappe.new_doc("Pokedex")

    #             # Establecer valores de los campos
    #             pokemon.nombre_pokemon = pokemon_name
    #             pokemon.route = ""  # Agrega el valor de ruta si lo deseas
    #             pokemon.publicado = True

    #             # Guardar el documento en la base de datos
    #             pokemon.save()

    #     frappe.msgprint("Pokémon actualizados correctamente desde la API.")
    # else:
    #     frappe.msgprint("Error al obtener los Pokémon de la API.")