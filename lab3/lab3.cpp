#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

void zad1(int n) {
    const int num_section = 10;
    int* numbers = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        double number = rand() % 100 / 100.0;
        double x = 100.0;
        double y = 50.0;
        double postman;

        __asm {
            fld number
            fld y
            fld x
           
            fmulp st(2), st(0)
            faddp st(1), st(0)
            fstp postman
        }
        numbers[i] = postman;
    }

    vector<int> section(num_section, 0);
    for (int k = 0; k < n; k++) {
        section[int((numbers[k] - 50) / 10)] += 1;
    }

    cout << "zad1:\n";
    for (int i = 0; i < num_section; i++) {
        cout << i * 10 + 50 << "," << i * 10 + 60 << " --> " << section[i] << endl;
    }
    free(numbers);
}

int genNumber()
{
    double x = (rand() % 100) / 100.0;
    if (x < 0.1) return 1;
    else if (x < 0.3) return 2;
    else if (x < 0.6) return 3;
    else if (x <= 1) return 4;
    else return 0;
}

void zad2(int n)
{
    int numbers[4] = { 0 };
    for (int i = 0; i < n; i++)
    {
        int x = genNumber();
        numbers[x - 1] += 1;
    }

    cout << "\nzad2:\n";
    for (int i = 0; i < 4; i++)
    {
        cout << i + 1 << " --> " << numbers[i] << endl;
    }
}

int main() {
    srand(time(NULL));
    const int n = 10000;
    zad1(n);
    zad2(n);
    return 0;
}