#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Node {
    string value;
    vector<Node*> children;
    bool checked;
    Node(string v) : value(v), checked(false) {}
};

void getPrimeImplicants(Node* root, vector<string>& primeImplicants) {
    if (root->children.empty()) {
        primeImplicants.push_back(root->value);
        return;
    }
    for (auto child : root->children) {
        getPrimeImplicants(child, primeImplicants);
    }
}

void combine(Node* root, int numVars) {
    for (int i = 0; i < numVars; i++) {
        vector<Node*> newChildren;
        for (auto child1 : root->children) {
            for (auto child2 : root->children) {
                if (child1->value[i] != child2->value[i] && !child1->checked && !child2->checked) {
                    string newValue = child1->value;
                    newValue[i] = '-';
                    Node* newNode = new Node(newValue);
                    newChildren.push_back(newNode);
                    child1->checked = true;
                    child2->checked = true;
                }
            }
        }
        for (auto child : newChildren) {
            root->children.push_back(child);
        }
    }
}

int main() {
    int numVars;
    cout << "Enter the number of variables: ";
    cin >> numVars;

    int numMinterms;
    cout << "Enter the number of minterms: ";
    cin >> numMinterms;

    Node* root = new Node("");
    for (int i = 0; i < numMinterms; i++) {
        int minterm;
        cin >> minterm;

        string binary = "";
        for (int j = 0; j < numVars; j++) {
            binary = to_string(minterm % 2) + binary;
            minterm /= 2;
        }

        Node* newNode = new Node(binary);
        root->children.push_back(newNode);
    }

    combine(root, numVars);

    vector<string> primeImplicants;
    getPrimeImplicants(root, primeImplicants);

    cout << "Prime implicants: ";
    for (auto implicant : primeImplicants) {
        cout << implicant << " ";
    }
    cout << endl;

    return 0;
}