import unittest  
import networkx as nx
import Graph  
from Graph import find_shortest_path  # 假设你的函数在名为your_module的模块中  
  
class TestFindShortestPath(unittest.TestCase):  
    def setUp(self):  
        # 在这里设置你的测试图G 
        filename = "D:\\software_labs\\lab1\\input.txt" 
        # G1 是一个正常图
        self.G = Graph.create_word_graph(Graph.read_and_process_text(filename)) 
        self.G2 = nx.DiGraph() 
  
    def test_normal_path(self):  
        # 设置测试用例1和2的输入和期望输出  
        try:
            find_shortest_path(self.G, 'to', 'worlds')  
            # 你可能需要检查print输出或使用其他方式来验证结果
        except Exception as e:
            self.fail(f"find_shortest_path raised Exception unexpectedly: {e}")  
  
    def test_no_path(self):  
        # 设置测试用例3的输入和期望输出  
        # 修改图G或输入单词以确保没有路径  
        try:
            find_shortest_path(self.G, 'ok', 'worlds')  
            # 你可能需要检查print输出或使用其他方式来验证结果
        except Exception as e:
            self.fail(f"find_shortest_path raised Exception unexpectedly: {e}")  
  
    def test_graph_is_empty(self):  
        # 设置测试用例3的输入和期望输出  
        # 修改图G或输入单词以确保没有路径  
        try:
            find_shortest_path(self.G2, 'ok', 'worlds')  
            # 你可能需要检查print输出或使用其他方式来验证结果
        except Exception as e:
            self.fail(f"find_shortest_path raised Exception unexpectedly: {e}") 
if __name__ == '__main__':  
    unittest.main()