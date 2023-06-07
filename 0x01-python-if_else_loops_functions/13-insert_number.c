#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 *insert_node - inserts a new node in a sorted linked list
 *@head: pointer to the head of the list
 *@number: number to insert
 *Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *temp = *head, *current = *head;
	int count = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
	while (current)
	{
		if (number > current->n)
		{
			temp = current;
			current = current->next;
			count++;
		}
		else
			break;
	}
	if (count)
		temp->next = new;
	else
		*head = new;
	new->next = current;
	}
	return (new);
}
