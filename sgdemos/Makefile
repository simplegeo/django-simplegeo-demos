M4   := $(shell which m4)
DEPS := ../m4/base.m4

ifeq ($(shell test -f overrides.m4 || echo n),n)
    .PHONY: overrides.m4
else
    DEPS += overrides.m4
endif


all: settings.py

settings.py: $(DEPS) settings.py.m4
	m4 $^ > $@

clean:
	rm -f settings.py && find . -name \*.pyc -print -delete

