#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
INFO MODULE
Returns a greeting message.
"""
import sys
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True)
        )
    )
        name = module.params["name"]
    module.exit_json(
        changed=False,
        message=f"Hello, {name}! This is the info module.",
        python_version=sys.version
    )

if __name__ == '__main__':
    main()