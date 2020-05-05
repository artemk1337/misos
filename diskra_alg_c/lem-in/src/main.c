/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cchadwic <cchadwic@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/02/14 15:04:40 by cchadwic          #+#    #+#             */
/*   Updated: 2020/03/02 15:32:02 by cchadwic         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "lemin.h"
//#define DEBUG
#ifndef DEBUG
# define STDIN 0
#endif

// TODO Comments and unknown commands must be ignored by program
//  - 101
// TODO Replace checking funcs if necessary


// TODO delete DEBUG macros before deploy
//  - 24
//  - 155

#ifdef DEBUG
# include <fcntl.h>
# define STDIN 3
int g_fd;
#endif

void	put_way_dop(t_tmp *tmp, t_tmp *tmp_2, char *s2, int weight)
{
	t_next *neigh;

	if (!tmp->room->next)
	{
		if (!(tmp->room->next = malloc(sizeof(t_next))))
			error_exit();
		neigh = tmp->room->next;
	}
	else
	{
		neigh = tmp->room->next;
		while (neigh->next)
		{
			if (!ft_strcmp(neigh->room->name, s2))
			    return ;
				//				error_exit();
			neigh = neigh->next;
		}
		if (!(neigh->next = malloc(sizeof(t_next))))
			error_exit();
		neigh = neigh->next;
	}
	neigh->weight = weight;
	neigh->toggle = 1;
	neigh->next = NULL;
	while (tmp_2 && ft_strcmp(tmp_2->room->name, s2))
		tmp_2 = tmp_2->next;
	if (tmp_2)
		neigh->room = tmp_2->room;
}

void	put_way(char *s, t_tmp *tmp)
{
	t_tmp	*start;
	int		i;

	i = 0;
	(g_lemin->edge)++;
	check_edge(s);
	while (s[i] != '-')
		i++;
	s[i] = '\0';
	start = tmp;
	while (tmp && ft_strcmp(tmp->room->name, s))
		tmp = tmp->next;
	if (tmp)
		put_way_dop(tmp, start, &(s[i + 1]), 1);
	tmp = start;
	while (tmp && ft_strcmp(tmp->room->name, &(s[i + 1])))
		tmp = tmp->next;
	if (tmp)
		put_way_dop(tmp, start, s, 1);
	else
		error_exit();
}

static t_tmp	*create_struct_(char *line, t_tmp *tmp)
{
	if (ft_strchr(line, ' '))
	{
		check_node(line);
		tmp = init_tmp(tmp, 1, line);
		(g_lemin->rooms)++;
	}
	else if (ft_strchr(line, '-'))
		put_way(line, tmp);
	return (tmp);
}

static t_tmp	*create_struct_prefix(char **line, t_tmp *tmp)
{
	if (!ft_strcmp(&(line[0][2]), "start"))
	{
		ft_strdel(line);
		if ((get_next_line(STDIN, line)) < 1)
			error_exit();
		check_node(*line);
		g_lemin->vector = ft_put_vec(g_lemin->vector, *line);
		tmp = init_tmp(tmp, 0, *line);
		(g_lemin->rooms)++;
	}
	else if (!ft_strcmp(&(line[0][2]), "end"))
	{
		ft_strdel(line);
		if ((get_next_line(STDIN, line)) < 1)
			error_exit();
		check_node(*line);
		g_lemin->vector = ft_put_vec(g_lemin->vector, *line);
		tmp = init_tmp(tmp, -1, *line);
		(g_lemin->rooms)++;
	}
	return (tmp);
}


t_tmp	*create_struct(void)
{
	char	*line;
	t_tmp	*tmp;

	tmp = NULL;
	while (get_next_line(STDIN, &line) > 0)
	{
		if (*line == '\0')
		{
			ft_strdel(&line);
			break ;
		}
		g_lemin->vector = ft_put_vec(g_lemin->vector, line);
		if (line[0] != '#')
			tmp = create_struct_(line, tmp);
		else if (line[0] == '#' && line[1] == '#')
			tmp = create_struct_prefix(&line, tmp);
		ft_strdel(&line);
	}
	if (!(tmp))
		error_exit();
	return (tmp);
}













static int	alg_bell_ford(t_tmp *start, int counter)
{
	t_tmp	*curr;
	t_room	*prev_r;
	t_next	*curr_n;
	t_next	*prev_n;

	curr = start;
	while (curr)
	{
		curr_n = curr->room->next;
		while (curr_n)
		{
			prev_r = curr_n->room;
			prev_n = prev_r->next;
			while (prev_n && prev_n->room != curr->room)
				prev_n = prev_n->next;
			if (prev_n->toggle && prev_r->min_w + prev_n->weight < curr->room->min_w
			&& prev_r != g_lemin->finish && !curr->room->superpos && !prev_r->superpos
			&& prev_r->min_w != (INT_MAX / 2) && prev_r->path == NULL)
			/*
			**add prev_r->path == NULL && prev_r != g_lemin->finish && curr->room->path == NULL
			*/
			{
				counter++;
				curr->room->min_w = prev_r->min_w + prev_n->weight;
				curr->room->prev = prev_r;
			}
			curr_n = curr_n->next;
		}
		curr = curr->next;
	}
	return (counter);
}


