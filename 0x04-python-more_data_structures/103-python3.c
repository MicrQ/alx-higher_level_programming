#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - gives a data of pythone byte object
 * @p: PyObject
*/
void print_python_bytes(PyObject *p)
{
	char *str = NULL;
	Py_ssize_t i = 0, size = 0;

	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	if (Bytes_AsStringAndSize(p, &str, &size) != -1)
	{
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", str);
		printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
		while (i < 10 && i < size + 1)
			printf(" %02hhx", str[i++]);
		printf("\n");
	}

}
/**
 * print_python_list - prints information about a PyListObject
 * @p: a pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t listSize = 0;
	PyObject *obj;
	int count = 0;

	if (PyList_CheckExact(p))
	{
		listSize = PyList_Size(p);
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", listSize);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (count < listSize)
		{
			obj = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", count, obj->oc_type->tp_name);
			if (PyBytes_check(obj))
				print_python_bytes(obj);
			count++;
		}
	}
}
