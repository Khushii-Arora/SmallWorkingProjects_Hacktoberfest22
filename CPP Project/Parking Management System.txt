#include<iostream>

using namespace std;

string arr1[20],arr2[20],arr3[20],arr4[20],arr5[20];

int total=0;

void enter()       //funciton for entering new data

{

		int ch=0;  //choice 

			cout<<"How many Transport do you want to enter ?"<<endl;

			cin>>ch;

			if(total==0) 

			{

			total=ch+total;

			for(int i=0;i<ch;i++)

			{

				cout<<"\nEnter the Data of Transport : "<<i+1<<endl<<endl;

				cout<<"Enter the type of Transport : ";

				cin>>arr1[i];

				cout<<"Enter Transport Plate Number : ";

				cin>>arr2[i];

				cout<<"Enter transport's Admin Name : ";

				cin>>arr3[i];

				cout<<"Enter Entry time : ";

				cin>>arr4[i];

				cout<<"Enter Expected Exit Time :";

				cin>>arr5[i];

				

			}

	    	}

	    	else

	    	{

	    		

	    		for(int i=total;i<ch+total;i++)   //this repeated loop is apply when user wants to add some more data

			{

			cout<<"\nEnter the Data of Transport : "<<i+1<<endl<<endl;

				cout<<"Enter the type of Transport : ";

				cin>>arr1[i];

				cout<<"Enter Transport Plate Number : ";

				cin>>arr2[i];

				cout<<"Enter transport's Admin Name': ";

				cin>>arr3[i];

				cout<<"Enter Entry time : ";

				cin>>arr4[i];

				cout<<"Enter Expected Exit Time: ";

				cin>>arr5[i];

			}

			total=ch+total;

			}

	

}

void show()     // for showing the data

{

	if(total==0)

	{
cout<<"---------------------------\n";
		cout<<"No data is entered"<<endl;
cout<<"---------------------------\n";
	}

	else{

		for(int i=0;i<total;i++)

	    		{

	    		cout<<"\nData of Transport: "<<i+1<<endl<<endl;
 
	    		cout<<"transport Name: "<<arr1[i]<<endl;

	    		cout<<"Plate Number: "<<arr2[i]<<endl;

	    		cout<<"Admin'Name: "<<arr3[i]<<endl;

	    		cout<<"Entry Time: "<<arr4[i]<<endl;

	    		cout<<"Expected Exit Time: "<<arr5[i]<<endl;

	    	    }

	    	}

}

void search()        // function : we user want to search their data

{

	if(total==0)

	{

		cout<<"No data is entered"<<endl;

	}

	else{

	string Plate_no;       // specific rol

				cout<<"Enter the Number Plate of Transport: "<<endl;

				cin>>Plate_no;

				for(int i=0;i<total;i++)

				{

					if(Plate_no==arr2[i])

					{

				cout<<"\nData of Transport: "<<i+1<<endl<<endl;

	    		cout<<"transport Name: "<<arr1[i]<<endl;

	    		cout<<"Plate Number: "<<arr2[i]<<endl;

	    		cout<<"Admin'Name: "<<arr3[i]<<endl;

	    		cout<<"Entry Time: "<<arr4[i]<<endl;

	    		cout<<"Expected Exit Time: "<<arr5[i]<<endl;

					}

				}

			}

}

void update()

{

	if(total==0)

	{

		cout<<"No data is entered"<<endl;

	}

	else{

		string Plate_no;     // update any transport and for this we want to search a unique no (vechile Plate no.)

				cout<<"Enter the Transport's Plate Number which you want to update"<<endl;

				cin>>Plate_no;

					for(int i=0;i<total;i++)

				{

					if(Plate_no==arr2[i])

					{

						cout<<"\nPrevious data"<<endl<<endl;

						cout<<"Data of Transport: "<<i+1<<endl<<endl;

	    		cout<<"transport Name: "<<arr1[i]<<endl;

	    		cout<<"Plate Number: "<<arr2[i]<<endl;

	    		cout<<"Admin'Name: "<<arr3[i]<<endl;

	    		cout<<"Entry Time: "<<arr4[i]<<endl;

	    		cout<<"Expected Exit Time: "<<arr5[i]<<endl;

	    	        	cout<<"\nEnter new data"<<endl<<endl;


				cout<<"Enter the type of Transport : ";

				cin>>arr1[i];

				cout<<"Enter Transport Plate Number : ";

				cin>>arr2[i];

				cout<<"Enter transport's Admin Name : ";

				cin>>arr3[i];

				cout<<"Enter Entry time : ";

				cin>>arr4[i];

				cout<<"Enter Exit Time :";

				cin>>arr5[i];


					}

				}

			}

		}



