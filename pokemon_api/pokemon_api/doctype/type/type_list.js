frappe.listview_settings['type'] = {
    onload: function(listview) {
        listview.page.add_inner_button(__('Cargar tipos'), function() {
            frappe.call({
                method: 'pokemon_api.pokemon_api.doctype.type.type.update_type_from_api',
                callback: function(response) {
                    if (response.message) {
                        frappe.show_alert('tipos cargadas exitosamente', 5);
                        listview.refresh();
                    }
                }
            });
        });
    }
};