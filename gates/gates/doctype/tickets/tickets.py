# Copyright (c) 2022, ahmed and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from gates.qr_generator import get_qr


class Tickets(Document):
    def before_save(self):
        for d in self.tickets:
            print(d.qr_number)
            d.qr = get_qr(d.qr_number)
