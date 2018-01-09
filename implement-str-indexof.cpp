#include <iostream>
#include <string>

using namespace std;

class Solution
{
  public:
    int strStr(string haystack, string needle)
    {
        int haystack_len = haystack.size();
        int needle_len = needle.size();

        if (needle_len == 0 || (haystack_len == needle_len && haystack == needle))
        {
            return 0;
        }
        else if (haystack_len < needle_len)
        {
            return -1;
        }

        int j = 0, index = 0;
        for (int i = 0; i < haystack_len; i++)
        {
            if (haystack.at(i) == needle.at(j))
            {
                index = i;
                while (j < needle_len && index <  haystack_len)
                {
                    if (haystack.at(index) == needle.at(j))
                    {
                        j++;
                        index++;
                    }
                    else
                    {
                        j = 0;
                        break;
                    }
                }
                if (j == needle_len)
                {
                    return i;
                }
            }
        }

        return -1;
    }
};

int main()
{
    Solution obj = Solution();
    string haystack = "hello";
    string needle = "llo";
    int index = obj.strStr(haystack, needle);
    cout << index << endl;
    return 0;
}