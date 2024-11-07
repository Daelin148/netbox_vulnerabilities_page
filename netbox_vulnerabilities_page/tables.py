import django_tables2 as tables
from netbox.tables import NetBoxTable

class DeviceTable(NetBoxTable):
    
    cve_id = tables.Column()
    product = tables.Column()
    vendor = tables.Column()
    product_version = tables.Column()
    cvss_metric = tables.Column()