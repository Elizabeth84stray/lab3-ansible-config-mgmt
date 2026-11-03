#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
FACTS MODULE
Collects custom OS facts.
"""
from ansible.module_utils.basic import AnsibleModule
import platform

def main():
    module = AnsibleModule(argument_spec={})
    
    module.exit_json(
        changed=False,
        ansible_facts=dict(
            custom_os=platform.system()
        )
    )

if __name__ == '__main__':
    main()
