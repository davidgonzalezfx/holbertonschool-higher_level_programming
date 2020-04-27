#include "lists.h"
/**
 * check_cycle - search infinite loop on linkedlists
 * @list: linkedlist head *
 * Return: 1 if cycle found, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *forwd = list;
	listint_t *back = list;

	if (!list || !list->next)
		return (0);

	for (; forwd && back && forwd->next;)
	{
		if (back == forwd)
			return (1);

		back = back->next;
		forwd = forwd->next->next;

	}
	return (0);
}
