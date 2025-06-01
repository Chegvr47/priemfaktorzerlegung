#include <iostream>
#include <string>

using namespace std;
int main() {
    int n;
    cout << "Enter an integer: ";
    cin >> n;
    bool end = false;

    while(end ==false){
    // Check if the number is prime
    bool isPrime = true;
    if (n <= 1) {
        isPrime = false;
    } else {
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0) {
                isPrime = false;
                break;
            }
        }
    }

    // Output the result
    if (isPrime) {
        cout << n << " is a prime number." << endl;
    } else {
        cout << n << " is not a prime number." << endl;
    }
    // Ask the user if they want to check another number
    string answer;
    cout << "Do you want to check another number? (yes/no): ";
    cin >> answer;
    if (answer == "no") {
        end = true;
    } else if (answer == "yes") {
        cout << "Enter an integer: ";
        cin >> n;
    } else {
        cout << "Invalid input. Exiting." << endl;
        end = true;
    }
    }

    return 0;
}