// Copyright (c) 2022, ahmed and contributors
// For license information, please see license.txt

frappe.ui.form.on('Monitor', {
    refresh: function (frm) {
        let template = '<img src="' + frm.doc.image + '" width="500px" height="700px"/>';
        frm.set_df_property('prof_pic', 'options', frappe.render_template(template));

        frm.add_custom_button(__('Show Family'), function () {
            frappe.call({
                method: 'gates.api.get_family',
                args: {
                    'name': frm.doc.name1
                },
                callback: function (r) {
                    let parent = r.message.message
                    frappe.call({
                        async: false,
                        method: 'frappe.client.get',
                        args: {
                            'doctype': 'Gates Actiivation',
                            'name': parent
                        },
                        callback: function (resp) {
                            // frm.doc.family = resp.message.gates_activation_list;
                            frm.doc.gates_activation_list = []
                            for (let m of resp.message.gates_activation_list) {
                                frm.add_child("family", { ...m })
                            }
                            refresh_field("family");
                        }
                    })
                }
            })
        });
    }

})
