import frappe
import datetime

@frappe.whitelist()
def add_member(pin):
    exist = frappe.db.exists("member_lisr", {"pin": pin})
    if exist:
        member = frappe.get_doc("member_lisr", {"pin": pin})
        record = frappe.new_doc("Monitor")
        record.name1 = member.name1
        record.card_number = member.card_number
        record.image = member.image
        record.pin = member.pin
            
        record.insert()
        frappe.db.commit()
        return {'success': True}
    return {'success': False, 'message': "Member Doesn't exists"}


def clean_records():
    delta = datetime.datetime.now() - datetime.timedelta(minutes=1)
    records = frappe.get_list("Monitor", {'creation': ("<", delta)})

    for rec in records:
        frappe.db.delete("Monitor", rec)
    frappe.db.commit()
    return {'success': True}
