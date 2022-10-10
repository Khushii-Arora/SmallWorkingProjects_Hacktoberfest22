#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <stack>
#include <cfloat>
#include <cmath>
using namespace std;

//initiallising row and columns initially

#define ROW 100
#define COL 100


typedef pair<int,int> pair1;
typedef pair<double,pair<int,int> > pPair;

vector<pair<int,int>> v;

struct cell{

	//row and column index of its parent
	int parent_i,parent_j;

	//g is the movement cost to move from the starting point to a 
	// given square on the grid

	//h is estimated cost to move from that given square on the grid to the final destination

	//f = g + h

	double f,g,h;

};

//function to check whether the given cell is valid or not
bool isValid(int row,int col){
	//returns true if row and col is in range

	return (row>=0) && (row<ROW) && (col>=0) && (col<COL);
}

// function to check whether the given cell is blocked or not
bool isUnblocked(int grid[][COL],int row,int col){

	if(grid[row][col]==1){
		return true;
	}
	else{
		return false;
	}
}

//function to check whether robot has reached the destination cell or not
bool isDestination(int row,int col,pair1 dest){

	if(row==dest.first && col==dest.second){
		return true;
	}
	else{
		return false;
	}
}

//function to calculate the h heuristics
double calculateHvalue(int row,int col,pair1 dest){
	
	return ((double)sqrt(((row - dest.first)*(row - dest.first)) + (col - dest.second)*(col - dest.second)));
}


// function to trace the path from the source
void tracePath(cell cellDetails[][COL],pair1 dest){

	int row = dest.first;
	int col = dest.second;

	stack<pair1> path;

	while(!(cellDetails[row][col].parent_i==row && cellDetails[row][col].parent_j==col)){
		path.push(make_pair(row,col));
		int temp_row = cellDetails[row][col].parent_i;
		int temp_col = cellDetails[row][col].parent_j;
		row = temp_row;
		col = temp_col;
	}

	path.push(make_pair(row,col));
	while(!path.empty()){
		pair<int,int> p = path.top();
		path.pop();
        v.push_back(make_pair(p.first,p.second));
	}
	return;
}


//a function to find the shortest path btw
//source cell to the destination cell
//a*search algorithm

