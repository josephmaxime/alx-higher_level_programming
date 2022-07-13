#include <stdio.h>
#include <Python.h>


void print_python_bytes(PyObject *p);
/*
 * print_python_list - print info of list python in C.
 *
 * @p: python objet
 */

void print_python_list(PyObject *p)
{
	PyListObject *list_ob;
	struct _typeobject *type;
	Py_ssize_t size, i;
	PyObject *object;

	list_ob = (PyListObject *)p;
	size = list_ob->ob_base.ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list_ob->allocated);

	for (i = 0; i < size; i++)
	{
		object = list_ob->ob_item[i];
		type = object->ob_type;
		printf("Element %ld: %s\n", i, type->tp_name);
		if (PyBytes_Check(object))
			print_python_bytes(object);
	}
}

/*
 * print_python_bytes - print info in bytes of ptyhon objet in C.
 *
 * @p: python objet.
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (PyBytes_AsStringAndSize(p, &str, &size) != -1)
	{
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", str);
		printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

		i = 0;
		while (i < size + 1 && i < 10)
		{
			printf(" %02hhx", str[i]);
			i++;
		}
		printf("\n");
	}
}
