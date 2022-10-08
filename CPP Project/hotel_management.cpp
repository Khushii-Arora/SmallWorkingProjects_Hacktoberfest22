#include<iostream>

using namespace std;

int main()
{
    int quant;
    int choice;
    
    //Holds quantity.
    int Qrooms = 0,Qpasta = 0, Qburger = 0, Qnoodles = 0, Qshake = 0, Qchickens = 0;
    //Holds total sold.
    int Srooms = 0,Spasta = 0, Sburger = 0, Snoodles = 0, Sshake = 0, Schickens = 0; 
    //Holds total peice of items.
    int Total_rooms = 0,Total_pasta = 0, Total_burger = 0, Total_noodles = 0, Total_shake = 0, Total_chickens = 0;

    cout<<"\n\t Quantity of items we have";
    cout<<"\n Rooms availabe";
    cin>>Qrooms;
    cout<<"\n Quantity of pasta : ";
    cin>>Qpasta;
    cout<<"\n Quantity of burger : ";
    cin>>Qburger;
    cout<<"\n Quantity of noodles : ";
    cin>>Qnoodles;
    cout<<"\n Quantity of shake : ";
    cin>>Qshake;
    cout<<"\n Quantity of Chicken rolls : ";
    cin>>Qchickens;
    m:
    cout<<"\n\t\t\t Please select from the menu options ";
    cout<<"\n\n1) Rooms";
    cout<<"\n\n2) Pasta";
    cout<<"\n\n3) Burger";
    cout<<"\n\n4) Noodles";
    cout<<"\n\n5) Shake";
    cout<<"\n\n6) Chicken rolls";
    cout<<"\n\n7) Information regarding sales and collection";
    cout<<"\n\n8) Exit";


    cout<<"\n\n Please Enter Your choice!";
    cin>>choice;

    switch(choice){
        case 1:
        cout<<"\n\n Enter the number of rooms that you want: ";
        cin>>quant;
        if(Qrooms - Srooms >= quant){
            Srooms = Srooms+quant;
            Total_rooms = Total_rooms+(quant*1200);
            cout<<"\n\n\t\t"<<quant<<"Room/Rooms have been alloted to you!";
        }
        else{
            cout<<"\n\tOnly"<<Qrooms-Srooms<<"Rooms remaining in hotel";
            break;
        }
        case 2:
        cout<<"\n\n Enter Pasta quantity ";
        cin>>quant;
        if(Qpasta - Spasta >= quant){
            Spasta = Spasta+quant;
            Total_pasta = Total_pasta+(quant*250);
            cout<<"\n\n\t\t"<<quant<<"Pasta is the order";
        }
        else{
            cout<<"\n\tOnly"<<Qpasta-Spasta<<"pasta remaining in hotel";
            break;
        }
    
    case 3:
        cout<<"\n\n Enter Burger quantity ";
        cin>>quant;
        if(Qburger - Sburger >= quant){
            Sburger = Sburger+quant;
            Total_burger = Total_burger+(quant*99);
            cout<<"\n\n\t\t"<<quant<<"Burger is the order";
        }
        else{
            cout<<"\n\tOnly"<<Qburger-Sburger<<"Burger remaining in hotel";
            break;
        }
    
    case 4:
        cout<<"\n\n Enter Noodles quantity ";
        cin>>quant;
        if(Qnoodles - Snoodles >= quant){
            Snoodles = Snoodles+quant;
            Total_noodles = Total_noodles+(quant*140);
            cout<<"\n\n\t\t"<<quant<<"Noodles is the order";
        }
        else{
            cout<<"\n\tOnly"<<Qnoodles-Snoodles<<"Noodles remaining in hotel";
            break;
        }
    
    case 5:
        cout<<"\n\n Enter Shake quantity ";
        cin>>quant;
        if(Qshake - Sshake >= quant){
            Sshake = Sshake+quant;
            Total_shake = Total_shake+(quant*60);
            cout<<"\n\n\t\t"<<quant<<"Shake is the order";
        }
        else{
            cout<<"\n\tOnly"<<Qshake-Sshake<<"Shake remaining in hotel";
            break;
        }
    
    case 6:
        cout<<"\n\n Enter Chickens Rolls quantity ";
        cin>>quant;
        if(Qchickens - Schickens >= quant){
            Schickens = Schickens+quant;
            Total_chickens = Total_chickens+(quant*200);
            cout<<"\n\n\t\t"<<quant<<"Chickens Rolls is the order";
        }
        else{
            cout<<"\n\tOnly"<<Qchickens-Schickens<<"Chickens Rolls remaining in hotel";
            break;
        }
    

    case 7:
    cout<<"\n\tDetails of sales and collection ";
    cout<<"\n\n Number of rooms we had : "<<Qrooms;
    cout<<"\n\n Number of rooms we gave for rent: "<<Srooms;
    cout<<"\n\n Remaining Rooms: "<<Qrooms-Srooms;
    cout<<"\n\n Total rooms collection for the day: "<<Total_rooms;

    cout<<"\n\n Number of Pastas we had : "<<Qpasta;
    cout<<"\n\n Number of Pastas we sold: "<<Spasta;
    cout<<"\n\n Remaining Pastas: "<<Qpasta-Spasta;
    cout<<"\n\n Total Pastas collection for the day: "<<Total_pasta;

    cout<<"\n\n Number of Burger we had : "<<Qburger;
    cout<<"\n\n Number of Burger we sold: "<<Sburger;
    cout<<"\n\n Remaining Burger: "<<Qburger-Sburger;
    cout<<"\n\n Total Burger collection for the day: "<<Total_burger;

    cout<<"\n\n Number of Noodles we had : "<<Qnoodles;
    cout<<"\n\n Number of Noodles we sold: "<<Snoodles;
    cout<<"\n\n Remaining Noodles: "<<Qnoodles-Snoodles;
    cout<<"\n\n Total Noodles collection for the day: "<<Total_noodles;

    cout<<"\n\n Number of Shakes we had : "<<Qshake;
    cout<<"\n\n Number of Shakes we sold: "<<Sshake;
    cout<<"\n\n Remaining Shakes: "<<Qshake-Sshake;
    cout<<"\n\n Total Shakes collection for the day: "<<Total_shake;

    cout<<"\n\n Number of Chicken Rolls we had : "<<Qchickens;
    cout<<"\n\n Number of Chicken Rolls we sold: "<<Schickens;
    cout<<"\n\n Remaining Chicken Rolls: "<<Qchickens-Schickens;
    cout<<"\n\n Total Chicken Rolls collection for the day: "<<Total_chickens;
    cout<<"\n\n Total collection for a day : "<<Total_rooms+Total_pasta+Total_burger+Total_noodles+Total_shake+Total_chickens;

    case 8: 
    exit(0);

    default:
    cout<<"\n Please select the number mentioned above!";

    }
    goto m;



    return 0;
}
