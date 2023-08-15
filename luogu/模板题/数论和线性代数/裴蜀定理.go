package main

import (
	"bufio"
	. "fmt"
	"os"
)

func main(){
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	Fscan(in, &n)
	res := 0 
	for i := 0 ; i < n ; i ++ {
		var v int 
		Fscan(in, &v)
		res = gcd(v, res)
	}
	Fprintln(out, abs(res))
}
func abs(a int) int {if a < 0 {return -a}; return a}

func gcd(a, b int) int {
	if b == 0{
		return a 
	}
	return gcd(b, a % b)
}