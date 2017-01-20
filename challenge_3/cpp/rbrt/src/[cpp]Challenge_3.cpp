#include <iostream> 

 
using namespace std;

int find_max(int x[],int n); //This function read an array and give as output the maximum element in the array

int main()
{
 		int n; 
		
	 	//we accept as input a value representing the length of the array
		// And the list of elements of the array.
		// The maximum size of the array is 1000 elements, is an arbitrary size that I
		// believe to be enough for the task at hand 


		cout<< "Please insert the array length >> ";
		cin>>n;
		int x[1000]={0};

		cout<< "Please insert an array >> ";
		 
		for(int i=0;i<n;i++){
			cin>>x[i];
		}
		
		
		//we generate an array from 1 to the maximum value present in the input array.
		//Every time that a value occurs in the input array we increment it in ctrl
		//To know which element occur most of the time we check ctrl[i]>n/2
 
		int *ctrl=new int[find_max(x,n)+1];
 
		for(int  i=0;i<n;i++)
		{
		  
			ctrl[x[i]]++; 
	
			if(ctrl[x[i]]>(n/2))
			{
				cout<<"The element that is present the majority of times is:"<<endl;
				cout<<x[i]<<endl;
				break;
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