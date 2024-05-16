import networkx as nx  
import re  
import sys  
from collections import defaultdict  
import matplotlib.pyplot as plt  
import random

# 读取文本文件并处理文本  
def read_and_process_text(filename):  
    with open(filename, 'r', encoding='utf-8') as file:  
        text = file.read()  
    # 替换标点符号、换行符、空格和非字母字符为单个空格  
    # 将文本转为小写，并将连续的空格压缩为一个空格  
    processed_text = re.sub(r'[^\w\s]', ' ', re.sub(r'\s+', ' ', text.lower())).strip()  
    # 将文本分割为单词列表  
    words = processed_text.split()  
    return words  
  
# 分析文本数据，并创建有向图  
def create_word_graph(words):  
    G = nx.DiGraph()  
    # 初始化单词对的计数  
    word_pairs = defaultdict(int)  
      
    # 遍历单词列表，统计相邻单词对的出现次数  
    for i in range(len(words) - 1):  
        word_pair = (words[i], words[i+1])  
        word_pairs[word_pair] += 1  
      
    # 根据统计结果，添加边和权重到有向图中  
    for (word_a, word_b), weight in word_pairs.items():  
        G.add_edge(word_a, word_b, weight=weight)  
      
    return G  
  
# 绘制有向图  
def draw_graph(G):  
    # 可以使用spring_layout或其他布局算法  
    pos = nx.spring_layout(G)  
    edge_labels = nx.get_edge_attributes(G, 'weight')  
    nx.draw(G, pos, with_labels=True, font_weight='bold')  
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  
    plt.axis('off') 
    # 保存到磁盘  
    plt.savefig('directed_graph.png', dpi=300)  # dpi设置图片质量 
    plt.show()  

