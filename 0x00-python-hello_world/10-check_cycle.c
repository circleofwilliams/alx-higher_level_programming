#include "lists.h"

/**
 * num - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */

unsigned int number(listint_t *head)
{
	listint_t *ptr;
	unsigned int n; /* number of nodes */

	ptr = head;
	n = 0;
	while (ptr != NULL)
	{
		if (ptr->next == head)
			break;
		ptr = ptr->next;
		n++;
	}

	return (n);
}

#include "lists.h"

/**
* check_cycle - check if there is a cycle in a list
* @list: pointer to head of list
* Return: 0 or 1
*/

int check_cycle(listint_t *list)
{
	unsigned int i;

	listint_t *ptr = list;
	unsigned int num = number(list);

	if (list == NULL)
		return (0);

	for (i = 0; i < num; i++)
	{
		ptr = ptr->next;
	}

	if (ptr == NULL)
		return (0);
	else
		return (1);
}
