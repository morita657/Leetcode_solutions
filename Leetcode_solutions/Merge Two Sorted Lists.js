/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
  if (!l1 || !l2) {
    return l1 || l2;
  }
  if (l1.val > l2.val) {
    let crr = l2;
    l2 = l1;
    l1 = crr;
  }
  l1.next = mergeTwoLists(l1.next, l2);

  return l1;
};