#include <iostream> 

using namespace std;

int check_range(int l[],int start_point,int n){
	int end_point= start_point;

	for(int j= start_point; j<(n-1); j++)
	{
		if((l[j]+1)==l[j+1])
		{
			
		}else{
			end_point=j;
			break;	
		}
		if(((j+1)==(n-1)) && ((l[j]+1)==l[j+1])   ){
			end_point=j+1;
			break;
		}
	}
	return(end_point);
}

int main()
{
	// user input
	int l[1000],n;

	cout << "Please enter the  length of the list << "; //ask for input
	cin>>n;


	cout << endl << "Please enter the ordered list of integers: "; //ask for input
	for(int i=0; i<n; i++){
		cin>>l[i];
	}
	
	// we read the list looking for range of consecutive values
	// We use a function check_range that from a starting point "i"
	// checks that the element of the list are consecutive to the one considered.
	// When we find an element that it is not a consecutive number of the list we 		// give as output the last index of interest
 
	int i=0;
	while (i<n){
	
	int end_range=check_range(l,i,n);
		if(i==end_range)
		{
		}else{
			cout<<"[ "<<l[i] <<"-"<<l[end_range]<<"]"<<endl;
		}
		i=end_range+1;
	}


return(0);

}