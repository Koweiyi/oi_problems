#include <iostream>
#include <vector>
using namespace std;

class TrieNode {
public:
    bool isEnd;
    vector<TrieNode*> next;

    TrieNode() {
        isEnd = false;
        next = vector<TrieNode*>(26, nullptr);
    }
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode* cur = root;
        for (char c : word) {
            int idx = c - 'a';
            if (cur->next[idx] == nullptr) {
                cur->next[idx] = new TrieNode();
            }
            cur = cur->next[idx];
        }
        cur->isEnd = true;
    }

    bool search(string str, int pos, TrieNode* cur) {
        if (pos == str.length()) {
            return cur->isEnd;
        }
        int idx = str[pos] - 'a';
        if (cur->next[idx] == nullptr) {
            return false;
        }
        return search(str, pos+1, cur->next[idx]);
    }
};

int main() {
    int n;
    cin >> n;
    vector<Trie*> tries(n);
    for (int i = 0; i < n; i++) {
        tries[i] = new Trie();
        int k;
        cin >> k;
        for (int j = 0; j < k; j++) {
            string s;
            cin >> s;
            tries[i]->insert(s);
        }
    }
    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        string x;
        cin >> x;
        for (int j = 0; j < n; j++) {
            if (tries[j]->search(x, 0, tries[j]->root)) {
                cout << j+1 << " ";
            }
        }
        cout << endl;
    }
    return 0;
}