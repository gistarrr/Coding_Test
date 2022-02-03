#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

#define VMAX 2001

using namespace std;

int INF = 1e9;

vector <int> dijkstra(vector <pair<int, int> > graph[], int node, int start_node){
    vector <bool> visited(node+1, false);
    vector <int> distance(node+1, INF);
    priority_queue <pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;

    pq.push({0, start_node});
    distance[start_node] = 0;

    while (!pq.empty()){
        int dist = pq.top().first, current = pq.top().second;
        pq.pop();
        if (!visited[current]){
            for (int i = 0; i < graph[current].size(); i++){
                int new_node = graph[current][i].first;
                int cost = graph[current][i].second + dist;
                if (distance[new_node] > cost){
                    distance[new_node] = cost;
                    pq.push({cost, new_node});
                }
            }
            visited[current] = true;
        }
    }

    return distance;
}

int main(){
    int T;
    int n, m, t;
    int s, g, h;

    vector <int> destination;

    cin >> T;
    while (T != 0){
        cin >> n >> m >> t;
        cin >> s >> g >> h;

        vector <pair<int, int> > graph[n+1];
        vector <int> destination;
        int between;

        for (int i = 0; i < m; i++){
            int a, b, d;
            cin >> a >> b >> d;
            graph[a].push_back({b, d});
            graph[b].push_back({a, d});
            if ((a == g && b == h) || (a == h && b == g))   between = d;
        }
        for (int i = 0; i < t; i++){
            int x;
            cin >> x;
            destination.push_back(x);
        }
        
        vector<int> result;
        vector<int> short_path = dijkstra(graph, n, s);
        vector<int> g_distance = dijkstra(graph, n, g);
        vector<int> h_distance = dijkstra(graph, n, h);

        for(int i = 0; i < destination.size(); i++){
            int target = destination[i];

            if ((g_distance[s] + between + h_distance[target] == short_path[target]) || (h_distance[s] + between + g_distance[target] == short_path[target])){
                result.push_back(target);
            }
        }
        sort(result.begin(), result.end());
        for(int i = 0; i < result.size(); i++){
            cout << result[i] << ' ';
        }
        cout << endl;
        T--;
    }

    return 0;
}