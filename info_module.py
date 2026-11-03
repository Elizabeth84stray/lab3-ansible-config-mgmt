#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
   INFO MODULE
   ==========

   This is a custom Ansible module that returns a greeting message
   and the current Python version.

   Requirements:
       - ansible.module_utils.basic
       - sys

   Parameters:
       name (str): The name of the person to greet (required).

   Returns:
       dict: A dictionary containing:
           - changed (bool): Always False, as this is a read-only operation.
           - message (str): The greeting message.
           - python_version (str): The current Python version.
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
