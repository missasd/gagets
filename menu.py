from django.utils.translation import gettext_lazy as _

from netbox.registry import registry
from utilities.choices import ButtonColorChoices
from . import *

#
# Nav menus
#

ORGANIZATION_MENU = Menu(
    label=_('组织机构'),
    icon_class='mdi mdi-domain',
    groups=(
        MenuGroup(
            label=_('站点'),
            items=(
                get_model_item('dcim', 'site', _('数据中心')),
                get_model_item('dcim', 'region', _('区域')),
                get_model_item('dcim', 'sitegroup', _('站点组')),
                get_model_item('dcim', 'location', _('具体地点')),
            ),
        ),
        MenuGroup(
            label=_('机架'),
            items=(
                get_model_item('dcim', 'rack', _('机柜')),
                get_model_item('dcim', 'rackrole', _('机柜角色')),
                get_model_item('dcim', 'rackreservation', _('预留')),
                MenuItem(
                    link='dcim:rack_elevation_list',
                    link_text=_('立面图'),
                    permissions=['dcim.view_rack']
                ),
            ),
        ),
        MenuGroup(
            label=_('租凭'),
            items=(
                get_model_item('tenancy', 'tenant', _('租户')),
                get_model_item('tenancy', 'tenantgroup', _('租户组')),
            ),
        ),
        MenuGroup(
            label=_('Contacts'),
            items=(
                get_model_item('tenancy', 'contact', _('联系人')),
                get_model_item('tenancy', 'contactgroup', _('联系人组')),
                get_model_item('tenancy', 'contactrole', _('联系人角色')),
                get_model_item('tenancy', 'contactassignment', _('联系方式分配'), actions=['import']),
            ),
        ),
    ),
)

DEVICES_MENU = Menu(
    label=_('Devices'),
    icon_class='mdi mdi-server',
    groups=(
        MenuGroup(
            label=_('Devices'),
            items=(
                get_model_item('dcim', 'device', _('设备')),
                get_model_item('dcim', 'module', _('模块组件')),
                get_model_item('dcim', 'devicerole', _('设备角色')),
                get_model_item('dcim', 'platform', _('平台')),
                get_model_item('dcim', 'virtualchassis', _('虚拟机箱')),
                get_model_item('dcim', 'virtualdevicecontext', _('Virtual Device Contexts')),
            ),
        ),
        MenuGroup(
            label=_('类型'),
            items=(
                get_model_item('dcim', 'devicetype', _('设备型号')),
                get_model_item('dcim', 'moduletype', _('模块类型')),
                get_model_item('dcim', 'manufacturer', _('制造商')),
            ),
        ),
        MenuGroup(
            label=_('Device Components'),
            items=(
                get_model_item('dcim', 'interface', _('接口')),
                get_model_item('dcim', 'frontport', _('前端口')),
                get_model_item('dcim', 'rearport', _('后端口')),
                get_model_item('dcim', 'consoleport', _('Console 端口')),
                get_model_item('dcim', 'consoleserverport', _('Console 服务器端口')),
                get_model_item('dcim', 'powerport', _('电力接口')),
                get_model_item('dcim', 'poweroutlet', _('电源插座PDU')),
                get_model_item('dcim', 'modulebay', _('模块组件托架')),
                get_model_item('dcim', 'devicebay', _('设备托架')),
                get_model_item('dcim', 'inventoryitem', _('库存物品')),
                get_model_item('dcim', 'inventoryitemrole', _('库存项目角色')),
            ),
        ),
    ),
)