int aStarSearch(int grid[][COL],pair1 src,pair1 dest){

	v.clear();

	//if the source is out of range
	if(isValid(src.first,src.second)==false){
			cout<<"Destination is invalid\n";
			return 0;
	}

	if(isUnblocked(grid,dest.first,dest.second)==false){
			cout<<"Destination is blocked\n";
			return 0;
	}

	//if the destination cell is same as source cell
	if(isDestination(src.first,src.second,dest)==true){
		cout<<"We are already at the destination\n";
		return 0;
	}


	//create a closed list and initialise it ti false
	//which means no has been included yet

	bool closedList[ROW][COL];

	memset(closedList,false,sizeof(closedList));

	//declare a 2D array of structure for details
	cell cellDetails[ROW][COL];

	int i,j;

	for(i=0;i<ROW;i++){
		for(j=0;j<COL;j++){
			cellDetails[i][j].f = FLT_MAX;
			cellDetails[i][j].g = FLT_MAX;
			cellDetails[i][j].h = FLT_MAX;
			cellDetails[i][j].parent_i = -1;
			cellDetails[i][j].parent_j = -1;
		}
	}


	//initialising the parameters of the starting node
	i = src.first, j = src.second;
	cellDetails[i][j].f = 0.0;
	cellDetails[i][j].g = 0.0;
	cellDetails[i][j].h = 0.0;

	cellDetails[i][j].parent_i = i;
	cellDetails[i][j].parent_j = j;


	//create an open list having infromation as-
	set<pPair> openList;

	// put the starting cell on hte open list and set its f as 0

	openList.insert(make_pair(0.0,make_pair(i,j)));

	bool foundDest = false;


	while(!openList.empty()){

		pPair p = *openList.begin();

		//remove this vertex from the open list
		openList.erase(openList.begin());

		//add this vertex to the closed list
		i = p.second.first;
		j = p.second.second;

		closedList[i][j] = true;

		//******** generate all 8 successor of this cell********

		double gNew,hNew,fNew;

		//1st successor

		if(isValid(i-1,j)==true){

			if(isDestination(i-1,j,dest)==true){
			cellDetails[i-1][j].parent_i = i;
			cellDetails[i-1][j].parent_j = j;
			cout<<"the destination cell is found "<<endl;
			tracePath(cellDetails,dest);
			foundDest = true;
			return 1;
			}

			//if the successor is already on the closed
			else if(closedList[i-1][j]==false && isUnblocked(grid,i-1,j)==true){
				gNew = cellDetails[i][j].g + 1.0;
				hNew = calculateHvalue(i-1,j,dest);
				fNew = gNew + hNew;

				//if it isn't on the open list,add it to
				//the open list. Make the current square

				if(cellDetails[i-1][j].f==FLT_MAX || cellDetails[i-1][j].f > fNew){
					openList.insert(make_pair(fNew,make_pair(i-1,j)));

					//update the details of this cell
					cellDetails[i-1][j].f = fNew;
					cellDetails[i-1][j].g = gNew;
					cellDetails[i-1][j].h = hNew;
					cellDetails[i-1][j].parent_i = i;
					cellDetails[i-1][j].parent_j = j;
				}
			}
		}

		//2nd successor

		if(isValid(i+1,j)==true){

			if(isDestination(i+1,j,dest)==true){
			cellDetails[i+1][j].parent_i = i;
			cellDetails[i+1][j].parent_j = j;
			cout<<"the destination cell is found "<<endl;
			tracePath(cellDetails,dest);
			foundDest = true;
			return 1;
			}

			//if the successor is already on the closed
			else if(closedList[i+1][j]==false && isUnblocked(grid,i+1,j)==true){
				gNew = cellDetails[i][j].g + 1.0;
				hNew = calculateHvalue(i+1,j,dest);
				fNew = gNew + hNew;

				//if it isn't on the open list,add it to
				//the open list. Make the current square

				if(cellDetails[i+1][j].f==FLT_MAX || cellDetails[i+1][j].f > fNew){
					openList.insert(make_pair(fNew,make_pair(i+1,j)));

					//update the details of this cell
					cellDetails[i+1][j].f = fNew;
					cellDetails[i+1][j].g = gNew;
					cellDetails[i+1][j].h = hNew;
					cellDetails[i+1][j].parent_i = i;
					cellDetails[i+1][j].parent_j = j;
				}
			}
		}


		//3rd successor

		if(isValid(i,j+1)==true){

			if(isDestination(i,j+1,dest)==true){
			cellDetails[i][j+1].parent_i = i;
			cellDetails[i][j+1].parent_j = j;
			cout<<"the destination cell is found "<<endl;
			tracePath(cellDetails,dest);
			foundDest = true;
			return 1;
			}

			//if the successor is already on the closed
			else if(closedList[i][j+1]==false && isUnblocked(grid,i,j+1)==true){
				gNew = cellDetails[i][j].g + 1.0;
				hNew = calculateHvalue(i,j+1,dest);
				fNew = gNew + hNew;

				//if it isn't on the open list,add it to
				//the open list. Make the current square

				if(cellDetails[i][j+1].f==FLT_MAX || cellDetails[i][j+1].f > fNew){
					openList.insert(make_pair(fNew,make_pair(i-1,j)));

					//update the details of this cell
					cellDetails[i][j+1].f = fNew;
					cellDetails[i][j+1].g = gNew;
					cellDetails[i][j+1].h = hNew;
					cellDetails[i][j+1].parent_i = i;
					cellDetails[i][j+1].parent_j = j;
				}
			}
		}

		//4th successor

		if(isValid(i,j-1)==true){

			if(isDestination(i,j-1,dest)==true){
			cellDetails[i][j-1].parent_i = i;
			cellDetails[i][j-1].parent_j = j;
			cout<<"the destination cell is found "<<endl;
			tracePath(cellDetails,dest);
			foundDest = true;
			return 1;
			}

			//if the successor is already on the closed
			else if(closedList[i][j-1]==false && isUnblocked(grid,i,j-1)==true){
				gNew = cellDetails[i][j].g + 1.0;
				hNew = calculateHvalue(i,j-1,dest);
				fNew = gNew + hNew;

				//if it isn't on the open list,add it to
				//the open list. Make the current square

				if(cellDetails[i][j-1].f==FLT_MAX || cellDetails[i][j-1].f > fNew){
					openList.insert(make_pair(fNew,make_pair(i,j-1)));

					//update the details of this cell
					cellDetails[i][j-1].f = fNew;
					cellDetails[i][j-1].g = gNew;
					cellDetails[i][j-1].h = hNew;
					cellDetails[i][j-1].parent_i = i;
					cellDetails[i][j-1].parent_j = j;
				}
			}
		}

		//5th successor

		if(isValid(i-1,j+1)==true){

			if(isDestination(i-1,j+1,dest)==true){
			cellDetails[i-1][j+1].parent_i = i;
			cellDetails[i-1][j+1].parent_j = j;
			cout<<"the destination cell is found "<<endl;
			tracePath(cellDetails,dest);
			foundDest = true;
			return 1;
			}

			//if the successor is already on the closed
			else if(closedList[i-1][j+1]==false && isUnblocked(grid,i-1,j+1)==true){
				gNew = cellDetails[i][j].g + 1.0;
				hNew = calculateHvalue(i-1,j+1,dest);
				fNew = gNew + hNew;

				//if it isn't on the open list,add it to
				//the open list. Make the current square

				if(cellDetails[i-1][j+1].f==FLT_MAX || cellDetails[i-1][j+1].f > fNew){
					openList.insert(make_pair(fNew,make_pair(i-1,j+1)));

					//update the details of this cell
					cellDetails[i-1][j+1].f = fNew;
					cellDetails[i-1][j+1].g = gNew;
					cellDetails[i-1][j+1].h = hNew;
					cellDetails[i-1][j+1].parent_i = i;
					cellDetails[i-1][j+1].parent_j = j;
				}
			}
		}

		//6th successor

		if(isValid(i-1,j-1)==true){

			if(isDestination(i-1,j-1,dest)==true){
			cellDetails[i-1][j-1].parent_i = i;
			cellDetails[i-1][j-1].parent_j = j;
			cout<<"the destination cell is found "<<endl;
			tracePath(cellDetails,dest);
			foundDest = true;
			return 1;
			}

			//if the successor is already on the closed
			else if(closedList[i-1][j-1]==false && isUnblocked(grid,i-1,j-1)==true){
				gNew = cellDetails[i][j].g + 1.0;
				hNew = calculateHvalue(i-1,j-1,dest);
				fNew = gNew + hNew;

				//if it isn't on the open list,add it to
				//the open list. Make the current square

				if(cellDetails[i-1][j-1].f==FLT_MAX || cellDetails[i-1][j-1].f > fNew){
					openList.insert(make_pair(fNew,make_pair(i-1,j-1)));

					//update the details of this cell
					cellDetails[i-1][j-1].f = fNew;
					cellDetails[i-1][j-1].g = gNew;
					cellDetails[i-1][j-1].h = hNew;
					cellDetails[i-1][j-1].parent_i = i;
					cellDetails[i-1][j-1].parent_j = j;
				}
			}
		}

		//7th successor

		if(isValid(i+1,j+1)==true){

			if(isDestination(i+1,j+1,dest)==true){
			cellDetails[i+1][j+1].parent_i = i;
			cellDetails[i+1][j+1].parent_j = j;
			cout<<"the destination cell is found "<<endl;
			tracePath(cellDetails,dest);
			foundDest = true;
			return 1;
			}

			//if the successor is already on the closed
			else if(closedList[i+1][j+1]==false && isUnblocked(grid,i+1,j+1)==true){
				gNew = cellDetails[i][j].g + 1.0;
				hNew = calculateHvalue(i+1,j+1,dest);
				fNew = gNew + hNew;

				//if it isn't on the open list,add it to
				//the open list. Make the current square

				if(cellDetails[i+1][j+1].f==FLT_MAX || cellDetails[i+1][j+1].f > fNew){
					openList.insert(make_pair(fNew,make_pair(i+1,j+1)));

					//update the details of this cell
					cellDetails[i+1][j+1].f = fNew;
					cellDetails[i+1][j+1].g = gNew;
					cellDetails[i+1][j+1].h = hNew;
					cellDetails[i+1][j+1].parent_i = i;
					cellDetails[i+1][j+1].parent_j = j;
				}
			}
		}

		//8th successor

		if(isValid(i+1,j-1)==true){

			if(isDestination(i+1,j-1,dest)==true){
			cellDetails[i+1][j-1].parent_i = i;
			cellDetails[i+1][j-1].parent_j = j;
			cout<<"the destination cell is found "<<endl;
			tracePath(cellDetails,dest);
			foundDest = true;
			return 1;
			}

			//if the successor is already on the closed
			else if(closedList[i+1][j-1]==false && isUnblocked(grid,i+1,j-1)==true){
				gNew = cellDetails[i][j].g + 1.0;
				hNew = calculateHvalue(i+1,j-1,dest);
				fNew = gNew + hNew;

				//if it isn't on the open list,add it to
				//the open list. Make the current square

				if(cellDetails[i+1][j-1].f==FLT_MAX || cellDetails[i+1][j-1].f > fNew){
					openList.insert(make_pair(fNew,make_pair(i+1,j-1)));

					//update the details of this cell
					cellDetails[i+1][j-1].f = fNew;
					cellDetails[i+1][j-1].g = gNew;
					cellDetails[i+1][j-1].h = hNew;
					cellDetails[i+1][j-1].parent_i = i;
					cellDetails[i+1][j-1].parent_j = j;
				}
			}
		}
	}

	//when the destination cell is not found and the open list is empty
	//there is no way to destination cell

	if(foundDest==false){
		cout<<"Failed to find a path to the destination cell"<<endl;
		return 0;
	}
	return 0; 
}

