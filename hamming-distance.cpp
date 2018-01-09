#include <iostream>
#include <string>

using namespace std;

class Solution
{
  public:
    int hammingDistance(int x, int y)
    {
        if (x == y)
        {
            return 0;
        }

        int x_remainder = 0;
        int y_remainder = 0;
        int num_mismatch = 0;
        while (x != 0 && y != 0)
        {
            x_remainder = x % 2;
            y_remainder = y % 2;
            x = x / 2;
            y = y / 2;
            if (x_remainder != y_remainder)
            {
                num_mismatch++;
            }
        }

        while (x != 0)
        {
            if (x % 2)
            {
                num_mismatch++;
            }
            x = x / 2;
        }
        while (y != 0)
        {
            if (y % 2)
            {
                num_mismatch++;
            }
            y = y / 2;
        }

        return num_mismatch;
    }
};

int main()
{
    Solution obj = Solution();
    int x = 99;
    int y = 20;
    int index = obj.hammingDistance(x, y);
    cout << index << endl;
    return 0;
}