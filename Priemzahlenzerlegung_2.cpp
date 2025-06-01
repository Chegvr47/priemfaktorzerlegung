#include <iostream>
using namespace std;

int number = 1;

int main() {

    cout << "lol?";
    cin >> number;

    for(int n = 2; n <= 1000000; n++) {
        bool isPrime = true;

        for(int d = 2; d * d <= n; d++) {
            if(n % d == 0) {
                isPrime = false;
                break;
            }
        }
        if(isPrime) {
            cout << n << " ";
        }
    }
    cout << "Enter a number: ";
    cin >> number;
}