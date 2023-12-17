#include <iostream>
using namespace std;

int main() {

int semester;

do {

cout << "PROGRAM OUTLINE FOR CDIM110"<< endl;
cout << "1. Semester 1"<<endl;
cout << "2. Semester 2"<<endl;
cout << "3. Semester 3"<<endl;
cout << "4. Semester 4"<<endl;
cout << "5. Semester 5"<<endl;
cout << "6. Quit the application"<<endl;
cout << "Please select the Semester (1-5): ";
cin >> semester;


switch(semester)
{
	case 1:
		cout<<"\n\n\n--- PROGRAMME OUTLINE FOR SEMESTER 1 ---"<<endl;
		cout<<"IMC111 - COURSE NAME"<<endl;
		cout<<"IMC112 - COURSE NAME"<<endl;
		cout<<"IMC113 - COURSE NAME\n\n"<<endl;
	break;
	
	case 2:
	break;
	
	case 3:
	break;

	case 4:
	break;

	case 5:
	break;
	
	default:
	{
	}
	
}

} while (semester != 6);

return 0;
}
