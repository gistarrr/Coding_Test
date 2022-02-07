#include <iostream>
#include <vector>

using namespace std;

vector<vector<long long> > cal_matrix(vector<vector<long long> > A, vector<vector<long long> > B){
    long long N = A.size();
    vector<vector<long long> > matrix(N, vector(N,0LL));

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++){
            int temp = 0;
            for (int k = 0; k < N; k++){
                temp += (A[i][k] * B[k][j]);
            }
            matrix[i][j] = temp % 1000;
        }            
    
    return matrix;
}

vector<vector<long long> > calculate_pow(vector<vector<long long> > A, vector<vector<long long> > matrix, long long B){
    if (B == 1){
        return matrix;
    }
    else if (B % 2 == 0){
        return calculate_pow(A, cal_matrix(matrix, matrix), B / 2);
    }
    else {
        return cal_matrix(calculate_pow(A, cal_matrix(matrix, matrix), B / 2), matrix);
    }

}

int main(){
    long long N;
    long long B;
    cin >> N >> B;

    vector<vector<long long> > A(N, vector(N, 0LL));
    
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cin >> A[i][j];
        }
    }

    A = calculate_pow(A, A, B);

    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cout << A[i][j] % 1000 << ' ';
        }
        cout << endl;
    }


    return 0;
}