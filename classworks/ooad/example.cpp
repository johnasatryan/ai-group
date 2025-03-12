#include <string>
#include <iostream>

class BankAccount {

  public:
    BankAccount(float balance, const std::string& id) {
      this->balance = balance;
      this->id = id;
    }

  private:
    float balance;
    std::string id;
};

int main() {
  BankAccount account1(400.5, "1245435");

  float *p = (float *)&account1;
}