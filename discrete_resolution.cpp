#include <iostream>
using namespace std;
int main(void){
    cout << "Input rainfall number: ";
    int number_rainfall = 0;
    cin >> number_rainfall;
    cout << "Input rainfall data: ";
    float* rainfall = new float[number_rainfall];
    for (int i = 0; i < number_rainfall; i++){
        cin >> rainfall[i];
    }
    cout << "Input weight number: ";
    int number_weight = 0;
    cin >> number_weight;
    cout << "Input rainfall weight: ";
    float* weight = new float[number_weight];
    for (int i = 0; i < number_weight; i++){
        cin >> weight[i];
    }
    
    float* output = new float[number_rainfall + number_weight - 1];
    for (int i = 0; i < number_rainfall + number_weight - 1; i++)
        output[i] = 0;

    for (int i = 0; i < number_rainfall; i++){
        for (int j = 0; j < number_weight; j++){
            output[i + j] += rainfall[i] * weight[j];
        }
    }
    cout << "output: " << endl;
    for (int i = 0; i < number_rainfall + number_weight - 1; i++){
        cout << output[i]  << endl;
    }

    return 0;
}