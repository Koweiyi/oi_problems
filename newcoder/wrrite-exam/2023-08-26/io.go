package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func threeSum(nums []int) (res [][]int) {
	used := map[int]bool{}
	sort.Ints(nums)
	for i := 0; i < len(nums)-2; {
		if used[i]{
			i ++ 
			continue
		}
		j, k := i+1, len(nums)-1
		for j < k {
			if used[j]{
				j ++ 
				continue
			}
			if used[k]{
				k -- 
				continue
			}
			s := nums[i] + nums[j] + nums[k]
			if s == 0 {
				res = append(res, []int{nums[i], nums[j], nums[k]})
				used[i] = true
				used[j] = true
				used[k] = true
				j ++ 
				k --
			} else if s > 0 {
				k--
			} else {
				j++
			}
		}
		i++ 
	}
	return
}
func main() {
	scanner := bufio.NewScanner(os.Stdin)
	numbers := []int{}
	scanner.Scan()
	input := scanner.Text()
	nums := strings.Split(input, " ")
	for _, x := range nums {
		num, _ := strconv.Atoi(x)
		numbers = append(numbers, num)
	}
	res := threeSum(numbers)
	fmt.Fprintln(os.Stdout, res)
}
