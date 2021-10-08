//Author: Zachary Bowditch (Edargorter)
//Inspired by Python tutorial https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

#include "base.h"
#include "block.h"
#include "transaction.h"
#include <chrono>
#include <openssl/sha.h> // ???

class Blockchain
{
private:
	vector<Block> chain;
	vector<Transaction> transactions;

public:
	Blockchain()
	{
	}

	void new_block(uint64_t proof, string prev_hash)
	{
		Block new_block(chain.size() + 1, system_clock::now(), &transactions, proof, prev_hash);
		transactions.erase(transactions.begin(), transactions.end());
	}

	void new_transaction(string sender, string recipient, uint64_t amount)
	{
		Transaction new_transaction(sender, recipient, amount);
		transactions.push_back(new_transaction);
	}

	static string to_string_transactions()
	{
		string tst = "";
		for(Transaction t : transactions)
			tst += "," + to_string(t);
		return tst;
	}

	static string hash(Block block)
	{
		//SHA-256 hash of JSONified block 
		string sha256hash = SHA256(block.to_string());
		return sha256hash;
	}

	Block* last_block()
	{
		return chain.back();
	}
};