# 功能3，查找桥接词 
def find_bridge_words(G, word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    # 检查word1和word2是否在图中  
    if word1 not in G or word2 not in G:  
        return "No word1 or word2 in the graph!"  
  
    # 初始化桥接词列表  
    bridge_words = []  
  
    # 遍历word1的邻居（即可以直接到达的节点）  
    for neighbor in G.neighbors(word1):  
        # 检查neighbor是否可以直接到达word2  
        if G.has_edge(neighbor, word2):  
            bridge_words.append(neighbor)  
  
    # 根据桥接词的数量输出不同的结果  
    if not bridge_words:  
        return "No bridge words from {} to {}!".format(word1, word2)  
    elif len(bridge_words) == 1:  
        return "The bridge word from {} to {} is: {}.".format(word1, word2, bridge_words[0])  
    else:  
        # 使用逗号+空格分隔最后一个单词前的所有单词，并在最后添加"and"  
        words_str = ", ".join(bridge_words[:-1]) + ", and " + bridge_words[-1]  
        return "The bridge words from {} to {} are: {}.".format(word1, word2, words_str)  


# 功能4，根据桥接词关系在新文本中插入桥接词  
def insert_bridge_words(G, text):  
    # 分割文本成单词列表  
    words = text.lower().split()  
    new_text = []  
      
    # 遍历单词对，查找并插入桥接词  
    for i in range(len(words) - 1):  
        word1, word2 = words[i], words[i+1]  
          
        # 检查单词对是否在图中，并且存在桥接词
        if word1 not in G or word2 not in G:
            new_text.append(word1)
            continue
        bridge_words = [node for node in G.neighbors(word1) if G.has_edge(node, word2)]  
          
        # 如果存在桥接词，随机选择一个插入  
        if bridge_words:  
            bridge_word = random.choice(bridge_words)  
            new_text.append(word1)  
            new_text.append(bridge_word)  
        else:  
            new_text.append(word1)  
      
    # 添加最后一个单词  
    new_text.append(words[-1])  
      
    # 将列表转换回字符串并用空格分隔  
    return ' '.join(new_text) 

# 功能5，计算并显示两个单词之间的最短路径  
def find_shortest_path(G, word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()  
    try:  
        # 计算最短路径  
        path = nx.shortest_path(G, source=word1, target=word2, weight='weight')  
        path_length = nx.shortest_path_length(G, source=word1, target=word2, weight='weight')  
          
        # 可选：计算所有最短路径（如果需要）  
        # all_paths = nx.all_shortest_paths(G, source=word1, target=word2, weight='weight')  
          
        # 打印结果  
        print(f"Shortest path from {word1} to {word2}: {path}")  
        print(f"Path length: {path_length}")  
        
        # 可视化图的一部分（最短路径）  
        # 使用Matplotlib高亮显示最短路径  
        pos = nx.spring_layout(G)  # 可以选择其他布局方式  
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')  
        nx.draw_networkx_edges(G, pos, edgelist=list(zip(path[:-1], path[1:])), edge_color='red', width=2)  
        plt.title(f"Shortest Path from {word1} to {word2}")  
        plt.show()  
    except nx.NetworkXNoPath:  
        print(f"No path from {word1} to {word2} found.不可达") 


# 功能需求6：随机游走 
def random_walk(G, start_node=None):  
    if start_node is None:  
        # 如果没有指定起始节点，则随机选择一个  
        start_node = random.choice(list(G.nodes()))  
  
    visited_nodes = [start_node]  # 记录已访问的节点  
    visited_edges = []  # 记录已访问的边  
    current_node = start_node  
  
    while True:  
        # 获取当前节点的所有出边  
        out_edges = list(G.out_edges(current_node, data=True))  
          
        if not out_edges:  
            # 如果没有出边，则停止遍历  
            break  
          
        # 从出边中随机选择一条  
        chosen_edge = random.choice(out_edges)  
        chosen_node = chosen_edge[1]  
  
        # 如果该边已经访问过，则停止遍历  
        if (current_node, chosen_node,chosen_edge[2]) in visited_edges or (chosen_node, current_node,chosen_edge[2]) in visited_edges:  
            break  
  
        # 添加到已访问的节点和边中  
        visited_nodes.append(chosen_node)  
        visited_edges.append((current_node, chosen_node, chosen_edge[2]))  
  
        # 更新当前节点  
        current_node = chosen_node  

        '''
        # 使用input()函数并检查用户是否输入了'stop' 
        check = input("if continue: (y/n)")
        if check == 'N' or check == 'n':
            break
        '''
    return visited_nodes ,visited_edges

# 主程序  
if __name__ == "__main__":
    filename = "D:\\software_labs\\lab1\\test.txt"
    words = read_and_process_text(filename)  
    G = create_word_graph(words)
    print(G.nodes)  
    for u, v, data in G.edges(data=True):  
        print(f"Edge: ({u}, {v}, {data['weight']})")  
    draw_graph(G)

    while 1:
        print("\n功能需求3：查询桥接词\n功能需求4：根据bridge word生成新文本\n功能需求5：计算两个单词之间的最短路径\n功能需求6：随机游走\n")
        print("请输入功能编号（3，4，5，6），(如果想要结束程序请输入stop) ：")
        choose = input()
        if choose == '3':
            #功能需求3：查询桥接词（bridge words）
            word1 = input("Enter a word: ")
            word2 = input("Enter a word: ")  
            print(find_bridge_words(G,word1,word2))
        elif choose == '4':

            #功能需求4：根据bridge word生成新文本
            text = input("Enter a new text:")
            print(insert_bridge_words(G,text))
        elif choose == '5':
            #功能需求5：计算两个单词之间的最短路径
            word1 = input("Enter a word: ")
            word2 = input("Enter a word: ")
            if word2 == "":
                for target in G.nodes:
                    if target != word1:
                        find_shortest_path(G,word1,target)
            else:
                find_shortest_path(G,word1,word2)
        elif choose == '6':
            #功能需求6：随机游走
            visited_nodes = []
            visited_edges = []
            visited_nodes ,visited_edges= random_walk(G,'life')
            random_walk_path = "random_walk_path.txt"
            with open(random_walk_path, 'w') as f:   
                for node in visited_nodes:  
                    f.write(f"{node} ")
        elif choose == 'stop':
            break




    
