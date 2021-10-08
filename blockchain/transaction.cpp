class Transaction()
{
private:
	string src;
	string dest;
	uint64_t amount;

public:
	Transaction(string, string, uint64_t);
	
	static string to_string()
	{
		return src + "-" + dest + "-" + to_string(amount);
	}
};
