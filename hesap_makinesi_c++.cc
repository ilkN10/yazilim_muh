#include <iostream>
#include <limits>
using namespace std;

int main() {
    double num1, num2;
    char operation;
    char again;

    cout << "=== Basit Hesap Makinesi ===\n";
    cout << "Cikis icin herhangi bir sayi yerine 'q' yazabilirsiniz.\n";

    while (true) {
        cout << "\nBirinci sayiyi girin: ";
        if (!(cin >> num1)) {
            if (cin.fail()) {
                cin.clear(); // akışı temizle
                string temp;
                cin >> temp;
                if (temp == "q" || temp == "Q") {
                    cout << "Programdan cikiliyor...\n";
                    break;
                } else {
                    cout << "Gecersiz sayi girdiniz.\n";
                    continue;
                }
            }
        }

        cout << "Yapmak istediginiz islemi girin (+, -, *, /): ";
        cin >> operation;

        if (operation == 'q' || operation == 'Q') {
            cout << "Programdan cikiliyor...\n";
            break;
        }

        cout << "Ikinci sayiyi girin: ";
        if (!(cin >> num2)) {
            if (cin.fail()) {
                cin.clear();
                string temp;
                cin >> temp;
                if (temp == "q" || temp == "Q") {
                    cout << "Programdan cikiliyor...\n";
                    break;
                } else {
                    cout << "Gecersiz sayi girdiniz.\n";
                    continue;
                }
            }
        }

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
                else {
                    cout << "Hata: Sifira bolme yapilamaz! Lutfen gecerli bir sayi girin.\n";
                    continue;
                }
                break;
            default:
                cout << "Gecersiz islem girdiniz!" << endl;
        }

        cout << "\nBaska bir islem yapmak istiyor musunuz? (e/h): ";
        cin >> again;

        if (again == 'h' || again == 'H') {
            cout << "Programdan cikiliyor...\n";
            break;
        }

        // input akışını temizle
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    return 0;
}
