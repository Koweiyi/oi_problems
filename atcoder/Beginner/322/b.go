package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"strings"
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
	rs := func () (x string) {
		in.Scan()
		x = in.Text()
		return
	}
	a, b := read(), read()
	_ = []interface{}{read, rs, a, b, Fprintf, Fscan}

	s, t := rs(), rs()
	isPre := strings.HasPrefix(t, s)
	isSuf := strings.HasSuffix(t, s)
	Fprintln(out, 2 * btoi(!isPre) + btoi(!isSuf))
}
func main() { run(os.Stdin, os.Stdout)}
func btoi(b bool) int{if b{return 1};return 0}
	