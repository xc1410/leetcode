import time


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        node=head
        prev=None

        while node!=None:
            next_node=node.next
            node.next=prev
            prev=node
            node=next_node
        return prev


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def to_values(head: ListNode | None) -> list[int]:
    values = []
    while head != None:
        values.append(head.val)
        head = head.next
    return values


def run(values: list[int]) -> list[int]:
    return to_values(Solution().reverseList(build_list(values)))


assert run([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1], run([1, 2, 3, 4, 5])
assert run([1, 2]) == [2, 1], run([1, 2])
assert run([]) == [], run([])
assert run([7]) == [7], run([7])
assert run([3, 3, 1]) == [1, 3, 3], run([3, 3, 1])
print("全部用例通过")

big_values = list(range(100_000))
start = time.perf_counter()
result = run(big_values)
seconds = time.perf_counter() - start
assert result == big_values[::-1], result[:5]
print(f"10 万个结点：{seconds} 秒")