CONNECTIONS_MENU = Menu(
    label=_('Connections'),
    icon_class='mdi mdi-connection',
    groups=(
        MenuGroup(
            label=_('Connections'),
            items=(
                get_model_item('dcim', 'cable', _('线缆'), actions=['import']),
                get_model_item('wireless', 'wirelesslink', _('无线连接')),
                MenuItem(
                    link='dcim:interface_connections_list',
                    link_text=_('接口连接'),
                    permissions=['dcim.view_interface']
                ),
                MenuItem(
                    link='dcim:console_connections_list',
                    link_text=_('Console 连接'),
                    permissions=['dcim.view_consoleport']
                ),
                MenuItem(
                    link='dcim:power_connections_list',
                    link_text=_('电源连接'),
                    permissions=['dcim.view_powerport']
                ),
            ),
        ),
    ),
)

WIRELESS_MENU = Menu(
    label=_('Wireless'),
    icon_class='mdi mdi-wifi',
    groups=(
        MenuGroup(
            label=_('Wireless'),
            items=(
                get_model_item('wireless', 'wirelesslan', _('无线局域网')),
                get_model_item('wireless', 'wirelesslangroup', _('无线局域网组')),
            ),
        ),
    ),
)

IPAM_MENU = Menu(
    label=_('IPAM'),
    icon_class='mdi mdi-counter',
    groups=(
        MenuGroup(
            label=_('IP Addresses'),
            items=(
                get_model_item('ipam', 'ipaddress', _('IP 地址')),
                get_model_item('ipam', 'iprange', _('IP 范围')),
            ),
        ),
        MenuGroup(
            label=_('Prefixes'),
            items=(
                get_model_item('ipam', 'prefix', _('IP网段')),
                get_model_item('ipam', 'role', _('网段和VLAN 角色')),
            ),
        ),
        MenuGroup(
            label=_('ASNs'),
            items=(
                get_model_item('ipam', 'asnrange', _('ASN Ranges')),
                get_model_item('ipam', 'asn', _('ASNs')),
            ),
        ),
        MenuGroup(
            label=_('Aggregates'),
            items=(
                get_model_item('ipam', 'aggregate', _('Aggregates')),
                get_model_item('ipam', 'rir', _('RIRs')),
            ),
        ),
        MenuGroup(
            label=_('VRFs'),
            items=(
                get_model_item('ipam', 'vrf', _('VRFs')),
                get_model_item('ipam', 'routetarget', _('Route Targets')),
            ),
        ),
        MenuGroup(
            label=_('VLANs'),
            items=(
                get_model_item('ipam', 'vlan', _('VLANs')),
                get_model_item('ipam', 'vlangroup', _('VLAN Groups')),
            ),
        ),
        MenuGroup(
            label=_('Other'),
            items=(
                get_model_item('ipam', 'fhrpgroup', _('FHRP Groups')),
                get_model_item('ipam', 'servicetemplate', _('Service Templates')),
                get_model_item('ipam', 'service', _('Services')),
            ),
        ),
    ),
)

VPN_MENU = Menu(
    label=_('VPN'),
    icon_class='mdi mdi-graph-outline',
    groups=(
        MenuGroup(
            label=_('Tunnels'),
            items=(
                get_model_item('vpn', 'tunnel', _('Tunnels')),
                get_model_item('vpn', 'tunnelgroup', _('Tunnel Groups')),
                get_model_item('vpn', 'tunneltermination', _('Tunnel Terminations')),
            ),
        ),
        MenuGroup(
            label=_('L2VPNs'),
            items=(
                get_model_item('vpn', 'l2vpn', _('L2VPNs')),
                get_model_item('vpn', 'l2vpntermination', _('Terminations')),
            ),
        ),
        MenuGroup(
            label=_('Security'),
            items=(
                get_model_item('vpn', 'ikeproposal', _('IKE Proposals')),
                get_model_item('vpn', 'ikepolicy', _('IKE Policies')),
                get_model_item('vpn', 'ipsecproposal', _('IPSec Proposals')),
                get_model_item('vpn', 'ipsecpolicy', _('IPSec Policies')),
                get_model_item('vpn', 'ipsecprofile', _('IPSec Profiles')),
            ),
        ),
    ),
)

