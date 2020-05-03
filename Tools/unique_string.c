// Supercombination generator
// Zachary Bowditch (Edargorter) 2019
// If letters = n, length = k
// Then a supercombination is a string of length n^k + k - 1 containing all possible
// combinations of letters up to letter[n] of length k.

#include <stdio.h>
#include <stdlib.h>

#define newline printf("\n");

int main(int argc, char **argv)
{
	int letters = 26;
	int length = 4;
	int iterations = 10;

	if(argc > 3){
		letters = atoi(argv[1]);

		if(letters > 26){
			printf("Too many letters. Keep < 26\n");
			exit(1);
		}

		length = atoi(argv[2]);
		iterations = atoi(argv[3]);
	} 

	int offset;
	int base = 97;
	int char_offset = 0;
	char ch = 'a';

	for (int iter = 0; iter < iterations; iter++){

		for (int l = 0; l < letters - 1; l++){
			for (int i = 0; i < letters; i++){
				for (int j = 0; j < length; j++){

					ch = base + i;

					if(j == offset)
						ch = base + ((ch - base + char_offset) % letters);

					printf("%c", ch);
				}
			}
			char_offset = (char_offset + 1) % letters;
		}

		offset = (offset + 1) % length;
	}

	return 0;
}
