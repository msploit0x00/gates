# Copyright (c) 2022, ahmed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import time
class Monitor(Document):
        def after_insert(self):
                # frappe.local.response["type"] = "redirect"
                # frappe.local.response["location"] = "/desk"
                print("\n\n\n\n\n\n\n\n\n\n\n\n")
                # time.sleep(5)
                # frappe.publish_realtime(event='eval_js', message=f'frappe.set_route("Form", "Monitor/{self.name}")')
