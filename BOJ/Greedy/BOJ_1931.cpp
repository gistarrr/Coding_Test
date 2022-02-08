#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const pair<int,int> & a, const pair<int,int> & b){
    if (a.second == b.second){
        return a.first < b.first;
    }
    return a.second < b.second;
}

int main(){
    int N;
    cin >> N;
    
    vector<pair<int,int> > council(N);

    for (int i = 0; i < N; i++){
        int a, b;
        cin >> a >> b;
        council[i] = {a, b}; 
    }

    sort(council.begin(), council.end(), compare);
    
    int count = 0, lastest = 0;

    for (int i = 0; i < council.size(); i++){
        if ((council[i].first >= lastest)){
            count += 1;
            lastest = council[i].second;
        }
    }

    cout << count << endl;

    return 0;
}