class Block()
{
private:
	uint64_t index;
	uint64_t time_milli;
	string transactions;
	uint64_t proof;

public:
	Block(uint64_t, uint64_t, string, uint64_t);

	static string to_string()
	{
		return to_string(index) + "-" + to_string(time_milli) + "-" + transactions + to_string(proof);
	}
};
