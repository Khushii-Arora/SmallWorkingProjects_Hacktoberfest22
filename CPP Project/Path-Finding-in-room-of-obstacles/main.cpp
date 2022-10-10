#include "colors.hpp"
#include <stdlib.h>
#include <fstream>
#include <string>
#include <queue>
#include "inputdetector.cpp"
#include "code.cpp"
#include "clearscreen.cpp"
using namespace std;
using namespace rang;




pair1 home;

int map[100][100];

void sethome(){
	int x,y;
	cout<<fgB::yellow;
	cout<<"Enter abcissa: ";
	cout<<fg::reset;
	cin>>x;
	cout<<fgB::yellow;
	cout<<"\nEnter ordinate: ";
	cout<<fg::reset;
	cin>>y;
	if(isValid(x,y) and isUnblocked(map,x,y)){
		home.first=x;
		home.second=y;
		cout<<fgB::green;
		cout<<"Base Changed Successfully\n";
		cout<<fg::reset;
		cout<<"Press";
		cout<<style::italic;
		cout<<fgB::cyan;
		cout<<" ENTER ";
		cout<<style::reset;
		cout<<"to continue!\n";
		getchar();
	}
	else{
		cout<<fgB::red;
		cout<<"Entered point can't be source,Try Again!\n";
		cout<<fg::reset;
		cout<<"Press";
		cout<<style::italic;
		cout<<fgB::cyan;
		cout<<" ENTER ";
		cout<<style::reset;
		cout<<"to continue!\n";
		getchar();
		getchar();
		clear();
		sethome();
	}
	return;
	
}

void returnhome(pair1 curr_location){
	if(aStarSearch(map,curr_location,home)){
		path_smoother(map);
		print_grid(map);
	}
}

void InitialiseMap(){
	ifstream ob;
	char s[100];
	ob.open("floormap.txt");
	memset(map,-1,sizeof(map));
	for(int i=0;i<100;++i){
			ob.getline(s,101);
			for(int k=0;k<100;++k){
				if(s[k]=='0' or s[k]=='1')
					map[i][k]=s[k]-'0';
			}
		
	}
	ob.close();
}

void displayMap(){
	for(int i=0;i<100;++i){
		for(int j=0;j<100;++j){
			if(map[i][j]==0 or map[i][j]==1){
				if(map[i][j]==0)
					cout<<fg::red<<bg::red;
				else
					cout<<fg::green<<bg::green;
				cout<<map[i][j];
				cout<<bg::reset;
			}
		}
		cout<<"\n";
	}
}


int main()
{	int ch;
	home.first=1;
	home.second=1;
	InitialiseMap();
	homescreen:
	cout<<style::bold<<style::italic;
	cout<<fgB::yellow;
	cout<<"\t\tWELCOME\n\n";
	cout<<style::reset<<fgB::blue;
	cout<<"\t1.Clean Spots\n";
	cout<<"\t2.Configure Base Location\n";
	cout<<"\t3.Display Floor Map\n";
	cout<<"\t4.Exit\n";
	cin>>ch;
	getchar();
	pair1 src = home;
	if(ch==1){
		choice:
		clear();
		cout<<fgB::yellow<<"Enter Number of Points to be cleaned : ";
		cout<<fg::reset;
		int n;
		cin>>n;

		priority_queue< pair< int, pair<int,int> > , vector<pair<int,pair<int,int>  > > > pq;

		for(int i=0;i<n;i++){
			cout<<fgB::cyan;
			cout<<"Enter amount of dust and coordinates of point "<<i+1<<": ";
			cout<<fg::reset;
			int d,p1,p2;
			cin>>d>>p1>>p2;
			pq.push({d,{p1,p2}});
		}	

		getchar();
		clear();
		int i=1;
		while(!pq.empty()){
			
			pair<int,pair<int,int> > s = pq.top();
			cout<<fgB::magenta;
			cout<<"Destination "<<i<<": ("<<s.second.first<<","<<s.second.second<<")";
			i++;
			pq.pop();
			cout<<"\n";
			pair1 dest = make_pair(s.second.first,s.second.second);
			cout<<fgB::cyan;
			if(aStarSearch(map,src,dest)){
				path_smoother(map);
				print_grid(map);
				cout<<"\n\n";
				src = dest;
			}
			getchar();
			clear();
		}
		cout<<"Press enter in 10 seconds or robot would return to base\n";
		for(int i=10;i>0;--i){
	    	cout<<"You have "<<i<<" seconds remaining: ";
	    	cout.flush();
	    	usleep(1000000);
	    	for(int i=0;i<31;++i){
	        	cout<<"\b";
	   		}
	    	if(kbhit()){
	        	cin.clear();
				fflush(stdin);
	        	goto choice;
	        	break;
	    	}
	   }
		cout<<fgB::magenta;
		cout<<"Returning Base: ("<<home.first<<","<<home.second<<")";
		cout<<fgB::cyan;
		returnhome(src);
		getchar();
		clear();


	}
	if(ch==2){
		clear();
		sethome();
		getchar();
	}
	if(ch==3){
		clear();
		displayMap();
		cout<<fg::reset;
		cout<<"Press";
		cout<<style::italic;
		cout<<fgB::cyan;
		cout<<" ENTER ";
		cout<<style::reset;
		cout<<"to continue!\n";
		getchar();
	}
	if(ch==4){
		clear();
		return 0;
	}
	clear();
	goto homescreen;
	return 0;
}