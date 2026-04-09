GALAXY = @ansible-galaxy

NAMESPACE ?= $(shell yq -r .namespace galaxy.yml)
COLLECTION ?= $(shell yq -r .name galaxy.yml)
VERSION ?= $(shell yq -r .version galaxy.yml)

DISTDIR ?= ./dist

.PHONY: build
build:
	$(GALAXY) collection build --output-path "$(DISTDIR)"

.PHONY: install
install: $(DISTDIR)/$(NAMESPACE)-$(COLLECTION)-$(VERSION).tar.gz
ifeq (, $(shell which yq))
	$(error "no yq. try running pip3 install yq")
else
	$(GALAXY) collection install "$(DISTDIR)/$(NAMESPACE)-$(COLLECTION)-$(VERSION).tar.gz"
endif

.PHONY: publish
publish: $(DISTDIR)/$(NAMESPACE)-$(COLLECTION)-$(VERSION).tar.gz
ifeq (, $(shell which yq))
	$(error "no yq. try running pip3 install yq")
else
	$(GALAXY) collection publish "$(DISTDIR)/$(NAMESPACE)-$(COLLECTION)-$(VERSION).tar.gz" --token "$(GALAXY_API_TOKEN)"
endif

.PHONY: clean
clean:
	-rm --recursive "$(DISTDIR)"

$(DISTDIR)/$(NAMESPACE)-$(COLLECTION)-$(VERSION).tar.gz:
	$(MAKE) build
