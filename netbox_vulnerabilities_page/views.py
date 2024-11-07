import requests

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin

class VulnerabilitiesView(PermissionRequiredMixin, View):

    def get(self, request):

        data = requests.get(
            'https://services.nvd.nist.gov/rest/json/cves/2.0'
        )
        
        NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
        url_template = NVD_API_URL + "?startIndex={idx}"

        resp = requests.get(url_template.format(idx=268000))

        if not resp.ok:
            pass

        for vulnerability in data.get("vulnerabilities"):
            pprint(vulnerability)
        
        return render(
            request,
            "netbox_hello_world_page/helloworld.html",
            {
                "number": number,
                "query_params": query_params,
            },
        )