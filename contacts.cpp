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
#include <unordered_set>
#include <regex>

using namespace std;
const int MAX_BRANCHES = 26;

struct Node{
    struct Node* branches[MAX_BRANCHES];
    bool isEndOfWord;
};

struct Node* initializeNode(string word){
    struct Node *node = new Node;
    int word_length = sizeof(word) / sizeof(string);

    return node;
}

void insertNode(struct Node *node, string key){
    
}

int main()
{
    int n;
    cin >> n;
    set<string> contacts;
    int count = 0;
    string op = "";
    string contact = "";
    map<string, int> contacts_count;

    regex expression;
    

    for (int a0 = 0; a0 < n; a0++)
    {
        count = 0;
        cin >> op >> contact;
        if (op == "add")
        {
            contacts.insert(contact);
            contacts_count[contact] = 1;
        }
        else
        {
            auto search = contacts_count.find(contact);
            if(contacts_count[contact] == 1){
                cout<<1<<endl;
            }

            else if(search != contacts_count.end()) {
                contacts_count[contact] += 1;
                cout<<search->second<<endl;
            }
        }
    }
    return 0;
}
