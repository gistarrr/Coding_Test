#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int inf = 1e9;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); 
    cout.tie(0);
    int V, E, start;
    cin >> V >> E >> start;

    vector <bool> chk(V+1, false);
    vector <int> distance(V+1, inf);

    vector <vector<pair<int,int> > > edge(V+1);

    for(int i = 0; i < E; i ++){
        int from, to, cost;
        cin >> from >> to >> cost;
        edge[from].push_back({to, cost});
    }

    priority_queue <pair<int,int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;

    pq.push({0, start});
    distance[start] = 0;

    while (!pq.empty()){
        int dist= pq.top().first, node = pq.top().second;
        pq.pop();
        if (!chk[node]){
            for (int i = 0; i < edge[node].size(); i++){
                int new_node = edge[node][i].first;
                int cost = edge[node][i].second + dist;
                if (distance[new_node] > cost){
                    distance[new_node] = cost;
                    pq.push({distance[new_node], new_node});
                }
            }
            chk[node] = true;
        }
    }

    for (int i = 1; i < V+1; i++){
        if (distance[i] == 1e9)
            cout << "INF" << endl;
        else  cout << distance[i] << endl;
    }

    return 0;
}