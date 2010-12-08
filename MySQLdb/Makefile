
PYTHON := $(shell which python)


i :
	python setup.py build_ext -i
t :
	python test.py 
g :
	@echo enter \"set args test.py\" then \"r\"
	gdb $(PYTHON) 


.PHONY : i t g

