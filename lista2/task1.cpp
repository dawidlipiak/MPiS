#include <stdio.h>
#include <random>
#include <stdlib.h>
#include <chrono>
#include <time.h>
#include <math.h>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

//proper random generator marsene twister
std::mt19937 mt{ static_cast<unsigned int>(
    std::chrono::steady_clock::now().time_since_epoch().count()
    ) };


void ballsAndBins (int n, int k, fstream results[]) {

    // Vector with numbers of balls in a pocket 
    vector<unsigned short>pockets(n,0);
    
    // Radnom number from range 0-(n-1)
    uniform_int_distribution dieN{0,n-1};
    
    // Counter of throws into pockets
    int counter = 0;
    // Index of pocket number generated randomly 
    int index;
    // Moment of first collision
    int firstCollision;
    // State if the first collision was finded yet
    bool state1 = false;
    // State if all the pockets have at least one ball in it
    bool state2 = false;
    // Number of empty pockets for n thrown balls
    int emptyPockets=0;
    // Maximum number of balls in one pocket
    int max =0;
    // Counter of pockets that have two balls in it
    int countDoubles = 0;
    // Counter of pockets that have one ball in it 
    int countOnes = 0;
    // Moment when all pockets have at least one ball in it
    int allOnes;
    
    while(countDoubles != n){
        index = dieN(mt);
        pockets[index]++;
        counter++;
        
        // counter of pockets with 2 balls within
        if(pockets[index] == 2){
            countDoubles++;
        }
        if(pockets[index] == 1){
            //printf("%d\n",counter);
            countOnes++;
        }
        // First collision
        if((countDoubles == 1) && (state1 != true) ){
            firstCollision = counter;
            state1 = true;
        }
        // Empty pockets for n balls
        if( counter == n){
            for(int i = 0; i < n; i++){
                if(pockets[i] == 0){
                    emptyPockets++;
                }
                if(pockets[i] > max){
                    max = pockets[i];
                }
            }
        }
        // All pockets have at least one ball
        if((countOnes == n) && (state2 == false)){
            allOnes = counter;
            state2 = true;
        }
    }
    pockets.clear();
    results[0] << to_string(firstCollision) + ",";
    results[1] << to_string(emptyPockets)+",";
    results[2] << to_string(max)+",";
    results[3] << to_string(allOnes)+",";
    results[4] << to_string(counter)+",";
    results[5] << to_string(counter - allOnes)+",";
    
}

int main(int argc, char **argv)
{   
    // File pointer
    fstream results[6];

    // opens an existing csv file or creates a new file.
    results[0].open("Bn_results.csv", ios::out);
    results[1].open("Un_results.csv", ios::out);
    results[2].open("Ln_results.csv", ios::out);
    results[3].open("Cn_results.csv", ios::out);
    results[4].open("Dn_results.csv", ios::out);
    results[5].open("Dn-Cn_results.csv", ios::out);

    //number of pockets
    int n = 1000;
    // Number of repeats
    int k;

    for(; n <= 100000; n += 1000)
    {
        for (int i = 0; i < 6; i++){
                results[i] << to_string(n) + ",";
        }
        
        for (k = 0; k < 50; k++)
        {
            ballsAndBins(n, k, results);
        }

        for (int i = 0; i < 6; i++){
            results[i] << "\n";
        }
    }


    for (int i = 0; i < 6; i++)
    {
            results[i].close();
    }

    return 0;

}