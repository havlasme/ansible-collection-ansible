<!--
SPDX-FileCopyrightText: None
SPDX-License-Identifier: 0BSD
-->

Ansible Collection - havlasme.ansible
=====================================

[![Ansible Galaxy][galaxy-image]][galaxy-link]
[![Apache-2.0 license][license-image]][license-link]
[![CI][ci-image]][ci-link]

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
make build
```

Licensing
---------

[Apache-2.0][license-link]


[ci-image]: https://img.shields.io/gitlab/pipeline-status/havlas.me/ansible-collection-ansible
[ci-link]: https://gitlab.com/havlas.me/ansible-collection-ansible/-/pipelines
[galaxy-image]: https://img.shields.io/ansible/collection/v/havlasme/ansible
[galaxy-link]: https://galaxy.ansible.com/ui/repo/published/havlasme/ansible/
[license-image]: https://img.shields.io/badge/license-Apache2.0-blue.svg
[license-link]: LICENSE
