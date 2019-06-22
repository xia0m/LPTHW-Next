# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handlerName):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.routeName = handlerName

    def insert(self, paths, name):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for path in paths:
            if path not in current_node.children:
                current_node.insert(path)
            current_node = current_node.children[path]
        current_node.handler_name = name

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for path in paths:
            if path == '':
                return self.routeName
            if path not in current_node.children:
                return None
            current_node = current_node.children[path]
        return current_node.handler_name

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.


class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler_name = None
        self.children = {}

    def insert(self, path):
        # Insert the node as before
        self.children[path] = RouteTrieNode()
        # The Router class will wrap the Trie and handle


class Router:
    def __init__(self, rootHandler, notFoundHandler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(rootHandler)
        self.notFound = RouteTrie(notFoundHandler)

    def add_handler(self, handler_path, handler_name):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        handler_path = self.split_path(handler_path)
        self.root.insert(handler_path, handler_name)

    def lookup(self, paths):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler_path = self.split_path(paths)
        handler_name = self.root.find(handler_path)
        if handler_name is None:
            return self.notFound.routeName
        else:
            return handler_name

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        return path.replace('/', ' ').strip().split(' ')

# Here are some test cases and expected outputs you can use to test your implementation


# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route
# print(router.root.find(['home', 'about']))

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
