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
	
	n := read()
	g := make([][]int, n)
	for i := range g{
		g[i] = make([]int, n)
		for j := range g[i]{
			g[i][j] = read()
		}
	}
	vis := make([][]bool, n)
	for i := range(vis){
		vis[i] = make([]bool, n)
	}
	d := [4][2]int{{1,0},{0,1},{0,-1},{-1,0}}

	var fill func(x, y int) 
	fill = func(x, y int) {
		g[x][y] = 2
		for k := 0 ; k < 4 ; k ++ {
			nx, ny := x + d[k][0], y + d[k][1]
			if g[nx][ny] == 0{
				fill(nx, ny)
			}
		}
	}

	var dfs func(x, y int) bool 
	dfs = func(x, y int) bool {
		vis[x][y] = true 
		res := false 
		for i := 0 ; i < 4 ; i ++ {
			nx, ny := x + d[i][0], y + d[i][1]
			if nx < 0 || ny < 0 || nx >= n || ny >= n {
				res = true
				continue
			}
			if !vis[nx][ny] && g[nx][ny] == 0{
				res = dfs(nx, ny) || res 
			}
		} 
		return res 
	}

	for i := 0 ; i < n ; i ++ {
		for j := 0 ; j < n ; j ++ {
			if g[i][j] == 0 && !vis[i][j]{
				if !dfs(i, j){
					fill(i, j)
				}
			}
		} 
	}
	//  输出答案 
	for i := range g{
		for j := range g[i]{
			Print(g[i][j], " ")
		}
		Println()
	}
}
func main() { run(os.Stdin, os.Stdout)}
	