class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        #intervals question
        #queries represent the ending time, x is length of time
        #sort logs by timing -> slide windows to match duration -> track unique using a hashtable and variable. sort queries by time as well
        #this will only cause logs to be looked at twice at most
        #bounded by sorting either logs or queries
        #window will count unique that falls within query time

        unique = 0
        occurrence = defaultdict(int)
        sorted_logs = sorted(logs, key=lambda x: x[1])

        indexed_queries = sorted(
            (query, i) for i, query in enumerate(queries)
        )
        start = 0
        end = 0
        ans = [0] * len(queries)

        for query, i in indexed_queries:
            start_time = query - x
            end_time = query

            #expand endpoint until it crosses endtime
            while end < len(sorted_logs) and end_time >= sorted_logs[end][1]:
                server = sorted_logs[end][0]
                occurrence[server] += 1
                if occurrence[server] == 1:
                    unique += 1
                end += 1

            #shrink startpoint while its < start_time
            while start < end and start_time > sorted_logs[start][1]:
                server = sorted_logs[start][0]
                occurrence[server] -= 1
                if occurrence[server] == 0:
                    unique -= 1
                start += 1
            ans[i] = n - unique
        return ans
            


            
        