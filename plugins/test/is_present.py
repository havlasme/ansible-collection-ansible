from jinja2.runtime import UndefinedError

DOCUMENTATION = '''
---
module: is_present
version_added: "0.1.0"
short_description: Checks if a value is 'present'
description:
    - This filter checks if the given value is the string 'present'.
    - Useful for filtering lists with state parameter that can be marked as 'present'.
options:
    value:
        description:
            - The value to be checked if it equals 'present'.
        required: true
        type: any
author:
    - Tomas Havlas (@havlasme)
'''

RETURN = '''
boolean:
    description: Returns True if the value is 'present' or undefined, otherwise False.
    type: bool
    returned: always
'''


def is_present(value):
    try:
        return value == 'present'
    except UndefinedError:
        return True


class TestModule(object):
    def tests(self):
        return {
            'is_present': is_present
        }
