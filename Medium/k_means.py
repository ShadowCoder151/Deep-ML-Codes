import math

def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
    def dist(p1, p2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
    
    def centroid(points):
        n = len(points)
        if n == 0:
            return (0, 0)
        c = [sum(coord[i] for coord in points) / n for i in range(len(points[0]))]
        return tuple(c)
    
    H = {c: [] for c in initial_centroids}
    
    for _ in range(max_iterations):
        for t in points:
            _, min_c = min((dist(t, c), c) for c in H)
            H[min_c].append(t)
        
        T = {}
        for c in H:
            new_centroid = centroid(H[c])
            T[new_centroid] = []
        
        H = T
    
    return list(H.keys())