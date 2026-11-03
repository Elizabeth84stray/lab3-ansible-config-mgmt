#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
INFO MODULE
Returns a greeting message.
"""
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True)
        )
    )
    module.exit_json(changed=False, message="Module loaded")

if __name__ == '__main__':
    main()