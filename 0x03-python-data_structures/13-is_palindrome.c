#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Start of linked list
 * Return: 1 if a palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	char array[4000];
	listint_t *mover = *head;
	unsigned int i = 0;
	unsigned int k = 0;

	if (*head == NULL)
		return (1);
	while (mover != NULL)
	{
		array[i] = mover->n;
		mover = mover->next;
		i++;
	}
	i--;
	for (; k < i; i--, k++)
	{
		if (array[k] != array[i])
			return (0);
	}
	return (1);
}
