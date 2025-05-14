#include <iostream>
using namespace std;

int main() {
    double num1, num2;
    char operation;

    cout << "Birinci sayiyi girin: ";
    cin >> num1;

    cout << "Yapmak istediginiz islemi girin (+, -, *, /): ";
    cin >> operation;

    cout << "Ikinci sayiyi girin: ";
    cin >> num2;

    switch (operation) {
        case '+':
            cout << "Sonuc: " << num1 + num2 << endl;
            break;
        case '-':
            cout << "Sonuc: " << num1 - num2 << endl;
            break;
        case '*':
            cout << "Sonuc: " << num1 * num2 << endl;
            break;
        case '/':
            if (num2 != 0)
                cout << "Sonuc: " << num1 / num2 << endl;
            else
                cout << "Sifira bolme hatasi!" << endl;
            break;
        default:
            cout << "Gecersiz islem!" << endl;
    }

    return 0;
}
