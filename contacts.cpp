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

struct Node
{
    struct Node *branches[MAX_BRANCHES];
    int size = 0;
};

struct Node *initializeNode()
{
    struct Node *node = new Node;
    for (int i = 0; i < MAX_BRANCHES; i++)
    {
        node->branches[i] = NULL;
        node->size = 0;
    }
    return node;
}

void insertNode(struct Node *node, string key)
{
    struct Node *nodeCrawl = node;
    int key_length = key.length();
    int index = 0;
    for (int i = 0; i < key_length; i++)
    {
        index = key[i] - 'a';
        if (!nodeCrawl->branches[index])
        {
            nodeCrawl->branches[index] = initializeNode();
        }

        nodeCrawl = nodeCrawl->branches[index];
        nodeCrawl->size += 1;
    }
}

int search(struct Node *root, string key)
{
    struct Node *nodeCrawl = root;
    int key_length = key.length();
    int count = 0;
    int index = 0;
    for (int i = 0; i < key_length; i++)
    {
        index = key[i] - 'a';
        if (nodeCrawl->branches[index])
        {
            nodeCrawl = nodeCrawl->branches[index];
        }
        else
        {
            nodeCrawl = nodeCrawl->branches[index];
            break;
        }
    }
    if (nodeCrawl)
    {
        count = nodeCrawl->size;
    }

    return count;
}

int main()
{
    int n;
    int num_contacts = 0;
    cin >> n;

    set<string> contacts;
    string op = "";
    string contact = "";
    // initialize the root node. and keep on updating the root node.
    Node *root = initializeNode();
    stringstream result;

    for (int a0 = 0; a0 < n; a0++)
    {
        cin >> op >> contact;

        if (op == "add")
        {
            contacts.insert(contact);
            insertNode(root, contact);
        }
        else
        {
            num_contacts = search(root, contact);
            result << num_contacts << endl;
        }
    }
    cout << result.str();
    return 0;
}