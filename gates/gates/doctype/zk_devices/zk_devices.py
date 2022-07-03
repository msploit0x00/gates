# Copyright (c) 2022, ahmed and contributors
# For license information, please see license.txt
import requests
import json
import frappe
from frappe.model.document import Document


class ZKDevices(Document):
        url = frappe.get_doc('Gate Attributes').url
        headers = {
                'Content-Type': 'application/json'
        }

        def after_insert(self):
                payload = json.dumps({
                        "gate": self.gate,
                        "ip": self.ip,
                        "port": self.port,
                        "passwd": self.passwd or ''
                })
                response = requests.request("POST", self.url+'insertzk', headers=self.headers, data=payload)
                self.render_response(response)
                
        def after_delete(self):
                payload = json.dumps({
                        "ip": self.ip
                })
                response = requests.request("POST", self.url+'deletezk', headers=self.headers, data=payload)
                self.render_response(response)
                
        def before_rename(self, old, new, merge):
                payload = json.dumps({
                        "old_ip": old,
                        "ip": new
                })
                response = requests.request("POST", self.url+'updatezk', headers=self.headers, data=payload)
                self.render_response(response)

        def on_update(self):
                if self.creation != self.modified:
                        payload = json.dumps({
                                "old_ip": self.ip,
                                "port": self.port,
                                "gate": self.gate,
                                "passwd": self.passwd
                        });
                        response = requests.request("POST", self.url+'updatezk', headers=self.headers, data=payload)
                        self.render_response(response)
                        
        def render_response(self, response):
                resp = json.loads(response.text)
                if not resp['success']:
                        frappe.throw("Error happened")