static void	alg_deikstri(void)
{
	t_tmp	*start_stack;
	t_tmp	*curr_stack;
	t_next	*curr_neigh;
	t_tmp	*new_stack;

	start_stack = ft_memalloc(sizeof(t_tmp));
	curr_stack = start_stack;
	curr_stack->room = g_lemin->start;
	while (curr_stack)
	{
		curr_neigh = curr_stack->room->next;
		while (curr_neigh)
		{
			if (curr_neigh->toggle &&
				curr_stack->room->min_w + curr_neigh->weight < curr_neigh->room->min_w)
			{
				curr_neigh->room->min_w = curr_stack->room->min_w + curr_neigh->weight;
				curr_neigh->room->prev = curr_stack->room;
				 if (!curr_neigh->room->superpos)
				 {
				 	new_stack = curr_stack;
				 	while (new_stack->next)
				 		new_stack = new_stack->next;
				 	new_stack->next = ft_memalloc(sizeof(t_tmp));
				 	new_stack->next->room = curr_neigh->room;
				 }
				 curr_neigh->room->superpos = 1;
			}
			curr_neigh = curr_neigh->next;
		}
		curr_stack = curr_stack->next;
	}
}


void	algorithm(t_tmp *list)
{
	int i;
	int alg;

	while (1)
	{
		i = 0;
		alg = 0; // Choose algorithm
		if (alg == 0)
		{
			while (i++ < g_lemin->edge)
			if (!alg_bell_ford(list, 0))
				break ;
		}
		else
			alg_deikstri();
		if (!(g_lemin->finish->prev))
			break ;
		if (!save_tmp())
			break ;
		reset_struct(list);
		return ; // added to return after first solution
	}
}





void	print_sol(void)
{
	t_solution	*sol;
	int			i;

	if (!g_lemin->solution)
	{
		ft_putstr("NO SOLUTION\n");
		return ;	
	}
	ft_putstr("Ways:\n\n");
	sol = g_lemin->solution;
	while (sol)
	{
		//ft_putstr("Solve:\n");
		i = 0;
		while (sol->arr[i])
		{
			ft_putstr(sol->arr[i]->name);
			if (sol->arr[i + 1])
				ft_putstr(" -> ");
			i++;
		}
		ft_putchar('\n');
		sol = sol->next;
	}
	ft_putchar('\n');
}




	









int		main()
{
#ifdef DEBUG
	g_fd = open("interesting_maps/gemerald4", O_RDONLY);
#endif
	t_tmp	*tmp;

	g_lemin = init_lemin();
	tmp = create_struct();
	g_lemin->arr = create_array(&tmp);
	check_duplicate_nodes(g_lemin->arr);
	algorithm(tmp);
	print_sol();
	if (!(g_lemin->solution))
		error_exit();
	//show_input();
	return (0);
}