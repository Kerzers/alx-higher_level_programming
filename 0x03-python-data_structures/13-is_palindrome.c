#include "lists.h"
#include <stdio.h>

/**
 *is_palindrome - checks if a singly linked list is a palindrome
 *@head: reference to the head of a list
 *
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int *elmts = NULL;
	int i, len;
	listint_t *current = *head;

	if (!*head)
		return (1);
	len = length(head);
	elmts = malloc(sizeof(int) * len);
	if (!elmts)
		exit(1);
	for (i = 0; i < len; i++)
	{
		elmts[i] = current->n;
		current = current->next;
	}
	for (i = 0; i < (len / 2); i++)
	{
		if (elmts[i] != elmts[len - 1 - i])
			return (0);
	}
	free(elmts);
	return (0);
}

/**
 *length - counts the elements of a list
 *@head: the reference of the head of a list
 *
 *Return: the number of elements in a list
 */
int length(listint_t **head)
{
	int count = 0;
	listint_t *current = *head;

	while (current)
	{
		current = current->next;
		count++;
	}
	return (count);
}
