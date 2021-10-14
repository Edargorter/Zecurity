#include <cstdint>
#include <vector>
#include "Block.h"
#include "sha256.h"

using namespace std;

class Blockchain
{
private:
	uint32_t diff;
	vector<Block> chain;

	Block get_last_block() const;

public:
	Blockchain();
	void append_block(Block new_block);
	void print_chain();
};
