import frappe

@frappe.whitelist()
def add_member(pin):
    exist = frappe.db.exists("member_lisr", {"pin": pin})
    if exist:
        member = frappe.get_doc("member_lisr", {"pin": pin})
        rec = frappe.new_doc("Monitor")
        rec.name1 = member.name1
        rec.card_number = member.card_number
        rec.image = member.image
        rec.pin = member.pin
            
        rec.insert()
        frappe.db.commit()
        return {'success': True}
    return {'success': False, 'message': "Member Doesn't exists"}
