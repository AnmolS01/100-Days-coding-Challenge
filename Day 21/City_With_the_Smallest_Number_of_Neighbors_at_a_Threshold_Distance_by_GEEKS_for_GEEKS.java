 // Problem Statement : City With the Smallest Number of Neighbors at a Threshold Distance

class Solution {
    public int findCity(int n, int m, int[][] edges, int distanceThreshold) {
        int[][] distances = new int[n][n];
        int MAX_VALUE = Integer.MAX_VALUE / 2;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                distances[i][j] = MAX_VALUE;
            }
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            distances[u][v] = w;
            distances[v][u] = w;
        }

        for (int i = 0; i < n; i++)
            distances[i][i] = 0;

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (distances[i][k] != MAX_VALUE && distances[k][j] != MAX_VALUE) {
                        distances[i][j] = Math.min(distances[i][j], distances[i][k] + distances[k][j]);
                    }
                }
            }
        }

        int min_reachable_cities = Integer.MAX_VALUE;
        int city_index = -1;

        for (int i = 0; i < n; i++) {
            int reachable_cities = 0;
            for (int j = 0; j < n; j++) {
                if (distances[i][j] <= distanceThreshold)
                    reachable_cities++;
            }
            if (reachable_cities < min_reachable_cities || (reachable_cities == min_reachable_cities && i > city_index)) {
                min_reachable_cities = reachable_cities;
                city_index = i;
            }
        }

        return city_index;
    }
}
