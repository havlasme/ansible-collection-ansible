Ansible Collection - havlasme.ansible
=====================================

[![Apache-2.0 license][license-image]][license-link]

An [Ansible](https://www.ansible.com/) collection of ansible utilities used by `havlasme` collections and roles.

Installation
------------

```shell
ansible-galaxy collection install havlasme.ansible
```

```yaml title="requirements.yml"
---
collections:
- name: 'havlasme.ansible'
...
```

Development
-----------

```shell
make build
```

License
-------

[Apache-2.0][license-link]

Author Information
------------------

Created in 2024 by [Tomáš Havlas](https://havlas.me/).


[license-image]: https://img.shields.io/badge/license-Apache2.0-blue.svg?style=flat-square
[license-link]: LICENSE
