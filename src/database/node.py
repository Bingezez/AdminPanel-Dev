from db import ConnectionMongoDb


class NodeDb(ConnectionMongoDb):
    name_colection = "nodes"
    def __init__(self):
        ConnectionMongoDb.__init__(self)
        self._node = None
        self._unique_name = dict()
        
    @property
    def collection(self):
        return self._db[self.name_colection]
    
    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, node: dict):
        self._node = node
        self._unique_name['nodeUniqueName'] = node['nodeUniqueName']
    
    @property
    def update_node(self):
        return self._node

    @update_node.setter
    def update_node(self, update_node: dict):
        self._node = {"$set": update_node}
    
    def is_node(self) -> bool:
        if self.collection.find_one(self._unique_name) is not None:
            return True
        return False

    def insert_node(self):
        if self.is_node(self._unique_name):
            self.collection.insert_one(self._node)
    
    def update_node_perfomance(self):
        if self.is_node(self._unique_name):
            self.collection.update_one(self._unique_name, self._node, upsert=True)

    def node_is_activities(self):
        activities = {"$set": {"nodeActive": True}}
        if self.is_node(self._unique_name):
            self.collection.update_one(self._unique_name, activities, upsert=True)

    def node_is_not_activities(self):
        activities = {"$set": {"nodeActive": False}}
        if self.is_node(self._unique_name):
            self.collection.update_one(self._unique_name, activities, upsert=True)
    

if __name__ == '__main__':
    test = NodeDb()
    test.node = {'nodeUniqueName': 'help'}
    # print(test.is_node())
    # print(test.is_account('506564ace706feef525b512d6ceb955b', '1234'))
    # print(test.is_account('506564ace706feef525b512d6ceb955b', '123'))
    # print(result)