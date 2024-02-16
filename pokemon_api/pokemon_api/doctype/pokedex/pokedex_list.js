frappe.listview_settings['Pokedex'] = {
    onload: function(listview) {
        listview.page.add_inner_button(__('Cargar Pokémon'), function() {
            frappe.call({
                method: 'pokemon_api.pokemon_api.doctype.pokedex.pokedex.update_pokemon_from_api',
                callback: function(response) {
                    if (response.message) {
                        frappe.show_alert('Pokémon cargados exitosamente', 5);
                        listview.refresh();
                    }
                }
            });
        });
    }
};