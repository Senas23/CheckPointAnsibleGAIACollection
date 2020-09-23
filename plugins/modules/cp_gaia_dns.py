#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Ansible module to manage CheckPoint Firewall (c) 2019
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.gaia.plugins.module_utils.checkpoint import idempotent_api_call

DOCUMENTATION = """
author: 
description:
- Setting DNS configuration
module: cp_gaia_dns
options:
  suffix: 
    description: DNS Suffix to use. Use empty-string in order to remove the setting
    required: false
    type: str
  primary:
    description: Primary DNS server. Use empty-string in order to remove the setting
    required: false
    type: str 
  secondary:
    description: Secondary DNS server. Use empty-string in order to remove the setting
    required: false
    type: str
  tertiary:
    description: Tertiary DNS server. Use empty-string in order to remove the setting
    required: false
    type: str
short_description: Setting DNS configuration
version_added: '2.9'

"""

EXAMPLES = """
- name: DNS Change example
      check_point.gaia.cp_gaia_dns:
        primary: "8.8.4.4"
        secondary: "8.8.8.8"
        tertiary: "9.9.9.9"
        suffix: "mydnssuffix.net"

"""

RETURN = """
dns:
  description: The checkpoint object updated.
  returned: always.
  type: dict
"""


def main():
    # arguments for the module:
    fields = dict(
        primary=dict(type='str', required=True),
        secondary=dict(type='str', required=False),
        tertiary=dict(type='str', required=False),
        suffix=dict(type='str', required=False)
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'dns'
    ignore = []
    keys = []

    res = idempotent_api_call(module, api_call_object, ignore, keys)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
