#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 *
 * @list: A pointer to a linked list
 *
 * Return: An integer 1 for true, 0 for false
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *search;

	if (list == NULL)
		return (0);

	current = list;
	search = list->next;

	while (search->next != NULL && search->next != current)
	{
		search = search->next;
		if (search->next == NULL)
			return (0);
		else if (search->next == current)
			return (1);
		search = search->next;
		current = current->next;
	}
	if (search->next == current)
		return (1);
	return (0);
}
