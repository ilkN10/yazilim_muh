#include <iostream>
#include <limits> // numeric_limits kullanımı için
using namespace std;

int main() {
    double num1, num2;
    char operation;
    char again;

    cout << "Basit Hesap Makinesi (Cikis icin 'q' girin)\n";

    while (true) {
        cout << "\nBirinci sayiyi girin: ";
        if (!(cin >> num1)) {
            cout << "Gecersiz sayi girdiniz. Program sonlandiriliyor." << endl;
            break;
        }

        cout << "Yapmak istediginiz islemi girin (+, -, *, /): ";
        cin >> operation;

        if (operation == 'q') {
            cout << "Programdan cikiliyor..." << endl;
            break;
        }

        cout << "Ikinci sayiyi girin: ";
        if (!(cin >> num2)) {
            cout << "Gecersiz sayi girdiniz. Program sonlandiriliyor." << endl;
            break;
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
                else
                    cout << "Hata: Sifira bolme yapilamaz!" << endl;
                break;
            default:
                cout << "Gecersiz islem girdiniz!" << endl;
        }

        // Kullanıcı tekrar işlem yapmak istiyor mu?
        cout << "\nBaska bir islem yapmak istiyor musunuz? (e/h): ";
        cin >> again;

        if (again == 'h' || again == 'H') {
            cout << "Programdan cikiliyor..." << endl;
            break;
        }

        // Hatalı giriş sonrası input temizliği
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    return 0;
}
