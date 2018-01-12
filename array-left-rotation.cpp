#include <bits/stdc++.h>

using namespace std;

vector<int> leftRotation(vector<int> a, int d)
{
    // Complete this function
    int arr_len = a.size();
    if (d == arr_len)
    {
        return a;
    }
    vector<int>::iterator itr = a.begin();
    itr = itr + d;

    vector<int> result;
    while (itr != a.end())
    {
        result.push_back(*itr);
        itr++;
    }

    int i = 0;
    itr = a.begin();
    while (i < d)
    {
        result.push_back(*itr);
        itr++;
        i++;
    }

    return result;
}

int main()
{
    int n;
    int d;
    cin >> n >> d;
    vector<int> a = {1, 2, 3, 4, 5};
    vector<int> result = leftRotation(a, d);
    for (ssize_t i = 0; i < result.size(); i++)
    {
        cout << result[i] << (i != result.size() - 1 ? " " : "");
    }
    cout << endl;

    return 0;
}