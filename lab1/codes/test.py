import unittest  
import networkx as nx
import Graph

  
class TestBridgeWords(unittest.TestCase):  
  
    def setUp(self):  
        # 创建示例图 
        filename = "D:\\software_labs\\lab1\\input.txt" 
        # G1 是一个正常图
        self.G1 = Graph.create_word_graph(Graph.read_and_process_text(filename))  
  
        self.G2 = nx.DiGraph()  # 空的图  
  
    def test_case_1(self):  
        result = Graph.find_bridge_words(self.G1, 'to', 'explore')  
        self.assertEqual(result, "No bridge words from to to explore!")  
  
    def test_case_2(self):  
        result = Graph.find_bridge_words(self.G1, 'explore', 'new')  
        self.assertEqual(result, "The bridge words from explore to new are: strange, and exciting.")  
  
    def test_case_3(self):  
        result = Graph.find_bridge_words(self.G1, 'to', 'hello')  
        self.assertEqual(result, "No word1 or word2 in the graph!")  
  
    def test_case_4(self):  
        result = Graph.find_bridge_words(self.G1, 'to', 'to')  
        self.assertEqual(result, "No bridge words from to to to!")  

    def test_case_5(self):  
        result = Graph.find_bridge_words(self.G2, 'word1', 'word2')  
        self.assertEqual(result, "G is empty") 
  
if __name__ == '__main__':  
    unittest.main()