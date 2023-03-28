#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>
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

vector<string> getMinExpression(vector<vector<int>>& primeImplicantChart) {
    vector<vector<int>> product;
    for (auto row : primeImplicantChart) {
        vector<vector<int>> newProduct;
        for (int i = 0; i < row.size(); i++) {
            if (row[i] == 1) {
                if (product.empty()) {
                    newProduct.push_back({i});
                } else {
                    for (auto p : product) {
                        p.push_back(i);
                        newProduct.push_back(p);
                    }
                }
            }
        }
        product = newProduct;
    }

    int minSize = INT_MAX;
    for (auto p : product) {
        minSize = min(minSize, (int)p.size());
    }

    vector<string> minExpression;
    for (auto p : product) {
        if (p.size() == minSize) {
            string expression = "";
            for (int i = 0; i < p.size(); i++) {
                expression += to_string(p[i]);
                if (i != p.size() - 1) {
                    expression += " + ";
                }
            }
            minExpression.push_back(expression);
        }
    }

    return minExpression;
}


int main() {
    int numVars;
    cout << "Enter the number of variables: ";
    cin >> numVars;

    int numMinterms;
    cout << "Enter the number of minterms: ";
    cin >> numMinterms;

    Node* root = new Node("");
    vector<int> minterms(numMinterms);
    for (int i = 0; i < numMinterms; i++) {
        cin >> minterms[i];

        string binary = "";
        for (int j = 0; j < numVars; j++) {
            binary = to_string(minterms[i] % 2) + binary;
            minterms[i] /= 2;
        }

        Node* newNode = new Node(binary);
        root->children.push_back(newNode);
    }

    int numDontCares;
    cout << "Enter the number of don't care conditions: ";
    cin >> numDontCares;

    for (int i = 0; i < numDontCares; i++) {
        int dontCare;
        cin >> dontCare;

        string binary = "";
        for (int j = 0; j < numVars; j++) {
            binary = to_string(dontCare % 2) + binary;
            dontCare /= 2;
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

    vector<vector<int>> primeImplicantChart(numMinterms, vector<int>(primeImplicants.size()));
    for (int i = 0; i < numMinterms; i++) {
        for (int j = 0; j < primeImplicants.size(); j++) {
            bool covered = true;
            for (int k = 0; k < numVars; k++) {
                if (primeImplicants[j][k] != '-' && ((minterms[i] >> k) & 1) != (primeImplicants[j][k] - '0')) {
                    covered = false;
                    break;
                }
            }
            if (covered) {
                primeImplicantChart[i][j] = 1;
            }
        }
    }

    vector<string> minExpression = getMinExpression(primeImplicantChart);

    cout << "Minimum expression: ";
    for (auto expression : minExpression) {
        cout << expression << endl;
    }

    return 0;
}