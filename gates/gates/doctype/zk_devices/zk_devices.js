// // Copyright (c) 2022, ahmed and contributors
// // For license information, please see license.txt

// frappe.ui.form.on('ZK Devices', {
//     before_save: function(frm) {
// 	let myHeaders = new Headers();
// 	myHeaders.append("Content-Type", "application/json");
// 	if(!frm.is_new()) {
// 	    let myHeaders = new Headers();
// 	    myHeaders.append("Content-Type", "application/json");
// 	    let raw = JSON.stringify({
// 		"old_ip": frm.doc.ip,
// 		"port": frm.doc.port,
// 		"gate": frm.doc.gate,
// 		"passwd": frm.doc.passwd
// 	    });
// 	    let requestOptions = {
// 		method: 'POST',
// 		headers: myHeaders,
// 		body: raw,
// 		redirect: 'follow'
// 	    };
// 	    let result = 
// 	    frappe.call({
// 		async: false,
// 		method: 'frappe.client.get_value',
// 		args: {'doctype':'Gate Attributes', 'fieldname': ['url']},
// 		callback: function(r) {
// 		    var url = r.message.url;
// 		    frappe.run_serially([
// 			() => {
// 			    fetch(url+"updatezk", requestOptions)
// 				.then(response =>response.json())
// 				.then(result => {
// 				    if (!result['success']) {
// 					frappe.throw("Error Happened")
// 				    }
// 				})
// 				.catch(error => frappe.throw(error));
// 			}
// 		    ]);
// 		}
// 	    })
// 	}   
//     },
// });



// // var raw = JSON.stringify({
// //     "old_ip": "192.168.3.324",
// //     "ip": "192.168.6.201",
// //     "port": "5532",
// //     "gate": "Gate 4"
// // });

// // var requestOptions = {
// //     method: 'POST',
// //     headers: myHeaders,
// //     body: raw,
// //     redirect: 'follow'
// // };

// // fetch("http://192.168.2.250/gates/updatezk", requestOptions)
// //     .then(response => response.text())
// //     .then(result => console.log(result))
// //     .catch(error => console.log('error', error));
