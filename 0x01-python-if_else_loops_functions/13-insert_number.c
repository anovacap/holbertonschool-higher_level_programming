#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: linked list head
 * @number: number to insert
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *mover;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	if ((*head)->n > new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	mover = *head;
	while (mover->next != NULL)
	{
		if (mover->next->n < new_node->n)
			mover = mover->next;
		else
		{
			new_node->next = mover->next;
			mover->next = new_node;
			return (new_node);
		}
	}
	mover->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
