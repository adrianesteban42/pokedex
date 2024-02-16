// Copyright (c) 2024, Adrian Martinez and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Pokedex", {
// 	refresh(frm) {

frappe.ui.form.on('Pokedex', {
    refresh: function(frm) {
        frm.add_custom_button('Cargar Pokemon', function() {
            frappe.call ({
                method: 'pokemon_api.pokemon_api.doctype.pokedex.pokedex.update_pokemon_from_api'
            })
        })
    }
});

// 	},
// });
