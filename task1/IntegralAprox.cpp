#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <random>
#include <iostream>
#include <fstream>
#include <math.h>
#include <chrono>

using namespace std;

double f(double x, int k)
{
    switch (k)
    {
        case 1:
            return pow(x,(1/3.0));    
            break;
        case 2:
            return sin(x);
            break;
        case 3:
            return 4*x*(pow((1-x),3));
            break;
        default:
            break;
    } 
}


float integralProb (float a, float b, float M, int n, int functionNr){
    double pointX;
    double pointY;
    int counter = 0;

    for(int i = 0; i < n; i++){
        mt19937 mt { 
            static_cast<unsigned int>(chrono::steady_clock::now().time_since_epoch().count()) 
        };
             
        uniform_real_distribution<double> disX(a,b);
        uniform_real_distribution<double> disY(0.0, M);
        pointX = disX(mt);
        pointY = disY(mt);

        if(pointY <= f(pointX,functionNr)){
            counter++;
        }
    }
    return ((float)counter/n)*(b-a)*M;
}

int main (int argc, char** argv)
{
    ofstream myFile1;
    ofstream myFile2;
    ofstream myFile3;
   
    myFile1.open ("results1.txt");
    myFile2.open ("results2.txt");
    myFile3.open ("results3.txt");
    
    myFile1 << "n;";
    myFile2 << "n;";
    myFile3 << "n;";

    for(int i = 1; i <= 50; i++ ){
        myFile1 << "Wynik " << i << ';';
        myFile2 << "Wynik " << i << ';';
        myFile3 << "Wynik " << i << ';';
    }
    myFile1 << '\n';
    myFile2 << '\n';
    myFile3 << '\n';

    for(int n = 50; n <= 5000; n += 50){
        myFile1 << n << ";";
        myFile2 << n << ";";
        myFile3 << n << ";";

        for(int i = 0; i < 50; i++ ){
            myFile1 << integralProb (0,8,2,n,1) << ';';
            myFile2 << integralProb (0,M_PI,1,n,2) << ';';
            myFile3 << integralProb (0,1,0.5,n,3) << ';'; 
        }

        myFile1 << "\n";
        myFile2 << "\n";
        myFile3 << "\n";
    }

    myFile1.close();
    myFile2.close();
    myFile3.close();

    return 0;
}



