GALAXY = @ansible-galaxy
NAMESPACE = $(shell yq -r .namespace galaxy.yml)
COLLECTION = $(shell yq -r .name galaxy.yml)
VERSION = $(shell yq -r .version galaxy.yml)
DIST = ./dist

.PHONY: build
build:
	$(GALAXY) collection build --output-path "$(DIST)"

.PHONY: install
install:
ifeq (, $(shell which yq))
	$(error "no yq. try running pip3 install yq")
else
	$(GALAXY) collection install "$(DIST)/$(NAMESPACE)-$(COLLECTION)-$(VERSION).tar.gz"
endif

.PHONY: publish
publish:
ifeq (, $(shell which yq))
	$(error "no yq. try running pip3 install yq")
else
	$(GALAXY) collection publish "$(DIST)/$(NAMESPACE)-$(COLLECTION)-$(VERSION).tar.gz" --token "$(GALAXY_API_TOKEN)"
endif

.PHONY: clean
clean:
	-rm --recursive "$(DIST)"
