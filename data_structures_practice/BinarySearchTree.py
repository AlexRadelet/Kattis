# Dans BST, chaque noeud peut avoir 2 enfants
# chaque noeud à gauche est plus petit que son parent
# chaque noeud à droite est plus grand que son parent
# root : noeud source
# leaf : noeud sans enfants
# node = noeud
# pour la recherche, regarde à chaque neodu si valeur < ou > que node, et choisis gauche ou droite en fonction
# Dans un tree est balanced, O(h) height ou O(log(n))
#worst case : O(n) - ça devient donc une LinkedList

# On ne recherche jamais par value mais tjrs par key

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = None

    def __repr__(self):
        return f"({self.key}, {self.value})"


class BinarySearchTree:

    def __init__(self):
        self.root = None

    # O(n) worts case, O(log(n)) average case, O(h) always
    def __contains__(self, key):
        current_node = self.root
        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return True
        return False


    #__iter__ : Permet de pouvoir itérer comme ceci :
    #tree = BinarySearchTree()
    #for i in tree:
    #   pass

    #O(n) - linear time
    def __iter__(self):
        yield from self._in_order_traversal(self.root)

    # O(n) - linear time
    def __repr__(self):
        return str(list(self._in_order_traversal(self.root)))

    # O(n) worst case, O(log(n)) average case, O(h) always
    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key)
            self.root.value = value
        else :
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left is None:
                        current_node.left = Node(key)
                        current_node.left.value = value
                        current_node.left.parent = current_node
                        break

                    else:
                        current_node = current_node.left
                elif key > current_node.key:

                        if current_node.right is None:
                            current_node.right = Node(key)
                            current_node.right.value = value
                            current_node.right.parent = current_node
                            break

                        else:
                            current_node = current_node.right
                else:
                    #update d'une value déjà existante
                    current_node.value = value
                    break

    # O(n) worst case, O(log(n)) average case, O(h) always
    def search(self, key):
        current_node = self.root
        while True:
            if current_node is None or current_node.key == key:
                return current_node
            elif key < current_node.key:
                if current_node.left is None:
                    return None
                else :
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    return None
                else :
                    current_node = current_node.right

    # O(n) worst case, O(log(n)) average case, O(h) always
    def delete(self, key):
        #3 diffrentes cas :
        """
        1) delete a leaf
            il suffit de couper le lien entre leaf et son parent ( nb : bien le faire dans les 2 sens)

        2) delete node with 1 child
            Je remplace le node supprimé par son enfant unique

        3) delete a node with 2 child
            Je remplace le node supprimé par son successeur
                -> successeur : node with smaller key that's larger than the key i'm remplacing (dans la partie du tree en dessous)

                -> predecesseur : node with larger key that's smaller than the key i'm remplacing (dans la partie du tree en dessous)

        """
        node = self.search(key)
        if node is None:
            raise KeyError('Node with ths key does not exist')

        self._delete(node)

    # O(n) - linear time
    def traverse(self, order):
        if order == 'inorder':
            yield from self._in_order_traversal(self.root)
        elif order == 'preorder':
            yield from self._pre_order_traversal(self.root)
        elif order == 'postorder':
            yield from self._post_order_traversal(self.root)
        else:
            raise ValueError("Unknown order")

    def _delete(self, node):
        # Node is leaf node
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.right == node:
                    node.parent.right = None
                else:
                    node.parent.left = None
                node.parent = None

        # Node has two child nodes
        elif node.left is not None and node.right is not None:
            successor = self._successor(node)
            node.key = successor.key
            node.value = successor.value
            self._delete(successor)

        # Node has one child node
        else:
            child_node = node.left if node.left is not None else node.right
            if node.parent is None:
                child_node.parent = None
                self.root = child_node
            else:
                if node.parent.right == node:
                    node.parent.right = child_node
                else:
                    node.parent.left = child_node
                child_node.parent = node.parent
            node.parent = node.left = node.right = None

    def _successor(self, node):
         if node is None:
             raise ValueError('Cannot find a successor of None')
         if node.right is None:
             return None
         else :
             #aller une fois à droite puis un max de fois à gauche
            current_node = node.right
            while current_node.left is not None:
                current_node = current_node.left
            return current_node

    def _predecessor(self, node):
        if node is None:
            raise ValueError('Cannot find a predecessor of None')
        if node.left is None:
            return None
        else:
            # aller une fois à gauche puis un max de fois à droite
            current_node = node.left
            while current_node.right is not None:
                current_node = current_node.right
            return current_node

    def _in_order_traversal(self, node):
        # yield : generate value
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield (node.key, node.value)
            yield from self._in_order_traversal(node.right)


    def _pre_order_traversal(self, node):
        # yield : generate value
        if node is not None:
            yield (node.key, node.value)
            yield from self._pre_order_traversal(node.left)
            yield from self._pre_order_traversal(node.right)

    def _post_order_traversal(self, node):
        # yield : generate value
        if node is not None:
            yield from self._post_order_traversal(node.left)
            yield from self._post_order_traversal(node.right)
            yield (node.key, node.value)


if __name__ == '__main__':

    bst = BinarySearchTree()

    bst.insert(10, 'hello')
    bst.insert(5, 'hello')
    bst.insert(22, 'hello')
    bst.insert(2, 'hello')
    bst.insert(9, 'hello')
    bst.insert(12, 'hello')
    bst.insert(30, 'hello')
    bst.insert(11, 'hello')
    bst.insert(15, 'hello')
    bst.insert(30, 'hello')
    bst.insert(23, 'hello')
    bst.insert(35, 'hello')
    bst.insert(1, 'hello')

    bst.delete(1)

    for i in bst.traverse('preorder'):
        print(i)
