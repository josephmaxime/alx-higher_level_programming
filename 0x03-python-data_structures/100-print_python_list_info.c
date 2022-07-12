#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *list_ob;
	struct _typeobject *type;
	long length;
	PyObject *object;

	list_ob = (PyListObject *)p;

	length = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %ld\n", list_ob->allocated);

	for (i = 0; i < length; i++)
	{
		object = PyList_GetItem(list_ob, i);
		type = object->ob_type;
		printf("Element %ld: %s\n", i, type->tp_name);
	}
	
}
