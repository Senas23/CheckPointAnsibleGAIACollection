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
- Sets NTP status and servers
module: cp_gaia_ntp
options:
  servers:
    description: Servers to set
    required: false
    type: list
    ntp_version:
      description: NTP version to use 1-4
      required: false
      type: int
    type:
      description: primary or secondary ntp servers
      required: false
      type: string
    address:
      description: ipv4-address or ipv6-address
      required: false
      type: string
  
short_description: Sets NTP status and servers
version_added: '2.9'

"""

EXAMPLES = """
- name: NTP Test
      check_point.gaia.cp_gaia_ntp:
        enabled: True
        servers:
          - type: primary
            ntp_version: 4
            address: "10.0.0.1"
          - type: secondary
            ntp_version: 4
            address: "10.0.0.2"

"""

RETURN = """
ntp:
  description: The checkpoint ntp updated.
  returned: always.
  type: dict
"""


def main():
    # arguments for the module:
    fields = dict(
        enabled=dict(type='bool', required=True),
        servers=dict(type='list', options=dict(
            ntp_version=dict(type='int', choices=['1', '2', '3', '4']),
            type=dict(type='str', choices=['primary','secondary']),
            address=dict(type='str')
        ))
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    api_call_object = 'ntp'
    ignore = []
    keys = []

    res = idempotent_api_call(module, api_call_object, ignore, keys)
    module.exit_json(**res)


if __name__ == "__main__":
    main()
