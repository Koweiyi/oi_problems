/*
 * @lc app=leetcode.cn id=2407 lang=golang
 * @lcpr version=21913
 *
 * [2407] 最长递增子序列 II
 *
 * https://leetcode.cn/problems/longest-increasing-subsequence-ii/description/
 *
 * algorithms
 * Hard (30.88%)
 * Likes:    67
 * Dislikes: 0
 * Total Accepted:    5.8K
 * Total Submissions: 18.7K
 * Testcase Example:  '[4,2,1,4,3,4,5,8,15]\n3'
 *
 * 给你一个整数数组 nums 和一个整数 k 。
 *
 * 找到 nums 中满足以下要求的最长子序列：
 *
 *
 * 子序列 严格递增
 * 子序列中相邻元素的差值 不超过 k 。
 *
 *
 * 请你返回满足上述要求的 最长子序列 的长度。
 *
 * 子序列 是从一个数组中删除部分元素后，剩余元素不改变顺序得到的数组。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [4,2,1,4,3,4,5,8,15], k = 3
 * 输出：5
 * 解释：
 * 满足要求的最长子序列是 [1,3,4,5,8] 。
 * 子序列长度为 5 ，所以我们返回 5 。
 * 注意子序列 [1,3,4,5,8,15] 不满足要求，因为 15 - 8 = 7 大于 3 。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [7,4,5,1,8,12,4,7], k = 5
 * 输出：4
 * 解释：
 * 满足要求的最长子序列是 [4,5,8,12] 。
 * 子序列长度为 4 ，所以我们返回 4 。
 *
 *
 * 示例 3：
 *
 * 输入：nums = [1,5], k = 1
 * 输出：1
 * 解释：
 * 满足要求的最长子序列是 [1] 。
 * 子序列长度为 1 ，所以我们返回 1 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i], k <= 10^5
 *
 *
 */
package leetcode

type TreeNode struct {
    Val int
    Right *TreeNode
    Left *TreeNode
}
// @lc code=start
type lazySeg []struct {
	l, r int
	todo int64
	min  int64
}

func (lazySeg) op(a, b int64) int64 {
	if a > b {
		return a 
	} 
	return b  // % mod
}

func (t lazySeg) maintain(o int) {
	lo, ro := t[o<<1], t[o<<1|1]
	t[o].min = t.op(lo.min, ro.min)
}

func (t lazySeg) build(a []int64, o, l, r int) {
	t[o].l, t[o].r = l, r
	if l == r {
		t[o].min = a[l-1]
		return
	}
	m := (l + r) >> 1
	t.build(a, o<<1, l, m)
	t.build(a, o<<1|1, m+1, r)
	t.maintain(o)
}

func (t lazySeg) do(o int, add int64) {
	to := &t[o]
	to.todo = add                     // % mod
	to.min = add                      // % mod
}

func (t lazySeg) spread(o int) {
	if add := t[o].todo; add != 0 {
		t.do(o<<1, add)
		t.do(o<<1|1, add)
		t[o].todo = 0
	}
}

// 如果维护的数据（或者判断条件）具有单调性，我们就可以在线段树上二分
// 下面代码返回 [l,r] 内第一个值不低于 val 的下标（未找到时返回 n+1）
// o=1  [l,r] 1<=l<=r<=n
// https://codeforces.com/problemset/problem/1179/C
func (t lazySeg) lowerBound(o, l, r int, val int64) int {
	if t[o].l == t[o].r {
		if t[o].min >= val {
			return t[o].l
		}
		return t[o].l + 1
	}
	t.spread(o)
	// 注意判断比较的对象是当前节点还是子节点，是先递归左子树还是右子树
	if t[o<<1].min >= val {
		return t.lowerBound(o<<1, l, r, val)
	}
	return t.lowerBound(o<<1|1, l, r, val)
}

// o=1  [l,r] 1<=l<=r<=n
func (t lazySeg) update(o, l, r int, add int64) {
	if l <= t[o].l && t[o].r <= r {
		t.do(o, add)
		return
	}
	t.spread(o)
	m := (t[o].l + t[o].r) >> 1
	if l <= m {
		t.update(o<<1, l, r, add)
	}
	if m < r {
		t.update(o<<1|1, l, r, add)
	}
	t.maintain(o)
}

// o=1  [l,r] 1<=l<=r<=n
func (t lazySeg) query(o, l, r int) int64 {
	if l <= t[o].l && t[o].r <= r {
		return t[o].min
	}
	t.spread(o)
	m := (t[o].l + t[o].r) >> 1
	if r <= m {
		return t.query(o<<1, l, r)
	}
	if m < l {
		return t.query(o<<1|1, l, r)
	}
	vl := t.query(o<<1, l, r)
	vr := t.query(o<<1|1, l, r)
	return t.op(vl, vr)
}

func (t lazySeg) queryAll() int64 { return t[1].min }

// a 从 0 开始
func newLazySegmentTree(a []int64) lazySeg {
	t := make(lazySeg, 4*len(a))
	t.build(a, 1, 1, len(a))
	return t
}

// EXTRA: 适用于需要提取所有元素值的场景
func (t lazySeg) spreadAll(o int) {
	if t[o].l == t[o].r {
		return
	}
	t.spread(o)
	t.spreadAll(o << 1)
	t.spreadAll(o<<1 | 1)
}


func lengthOfLIS(nums []int, k int) int {
	a := make([]int64, int(1e5+5))
	ls := newLazySegmentTree(a)
	res := 0
	for _, x := range nums{
		l, r := max(1, x - k), x - 1
		var ll int
		if l > r{
			ll = 0
		}else {
			ll = int(ls.query(1, max(1, x - k), x - 1))
		}
		res = max(res, int(ll + 1))
		ls.update(1,x,x,int64(ll + 1))
	}
	return res 
}

func max(a, b int) int { if a > b { return a} ;return b}
// @lc code=end



/*
// @lcpr case=start
// [4,2,1,4,3,4,5,8,15]\n3\n
// @lcpr case=end

// @lcpr case=start
// [7,4,5,1,8,12,4,7]\n5\n
// @lcpr case=end

// @lcpr case=start
// [1,5]\n1\n
// @lcpr case=end

 */

