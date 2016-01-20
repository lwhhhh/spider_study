# 性能分析
import pstats
p = pstats.Stats("test1.out")
p.sort_stats("time").print_stats()
