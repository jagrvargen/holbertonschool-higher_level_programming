#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * @head: A pointer to a pointer to a linked list.
 *
 * Return: 1 if list is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	unsigned int len = 0, jump = 0;
	listint_t *end, *hold_s, *hold_e;

	if (head == NULL || *head == NULL)
		return (0);
	end = *head;
	hold_s = *head;
	while (end->next != NULL)
	{
		end = end->next;
		len++;
	}
	hold_e = end;
	end->next = *head;
	while (end->n == (*head)->n && end != *head)
	{
		jump = len;
		(*head) = (*head)->next;
		while (jump > 0)
		{
			end = end->next;
			jump--;
		}
		if (end->next == *head)
			break;
	}
	if ((end == (*head) || end->next == (*head)) && end->n == (*head)->n)
	{
		*head = hold_s;
		end = hold_e;
		end->next = NULL;
		return (1);
	}
	*head = hold_s;
	end = hold_e;
	end->next = NULL;
	return (0);
}
