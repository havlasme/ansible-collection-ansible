# SPDX-FileCopyrightText: None
# SPDX-License-Identifier: 0BSD

GITHOOKS := .githooks

.PHONY: githooks
githooks:
	git config --local core.hooksPath "$(GITHOOKS)"
