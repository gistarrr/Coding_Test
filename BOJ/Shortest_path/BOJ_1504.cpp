#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

long long INF = 1e9;
vector <pair<int, int> > graph[801];

void dijkstra(vector <long long> &distance, int start_node){
    bool visited[801] = {false, };
    priority_queue< pair<int, int>, vector< pair<int, int> >, greater< pair<int, int> > > pq;

    pq.push(make_pair(0, start_node));
    distance[start_node] = 0;

    while (!pq.empty()){
        int dist = pq.top().first, node = pq.top().second;
        pq.pop();

        if (!visited[node]){
            for (int i = 0; i < graph[node].size(); i++){
                int new_node = graph[node][i].first;
                int cost = graph[node][i].second + dist;
                if (distance[new_node] > cost){
                    distance[new_node] = cost;
                    pq.push(make_pair(cost, new_node));
                }
            }
            visited[node] = true;
        }
    }
}

int main(){
    int N, E;
    int v_1, v_2;

    cin >> N >> E;
    for(int i = 0; i < E; i++){
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }
    cin >> v_1 >> v_2;

    vector <long long> distance_1(N+1, INF);
    vector <long long> distance_2(N+1, INF);

    dijkstra(distance_1, v_1);
    dijkstra(distance_2, v_2);

    int result = min({INF, distance_1[1] + distance_1[v_2] + distance_2[N], distance_2[1] + distance_2[v_1] + distance_1[N]});

    if (result >= INF)  cout << -1 << endl;
    else cout << result << endl;

    return 0;
}