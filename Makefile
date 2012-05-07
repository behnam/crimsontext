NAME=Crimson
VERSION=0.8

SRC=sources
BLD=builds
DIST=$(NAME)-$(VERSION)

PY=python
SCRIPT=tools/generate.py

FONTS=Roman Bold Italic BoldItalic Semibold SemiboldItalic

SFD=$(FONTS:%=$(SRC)/$(NAME)-%.sfd)
OTF=$(FONTS:%=$(BLD)/$(NAME)-%.otf)
TTF=$(FONTS:%=$(BLD)/$(NAME)-%.ttf)

all: otf ttf

otf: $(OTF)
ttf: $(TTF)

$(BLD)/%.otf: $(SRC)/%.sfd Makefile $(SCRIPT)
	@echo "Generating	 $@"
	@$(PY) $(SCRIPT) $< $@ $(VERSION)

$(BLD)/%.ttf: $(SRC)/%.sfd Makefile $(SCRIPT)
	@echo "Generating	 $@"
	@$(PY) $(SCRIPT) $< $@ $(VERSION)

dist: $(OTF) $(TTF)
	@echo "Making dist tarball"
	@mkdir -p $(DIST)/$(SRC)
	@mkdir -p $(DIST)/$(BLD)
	@mkdir -p $(DIST)/tools
	@cp $(SFD) $(DIST)/$(SRC)
	@cp $(OTF) $(DIST)/$(BLD)
	@cp $(TTF) $(DIST)/$(BLD)
	@cp $(SCRIPT) $(DIST)/tools
	@cp Makefile README $(DIST)
	@zip -r $(DIST).zip $(DIST)

clean:
	@rm -rf $(OTF) $(TTF) $(DIST) $(DIST).zip
