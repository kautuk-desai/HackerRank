#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n = 0;
    cin >> n;
    map<string, int> occurences_map;
    map<string, int>::iterator itr;
    string s = "";

    for (int i = 0; i < n; i++)
    {
        cin >> s;
        itr = occurences_map.find(s);
        if (itr != occurences_map.end())
        {
            occurences_map[s] += 1;
        }
        else
        {
            occurences_map.insert(pair<string, int>(s, 1));
        }
    }

    int q = 0;
    cin >> q;
    int result[q];
    string query = "";
    for (int i = 0; i < q; i++)
    {
        cin >> query;

        itr = occurences_map.find(query);
        if (itr != occurences_map.end())
        {
            result[i] = occurences_map[query];
        }
        else
        {
            result[i] = 0;
        }
    }

    for (int i = 0; i < q; i++)
    {
        cout << result[i] << endl;
    }
    return 0;
}