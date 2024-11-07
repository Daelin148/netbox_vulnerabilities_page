from netbox.plugins import PluginMenu, PluginMenuItem

menuitem1 = PluginMenuItem(

    link="plugins:netbox_vulnerabilities_page:vulnerabilities",
    link_text="Vulnerabilities",
)

menu = PluginMenu(
    label="Vulnerabilities",
    groups=(
        ("Pages", (menuitem1,)),
    ),
    icon_class="mdi alert",
)