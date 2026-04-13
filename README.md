<!--
SPDX-FileCopyrightText: None
SPDX-License-Identifier: 0BSD
-->

Ansible Collection - havlasme.ansible
=====================================

[![Ansible Galaxy][galaxy-image]][galaxy-link]
[![Apache-2.0 license][license-image]][license-link]
[![CI][ci-image]][ci-link]

An [Ansible](https://www.ansible.com/) collection of plugins used by `havlasme` collections and roles.

Installation
------------

```shell
ansible-galaxy collection install havlasme.ansible
```

```yaml
collections:
- name: 'havlasme.ansible'
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


[ci-image]: https://img.shields.io/gitlab/pipeline-status/havlas.me/ansible-collection-ansible?style=for-the-badge
[ci-link]: https://gitlab.com/havlas.me/ansible-collection-ansible/-/pipelines
[galaxy-image]: https://img.shields.io/ansible/collection/v/havlasme/ansible?style=for-the-badge
[galaxy-link]: https://galaxy.ansible.com/ui/repo/published/havlasme/ansible/
[license-image]: https://img.shields.io/badge/license-Apache2.0-blue.svg?style=for-the-badge
[license-link]: LICENSE
