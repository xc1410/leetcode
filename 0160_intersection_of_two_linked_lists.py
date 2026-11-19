import time


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        seen=set()
        node=headA
        while node !=None:
            seen.add(node)
            node=node.next

        node=headB
        while node!=None:
            if node in seen:
                return node
            else:
                node=node.next
        return None
        


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def attach(head: ListNode | None, tail_head: ListNode | None) -> ListNode | None:
    if head == None:
        return tail_head
    node = head
    while node.next != None:
        node = node.next
    node.next = tail_head
    return head


def run(a_values: list[int], b_values: list[int], common_values: list[int]) -> bool:
    common_head = build_list(common_values)
    head_a = attach(build_list(a_values), common_head)
    head_b = attach(build_list(b_values), common_head)
    result = Solution().getIntersectionNode(head_a, head_b)
    return result == common_head


assert run([4, 1], [5, 6, 1], [8, 4, 5]), "相交在 8"
assert run([1, 9, 1], [3], [2, 4]), "相交在 2"
assert run([2, 6, 4], [1, 5], []), "不相交，应该返回 None"
assert run([], [], [1, 2, 3]), "两条链表从头开始就是同一条"
assert run([1, 2, 3], [1, 2, 3], [4]), "前面的值一样但不是同一个结点，相交在 4"
assert run([], [7], []), "一条是空链表"
print("全部用例通过")

start = time.perf_counter()
ok = run(list(range(50_000)), list(range(30_000)), list(range(50_000)))
seconds = time.perf_counter() - start
assert ok, "大数据"
print(f"13 万个结点：{seconds} 秒")