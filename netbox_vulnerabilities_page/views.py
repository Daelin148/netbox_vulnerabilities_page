import random
import requests
import json

from .tables import DeviceTable

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin

class VulnerabilitiesView(PermissionRequiredMixin, View):

    def get(self, request):

        # data = requests.get(
        #     'https://services.nvd.nist.gov/rest/json/cves/2.0'
        # )
        
        # NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
        # url_template = NVD_API_URL + "?startIndex={idx}"

        # resp = requests.get(url_template.format(idx=268000))

        # if not resp.ok:
        #     pass

        with open('vulnerabilities.json') as file:
            data = json.load(file)
        
        payload = list()
        
        for vulnerability in data.get('vulnerabilities'):
            vuln = {
                'cve_id': vulnerability.get('cve').get('id'),
                'product': 'product',
                'vendor': 'vendor',
                'product_version': 1.1,
                'cvss_metric': round(random.uniform(1, 10))
            }
            payload.append(vuln)
            
        table = DeviceTable(payload)
        
        return render(
            request,
            "netbox_vulnerabilities_page/vulnerabilities.html",
            {
                "table": table,
            },
        )