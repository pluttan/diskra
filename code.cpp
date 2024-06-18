#include <iostream>
#include <queue>

bool search(int se, int t, int graph[12][12], int* par){
    bool in[12] = {0,0,0,0,0,0,0,0,0,0,0,0};
    std::queue<int> que;
    que.push(se);
    in[se] = true;
    while (!que.empty()){
        int last = que.front();
        que.pop();
        for (int j = 0; j < 12; j++){
            if (!in[j] && graph[last][j] > 0){
                que.push(j);
                in[j] = 1;
                par[j] = last; 
            }
        }
    }
    return in[t];
}

int algo(int matrix[12][12]){
    int par[12] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
    int flowMax = 0;
    while (search(0, 11, matrix, par)){
        int flow = 1000;
        int t = 11;
        while (t != 0){
            flow = flow > matrix[par[t]][t] ? matrix[par[t]][t]: flow;
            t = par[t];
        }
        flowMax += flow;
        t = 11;
        while (t != 0){
            int pt = par[t];
            matrix[pt][t] -= flow;
            matrix[t][pt] += flow;
            t = pt;
        }
    }
    return flowMax;
}

int main(){
    int matrix[12][12] = {
        {0, 13,  0, 46, 26,  0,  0,  0,  0,  0,  0,  0},
        {0,  0,  0,  0,  0,  0, 20,  0,  0,  0,  0,  0},
        {0,  0,  0,  0,  0, 12,  0,  0,  0,  0,  0,  0},
        {0,  0,  0,  0,  0, 21,  0,  0,  0,  0, 24,  0},
        {0,  0, 27,  0,  0,  0, 15, 14,  0,  0,  0,  0},
        {0,  0,  0,  0,  0,  0,  0,  0, 16,  0,  0,  0},
        {0,  0,  0,  0,  0,  0,  0,  8,  0, 13,  0, 31},
        {0,  0, 33,  0,  0,  0,  0,  0,  0, 22,  0,  0},
        {0,  0,  0,  0,  0,  0,  0,  4,  0, 10,  0, 18},
        {0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 17, 50},
        {0,  0,  0,  0,  0,  0,  0,  0, 22,  0,  0,  7},
        {0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0}};

    std::cout << algo(matrix) << "\n";
}
