#include <iostream> 

 
using namespace std;

int find_max(int x[],int n); //This function read an array and give as output the maximum element in the array

int main()
{
 		int n; 
		
	 	//we accept as input a value representing the length of the array
		//and we create an array of the given size


		cout<< "Please insert the array length >> ";
		cin>>n;
		int *x=new int[n+1];

		cout<< "Please insert an array >> ";
		 
		for(int i=0;i<n;i++){
			cin>>x[i];
		}
		
		
		//we generate an array from 1 to the maximum value present in the input array.
		//Every time that a value occurs in the input array we increment it in ctrl
		//To know which element occur once is sufficient to find the value in ctrl==1
 
		int *ctrl=new int[find_max(x,n)+1];

		for(int  i=0;i<n;i++){
			if(ctrl[x[i]]<=1)
			{
				 
				ctrl[x[i]]++; 
			}
		}
		for(int  i=0;i<1000;i++){
			if(ctrl[i]==1)
			{
				cout<<"The only element occurring once is:"<<endl;
				cout<<i<<endl;
			}
	
		}
		 
 
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