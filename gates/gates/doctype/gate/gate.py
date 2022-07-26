# Copyright (c) 2022, ahmed and contributors
# For license information, please see license.txt

import requests
import json
import frappe
from frappe.model.document import Document


class Gate(Document):
    headers = {
        'Content-Type': 'application/json'
    }

    def after_insert(self):
        url = frappe.get_doc('Gate Attributes').url
        payload = json.dumps({
            "gate": self.name
        })

        response = requests.request(
            "POST", url+'insertgate', headers=self.headers, data=payload)
        self.render_response(response)

    def after_delete(self):
        # TODO delete gate and devices related to this gate in django app
        url = frappe.get_doc('Gate Attributes').url
        payload = json.dumps({
            "gate": self.name
        })
        response = requests.request(
            "POST", url+'deletegate', headers=self.headers, data=payload)
        self.render_response(response)

    def before_rename(self, old, new, merge):
        url = frappe.get_doc('Gate Attributes').url
        print(f"old one {old} and the new one {new}")
        payload = json.dumps({
            "old_name": old,
            "name": new
        })
        response = requests.request(
            "POST", url+'updategate', headers=self.headers, data=payload)
        self.render_response(response)

    def render_response(self, response):
        url = frappe.get_doc('Gate Attributes').url
        resp = json.loads(response.text)
        if not resp['success']:
            frappe.throw("Error happened")
