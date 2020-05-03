#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
 * Generation program for De Bruijn Sequences.
 * A De Bruijn sequence will contain, as substrings,
 * exactly one instance of every possible string made 
 * from a specified alphabet.
 *
*/

#define newline printf("\n")

int* arr;
char* alphabet;
int n;
int k;

void db_gen(int t, int p)
{
	if(t > p){
		if(!(n % p)){
			for(int i = 1; i < p + 1; i++)
				printf("%c", alphabet[arr[i]]);
		}
	} else {
		arr[t] = arr[t - p];
		db_gen(t + 1, p);

		for(int i = arr[t - p] + 1; i < k; i++){
			arr[t] = i;
			db_gen(t + 1, t);
		}
	}
}

int main(int argc, char **argv)
{
	if(argc < 3){
		printf("Usage: %s [ alphabet ] [ length ]\n", argv[0]);
		exit(1);
	}

	alphabet = argv[1];
	k = strlen(alphabet);

	arr = (int*) malloc(sizeof(int) * k * n);

	for(int i = 0; i < k*n; i++)
		arr[i] = 0;

	if(!(n = (int) strtol(argv[2], (char **) NULL, 10))){
		printf("Error: [ n ] needs to be an integer > 0.\n");
		exit(2);
	}

	newline;
	printf("Alphabet: %s\n", alphabet);
	newline;
	printf("N: %d\n", n);

	db_gen(1, 1);
	newline;

	return 0;
}
