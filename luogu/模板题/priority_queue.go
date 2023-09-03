package main

import (
	"bufio"
	"container/heap"
	. "fmt"
	"io"
	"os"
	"sort"
)



func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	var n int 
	Fscan(in, &n)
	
}

func main() { run(os.Stdin, os.Stdout)}

type pair struct{x, y int}
type hpp []pair

func(h hpp) Len() int 			{ return len(h)}
func(h hpp) Less(i, j int) bool { return h[i].x < h[j].x || h[i].x == h[j].x && h[i].y < h[j].y}
func(h hpp) Swap(i, j int) 		{ h[i], h[j] = h[j], h[i]}
func(h hpp) top() pair			{ return h[0] }
func(h *hpp) Pop() any 			{ a := *h; v := a[len(a) - 1] ; a = a[:len(a) - 1] ; *h = a; return v}
func(h *hpp) Push(v any) 		{ *h = append(*h, v.(pair))}
func(h *hpp) push(v pair) 		{ heap.Push(h, v)}
func(h *hpp) pop() int			{ return heap.Pop(h).(int)}


type hp struct{ sort.IntSlice }

//func (h hp) Less(i, j int) bool { return h.IntSlice[i] > h.IntSlice[j] } // 加上这行变成最大堆
func (h hp)  Len() int   { return len(h.IntSlice) }
func (h hp)  top() int   { return h.IntSlice[0] }
func (h *hp) Push(v any) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() any   { a := h.IntSlice; v := a[len(a)-1]; h.IntSlice = a[:len(a)-1]; return v }
func (h *hp) push(v int) { heap.Push(h, v) }
func (h *hp) pop() int   { return heap.Pop(h).(int) } // 稍微封装一下，方便使用

// EXTRA: 参考 Python，引入下面两个效率更高的方法（相比调用 push + pop）
// replace 弹出并返回堆顶，同时将 v 入堆
// 需保证 h 非空
func (h *hp) replace(v int) int {
	top := h.IntSlice[0]
	h.IntSlice[0] = v
	heap.Fix(h, 0)
	return top
}

// pushPop 将 v 入堆，然后弹出并返回堆顶
func (h *hp) pushPop(v int) int {
	if h.Len() > 0 && v > h.IntSlice[0] { // 最大堆改成 v < h.IntSlice[0]
		v, h.IntSlice[0] = h.IntSlice[0], v
		heap.Fix(h, 0)
	}
	return v
}

// 自定义类型（int64 可以替换成其余类型）
type hp64 []int64

func (h hp64) Len() int           { return len(h) }
func (h hp64) Less(i, j int) bool { return h[i] < h[j] } // > 为最大堆
func (h hp64) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h hp64) top() int64         { return h[0] }
func (h *hp64) Push(v any)        { *h = append(*h, v.(int64)) }
func (h *hp64) Pop() any          { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }
func (h *hp64) push(v int64)      { heap.Push(h, v) }
func (h *hp64) pop() int64        { return heap.Pop(h).(int64) } // 稍微封装一下，方便使用