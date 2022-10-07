
#include<iostream>
using namespace std;
void bill(string,string,int);
int count_r=0;
struct Details
{
    string username, pasword, emialid;
} d1, d2;

void car_details()
{
     cout << "\t\t\t-----------------------------" << endl;
    cout << "\t\t\t---Dev_Rental-service_Home---" << endl;
    cout << "\t\t\t-----------------------------" << endl;
    cout << "\n\n\t\t\tWelcome to Dev_Rental-service_Home" << endl;
    cout << "\n\t Here you can see the avialable cars with all the specifications and rent........" << endl
         << endl;
    cout << "\t\t--|#######################################################|--" << endl;
    cout << "\t\t  |"
         << " "
         << "CAR_NAME  | "
         << " "
         << "AVAIABLE MODEL | "
         << " "
         << "MILAGE |"
         << " "
         << "RENTING PRICE | " << endl;
    cout << "\t\t--|#######################################################|--" << endl;
    cout << "\t\t  |"
         << "1.HOYUNDAI | "
         << "   "
         << "Veloster     | "
         << "120kmph |"
         << "   "
         << "300/day     | " << endl;
    cout << "\t\t  |"
         << "2.NANO     | "
         << "   "
         << "Nano-Tz      | "
         << "100kmph |"
         << "   "
         << "150/day     | " << endl;
    cout << "\t\t  |"
         << "3.SUZUKI   | "
         << "   "
         << "Celerio      | "
         << "130kmph |"
         << "   "
         << "350/day     | " << endl;
    cout << "\t\t  |"
         << "4.TOYOTA   | "
         << "   "
         << "Avalon       | "
         << "120kmph |"
         << "   "
         << "300/day     | " << endl;
    cout << "\t\t  |"
         << "5.TATA     | "
         << "   "
         << "Safari       | "
         << "150kmph |"
         << "   "
         << "350/day     | " << endl;
    cout << "\t\t  |"
         << "6.MERCEDES | "
         << "   "
         << "E_Class      | "
         << "200kmph |"
         << "   "
         << "650/day     | " << endl;
    cout << "\t\t  |"
         << "7.FROD     | "
         << "   "
         << "Explorer     | "
         << "200kmph |"
         << "   "
         << "400/day     | " << endl;

          if(count_r!=0)
            cout<<"\n\t\tHello....."<<"Dear user-->"<<" "<<d2.username<<endl;
             int ser;
         cout << "\n\tSelect any car by pressibng their respective serial number(sholud be integer)...:";
    cin >> ser;
    if(count_r==0)
    cout << "\t\tPlease creat your account first.............." << endl;
    cout << endl;
}
void login()
{
     char c;
    int con1 = 1, count = 0;// con2 = 1;//tmp = 0;
    string ex;
   // struct Details d1, d2;
    cout << "\t\t-------HEY USER MAKE YOUR OWN ACCOUNT FOR BEST EXPERIENCE-------\n"
         << endl;
    cout << "1.Register\n2.Log in(If you alredy have an account)" << endl;
    cout << "Press '1' for Register or '2' for log in." << endl;

    while (con1)
    {
        cin >> c;
        if (c == '1')
        {


            cout << "\nEnter your Email-id" << endl;
            cin >> d1.emialid;

            if (ex == d1.emialid && count > 0)
            {
                cout << "\nThis email_id alredy exist" << endl;
                cout << "\nPress '1' for Register or '2' for log in." << endl;
                continue;
            }
            cout << "\nEnter Username(Don't use any extra space)" << endl;
            cin >> d1.username;
            cout << "\nSelect password" << endl;
            cin >> d1.pasword;

            cout << "\nDone ✔" << endl;
            count++;
            cout << "\nPress '1' for Register or '2' for log in" << endl;

            ex = d1.emialid;
            continue;

        }
        else if (c == '2')
        {
            cout << "\nEnter Username(Don't use any extra space)" << endl;
            cin >> d2.username;
            cout << "Select password" << endl;
            cin >> d2.pasword;
            if (d2.username != d1.username)
            {
                cout << "\nOopss!Sorry cant't find any account.Make sure you have an account" << endl;
                cout << "\nPress '1' for Register or '2' for log in." << endl;
                continue;
            }


            else if (d2.username == d1.username && d2.pasword != d1.pasword)
            {
                cout << "\nWRONG PASSWORD ❌" << endl;
                cout << "\nPress 'R' to Retry\t or \t'F' to do Forget password" << endl;
                cin >> c;
                if (c == 'R')
                { cout << "\nPress '1' for Register or '2' for log in." << endl;
                    continue;
                }
                else if (c == 'F')
                {
                    cout << "\nEnter new password" << endl;
                    cin >> d1.pasword;
                    cout << "\nConfirm Password" << endl;
                    cin >> d2.pasword;
                    cout << "\nSuccessful Password Reset ✔" << endl;
                    cout << "\nPress '1' for Register or '2' for log in." << endl;
                    continue;
                }
            }
            else
            {
                cout << "Your username:-" << d2.username << endl;
                cout << "LOGGED IN....\nSucessfully ✔" << endl;
                cout << "press '#' to check Your profile or * to go back to main menu..." << endl;
                cin >> c;
                //con2 = 0;
                if (c == '#')
                {
                    cout << "Gmail:-" << d1.emialid << endl
                         << "Username:-" << d2.username << endl
                         << "pasword:-" << d2.pasword<<endl;
                    con1 = 0;
                    cout<<"\nEnter * to go back to main menu"<<endl;
                    cin>>c;
                }
                 if (c == '*')
                {
                   break;
                }
                else
                cout<<"\nWrong input ❌"<<endl;
            }

        }
    }
count_r=1;
}
void car_select()
{
     int ser;
     cout << "\n\tSelect any car by pressibng their respective serial number(sholud be integer)...:";
    cin >> ser;
    cout << "\t\tPlease creat your account first.............." << endl;
    cout << endl;
    switch(ser)
    {
         case 1:bill("HOYUNDAI","Veloster ",300);
         break;
         case 2: bill("NANO","Nano-Tz",150);
         break;
         case 3: bill("SUZUKI","Celerio",350);
         break;
         case 4: bill("TOYOTA","Avalon",300);
         break;
          case 5: bill("TATA","Safari",350);
         break;
          case 6: bill("MERCEDES","E_Class",650);
         break;
         case 7: bill("FORD","Explorer ",400);
         break;
         default: cout<<"INVALID INPUT❗❌"<<endl;


    }

}
void bill(string car,string model,int p_d)
{ int day;
char a;
double a_price,t_price,gst;
 cout << "\n\t\tGreat..You have choised"<<car<<" "<<"(model-"<<model<<")......." << endl;
        cout << "\t\tEnter number of days you want to rent this car:-";
        cin >> day;
        cout << "\n\t\t\t Driver charge:" << 100 * day << endl;
        cout << "\n\t\tWhould you like to take driver ? please selelct (Y/N): ";
        cin >> a;

        cout << "\n\t\tyou have to advance min Rs- "<<" "<< double((day * p_d) / 3) << "to book your car..." << endl;
        cout << "\t\tprocess your payment to procced...........:";
        cin >> a_price;
        if (a_price >= (day * p_d) / 3)
        {
            cout << "\t\t\nOk............\n\t\t please wait few seconds to proess your bill........." << endl;
            cout << "\n\t\tProcessiong sucessfull......\n"
                << endl;
                cout << "\n\t\t\tHello"<<" "<< d1.username<<" "<< "Thank you for renting  car from Dev_Rental-service_Home" << endl;
                cout << "\n\t\t\t Your payment details__________.." << endl;
            if (a == 'y' || a == 'Y')
            {

                cout << "\n\t\t\tAdmin:-     " << d1.username << endl;
                cout << "\n\t\t\tDriver charge:-" << (100 * day);
                gst=double(((day * p_d) + (100 * day)) * 0.18);
                cout << "\n\t\t\tGST charge:  +" << gst<<endl;
                t_price=(gst+(100*day))-a_price;
                cout << "\n\t\t\tdue payment:=" <<t_price<<endl;
            }
            else
            {
                cout << "\n\t\t\tAdmin:-     " << d1.username << endl;
                cout << "\n\t\t\tDriver charge:-" << (0 * day);
                gst=double(((day * p_d) + (0 * day)) * 0.18);
                cout << "\n\t\t\tGST charge:  +" << gst<<endl;
                t_price=(day*p_d)-(gst+(0*day))-a_price;
                cout << "\n\t\t\tdue payment:=" <<t_price<<endl;
            }

        }
        else
        cout<<"\n\t\t\tYour payment is not suffecient to proceed......";
        cout<<"\n\t\t\t\t WARNNING!!!!!!!!"<<endl;
        cout<<"\n\t\tPay your bill due the end of tha date else extra fine will be charged!!!!!!"<<endl;
    }

int main(){
    car_details();
    login();
    car_details();
    car_select();
   // bill();
    return 0;
}
