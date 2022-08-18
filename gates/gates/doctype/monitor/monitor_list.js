frappe.listview_settings['Monitor'] = {
    onload: function (listview) {
        listview.page.add_inner_button(__("Activate"), function () {
            toggle_gate('activate');
        });
        listview.page.add_inner_button(__("Deactivate"), function () {
            toggle_gate('deactivate');
        });
    }
}


function toggle_gate(task) {
    // frappe.show_progress("Activating Gates", 20, 100, "Please wait");
    let url = '';
    frappe.call({
        async: false,
        method: 'frappe.client.get',
        args: {
            'doctype': 'Gate Attributes',
        },
        callback: function (r) {
            console.log(r.message);
            url = r.message.url;
            console.log(url)
        }
    });
    frappe.call({
        async: false,
        method: 'frappe.client.get_list',
        args: {
            'doctype': 'Gate',
        },
        callback: function (r) {
            r.message.forEach((gate) => {
                console.log(gate)
                frappe.call({
                    async: false,
                    method: 'frappe.client.get',
                    args: {
                        'doctype': 'Gate',
                        'name': gate.name
                    },
                    callback: function (r) {
                        r.message.security.forEach((member) => {
                            if (member.security_member == frappe.user.name) {
                                var settings = {
                                    "url": url + 'live',
                                    "method": "POST",
                                    "timeout": 0,
                                    "headers": {
                                        "Content-Type": "application/json"
                                    },
                                    "data": JSON.stringify({
                                        "gate": gate.name,
                                        "task": task
                                    }),
                                };

                                $.ajax(settings).done(function (response) {
                                    // frappe.show_progress("Sending Tickets to Gates", 100, 100, "Please wait");
                                    // frappe.hide_progress();
                                    console.log(response);
                                });
                            }
                        });
                    }

                });
            });
        }
    });
}