// Copyright (c) 2022, ahmed and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tickets', {
	refresh: function (frm) {
		frm.add_custom_button(__('Activate Gate'), function () {
			if (frm.doc.tickets && frm.doc.tickets.length > 0) {
				let myHeaders = new Headers();
				myHeaders.append("Content-Type", "application/json");
				let requestOptions = {
					method: 'POST',
					headers: myHeaders,
					redirect: 'follow'
				};
				let raw = JSON.stringify({ "ticket_num": frm.doc.tickets[0].qr_number });
				requestOptions['body'] = raw
				frappe.show_progress("Sending Tickets to Gates", 20, 100, "Please wait");
				fetch("http://192.168.2.250/gates/addticket", requestOptions)
					.then(response => response.json())
					.then(result => {
						if (result.success) {
							frappe.show_progress("Sending Tickets to Gates", 100, 100, "Please wait");
							frappe.hide_progress();
						}
					})
					.catch(error => {
						frappe.throw(error);
					});
			}
		})
	},
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
