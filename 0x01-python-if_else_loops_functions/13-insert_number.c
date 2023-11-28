#include "lists.h"

/**
 * insert_node - inserts a node in a sorted singly linkedlist
 * @head: a pointer to the sorted singly linkedlist
 * @number: the data of the node
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t)), *tmp = *head;

	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (number < tmp->n || !tmp)
	{
		node->next = *head;
		*head = node;
		return (*head);
	}
	while (tmp->next->n < number && tmp->next != NULL)
		tmp = tmp->next;

	node->next = tmp->next;
	tmp->next = node;
	return (node);
}
