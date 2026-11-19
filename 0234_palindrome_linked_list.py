import time


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow=fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        if fast!=None:
            slow=slow.next

        node=slow
        prev=None
        while node!=None:
            node_next=node.next
            node.next=prev
            prev=node
            node=node_next
        left=head
        right=prev
        while left!=None and right!=None:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True

        


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def run(values: list[int]) -> bool:
    return Solution().isPalindrome(build_list(values))


assert run([1, 2, 2, 1]) == True, "偶数个，是回文"
assert run([1, 2]) == False, "两个不一样"
assert run([1]) == True, "只有一个结点"
assert run([1, 2, 3, 2, 1]) == True, "奇数个，是回文"
assert run([1, 2, 3, 1]) == False, "头尾一样，中间不一样"
assert run([1, 1, 2, 1]) == False, "前一半像回文，后一半不是"
print("全部用例通过")

half = list(range(50_000))
start = time.perf_counter()
ok = run(half + half[::-1])
seconds = time.perf_counter() - start
assert ok == True, "大数据"
print(f"10 万个结点：{seconds} 秒")