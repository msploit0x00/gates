import frappe
import datetime


@frappe.whitelist()
def get_family(name):
    exist = frappe.db.exists("Gates_Activation_table", {"name1": name})
    if exist:
        parent = frappe.get_doc("Gates_Activation_table", {
                                "name1": name}).parent
        return {"success": True, "message": parent}
    return {"success": False, "message": "Couldn't find member check his name"}


@frappe.whitelist()
def add_member(pin, gate):
    exist = frappe.db.exists("Gates_Activation_table", {"pin": pin})
    if exist:
        member = frappe.get_doc("Gates_Activation_table", {"pin": pin})
        print(member)
        gate_details = frappe.get_doc("Gate", gate)

        record = frappe.new_doc('Monitor')
        record.name1 = member.name1
        record.card_number = member.card_no
        record.image = member.img
        record.pin = member.pin
        record.gate = gate_details.gate_name

        record.insert()
        frappe.db.commit()
        for security in gate_details.security:
            frappe.publish_realtime(event='eval_js', message=f'frappe.set_route("Form", "Monitor/{record.name}")',
                                    user=security.security_member)

        return {'success': True}
    return {'success': False, 'message': "Member Doesn't exists"}


def clean_records():
    delta = datetime.datetime.now() - datetime.timedelta(minutes=1)
    records = frappe.get_list("Monitor", {'creation': ("<", delta)})

    for rec in records:
        frappe.db.delete("Monitor", rec)
    frappe.db.commit()
    return {'success': True}
