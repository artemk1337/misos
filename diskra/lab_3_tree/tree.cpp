#include <iostream>
#include <stdlib.h>
using namespace std;

struct	Node
{
    int		data;
	int		depth;
	Node	*left;
	Node	*right;
    Node	*next;
};


class	Nodes
{
	public:
		Node	*create_node(Node *prev)
		{
			Node	*nd;

			nd = new Node;
			nd->data = NULL;
			if (prev)
				nd->depth = prev->depth + 1;
			else
				nd->depth = 0;
			nd->left = NULL;
			nd->right = NULL;
			return nd;
		}

		// Recursion
		void	create_left_right_nodes(Node *curr, int max_depth)
		{
			if (max_depth > curr->depth)
				return ;
			curr->left = create_node(curr);
			curr->right = create_node(curr);
			create_left_right_nodes(curr->left, max_depth);
			create_left_right_nodes(curr->right, max_depth);
		}
};


int		*create_tree_arr(int depth)
{
	int		n;
	int		*arr;

	n = 1;
	while (depth--)
		n = n * 2 + 1;
	n++;
	arr = (int *)malloc(sizeof(int) * (n + 1));
	arr[n] = NULL;
	return arr;
}

int		main()
{
	Node		*first_node;
	Nodes		list;
	int			*arr;
	

	// Create tree on list
	first_node = list.create_node(NULL);
	list.create_left_right_nodes(first_node, 5); // 5 - depth
	// Create tree on array
	arr = create_tree_arr(5); // 5 - depth
    return 0;
}


