package main

import (
	"bufio"
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
	a := make([]int, n)
	for i := 0 ; i < n ; i ++{
		Fscan(in, &a[i]);
		a[i] -= i 
	}

	st := []int{}
	id := []int{} // 使用了那些下标 来组成最长上升子序列
	for i, x := range a{
		j := sort.SearchInts(a, x)
		if j == len(st){
			st = append(st, x)
			id = append(id, i)
		}else{

		}
	}
}

func main() { run(os.Stdin, os.Stdout)}