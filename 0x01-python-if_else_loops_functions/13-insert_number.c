#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: A pointer to a pointer to the head node.
 * @number: A value to be added to new node.
 *
 * Return: A pointer to the address of the new_node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *search;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	if (*head == NULL || (*head)->n > new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		search = *head;
		while (search->next != NULL && search->next->n < new_node->n)
			search = search->next;
		new_node->next = search->next;
		search->next = new_node;
	}
	return (new_node);
}
