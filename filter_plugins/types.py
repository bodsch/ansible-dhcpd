# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, print_function)
__metaclass__ = type

import ipaddress

from ansible.utils.display import Display

display = Display()

class FilterModule(object):
    """
        Ansible file jinja2 tests
    """

    def filters(self):
        return {
            'type': self.var_type,
            'has_valid_values': self.has_values,
            'dhcp_subnet': self.dhcp_subnet,
        }

    def var_type(self, var):
        '''
          Get the type of a variable
        '''
        return type(var).__name__

    def has_values(self, var):
        """
        """
        result = False
        result_value = var

        # display.v(f"- var   : '{var}' ({type(var)} / {self.var_type(var)})")

        if isinstance(var, int) and int(var) > 0:
            result = True
        if isinstance(var, str) or type(var).__name__ == "AnsibleUnsafeText" or type(var).__name__ == "AnsibleUnicode":
            try:
                ip = ipaddress.ip_address(var)
                display.v(f"ip   : '{ip}'")
                result_value = f"{str(var)}"
            except Exception:
                result_value = f'"{str(var)}"'

            if len(var) > 0:
                result = True

        if isinstance(var, list) and len(var) > 0:
            result_joined = ', '.join(var)
            result_value = f"{result_joined}"
            result = True

        # display.v(f" = {result} {result_value}")

        return result, result_value

    def dhcp_subnet(self, data):
        """
      {% if (values.subnet + '/' + values.netmask) | ipaddr('cidr') | ipaddr('network') %}
subnet {{ (values.subnet + '/' + values.netmask) | ipaddr('cidr') | ipaddr('network') }} netmask {{ values.netmask }} {
      {% elif values.subnet | ipaddr('cidr') | ipaddr('network') %}
subnet {{ values.subnet | ipaddr('cidr') | ipaddr('network') }} netmask {{ values.subnet | ipaddr('netmask') }} {
      {% else %}
subnet {{ values.subnet | ipaddr('cidr') | ipaddr('address') }} netmask 255.255.255.255 {
      {% endif %}
        """
        display.v(f"- data   : '{data}' ({type(data)} / {self.var_type(data)})")

        subnet = data.get("subnet", None)
        netmask = data.get("netmask", None)


        if isinstance(var, str) or type(var).__name__ == "AnsibleUnsafeText" or type(var).__name__ == "AnsibleUnicode":
            try:
                ip = ipaddress.ip_address(var)
                display.v(f"ip   : '{ip}'")
                result_value = f"{str(var)}"
            except Exception:
                result_value = f'"{str(var)}"'


