data = {
    "count": 268486,
    "next": "http://ubuntu.home/api/cve/?page=101",
    "previous": "http://ubuntu.home/api/cve/?page=99",
    "results": [
        {
            "created_at": "2024-01-11T06:49:34.348000Z",
            "updated_at": "2024-11-06T19:01:00.473000Z",
            "cve_id": "CVE-2023-6699",
            "description": "The WP Compress – Image Optimizer [All-In-One] plugin for WordPress is vulnerable to Directory Traversal in all versions up to, and including, 6.10.33 via the css parameter. This makes it possible for unauthenticated attackers to read the contents of arbitrary files on the server, which can contain sensitive information.",
            "nvd_versions": [
                {
                    "vendor": "wpcompress",
                    "product": "wp_compress",
                    "version": None,
                    "vulnerable": True,
                    "version_end_including": "6.10.33"
                }
            ]
        },
        {
            "created_at": "2023-06-13T18:40:14.005000Z",
            "updated_at": "2024-11-06T18:59:34.182000Z",
            "cve_id": "CVE-2023-34115",
            "description": "Buffer copy without checking size of input  in Zoom Meeting SDK  before 5.13.0 may allow an authenticated user to potentially enable a denial of service via local access. This issue may result in the Zoom Meeting SDK to crash and need to be restarted.",
            "nvd_versions": [
                {
                    "vendor": "zoom",
                    "product": "meeting_sdk",
                    "version": None,
                    "vulnerable": True,
                    "version_end_including": None
                }
            ]
        },
        {
            "created_at": "2024-01-11T08:32:36.170000Z",
            "updated_at": "2024-11-06T18:56:25.048000Z",
            "cve_id": "CVE-2023-6994",
            "description": "The List category posts plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the plugin's 'catlist' shortcode in all versions up to, and including, 0.89.3 due to insufficient input sanitization and output escaping on user supplied attributes. This makes it possible for authenticated attackers with contributor-level and above permissions to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page.",
            "nvd_versions": [
                {
                    "vendor": "fernandobriano",
                    "product": "list_category_posts",
                    "version": None,
                    "vulnerable": True,
                    "version_end_including": "0.89.3"
                }
            ]
        },
        {
            "created_at": "2024-01-11T08:32:37.107000Z",
            "updated_at": "2024-11-06T18:55:13.392000Z",
            "cve_id": "CVE-2023-6567",
            "description": "The LearnPress plugin for WordPress is vulnerable to time-based SQL Injection via the ‘order_by’ parameter in all versions up to, and including, 4.2.5.7 due to insufficient escaping on the user supplied parameter and lack of sufficient preparation on the existing SQL query.  This makes it possible for unauthenticated attackers to append additional SQL queries into already existing queries that can be used to extract sensitive information from the database.",
            "nvd_versions": [
                {
                    "vendor": "thimpress",
                    "product": "learnpress",
                    "version": None,
                    "vulnerable": True,
                    "version_end_including": None
                }
            ]
        },
        {
            "created_at": "2024-01-11T08:32:37.581000Z",
            "updated_at": "2024-11-06T18:53:38.358000Z",
            "cve_id": "CVE-2023-6828",
            "description": "The Contact Form, Survey & Popup Form Plugin for WordPress –  ARForms Form Builder plugin for WordPress is vulnerable to Stored Cross-Site Scripting via the ‘ arf_http_referrer_url’ parameter in all versions up to, and including, 1.5.8 due to insufficient input sanitization and output escaping. This makes it possible for unauthenticated attackers to inject arbitrary web scripts in pages that will execute whenever a user accesses an injected page.",
            "nvd_versions": [
                {
                    "vendor": "reputeinfosystems",
                    "product": "arforms_form_builder",
                    "version": None,
                    "vulnerable": True,
                    "version_end_including": "1.5.8"
                }
            ]
        },
        {
            "created_at": "2023-06-27T19:25:24.382000Z",
            "updated_at": "2024-11-06T18:53:34.333000Z",
            "cve_id": "CVE-2023-30993",
            "description": "IBM Cloud Pak for Security (CP4S) 1.9.0.0 through 1.9.2.0 could allow an attacker with a valid API key for one tenant to access data from another tenant's account.  IBM X-Force ID:  254136.",
            "nvd_versions": [
                {
                    "vendor": "ibm",
                    "product": "cloud_pak_for_security",
                    "version": None,
                    "vulnerable": True,
                    "version_end_including": "1.9.2.0"
                }
            ]
        },
        {
            "created_at": "2024-04-16T21:26:14.451000Z",
            "updated_at": "2024-11-06T18:53:24.237000Z",
            "cve_id": "CVE-2024-21048",
            "description": "Vulnerability in the Oracle Web Applications Desktop Integrator product of Oracle E-Business Suite (component: XML input).  Supported versions that are affected are 12.2.3-12.2.13. Easily exploitable vulnerability allows low privileged attacker with network access via HTTP to compromise Oracle Web Applications Desktop Integrator.  Successful attacks of this vulnerability can result in  unauthorized read access to a subset of Oracle Web Applications Desktop Integrator accessible data. CVSS 3.1 Base Score 4.3 (Confidentiality impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N).",
            "nvd_versions": []
        },
        {
            "created_at": "2024-04-16T00:00:00Z",
            "updated_at": "2024-11-06T18:53:23.488000Z",
            "cve_id": "CVE-2024-21056",
            "description": "Vulnerability in the MySQL Server product of Oracle MySQL (component: Server: DML).  Supported versions that are affected are 8.0.34 and prior. Easily exploitable vulnerability allows high privileged attacker with network access via multiple protocols to compromise MySQL Server.  Successful attacks of this vulnerability can result in unauthorized ability to cause a hang or frequently repeatable crash (complete DOS) of MySQL Server. CVSS 3.1 Base Score 4.9 (Availability impacts).  CVSS Vector: (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:H).",
            "nvd_versions": []
        },
        {
            "created_at": "2023-06-28T01:48:22.850000Z",
            "updated_at": "2024-11-06T18:52:24.792000Z",
            "cve_id": "CVE-2023-3427",
            "description": "The Salon Booking System plugin for WordPress is vulnerable to Cross-Site Request Forgery in versions up to, and including, 8.4.6. This is due to missing or incorrect nonce validation on the 'save_customer' function. This makes it possible for unauthenticated attackers to change the admin role to customer or change the user meta to arbitrary values via a forged request, granted they can trick a site administrator into performing an action such as clicking on a link.",
            "nvd_versions": [
                {
                    "vendor": "salonbookingsystem",
                    "product": "salon_booking_system",
                    "version": None,
                    "vulnerable": True,
                    "version_end_including": "8.4.6"
                }
            ]
        },
        {
            "created_at": "2024-01-11T08:32:41.439000Z",
            "updated_at": "2024-11-06T18:52:23.504000Z",
            "cve_id": "CVE-2023-6636",
            "description": "The Greenshift – animation and page builder blocks plugin for WordPress is vulnerable to arbitrary file uploads due to missing file type validation on the 'gspb_save_files' function in versions up to, and including, 7.6.2. This makes it possible for authenticated attackers with administrator-level capabilities or above, to upload arbitrary files on the affected site's server which may make remote code execution possible.",
            "nvd_versions": [
                {
                    "vendor": "greenshiftwp",
                    "product": "greenshift_-_animation_and_page_builder_blocks",
                    "version": None,
                    "vulnerable": True,
                    "version_end_including": "7.6.2"
                }
            ]
        }
    ]
}

import random
import requests
import json

from .tables import DeviceTable

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin

class VulnerabilitiesView(PermissionRequiredMixin, View):

    permission_required = "ipam.view_prefix"

    def get(self, request):

        # data = requests.get(
        #     'https://services.nvd.nist.gov/rest/json/cves/2.0'
        # )
        
        # NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
        # url_template = NVD_API_URL + "?startIndex={idx}"

        # resp = requests.get(url_template.format(idx=268000))

        # if not resp.ok:
        #     pass


        
        payload = list()
        
        for vulnerability in data.get('results'):
            vuln = {
                'cve_id': vulnerability.get('cve_id'),
                'product': 'product',
                'vendor': 'vendor',
                'product_version': 1.1,
                'cvss_metric': round(random.uniform(1, 10), 2)
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