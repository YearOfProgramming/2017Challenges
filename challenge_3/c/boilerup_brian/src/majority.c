#include <stdio.h>

int getMode(int *, int);
int isMaj(int, int *, int);

void printMaj(int set[], int size){
    int mode = getMode(set, size);
    int maj = isMaj(mode, set, size);
    
    if (maj == 0){
        printf("Majority element not found\n");
    }
    else{
        printf("Majority element is %d\n", mode);
    }
}

int getMode(int set[], int size){
    int i;
    int mode_index = 0;
    int count = 1;
    for(i = 1; i < size; i++){
        if(set[i] == set[mode_index]){
            count ++;
        }
        else{
            mode_index = i;
            count = 1;
        }
    }
    return set[mode_index];
}

int isMaj(int mode, int set[], int size){
    int i;
    int mode_count = 0;
    
    for( i = 0; i < size; i ++){
        if (set[i] == mode){
            mode_count ++;
        }
    }
    if (mode_count > (size / 2)){
        return 1;
    }
    else{
        return 0;
    }
}

main(){
    int set[] = {1,2,3,4,3,3,4,5,3,3,5,3,4,3,3,3,6,3,3,3};
    int size = sizeof(set) / sizeof(set[0]);
    
    printMaj(set, size);
    
    return 0;
}
        
    