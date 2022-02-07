#include <iostream>
#include <vector>

using namespace std;

int dp[100001] = {0, };

int main(){
    int N, K;

    cin >> N >> K;

    for (int i = 0; i < N; i++){
        int W, V;
        cin >> W >> V;
        for (int i = K; i > W-1; i--){
            dp[i] = max(dp[i-W]+V, dp[i]);
        }
    }
    cout << dp[K] << endl;

    return 0;
}