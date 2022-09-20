#include "Blockchain.h"

int main()
{
	Blockchain bchain = Blockchain();

	cout << "Mine block 1..." << "\n";
	bchain.append_block(Block(1, "Block 1 data"));
	cout << "Mine block 2..." << "\n";
	bchain.append_block(Block(2, "Block 2 data"));
	cout << "Mine block 3..." << "\n";
	bchain.append_block(Block(3, "Block 3 data"));

	bchain.print_chain();

	return 0;
}
