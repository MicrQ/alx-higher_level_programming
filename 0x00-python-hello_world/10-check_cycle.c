#include "lists.h"

/**
 * check_cycle - is a function that checks if there is a cycle
 *		 in a singly linked list.
 * @list: a pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *nextP = list;

	while (list && nextP && nextP->next)
	{
		nextP = nextP->next->next;
		if (list == nextP)
			return (1);
		list = list->next;
	}
	return (0);
}
