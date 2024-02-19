frappe.listview_settings['Ability'] = {
    onload: function(listview) {
        listview.page.add_inner_button(__('Cargar Abilidades'), function() {
            frappe.call({
                method: 'pokemon_api.pokemon_api.doctype.ability.ability.update_ability_from_api',
                callback: function(response) {
                    if (response.message) {
                        frappe.show_alert('Abilidades cargadas exitosamente', 5);
                        listview.refresh();
                    }
                }
            });
        });
    }
};