#include <iostream>

using namespace std;

void print(int* vec, int length, int position) {
	bool k = true;
	for (size_t i = 1; i <= length; i++) {
		for (size_t j = 0; j < position; j++) {
			if (i == vec[j])
				k = false;
		}
		if (!k)
		{
			k = true;
			continue;
		}
		vec[position] = i;
		if (position == length - 1) {
			for (size_t i = 0; i < length; i++)	{
				cout << vec[i];
			}
			cout << endl;
			return;
		}
		else {
			print(vec, length, position + 1);
		}
	}
}

int main() {
	int n;
	cin >> n;
	int *vec = new int[n];
	print(vec, n, 0);
	return 0;
}