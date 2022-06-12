# Copyright (c) 2022, ahmed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Gate(Document):
        def after_insert(self):
                #TODO send gate name to django app
                print(f"\n\n\n\n\n\n\n\n inserted \n\n\n\n {self}")

        def after_delete(self):
                #TODO delete gate and devices related to this gate in django app
                print(f"\n\n\n\n\n\n\n\n deleted \n\n\n\n {self}")

        def before_rename(self, old, new, merge):
                print(f"old one {old} and the new one {new}")
