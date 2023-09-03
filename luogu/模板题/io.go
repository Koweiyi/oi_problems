package main

import (
	"bufio"
	"bytes"
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


func lineIO() {
	in := bufio.NewScanner(os.Stdin)
	in.Buffer(nil, 1e9) // 若单个 token 大小超过 65536 则加上这行
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	for in.Scan() {
		line := in.Bytes()
		sp := bytes.Split(line, []byte{' '})
		// ...

		_ = sp
	}
}
func main() { run(os.Stdin, os.Stdout)}

