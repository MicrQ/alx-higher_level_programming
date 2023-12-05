#include "lists.h"

int palindrome(listint_t **left, listint_t *right)
{
	int flag;
	if (right == NULL)
	{
		return (1);
	}
	flag = (palindrome(left, right->next) && (*left)->n == right->n);
	*left = (*left)->next;
	return (flag);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!(*head) || !head)
	{
		return (1);
	}
	return (palindrome(head, *head));
}
