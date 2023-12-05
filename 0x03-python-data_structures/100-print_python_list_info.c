#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - a functuion that prints info about a python list
 * @p: a pointer to python object
 *
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size = PyList_Size(p);
	PyObject *item;

	printf("[*] Size of the Python List = %d\n", (int)size);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
	
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", (int)i, Py_TYPE(item)->tp_name);
	}
}