void deleterecord()    //for delete any type of data

{

	if(total==0)

	{

		cout<<"No data is entered"<<endl;

	}

	else{

		int a;

	        	cout<<"Press 1 to delete all record"<<endl;

				cout<<"Press 2 to delete specific record"<<endl;

				cin>>a;

				if(a==1)

				{

					total=0;

					cout<<"All record is deleted..!!"<<endl;

				}

				else if(a==2)

				{

				string Plate_no;      // for particula any transport data delete and for this we want to require a unique no 
				                      //  (vechile Plate no.)

				cout<<"Enter the Transport's Plate Number which you wanted to delete"<<endl;

				cin>>Plate_no;

				for(int i=0;i<total;i++)

				{

					if(Plate_no==arr2[i])

					{

						for(int j=i;j<total;j++)

						{

						arr1[j]=arr1[j+1];

						arr2[j]=arr2[j+1];

					    arr3[j]=arr3[j+1];

						arr4[j]=arr4[j+1];

						arr5[j]=arr5[j+1];

				     	}

					total--;

					cout<<"Your required record is deleted"<<endl;

					}

				}

				}

				 

			

			else 

			{

				cout<<"Invalid input";

			}

}

}

int main()

{

	int value;
cout<<"*********************************************************************************************************************************************\n";
cout<<"\n\n\t\t\t\t******************            MINI PROJECT             ******************"<<endl;
		cout<<"\n\t\t\t\t****************** WELCOME TO PARKING MANAGEMENT SYSTEM ******************"<<endl<<endl<<endl;
	while(true)

	{

	//	cout<<"----------------------------"<<endl<<endl;
	cout<<"::::::::::::::::::::::::::::::"<<endl;
	cout<<"*** Press 1 to enter data ****"<<endl;

	cout<<"*** Press 2 to show data *****"<<endl;

	cout<<"*** Press 3 to search data ***"<<endl;

	cout<<"*** Press 4 to update data ***"<<endl;

	cout<<"*** Press 5 to delete data ***"<<endl;

	cout<<"***    Press 6 to exit   *****  "<<endl;
		cout<<"::::::::::::::::::::::::::::::"<<endl;
	//cout<<"----------------------------"<<endl<<endl;

	cin>>value;

	switch(value)

	{

		case 1:
		cout<<"----------------------------"<<endl;
		cout<<"You Choose for Enter new Data----"<<endl;
		cout<<"----------------------------"<<endl;
			enter();

			break;

		case 2:
        cout<<"----------------------------"<<endl;
		cout<<"You Choose for showing your Data----"<<endl;
		cout<<"----------------------------"<<endl;
			show();

			break;

		case 3:
        cout<<"----------------------------"<<endl;
		cout<<"You Choose for Searching your Data----"<<endl;
		cout<<"----------------------------"<<endl;
			search();

			break;

		case 4:
		cout<<"----------------------------"<<endl;
		cout<<"You Choose for Update your Data----"<<endl;
		cout<<"----------------------------"<<endl;

			update();

			break;

		case 5:
        cout<<"----------------------------"<<endl;
		cout<<"You Choose for Delete your Data----"<<endl;
		cout<<"----------------------------"<<endl;
			deleterecord();

			break;

		case 6:
		cout<<"****************************"<<endl;
		
			exit(0);

			break;

		default:

			cout<<"Invalid input"<<endl;

			break;

	}

}
return 0;

}


///// **************************THE END 






















































