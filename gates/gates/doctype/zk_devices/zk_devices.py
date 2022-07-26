# Copyright (c) 2022, ahmed and contributors
# For license information, please see license.txt
import requests
import json
import frappe
from frappe.model.document import Document


class ZKDevices(Document):

    headers = {
        'Content-Type': 'application/json'
    }

    def after_insert(self):
        url = frappe.get_doc('Gate Attributes').url
        payload = json.dumps({
            "gate": self.gate,
            "ip": self.ip,
            "port": self.port,
            "passwd": self.passwd or ''
        })
        response = requests.request(
            "POST", url+'insertzk', headers=self.headers, data=payload)
        self.render_response(response)

    def after_delete(self):
        url = frappe.get_doc('Gate Attributes').url
        payload = json.dumps({
            "ip": self.ip
        })
        response = requests.request(
            "POST", url+'deletezk', headers=self.headers, data=payload)
        self.render_response(response)

    def before_rename(self, old, new, merge):
        url = frappe.get_doc('Gate Attributes').url
        payload = json.dumps({
            "old_ip": old,
            "ip": new
        })
        response = requests.request(
            "POST", url+'updatezk', headers=self.headers, data=payload)
        self.render_response(response)

    def on_update(self):
        url = frappe.get_doc('Gate Attributes').url
        if self.creation != self.modified:
            payload = json.dumps({
                "old_ip": self.ip,
                "port": self.port,
                "gate": self.gate,
                "passwd": self.passwd
            })
            response = requests.request(
                "POST", url+'updatezk', headers=self.headers, data=payload)
            self.render_response(response)

    def render_response(self, response):
        url = frappe.get_doc('Gate Attributes').url
        resp = json.loads(response.text)
        if not resp['success']:
            frappe.throw("Error happened")
