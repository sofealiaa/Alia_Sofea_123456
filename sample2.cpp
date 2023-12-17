#include <iostream>
using namespace std;

int main()
{
int choice;

do
{


cout << endl
<< " 1 - Calculate BMI.\n"
<< " 2 - Convert Weight (Gram - Kilogram).\n"
<< " 3 - Convert Weight (Gram - Tonne).\n"
<< " 4 - Convert Weight (kilogram - pound).\n"
<< " 5 - Exit.\n"
<< " Enter your choice and press return: ";
cin >> choice;

switch (choice)
{
case 1:
//code to Calculate BMI
break;

case 2:
//code to Convert Weight (Gram - Kilogram)
break;

case 3:
//code to Convert Weight (Gram - Tonne)
break;

case 4:
//Convert Weight (kilogram - pound)
break;
case 5:
cout << "End of Program.\n";
break;

default:
cout << "Not a Valid Choice. \n"
<< "Choose again.\n";
break;
}

}while (choice !=5);
return 0;
}

