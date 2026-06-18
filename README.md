<!--
SPDX-FileCopyrightText: None
SPDX-License-Identifier: 0BSD
-->

Ansible Collection - havlasme.ansible
=====================================

[![Ansible Galaxy][galaxy-image]][galaxy-link]
[![Apache-2.0 license][license-image]][license-link]
[![CI](https://img.shields.io/gitlab/pipeline-status/havlas.me/ansible-collection-ansible)](https://gitlab.com/havlas.me/ansible-collection-ansible/-/pipelines)

An [Ansible](https://www.ansible.com/) Collection of modules and plugins used by `havlasme` collections and roles.

Installation
------------

```shell
ansible-galaxy collection install havlasme.ansible
```

```yaml
collections:
- name: 'havlasme.ansible'
```

See [Using Ansible collections](https://docs.ansible.com/projects/ansible/latest/user_guide/collections_using.html).

Development
-----------

```shell
just build
```

Licensing
---------

[Apache-2.0](LICENSE)


[galaxy-image]: https://img.shields.io/ansible/collection/v/havlasme/ansible
[galaxy-link]: https://galaxy.ansible.com/ui/repo/published/havlasme/ansible/
[license-image]: https://img.shields.io/badge/license-Apache2.0-blue.svg
[license-link]: LICENSE
