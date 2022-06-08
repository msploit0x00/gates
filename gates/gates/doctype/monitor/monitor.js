// Copyright (c) 2022, ahmed and contributors
// For license information, please see license.txt

frappe.ui.form.on('Monitor', {
    refresh: function(frm) {
	let template = '<img src="' + frm.doc.image + '" width="500px" height="700px"/>';
	frm.set_df_property('prof_pic', 'options', frappe.render_template(template));
    }
})
