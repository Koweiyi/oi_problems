package main
import (
	"bufio"
	. "fmt"
	"io"
	"os"
)
func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewScanner(_r)
	in.Split(bufio.ScanWords)
	out := bufio.NewWriter(_w)
	defer func(out *bufio.Writer) {
		_ = out.Flush()
	}(out)
	read := func() (x int) {
		in.Scan()
		tmp := in.Bytes()
		if tmp[0] == '-' {
			for _, b := range tmp[1:] {
				x = x*10 + int(b&15)
			}
			return -x
		} else {
			for _, b := range in.Bytes() {
				x = x*10 + int(b&15)
			}
		}
		return
	}
	_ = []interface{}{read, Fprintf, Fscan}
	
}
func main() { run(os.Stdin, os.Stdout)}


type lazySeg []struct {
	l, r int
	todo int64
	min  int64
}
func (lazySeg) op(a, b int64) int64 {
	if a < b {
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
	to.todo += add                     // % mod
	to.min += add                      // % mod
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