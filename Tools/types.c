#include <stdio.h>

int main(int argc, char **argv)
{
	size_t result = sizeof(size_t);
	int int_result = sizeof(size_t);

	printf("size_t result: %zd\n", result);
	printf("int result: %d\n", int_result);
	return 0;
}
