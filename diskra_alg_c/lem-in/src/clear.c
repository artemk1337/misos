#include "lemin.h"

t_solution	*clean_sol(void)
{
	t_solution	*tmp_sol;
	t_solution	*tmp_sol_next;

	tmp_sol = g_lemin->solution;
	while (tmp_sol)
	{
		free(tmp_sol->arr);
		tmp_sol_next = tmp_sol->next;
		free(tmp_sol);
		tmp_sol = tmp_sol_next;
	}
	return (NULL);
}

void			clean_tmp(t_tmp **tmp)
{
	t_tmp	*temp_ptr;

	while (*tmp)
	{
		temp_ptr = (*tmp)->next;
		free(*tmp);
		*tmp = temp_ptr;
	}
}
