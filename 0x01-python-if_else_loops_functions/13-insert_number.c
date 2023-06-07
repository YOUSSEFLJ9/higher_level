#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *sorted, *tmp;
	int i, j;
	sorted = malloc(sizeof(listint_t));
	if (!sorted)
		return (NULL);
	sorted->n = number;
	tmp = *head;
	if (!(*head))
	{
		*head = sorted;
		sorted->next = NULL;
		return (sorted);
	}
	while (tmp)
	{
		if (number > tmp->n)
		{
			if (!tmp->next)
			{
				tmp->next = sorted;
				sorted->next = NULL;
				return (sorted);
			}
			tmp = tmp->next;
			continue;
		}
		else
		{
			sorted->next = tmp;
			if (tmp = *head)
			{
				*head = sorted;
				break;
			}
			 tmp = *head;
	  for (j = 0; j < i; j++)
	    {
	      if (j == (i - 1))
		{
		  tmp->next = sorted;
		  break;
		}
	      tmp = tmp->next;
	    }
	  break;
	}
    }
  return (sorted);
}
		}

	}
}
