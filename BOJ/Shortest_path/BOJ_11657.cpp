#include <iostream>
#include <vector>

#define NMAX 501

using namespace std;

const int INF = 1e9;
struct Node{
    int from, to, w;
};

long long dist[NMAX];

int main(){
    int N, M;
    cin >> N >> M ;

    for (int i = 0; i < N+1; i++){
        dist[i] = INF;
    }
    vector<Node> graph;

    for (int i = 0; i < M; i++){
        int A, B, C;
        cin >> A >> B >> C;
        graph.push_back({A, B, C});
    }

    dist[1] = 0;

    for (int i = 1; i < N+1; i++){
        for (int j = 0; j < M; j++){
            int from = graph[j].from, to = graph[j].to, cost = graph[j].w;

            if ((dist[from] != INF) && (dist[to] > dist[from] + cost)){
                dist[to] = dist[from] + cost;
                if (i == N) {
                    cout << -1 << endl;
                    return 0;
                }
            }
        }
    }

    for (int i = 2; i < N+1; i++){
        if (dist[i] == INF) cout << -1 << endl;
        else cout << dist[i] << endl;
    }

    return 0;
}