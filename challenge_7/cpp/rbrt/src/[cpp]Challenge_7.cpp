#include <iostream> 

 
using namespace std;


 int main()
{
 		int n; 
		cout<< "Please insert the array length N >> ";
		cin>>n;

		int x[1000]={0};

		cout<< "Please insert an array from 0 to N>> ";
		 
		for(int i=0;i<n;i++){
			cin>>x[i];
		}

		int Total=(n*(n+1))/2; // total sum of elements in the range 0-N
		

		for(int  i=0;i<n;i++)
		{
		  
			Total= Total-x[i] ;
	 
		}
 		cout<<Total<<endl;
 
	return 0;
}


int find_max(int x[],int n){

	int max=x[0];
	int i=1;
	while(i<n){
		if(max<x[i])
		{
			max=x[i];
		}
		i++;
	}
	return(max);


};