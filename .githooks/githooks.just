# SPDX-FileCopyrightText: None
#
# SPDX-License-Identifier: 0BSD

GITHOOKS := ".githooks"

# Set up git hooks to use the .githooks directory.
[group('githooks')]
githooks:
    git config --local core.hooksPath "{{ GITHOOKS }}"
