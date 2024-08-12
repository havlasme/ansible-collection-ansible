from jinja2.runtime import UndefinedError

DOCUMENTATION = '''
---
module: is_directory
version_added: "0.1.0"
short_description: Checks if a value is 'directory'
description:
    - This filter checks if the given value is the string 'directory'.
    - Useful for filtering lists with state parameter that can be marked as 'directory'.
options:
    value:
        description:
            - The value to be checked if it equals 'directory'.
        required: true
        type: any
author:
    - Tomas Havlas (@havlasme)
'''

RETURN = '''
boolean:
    description: Returns True if the value is 'directory', otherwise False.
    type: bool
    returned: always
'''


def is_directory(value):
    try:
        return value == 'directory'
    except UndefinedError:
        return False


class TestModule(object):
    def tests(self):
        return {
            'is_directory': is_directory
        }
