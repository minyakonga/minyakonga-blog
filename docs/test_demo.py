import pytest
from demo import BinarySearchTree, CustomExceptions


class TestBinarySearchTree:
    @pytest.mark.asyncio
    async def test_insert_into_binary_search_tree(self) -> None:
        """test insert elements into bst
        """
        numbers = (7, 1, 14, 3, 6, 8, 10, 4, 13)
        self.bst = BinarySearchTree()

        for number in numbers:
            err, is_ok = await self.bst.insert(number)
            assert err == CustomExceptions.OK
            assert is_ok == True
