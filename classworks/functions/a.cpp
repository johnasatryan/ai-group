#include <iostream>

int main()
{
  int x =23;
  x > 0 ? std::cout << "yes" : std::cout << "no";

  if(x > 0)
  {
    std::cout << "yes";
  }
  else 
  {
    std::cout << "no";
  }
}