#include "Blockchain.h"

Blockchain::Blockchain()
{
	chain.emplace_back(Block(0, "genesis"));
	diff = 4;
}

void Blockchain::append_block(Block new_block)
{
	new_block.prev_hash = get_last_block().get_hash();
	new_block.mine(diff);
}

Block Blockchain::get_last_block() const
{
	return chain.back();
}

void Blockchain::print_chain()
{
	for(Block block : chain){
		cout << block.get_str() << "\n";
	}
}