void path_smoother(int grid[][100]){
	pair <int,int> point[3];
	for(int i=0;i<v.size();++i){
		point[0]=v[i];
		point[1]=v[i+1];
		point[2]=v[i+2];
		if(point[0].first == point[1].first)
			continue;
		else if(point[0].second == point[1].second)
			continue;
		else{
			if(point[0].first == point[2].first){
				if(grid[point[0].first][point[1].second] == 1){
					point[1].first=point[0].first;
				}
			}
			else if(point[0].second == point[2].second)
				if(grid[point[1].first][point[0].second] == 1)
					point[1].second=point[0].second;
			v[i+1]=point[1];
		}
	}
	cout<<"the path travelled is ->";
	for(auto p:v){
		cout<<"("<<p.first<<","<<p.second<<") -> ";
	}
	cout<<"Destination Reached!\n";
}

void print_grid(int grid[][COL]){

        int grid1[ROW][COL] = {0};
        for(int i=0;i<ROW;++i){
        	for(int j=0;j<COL;++j){
        		grid1[i][j]=grid[i][j];
        	}
        }


        for(auto x:v){
            grid1[x.first][x.second] = 2;
        }
        
        for(int i=0;i<ROW;i++){
            for(int j=0;j<COL;j++){
            		if(grid1[i][j]==0)
						cout<<rang::fg::red<<rang::bg::red;
					else if(grid1[i][j]==1)
						cout<<rang::fg::green<<rang::bg::green;
					else
						cout<<rang::fgB::yellow<<rang::bgB::yellow;
	                cout<<grid1[i][j];
	                cout<<rang::bg::reset;
            }
            cout<<"\n";
        }


    }

/*
	int main(){

		//description of the grid

		int grid[ROW][COL] = {

		{ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 }, 
        { 1, 1, 1, 0, 1, 1, 1, 0, 1, 1 }, 
        { 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 }, 
        { 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 }, 
        { 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 }, 
        { 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 }, 
        { 1, 0, 0, 0, 0, 1, 0, 0, 0, 1 }, 
        { 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 }, 
        { 1, 1, 1, 0, 0, 0, 1, 0, 0, 1 } 

		};

		//type the source(code it later)

		pair1 src = make_pair(8,0);

		//type the destination(code it later)

		pair1 dest = make_pair(0,0);

		aStarSearch(grid,src,dest);

        print_grid();
		return 0;
	}
	*/