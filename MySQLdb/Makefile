
PYTHON := $(shell which python)


i :
	touch _mysql.c
	python setup.py build_ext -i
t :
	python test.py 
g :
	@echo enter : set args test.py 
	@echo "enter :  b PyObject * _mysql_ResultObject_fetch_nparray( _mysql_ResultObject *self, PyObject* args,  PyObject* kwargs ) "
	gdb $(PYTHON) 

c :
	rm -rf _mysql.so



.PHONY : i t g

