#include <iostream>

int extendedEuclidean(int a, int b, int& x, int& y) {
    if (a == 0) {
        x = 0;
        y = 1;
        return b;
    }

    int x1, y1;
    int gcd = extendedEuclidean(b % a, a, x1, y1);

    x = y1 - (b / a) * x1;
    y = x1;

    return gcd;
}

int findInverse(int a, int b) {
    int x, y;
    int gcd = extendedEuclidean(a, b, x, y);

    if (gcd != 1) {
        std::cout << "Inverse does not exist." << std::endl;
        return -1;
    }

    // Ensure the result is positive
    return (x % b + b) % b;
}

int main() {
    cin>>a;
    cin>>b;

    int inverse = findInverse(a, b);

    if (inverse != -1) {
        std::cout << "Inverse of " << a << " modulo " << b << " is: " << inverse << std::endl;
    }

    return 0;
}
