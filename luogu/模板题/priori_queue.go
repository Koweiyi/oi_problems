package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
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
type hp []pair

func(h hp) Len() int {return len(h)}
func(h hp) Less(i, j int) bool {return h[i].x < h[j].x || h[i].x == h[j].x && h[i].y < h[j].y}
func(h hp) Swap(i, j int) {h[i], h[j] = h[j], h[i]}
func(h *hp) Pop() any {a := *h; v := a[len(a) - 1] ; a = a[:len(a) - 1] ; *h = a; return v}
func(h *hp) Push(v any) {*h = append(*h, v.(pair))}