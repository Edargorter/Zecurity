#include "Block.h"
#include "sha256.h"
#include <sstream>

Block::Block(uint32_t index_in, const string &data_in) : index(index_in), data(data_in)
{
	nonce = -1;
	timestamp = time(nullptr);
}
string Block::get_hash()

{
	return block_hash;
}

void Block::mine(uint32_t diff)
{
	char diff_ca[diff + 1];
	for(uint32_t i = 0; i < diff; i++)
		diff_ca[i] = '0';

	diff_ca[diff] = '\0';

	string diff_str(diff_ca);
	
	do {
		nonce++;
		block_hash = digest();
	} while(block_hash.substr(0, diff) != diff_str);

	cout << "Mined: " << index << " with hash: " << block_hash << "\n";
}

inline string Block::digest() const
{
	stringstream ss;
	ss << index << timestamp << data << nonce << prev_hash;
	return sha256(ss.str());
}

string Block::get_str()
{
	return "Index: " + to_string(index) + ", "
			+ "Nonce: " + to_string(nonce) + ", "
			+ "Data: " + data + ", "
			+ "SHA256: " + block_hash + ", "
			+ "Timestamp: " + to_string(timestamp) + ", "
			+ "Prev-hash: " + prev_hash;
}
