#include "lists.h"
#include <stdio.h>

/**
 *check_cycle - checks if a singly linked list has a cycle in it.
 *@list: list to be checked
 *Return: 0 if there is no cycle, 1 if there is a cycle
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (!list || !list->next)
		return (0);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
