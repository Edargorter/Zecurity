#include <cstdint>
#include <iostream>

using namespace std;

class Block
{
private:
	uint32_t index;
	uint64_t nonce;
	string data;
	string block_hash;
	time_t timestamp;

	string digest() const;

public:
	string prev_hash;

	Block(uint32_t index_in, const string &data_in);
	string get_hash();
	string get_str();
	void mine(uint32_t diff);
};
