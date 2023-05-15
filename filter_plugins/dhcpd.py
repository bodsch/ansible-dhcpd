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
            'has_valid_values': self.has_values,
            'dhcp_subnet': self.dhcp_subnet,
        }

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
        """
        display.v(f"dhcp_subnet({data})")

        cidr = None
        netmask = None

        if len(data) == 0:
            return cidr, netmask

        from ipaddress import IPv4Interface

        try:
            ipc = IPv4Interface(data)

            cidr = ipc.ip
            netmask = ipc.netmask
            # display.v(f"ip   : '{ipc}'")
            # display.v(f"     : '{ipc.ip}'")
            # display.v(f"     : '{ipc.netmask}'")

        except Exception as e:
            display.v(f"ERROR: '{e}'")
            pass

        return cidr, netmask