VIRTUALIZATION_MENU = Menu(
    label=_('裸金属虚拟化'),
    icon_class='mdi mdi-monitor',
    groups=(
        MenuGroup(
            label=_('Virtual Machines'),
            items=(
                get_model_item('virtualization', 'virtualmachine', _('虚拟机')),
                get_model_item('virtualization', 'vminterface', _('虚拟机接口')),
                get_model_item('virtualization', 'virtualdisk', _('Virtual Disks')),
            ),
        ),
        MenuGroup(
            label=_('Clusters'),
            items=(
                get_model_item('virtualization', 'cluster', _('虚拟化集群')),
                get_model_item('virtualization', 'clustertype', _('虚拟化集群类型')),
                get_model_item('virtualization', 'clustergroup', _('集群组')),
            ),
        ),
    ),
)

CIRCUITS_MENU = Menu(
    label=_('Circuits'),
    icon_class='mdi mdi-transit-connection-variant',
    groups=(
        MenuGroup(
            label=_('Circuits'),
            items=(
                get_model_item('circuits', 'circuit', _('线路')),
                get_model_item('circuits', 'circuittype', _('线路类型')),
            ),
        ),
        MenuGroup(
            label=_('Providers'),
            items=(
                get_model_item('circuits', 'provider', _('供应商')),
                get_model_item('circuits', 'provideraccount', _('供应商账号')),
                get_model_item('circuits', 'providernetwork', _('供应商网络')),
            ),
        ),
    ),
)

POWER_MENU = Menu(
    label=_('电力'),
    icon_class='mdi mdi-flash',
    groups=(
        MenuGroup(
            label=_('Power'),
            items=(
                get_model_item('dcim', 'powerfeed', _('电源线')),
                get_model_item('dcim', 'powerpanel', _('电源插座')),
            ),
        ),
    ),
)

PROVISIONING_MENU = Menu(
    label=_('设备配置'),
    icon_class='mdi mdi-file-document-multiple-outline',
    groups=(
        MenuGroup(
            label=_('Configurations'),
            items=(
                get_model_item('extras', 'configcontext', _('Config Contexts'), actions=['add']),
                get_model_item('extras', 'configtemplate', _('Config Templates'), actions=['add']),
            ),
        ),
    ),
)

CUSTOMIZATION_MENU = Menu(
    label=_('Customization'),
    icon_class='mdi mdi-toolbox-outline',
    groups=(
        MenuGroup(
            label=_('Customization'),
            items=(
                get_model_item('extras', 'customfield', _('自定义字段')),
                get_model_item('extras', 'customlink', _('自定义链接')),
                get_model_item('extras', 'exporttemplate', _('自定义验证')),
                get_model_item('extras', 'savedfilter', _('已保存的筛选条件')),
                get_model_item('extras', 'tag', 'Tags'),
                get_model_item('extras', 'imageattachment', _('图片附件'), actions=()),
            ),
        ),
        MenuGroup(
            label=_('Reports & Scripts'),
            items=(
                MenuItem(
                    link='extras:report_list',
                    link_text=_('报告'),
                    permissions=['extras.view_report'],
                    buttons=get_model_buttons('extras', "reportmodule", actions=['add'])
                ),
                MenuItem(
                    link='extras:script_list',
                    link_text=_('脚本'),
                    permissions=['extras.view_script'],
                    buttons=get_model_buttons('extras', "scriptmodule", actions=['add'])
                ),
            ),
        ),
    ),
)

OPERATIONS_MENU = Menu(
    label=_('运营'),
    icon_class='mdi mdi-cogs',
    groups=(
        MenuGroup(
            label=_('Integrations'),
            items=(
                get_model_item('core', 'datasource', _('Data Sources')),
                get_model_item('extras', 'eventrule', _('Event Rules')),
                get_model_item('extras', 'webhook', _('Webhooks')),
            ),
        ),
        MenuGroup(
            label=_('Jobs'),
            items=(
                MenuItem(
                    link='core:job_list',
                    link_text=_('Jobs'),
                    permissions=['core.view_job'],
                ),
            ),
        ),
        MenuGroup(
            label=_('Logging'),
            items=(
                get_model_item('extras', 'journalentry', _('日记列表'), actions=['import']),
                get_model_item('extras', 'objectchange', _('操作日志'), actions=[]),
            ),
        ),
    ),
)

