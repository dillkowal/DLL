"""
Project 1
CSE 331 FS24 
Authors of DLL: Andrew McDonald, Alex Woodring, Andrew Haas, Matt Kight, Lukas Richters, 
                Anna De Biasi, Tanawan Premsri, Hank Murdock, & Sai Ramesh
Authors of Application: Leo Specht
solution.py
"""

from __future__ import annotations
from typing import TypeVar, List, Tuple, Optional

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
DLL = TypeVar("DLL")

# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    DO NOT MODIFY
    """
    __slots__ = ["value", "next", "prev", "children_branch"]

    def __init__(self, value: T, next: Node = None, prev: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        DO NOT MODIFY
        """
        self.next = next
        self.prev = prev
        self.value = value

        # Variable only used in application problem.
        self.children_branch: Optional[GitBranch] = None

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        DO NOT MODIFY
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        DO NOT MODIFY
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        DO NOT MODIFY
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        DO NOT MODIFY
        """
        return repr(self)

    # MODIFY BELOW #
    # Refer to the classes provided to understand the problems better #

    def empty(self) -> bool:
        """
        Return boolean indicating whether DLL is empty.

        :return: True if DLL is empty, else False.
        """
        return self.size == 0

    def push(self, val: T, back: bool = True) -> None:
        """
        Create Node containing `val` and add to back (or front) of DLL. Increment size by one.

        :param val: value to be added to the DLL.
        :param back: if True, add Node containing value to back (tail-end) of DLL;
            if False, add to front (head-end).
        :return: None.
        """
        new_node = Node(val)
        
        if self.size == 0: #check if list is empyt
          self.head = new_node
          self.tail = new_node
        
        elif back: #Add to the back of the list if back is true
          new_node.prev = self.tail
          self.tail.next = new_node
          self.tail = new_node
        
        else: #Add to front of list if back is false 
          new_node.next = self.head
          self.head.prev = new_node
          self.head = new_node
        
        self.size += 1 #increment list size by 1 

    def pop(self, back: bool = True) -> None:
        """
        Remove Node from back (or front) of DLL. Decrement size by 1. If DLL is empty, do nothing.

        :param back: if True, remove Node from (tail-end) of DLL;
            if False, remove from front (head-end).
        :return: None.
        """

        if self.size == 0:
          return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        if back:
          if self.tail is not None:
            self.tail = self.tail.prev
            self.tail.next = None

          else:
            self.head = None
            self.tail = None

        else:
          if self.head is not None:
            self.head = self.head.next
            
            if self.head is not None:
              self.head.prev = None

          else:
            self.head = None
            self.tail = None

        self.size -= 1   

    def list_to_dll(self, source: List[T]) -> None:
        """
        Construct DLL from a standard Python list.

        :param source: standard Python list from which to construct DLL.
        :return: None.
        """
        self.head = None
        self.tail = None
        self.size = 0

        if not source:
          return
        
        self.head = Node(source[0])
        current_node = self.head
        self.size = 1
        
        #Iterate through the rest of the source list
        for item in source[1:]:
          new_node = Node(item)
          current_node.next = new_node #Link new node to the current node
          new_node.prev = current_node #Set prev pointer of the new node
          current_node = new_node
          self.size += 1
        
        #Set the tail to the last node
        self.tail = current_node
        

    def dll_to_list(self) -> List[T]:
        """
        Construct standard Python list from DLL.

        :return: standard Python list containing values stored in DLL.
        """
        result = []  #Initialize an empty python list to store nodes
        current_node = self.head #Start from the head of the DLL
        
        #Traverse through the whole DLL
        while current_node:
          result.append(current_node.value) #Append the current node's data to result list
          current_node = current_node.next #Moves to the next node 
        
        return result #Return the Python list with nodes

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Construct list of Nodes with value val in the DLL and return the associated Node list

        :param val: The value to be found
        :param find_first: If True, only return the first occurrence of val. If False, return all
        occurrences of val
        :return: A list of all the Nodes with value val.
        """
        result = []
        current_node = self.head

        while current_node: #Traverse the list
            if current_node.value == val: #Checks if node is the same as the target
                result.append(current_node) #Appends the node to result if true

                if find_first: #Stops after finding first node if find_first is True
                    break

            current_node = current_node.next #Move to next node
        
        return result #Returns a list of matching nodes

    def find(self, val: T) -> Node:
        """
        Find first instance of `val` in the DLL and return associated Node object..

        :param val: value to be found in DLL.
        :return: first Node object in DLL containing `val`.
            If `val` does not exist in DLL, return an empty list.
        """
        result = self._find_nodes(val, find_first = True) #Calls _find_nodes with find_first=True to return first matching node
        
        if result: #Returns the first node if found
            return result[0]
        
        else: #Returns None if result is empty
            return None 

    def find_all(self, val: T) -> List[Node]:
        """
        Find all instances of `val` in DLL and return Node objects in standard Python list.

        :param val: value to be searched for in DLL.
        :return: Python list of all Node objects in DLL containing `val`.
            If `val` does not exist in DLL, return None.
        """
        result = self._find_nodes(val, find_first = False) #Calls _find_nodes with find_first=False to return all matching nodes
        
        return result #Returns a list of all matching nodes

    def _remove_node(self, to_remove: Node) -> None:
        """
        Given a node in the linked list, remove it.
        Should only be called from within the DLL class.

        :param to_remove: node to be removed from the list
        :return: None
        """
        if to_remove == self.head:
            self.head = to_remove.next #Makes the head point to the next node 
            
            if self.head: #Checks if list is not empty after removing head
                self.head.prev = None 
            
            else: #Update tail as well if list is empty 
                self.tail = None
        
        elif to_remove == self.tail:
            self.tail = to_remove.prev #Makes the tail point to the previous node from tail

            if self.tail:
                self.tail.next = None
            
            else:
                self.head = None
        
        else:
            previous = to_remove.prev
            nexts = to_remove.next
            previous.next = nexts
            nexts.prev = previous
        
        self.size -= 1

        to_remove.prev = None
        to_remove.next = None
          
    def remove(self, val: T) -> bool:
        """
        Delete first instance of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: True if Node containing `val` was deleted from DLL; else, False.
        """
        node_remove = self.find(val) #Call to find the first node with the value

        if node_remove: #If node is found, remove it and return True
            self._remove_node(node_remove)
            return True
        
        #If node isnt found return False
        return False

    def remove_all(self, val: T) -> int:
        """
        Delete all instances of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: integer indicating the number of Nodes containing `val` deleted from DLL;
                 if no Node containing `val` exists in DLL, return 0.
        """
        nodes_to_remove = self.find_all(val)

        for node in nodes_to_remove:
            self._remove_node(node)

        return len(nodes_to_remove)

    def reverse(self) -> None:
        """
        Reverse DLL in-place by modifying all `next` and `prev` references of Nodes in the
        DLL and resetting the `head` and `tail` references.

        :return: None.
        """
        current = self.head
        prev_head = self.head
        prev_tail = None

        while current:

            current.next, current.prev = current.prev, current.next
            prev_tail = current
            current = current.prev
        
        #Update the head and tail 
        self.head, self.tail = prev_tail, prev_head


