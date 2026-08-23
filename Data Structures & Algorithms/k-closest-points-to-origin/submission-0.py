class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dict_dist = {}
        dists = []
        res = []
        # find distance of each point from origin -> O(n)
        # store these in a dict
        for point in points:
            tup_point = tuple(point)
            dict_dist[tup_point] = point[0]**2 + point[1]**2
            dists.append(dict_dist[tup_point])

        # sort distances -> O(nlog(n))
        dists.sort()

        # get top k values
        for i in range(k):
            dist = dists[i]
            keys = [k for k, v in dict_dist.items() if v == dist]
            
            res.append(list(keys[0]))
            del dict_dist[keys[0]]

        return res

