// Copyright (c) 2022, ahmed and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tickets', {
	// refresh: function(frm) {

	// }
	generate: function (frm) {
		let d = new Date();
		frm.doc.tickets = [];
		for (let i = 0; i < frm.doc.no_tickets; i++) {
			frm.add_child('tickets', {
				member_no: frm.doc.member_no,
				qr_number: (parseInt(frm.doc.member_no) * 1000) + 1,
				date: d.toISOString().split('T')[0]
			})
			refresh_field('tickets')
		}
	}
});
