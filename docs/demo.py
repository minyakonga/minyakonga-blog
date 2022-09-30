from typing import Union, Any
from enum import Enum


class CustomExceptions(Enum):
    """custom exceptions which will be used in bst
    """
    OK = ''
    ALREADY_EXIST = 'ALREADY_EXIST'
    NOT_FOUND_ERROR = 'NOT_FOUND_ERROR'
    INTERNAL_ERROR = 'INTERNAL_ERROR'


class TreeNode:
    """tree node represented by class
    """
    def __init__(self, value: Any, left: object=None, right: object=None) -> None:
        """initialize a tree node

        Args:
            value (Any): _description_
            left (object, optional): _description_. Defaults to None.
            right (object, optional): _description_. Defaults to None.
        """
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    """implementation of binary search tree, which support insert/delete/traverse etc
    """
    def __init__(self) -> None:
        """setting tree root node
        """
        self.root = None
    
    async def insert(self, value: Any) -> Union[str, bool]:
        """insert value into bst, non-recursive implementation

        Args:
            node (Any): an value

        Returns:
            Union[str, bool]: err, is_ok
        """
        # 1st, if tree not exist yet, create root node and return
        # 2nd, if value equals current node value, return
        # 3rd, find the leaf node to add current value into it's child
        cursor = self.root

        while cursor:
            if cursor.value > value:
                next_cursor = cursor.left
                if not next_cursor:
                    cursor.left = TreeNode(value, None, None)
                    return CustomExceptions.OK, True
            elif cursor.value < value:
                next_cursor = cursor.right
                if not next_cursor:
                    cursor.right = TreeNode(value, None, None)
                    return CustomExceptions.OK, True
            else:
                return CustomExceptions.ALREADY_EXIST, True
            
            cursor = next_cursor
        else:
            self.root = TreeNode(value, None, None)
            return CustomExceptions.OK, True

    async def delete(self, value: Any) -> Union[str, bool]:
        """delete value from tree

        Args:
            value (Any): an value

        Returns:
            Union[str, bool]: err, is_ok
        """
        return CustomExceptions.OK, True

    async def traverse(self) -> Union[str, bool]:
        """traverse the tree

        Returns:
            Union[str, bool]: err, is_ok
        """
        return CustomExceptions.OK, True

    async def find_in_order_successor(self, value: Any) -> Union[str, Any]:
        """in-order successor: the closest value greater than current value

        Args:
            value (Any): an value

        Returns:
            Union[str, Any]: err, Any
        """
        return CustomExceptions.OK, True

    async def find_pre_order_successor(self, value: Any) -> Union[str, Any]:
        """pre-order successor: the closest value smaller than current value

        Args:
            value (Any): an value

        Returns:
            Union[str, Any]: err, Any
        """
        return CustomExceptions.OK, True
