import time


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        seen=set()
        node=head
        while node!=None:
            seen.add(node)
            node=node.next
            if node in seen:
                return True
        return False


def build_cycle_list(values: list[int], pos: int) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    nodes = []
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
        nodes.append(tail)
    if pos != -1:
        tail.next = nodes[pos]
    return dummy.next


def run(values: list[int], pos: int) -> bool:
    return Solution().hasCycle(build_cycle_list(values, pos))


assert run([3, 2, 0, -4], 1) == True, "尾巴连回第 1 个结点，有环"
assert run([1, 2], 0) == True, "尾巴连回头，有环"
assert run([1], -1) == False, "一个结点，没环"
assert run([], -1) == False, "空链表"
assert run([1], 0) == True, "一个结点自己指向自己"
assert run([1, 1, 1], -1) == False, "值一样但没环"
print("全部用例通过")

start = time.perf_counter()
ok = run(list(range(100_000)), 50_000)
seconds = time.perf_counter() - start
assert ok == True, "大数据"
print(f"10 万个结点：{seconds} 秒")