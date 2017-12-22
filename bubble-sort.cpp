#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;
void bubbleSort(vector<int> a, int n);

int main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (int a_i = 0; a_i < n; a_i++)
    {
        cin >> a[a_i];
    }
    bubbleSort(a, n);
    return 0;
}

void bubbleSort(vector<int> a, int n)
{
    int temp = 0;
    int num_swap = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            // Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1])
            {
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
                num_swap++;
            }
        }
    }

    cout<<"Array is sorted in "<<num_swap<<" swaps.\n";
    cout<<"First Element: "<<a[0]<<"\n";
    cout<<"Last Element: "<<a[n-1];
}