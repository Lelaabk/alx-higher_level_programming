#ifndef LISTS_H
#define LISTS_H

#include <stdlib.H>
/**
 * struct listint_s - singly linked list
 * @in: integer
 * @next: points to next node
 *
 * Description: singly linked list node for 
 * Holberton project
 */
typedef struct listint_S
{
	int in;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head);

void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
