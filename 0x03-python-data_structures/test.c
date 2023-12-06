#include <stdio.h>
#include <stdlib.h>
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}
int is_palindrome(listint_t **head)
{       
        listint_t *ptr = *head;
        int nodes = 1;

        if (!ptr || !head || !(ptr->next))
                return 1;
        while (ptr->next != NULL)
        {
                nodes++;
                ptr = ptr->next;
        }
        printf("%d\n", nodes);
        return 1;
}    
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}
// listint_t printNode(listint_t *head){
//     if (!head->next)
//         return ;
//     a = head->n;
//     printNode(head->next);
//     printf("%d\n", a);
// }
listint_t *reverseNode(listint_t *head){
    listint_t *ptr = head, *nxt = NULL, *crt = NULL;
    if (!ptr)
        return ptr;
    while (ptr){
        crt = ptr->next;
        ptr->next = nxt;
        nxt = ptr;
    }
    ptr = nxt;
    return ptr;
}
int main(void){
    listint_t *head;
    head = NULL;
add_nodeint_end(&head, 1);
add_nodeint_end(&head, 17);
add_nodeint_end(&head, 972);
add_nodeint_end(&head, 50);
add_nodeint_end(&head, 98);/*
add_nodeint_end(&head, 98);
add_nodeint_end(&head, 50);
add_nodeint_end(&head, 972);
add_nodeint_end(&head, 17);
add_nodeint_end(&head, 1);
is_palindrome(&head);*/
head = reverseNode(head);
print_listint(head);
return (0);
}