ADMIN_MENU = Menu(
    label=_('Admin'),
    icon_class='mdi mdi-account-multiple',
    groups=(
        MenuGroup(
            label=_('Authentication'),
            items=(
                # Proxy model for auth.User
                MenuItem(
                    link=f'users:netboxuser_list',
                    link_text=_('Users'),
                    permissions=[f'auth.view_user'],
                    staff_only=True,
                    buttons=(
                        MenuItemButton(
                            link=f'users:netboxuser_add',
                            title='Add',
                            icon_class='mdi mdi-plus-thick',
                            permissions=[f'auth.add_user'],
                            color=ButtonColorChoices.GREEN
                        ),
                        MenuItemButton(
                            link=f'users:netboxuser_import',
                            title='Import',
                            icon_class='mdi mdi-upload',
                            permissions=[f'auth.add_user'],
                            color=ButtonColorChoices.CYAN
                        )
                    )
                ),
                # Proxy model for auth.Group
                MenuItem(
                    link=f'users:netboxgroup_list',
                    link_text=_('Groups'),
                    permissions=[f'auth.view_group'],
                    staff_only=True,
                    buttons=(
                        MenuItemButton(
                            link=f'users:netboxgroup_add',
                            title='Add',
                            icon_class='mdi mdi-plus-thick',
                            permissions=[f'auth.add_group'],
                            color=ButtonColorChoices.GREEN
                        ),
                        MenuItemButton(
                            link=f'users:netboxgroup_import',
                            title='Import',
                            icon_class='mdi mdi-upload',
                            permissions=[f'auth.add_group'],
                            color=ButtonColorChoices.CYAN
                        )
                    )
                ),
                MenuItem(
                    link=f'users:token_list',
                    link_text=_('API Tokens'),
                    permissions=[f'users.view_token'],
                    staff_only=True,
                    buttons=get_model_buttons('users', 'token')
                ),
                MenuItem(
                    link=f'users:objectpermission_list',
                    link_text=_('Permissions'),
                    permissions=[f'users.view_objectpermission'],
                    staff_only=True,
                    buttons=get_model_buttons('users', 'objectpermission', actions=['add'])
                ),
            ),
        ),
        MenuGroup(
            label=_('Configuration'),
            items=(
                MenuItem(
                    link='core:config',
                    link_text=_('Current Config'),
                    permissions=['core.view_configrevision'],
                    staff_only=True
                ),
                MenuItem(
                    link='core:configrevision_list',
                    link_text=_('Config Revisions'),
                    permissions=['core.view_configrevision'],
                    staff_only=True
                ),
            ),
        ),
    ),
)

MENUS = [
    ORGANIZATION_MENU,
    DEVICES_MENU,
    CONNECTIONS_MENU,
    WIRELESS_MENU,
    IPAM_MENU,
    VPN_MENU,
    VIRTUALIZATION_MENU,
    CIRCUITS_MENU,
    POWER_MENU,
    PROVISIONING_MENU,
    CUSTOMIZATION_MENU,
    OPERATIONS_MENU,
    ADMIN_MENU,
]

#
# Add plugin menus
#

for menu in registry['plugins']['menus']:
    MENUS.append(menu)

if registry['plugins']['menu_items']:

    # Build the default plugins menu
    groups = [
        MenuGroup(label=label, items=items)
        for label, items in registry['plugins']['menu_items'].items()
    ]
    plugins_menu = Menu(
        label=_("Plugins"),
        icon_class="mdi mdi-puzzle",
        groups=groups
    )
    MENUS.append(plugins_menu)
