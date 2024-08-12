from jinja2.runtime import UndefinedError

DOCUMENTATION = '''
---
module: is_absent
version_added: "0.1.0"
short_description: Checks if a value is 'absent'
description:
    - This filter checks if the given value is the string 'absent'.
    - Useful for filtering lists with state parameter that can be marked as 'absent'.
options:
    value:
        description:
            - The value to be checked if it equals 'absent'.
        required: true
        type: any
author:
    - Tomas Havlas (@havlasme)
'''

RETURN = '''
boolean:
    description: Returns True if the value is 'absent', otherwise False.
    type: bool
    returned: always
'''


def is_absent(value):
    try:
        return value == 'absent'
    except UndefinedError:
        return False


class TestModule(object):
    def tests(self):
        return {
            'is_absent': is_absent
        }
