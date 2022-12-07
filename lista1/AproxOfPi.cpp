#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <random>
#include <iostream>
#include <fstream>
#include <math.h>
#include <chrono>

using namespace std;

double distance(double x, double y){
    return sqrt((x-1)*(x-1) + (y-1)*(y-1));
}


float piAprox (int n){
    double pointX;
    double pointY;
    int counter = 0;

    for(int i = 0; i < n; i++){
        mt19937 mt { 
            static_cast<unsigned int>(chrono::steady_clock::now().time_since_epoch().count()) 
        };
             
        uniform_real_distribution<double> disX(0.0, 2.0);
        uniform_real_distribution<double> disY(0.0, 2.0);
        pointX = disX(mt);
        pointY = disY(mt);

        if(distance(pointX,pointY) <= 1.0 ){
            counter++;
        }
    }
    return ((float)counter/n)*2*2;
}

int main (int argc, char** argv)
{
    ofstream myFile ;
   
    myFile.open ("piResults.txt");
    
    myFile << "n;";

    for(int i = 1; i <= 50; i++ ){
        myFile << "Wynik " << i << ';';
    }
    myFile << '\n';

    for(int n = 50; n <= 5000; n += 50){
        myFile << n << ";";

        for(int i = 0; i < 50; i++ ){
            myFile << piAprox(n) << ';';
        }

        myFile << "\n";
    }

    myFile.close();

    return 0;
}



