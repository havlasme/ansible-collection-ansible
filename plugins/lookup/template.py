from __future__ import (absolute_import, division, print_function)

import os
from ansible.errors import AnsibleFileNotFound, AnsibleLookupError
from ansible.module_utils.six import string_types
from ansible.module_utils.common.text.converters import to_bytes, to_native, to_text
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display
from ansible.utils.path import unfrackpath

display = Display()


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        template_name = terms[0]
        b_template_name = to_bytes(template_name, errors='surrogate_or_strict')

        if not isinstance(template_name, string_types) or not template_name.endswith('.j2'):
            raise AnsibleLookupError(u'Invalid template name supplied, must be string ending in ".j2" but got: "%s"'.format(template_name))

        result = None
        search = []
        if template_name.startswith(u'~') or template_name.startswith(os.path.sep):
            # path is absolute, no relative needed, check existence and return template_name
            test_path = unfrackpath(b_template_name, follow=False)
            if os.path.exists(test_path):
                result = test_path
        else:
            template_basename = template_name[:-3]
            ansible_distribution = variables['ansible_distribution'].lower()

            upath = unfrackpath(variables['playbook_dir'], follow=False)
            b_upath = to_bytes(upath)
            search.append(os.path.join(b_upath, b'templates', to_bytes('{}.{}.j2'.format(template_basename, ansible_distribution))))
            search.append(os.path.join(b_upath, b'templates', to_bytes('{}.j2'.format(template_basename))))
            if 'role_path' in variables:
                upath = unfrackpath(variables['role_path'], follow=False)
                b_upath = to_bytes(upath)
                search.append(os.path.join(b_upath, b'templates', to_bytes('{}.{}.j2'.format(template_basename, ansible_distribution))))
                search.append(os.path.join(b_upath, b'templates', to_bytes('{}.j2'.format(template_basename))))

            display.debug(u'search_path:\n\t%s'.format(to_text(b'\n\t'.join(search))))
            for b_candidate in search:
                display.vvvvv(u'looking for "%s" at "%s"'.format(template_name, to_text(b_candidate)))
                if os.path.exists(b_candidate):
                    result = to_text(b_candidate)
                    break

        if result is None:
            raise AnsibleFileNotFound(file_name=template_name, paths=[to_native(p) for p in search])

        return [result]
