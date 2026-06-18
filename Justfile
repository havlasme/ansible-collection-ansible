# SPDX-FileCopyrightText: None
#
# SPDX-License-Identifier: 0BSD

import '.githooks/githooks.just'

NAMESPACE := `yq -r .namespace galaxy.yml`
COLLECTION := `yq -r .name galaxy.yml`
VERSION := `yq -r .version galaxy.yml`

DISTDIR := env("DISTDIR", "./dist")
TARBALL := "{{ NAMESPACE }}-{{ COLLETION }}-{{ VERSION }}.tar.gz"

# Build the collection tarball.
build:
    ansible-galaxy collection build --output-path "{{ DISTDIR }}"

# Install the locally built collection.
install:
    command -v yq >/dev/null 2>&1 || { echo "no yq. try running pip3 install yq"; exit 1; }
    ansible-galaxy collection install "{{ DISTDIR }}/{{ TARBALL }}"

# Publish the locally built collection.
publish:
    command -v yq >/dev/null 2>&1 || { echo "no yq. try running pip3 install yq"; exit 1; }
    ansible-galaxy collection publish "{{ DISTDIR }}/{{ TARBALL }}" --token "${GALAXY_API_TOKEN}"

# Clean up the build directory.
clean:
    -rm --recursive "{{ DISTDIR }}"

# Reset the repository to a clean state.
distclean: clean
	git clean --force -Xd

[private, default]
default:
    @just --list --unsorted
