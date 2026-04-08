DOCUMENTATION = '''
---
module: is_present
version_added: "0.1.0"
short_description: Checks if state attribute value is 'present'
description:
    - This filter checks if the given value is the string 'present'.
    - Useful for filtering lists with state parameter that can be marked as 'present'.
options:
    obj:
        description:
            - The object to be checked for the specified attribute.
        required: true
        type: dict
    attr:
        description:
            - The attribute name to check within the object. Defaults to 'state'.
        required: false
        type: str
author:
    - Tomas Havlas (@havlasme)
'''

RETURN = '''
boolean:
    description: Returns True if the value is 'present' or undefined, otherwise False.
    type: bool
    returned: always
'''


def is_present(obj, attr='state'):
    if not isinstance(obj, dict):
        return False
    return obj.get(attr, 'present') == 'present'


class TestModule(object):
    def tests(self):
        return {
            'is_present': is_present
        }
