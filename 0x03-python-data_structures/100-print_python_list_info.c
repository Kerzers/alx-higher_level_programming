#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

/**
*print_python_list_info - prints some basic info about Python lists
*@p: a python list object
*
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;

	printf("[*] Size of the Python List = %zd\n", Py_SIZE(p));
	printf("[*] Allocated = %zd\n", ((PyListObject*)p)->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
		printf("Element %zd: %s\n", i, Py_TYPE(PyList_GET_ITEM(p,i))->tp_name);
}
