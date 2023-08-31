package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func threeSum(nums []int) (res [][]int) {
    sort.Ints(nums)
    for i := 0 ; i < len(nums) - 2 ; {
        j, k := i + 1, len(nums) - 1
        for j < k {
            s := nums[i] + nums[j] + nums[k]
            if s == 0{
                res = append(res, []int{nums[i], nums[j], nums[k]})
                for j ++ ; j < len(nums) && nums[j] == nums[j - 1] ; j ++ {}
                for k -- ; k > i && nums[k] == nums[k + 1] ; k -- {}
            }else if s > 0{
                k --
            }else{
                j ++
            }
        }
        for i ++ ; i < len(nums) - 2 && nums[i] == nums[i - 1] ; i ++{}
    }
    return 
}
func run(_r io.Reader, _w io.Writer) {
	in := bufio.NewReader(_r)
	out := bufio.NewWriter(_w)
	defer out.Flush()
	Fprintln(out,x,y,z,k,p)
	
}

func main() { run(os.Stdin, os.Stdout)}