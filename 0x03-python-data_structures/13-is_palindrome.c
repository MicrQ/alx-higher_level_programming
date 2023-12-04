#include "lists.h"

/**
 * add_node - adds new node at the beginning
 * @head: a pointer to the linkedlist
 * @data: data of the new node
 * Return: NULL on failure and the new head
 */
listint_t *add_node(listint_t **head, int data)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = data;
	new->next = *head;
	return (new);
}


/**
 * is_palindrome - a function that checks if a linkedlis is palindrome
 * @head: a pointer to the linkedlist
 * Return: 0 if not, else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *new = NULL, *ptr = *head;
	int nodes = 1, i = 0;

	if (!ptr || !head || !(ptr->next))
		return (1);
	while (ptr->next != NULL)
	{
		nodes++;
		ptr = ptr->next;
	}
	ptr = *head;
	while (i < nodes / 2)
	{
		new = add_node(&new, ptr->n);
		ptr = ptr->next;
		i++;
	}
	i = 0;
	while (i < nodes / 2)
	{
		if (new->n != ptr->n)
			return (0);
		new = new->next;
		ptr = ptr->next;
		i++;
	}
	return (1);
}
