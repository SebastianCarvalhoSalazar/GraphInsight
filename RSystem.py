from collections import defaultdict
import networkx as nx
import numpy as np
import pandas as pd
from statistics import mode
from utils import Utils
utils = Utils()

class RecomendationSystem:
    def _setPartitions(self, G, df):
        for n, d in G.nodes(data=True):
            if n in df['target'].values:
                G.nodes[n]['bipartite'] = 'Product'
            elif n in df['source'].values:
                G.nodes[n]['bipartite'] = 'User'
            else:
                pass
        return G

    def _buildGraph(self, df):
        mydict = defaultdict(list)
        try:
            G = nx.from_pandas_edgelist(df, 'source', 'target')
            G = self._setPartitions(G, df)
            return G
        except:
            utils._successful_process("Remember --> Column names must be: source | target")
            exit()

    def _get_nodes_from_partition(self, G, partition):
        nodes = []
        for n in G.nodes():
            if G.nodes[n]['bipartite'] == partition:
                nodes.append(n)
        return nodes

    def _shared_partition_nodes(self, G, node1, node2):
        assert G.nodes[node1]['bipartite'] == G.nodes[node2]['bipartite']
        nbrs1 = G.neighbors(node1)
        nbrs2 = G.neighbors(node2)
        overlap = set(nbrs1).intersection(nbrs2)
        return overlap

    def _user_similarity(self, G, user1, user2, proj_nodes):
        assert G.nodes[user1]['bipartite'] == G.nodes[user2]['bipartite']
        assert G.nodes[user2]['bipartite'] == G.nodes[user1]['bipartite']
        shared_nodes = self._shared_partition_nodes(G,user1,user2)
        return len(shared_nodes) / len(proj_nodes)

    def _most_similar_users(self, G, user, user_nodes, proj_nodes):
        assert G.nodes[user]['bipartite'] == 'User'
        user_nodes = set(user_nodes)
        user_nodes.remove(user)
        similarities = defaultdict(list)
        for n in user_nodes:
            similarity = self._user_similarity(G, user, n, proj_nodes)
            similarities[similarity].append(n)
        max_similarity = max(similarities.keys())
        return similarities[max_similarity]

    def _recommend(self, G, from_user, to_user):
        from_repos = set(G.neighbors(from_user))
        to_repos = set(G.neighbors(to_user))
        return from_repos.difference(to_repos)

    def _predict(self, df, G):
        products = {}
        keys = list(set(df['source'].values.tolist()))
        user_nodes = self._get_nodes_from_partition(G, 'User')
        project_nodes = self._get_nodes_from_partition(G, 'Product')

        for key in keys:
            similar_users = self._most_similar_users(G, key, user_nodes, project_nodes)
            recommendProducts = [self._recommend(G, similarUsers, key) for similarUsers in similar_users]
            recommendProducts = [product for Recommendations in recommendProducts for product in Recommendations]
            products[key] = mode(recommendProducts) if len(recommendProducts) > 0 else "NR"
            print(f"Usuario: {key} --> Usuarios Similares: {similar_users} --> Productos Recomendados: {recommendProducts}")

        df = pd.DataFrame(products,index=[0]).T
        df.columns = ["Recommendations"]
        df['Nombre'] = df.index

        return df
