#include "lemin.h"

t_lemin	*init_lemin(void)
{
	t_lemin	*lemin;

	if (!(lemin = malloc(sizeof(t_lemin))))
		exit(1);
	lemin->count = 0;
    lemin->arr = NULL;
    lemin->arr = NULL;
    lemin->start = NULL;
	lemin->finish = NULL;
	lemin->rooms = 0;
	lemin->solution = NULL;
	lemin->prev_solution = NULL;
	lemin->edge = 0;
	lemin->sup_list = NULL;
	return (lemin);
}

t_room	*init_room(char *s)
{
	t_room	*room;

	if (!(room = malloc(sizeof(t_room))))
		exit(1);
	room->name = ft_strdup(s);
	room->next = NULL;
	room->prev = NULL;
	room->path = NULL;
	room->idx = 0;
	room->min_w = INT_MAX / 2;
	room->superpos = 0;
	return (room);
}

t_tmp	*init_tmp(t_tmp *tmp, int a, char *s)
{
	t_tmp	*start;
	int		i;

	if (!(i = 0) && !tmp)
	{
		if (!(tmp = malloc(sizeof(t_tmp))))
			exit(1);
		start = tmp;
	}
	else
	{
		start = tmp;
		while (tmp->next)
			tmp = tmp->next;
		if (!(tmp->next = malloc(sizeof(t_tmp))))
			exit(1);
		tmp = tmp->next;
	}
	tmp->next = NULL;
	while (s[i] && s[i] != ' ')
		i++;
	s[i] = '\0';
	tmp->room = init_room(s);
	if (a == 0 && !(tmp->room->min_w = 0))
		(!g_lemin->start) ? g_lemin->start = tmp->room : error_exit();
	else if (a == -1)
		(!g_lemin->finish) ? g_lemin->finish = tmp->room : error_exit();
	return (start);
}
