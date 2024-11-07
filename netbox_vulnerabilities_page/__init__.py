from netbox.plugins import PluginConfig

from .version import __version__

class VulnerabilitiesPageConfig(PluginConfig):
    name = "netbox_vulnerabilities_page"
    verbose_name = "Vulnerabilities page"
    description = "An example NetBox plugin"
    version = __version__
    author = "Me"
    # base_url is what comes after /plugins/ in the URL
    base_url = "vulnerabilities"
    required_settings = []
    default_settings = {}

config = VulnerabilitiesPageConfig