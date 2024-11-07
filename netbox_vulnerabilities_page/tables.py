import django_tables2 as tables
from netbox.tables import NetBoxTable

class DeviceTable(NetBoxTable):
    
    cve_id = tables.Column(verbose_name='cve_id')
    product = tables.Column(verbose_name='product')
    vendor = tables.Column(verbose_name='vendor')
    product_version = tables.Column(verbose_name='product_version')
    cvss_metric = tables.Column(verbose_name='cvss_metric')