# MODIFY BELOW #
# Refer to specs to know what can be changed #
class GitBranch(DLL):
    def __init__(self, name: str = "main", parent_node: Node = None):
        self.name = name
        self.parent_node = parent_node
        super().__init__()

    def push_commit(self, value: T) -> Optional[Node]:
        """
        Push a value in the Git timeline.
        If the value is the first in the branch, assign previous node to be the parent node.
        :param value: Value to be added to the branch.
        :return: The new last node of the branch.
        """

        super().push(value) #Push value to the back of the DLL
        return self.tail

    def get_first_commit(self) -> Node:
        """
        Get first commit on the branch/timeline.
        :return: The first commit node on the branch.
        """
        return self.head
    
    def get_last_commit(self) -> Node:
        """
        Get the last commit on the branch/timeline.
        :return: The last commit node on the branch.
        """
        return self.tail


class Git:
    __slots__ = ["current_branch", "start", "selected_commit", "visited_branches"]
    
    def __init__(self):
        # Reference to the original/main branch.
        self.start = GitBranch()
        # Current working branch.
        self.current_branch = self.start
        # The currently selected commit of a branch, which might not be in the active working branch or the main branch,
        # as we may be moving backwards or forward in the commit history
        self.selected_commit: Node = None
        # Keeps track of branches that have been visited on backwards movements.
        self.visited_branches = set()

    def get_current_commit(self) -> Optional[str]:
        """
        Return the value stored in the currently selected commit.
        :return: current working commit of tree.
        """

        #Check if there is no selected commit
        if self.selected_commit is None:
            return None #Returns None if selected_commit is empty
        
        #Else return the value stored in selected_commit
        return self.selected_commit.value

    def get_current_branch_name(self) -> Optional[str]:
        """
        Return the name of the current working/active branch.
        :return: Name of current working branch.
        """
        if self.current_branch is None:
            return None 

        return self.current_branch.name

    def commit(self, message: str) -> None:
        """
        Commit to the timeline if it is the last element in the commit.
        If current working commit is not the last commit, raise exception.
        :param message: Message to be added to commit.
        """
        if self.selected_commit is not None and self.selected_commit != self.current_branch.tail:
            raise Exception("Can’t commit in middle of timeline")
        
        #Push new commit to the current branch
        new_commit = self.current_branch.push_commit(message)
        
        #Updates current selected commit to new_commit
        self.selected_commit = new_commit



    def backwards(self) -> None:
        """
        Moves the reference of the current working commit back one commit.
        If already in the first commit of tree, do not move.
        """
        if self.selected_commit is None:
            if self.current_branch.parent_node:
                self.selected_commit = self.current_branch.parent_node
            else:
                return

        self.visited_branches.add(self.current_branch.name)

        if self.current_branch.name == "main":
            if self.selected_commit == self.current_branch.head:
                return
            elif self.selected_commit.prev:
                self.selected_commit = self.selected_commit.prev

        else:
            if self.selected_commit == self.current_branch.head and self.current_branch.parent_node:
                self.selected_commit = self.current_branch.parent_node
            elif self.selected_commit.prev:
                self.selected_commit = self.selected_commit.prev


            

    def forward(self) -> None:
        """
        Move the reference of the current working commit forward one commit.
        Keep the working commit on the working branch if multiple branches available.
        If already in the last commit of tree, do not move.
        """
        if self.selected_commit is None or self.current_branch.head is None:
            self.selected_commit = None
            return

        if self.current_branch.name == "main":
            if self.selected_commit == self.current_branch.tail:
                return
            elif self.selected_commit and self.selected_commit.next:
                self.selected_commit = self.selected_commit.next

        else:
            if self.selected_commit.next is not None:
                self.selected_commit = self.selected_commit.next
            elif self.selected_commit.next is None:
                if self.selected_commit.children_branch:
                    if self.selected_commit.children_branch.name in self.visited_branches:
                        self.selected_commit = self.selected_commit.children_branch.get_first_commit()
                elif self.current_branch.parent_node and self.current_branch.parent_node.children_branch:
                    if self.current_branch.parent_node.children_branch.name in self.visited_branches:
                        self.selected_commit = self.current_branch.parent_node.children_branch.get_first_commit()

        

    # DO NOT MODIFY BELOW #
    # The following methods are already implemented for you to (1) better understand how Git works,
    # (2) better understand tests.py as they are called in tests.py.
    def checkout_commit(self, message) -> None:
        """
        Check out any commit in the tree, moving the current selected branch to that commit's branch.
        If the commit is found, change the current selected branch to be the parent branch of the commit.
        If no such commit exists, raise an exception.

        :param message: Commit message to look for.
        """
        existing_commit = self.find_commit(self.start, message)
        if existing_commit is not None:
            self.current_branch = existing_commit[0]
            self.selected_commit = existing_commit[1]
            return

        raise Exception("Commit is not existent")

    def checkout_branch(self, name) -> None:
        """
        Check out a tree branch, and move the working commit to the last commit on the branch.
        If the branch with the given name already exist, change the current branch to be that one, and change the current
        commit to be the last commit on the branch. If branch does not exist and current working commit does not have a
        branch, then create a branch from that commit.

        :param name: The branch name to look for.
        :return: None.
        """
        existing_branch = self.find_branch(self.start, name)

        # Branch exists
        if existing_branch is not None:
            self.current_branch = existing_branch
            self.selected_commit = existing_branch.get_last_commit()
            self.visited_branches.clear()
            return

        # Trying to create a branch on an empty head (No commits on branch yet)
        if self.selected_commit is None:
            raise Exception("Branches cannot be created on empty commits")

        if self.selected_commit.children_branch is None:
            self.selected_commit.children_branch = GitBranch(name, self.selected_commit)
            self.current_branch = self.selected_commit.children_branch
            self.selected_commit = self.selected_commit.children_branch.head
            self.visited_branches.clear()

        else:
            raise Exception("Can't create multiple branches based of same commit")

    def find_branch(self, start: GitBranch, name: str) -> GitBranch | None:
        """
        Iteratively find branch on the tree.

        :param start: Current tree to look for in.
        :param name: Name of branch to look for.
        :return: Branch reference if found, else None.
        """
        next_trees = [start]
        while next_trees:
            start = next_trees.pop()
            if start.name == name:
                return start
            node = start.get_first_commit()
            while node:
                if node.children_branch:
                    next_trees.append(node.children_branch)
                node = node.next
        return

    def find_commit(self, start: GitBranch, message: str) -> Tuple[GitBranch, Node] | None:
        """
        Iteratively find a commit based on the given commit message.

        :param start: Current branch to look for commit
        :param message: Commit message to look for
        :return: If found commit, return branch and commit node, else None
        """
        next_trees = [start]
        while next_trees:
            start = next_trees.pop()
            node = start.get_first_commit()
            while node:
                if node.value == message:
                    return start, node
                if node.children_branch:
                    next_trees.append(node.children_branch)
                node = node.next
        return