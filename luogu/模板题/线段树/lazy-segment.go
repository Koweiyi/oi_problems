package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

// 10 ~ 125 为动态区间更新 和查询的带lazy-tag 线段树模板
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

func run(_r io.Reader, _w io.Writer) {
	const eof = 0
	out := bufio.NewWriter(_w)
	defer out.Flush()
	_i, _n, buf := 0, 0, make([]byte, 1<<12) // 4KB

	rc := func() byte {
		if _i == _n {
			_n, _ = _r.Read(buf)
			if _n == 0 { // EOF
				return eof
			}
			_i = 0
		}
		b := buf[_i]
		_i++
		return b
	}
	// 读一个非负整数
	rint := func() (x int) {
		b := rc()
		for ; '0' > b || b > '9'; b = rc() {
			// 某些多组数据的题目，不告诉有多少组数据，那么需要额外判断是否读到了 EOF
			if b == eof {
				return
			}
		}
		for ; '0' <= b && b <= '9'; b = rc() {
			x = x*10 + int(b&15)
		}
		return
	}
	M, N, Q := rint(), rint(), rint()
	rc()
	a := make([]int64, M - 1)
	for i := range a{
		a[i] = int64(N)
	}
	t := newLazySegmentTree(a)
	type pair struct{x, y int}
	mp := make(map[pair]int64)

	for i := 0 ; i < Q ; i ++ {
		op := rc()
		if op == 'Q'{
			x, y := rint(), rint()
			rc()
			Fprintln(out, t.query(1,x + 1, y))
		}else if op == 'B'{
			x, y, c := rint(), rint(), int64(rint())
			rc()
			if t.query(1,x + 1,y) >= c{
				Fprintln(out, "OK!")
				t.update(1,x + 1, y, -c)
				mp[pair{x,y}] += c
			}else{
				Fprintln(out, "Fail!")
			}
		}else{
			x, y, c := rint(), rint(), int64(rint())
			rc()
			if k, ok := mp[pair{x, y}]; ok && k >= c{
				Fprintf(out, "OK!")
				mp[pair{x,y}] -= c
				t.update(1, x + 1, y, c)
			}else{
				Fprintln(out, "Fail!")
			}
		}
	}	
}
func main() { run(os.Stdin, os.Stdout)}

/**
测试数据 :第一行M，N, Q 
M: 表示区间个数加一 ==> 区间中端点个数 
N: 表示每个区间中初始的值
Q: Q个询问 2...Q + 1 行输入Q个询问
Q a b   表示询问(a ,b]最小值  
B a b c 如果(a, b] 区间内最小值 >= c 更新(a, b]区间 ==> 减去c
R a b c 如果(a, b] 初始值 - 区间内最大值 >= c 更新(a, b]区间 ==> 加上c

5 5 10
Q 0 4
B 0 2 3
B 3 4 2
Q 2 3
B 1 4 3
B 1 4 2
Q 0 4
R 0 3 1
R 1 4 5
Q 2 4 

*/