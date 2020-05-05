#include "lists.h"
#include <stdlib.h>

/**
 * check_palindrome - recursive check
 * @init: first node
 * @last: size of linkedlist
 * Return: 1 if pass - 0 otherwise
 */
int check_palindrome(listint_t *init, int *last)
{
	listint_t *end = init;
	int i;

	if (!init)
		return (0);

	for (i = 0; i < *last; i++)
		end = end->next;

	*last = *last - 2;
	if (init->n != end->n)
		return (0);
	else if (*last > 0)
		return (check_palindrome(init->next, last));
	return (1);
}

/**
 * is_palindrome - check for palindrome linkedlist
 * @head: linkedlist
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *init = *head;
	listint_t *tmp = *head;
	int last = 0;

	if (!head || (*head)->next == NULL)
		return (1);
	for (; tmp->next; last++)
		tmp = tmp->next;

	return (check_palindrome(init, &last));
}