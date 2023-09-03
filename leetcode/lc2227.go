/*
* @lc app=leetcode.cn id=2227 lang=golang
* @lcpr version=21913
*
* [2227] 加密解密字符串
*
* https://leetcode.cn/problems/encrypt-and-decrypt-strings/description/
*
  - algorithms
  - Hard (39.65%)
  - Likes:    26
  - Dislikes: 0
  - Total Accepted:    5.7K
  - Total Submissions: 14.4K
  - Testcase Example:  '["Encrypter","encrypt","decrypt"]\n' +
    '[[["a","b","c","d"],["ei","zf","ei","am"],["abcd","acbd","adbc","badc","dacb","cadb","cbda","abad"]],["abcd"],["eizfeiam"]]'

*
* 给你一个字符数组 keys ，由若干 互不相同 的字符组成。还有一个字符串数组 values ，内含若干长度为 2 的字符串。另给你一个字符串数组
* dictionary ，包含解密后所有允许的原字符串。请你设计并实现一个支持加密及解密下标从 0 开始字符串的数据结构。
*
* 字符串 加密 按下述步骤进行：
*
*
* 对字符串中的每个字符 c ，先从 keys 中找出满足 keys[i] == c 的下标 i 。
* 在字符串中，用 values[i] 替换字符 c 。
*
*
* 字符串 解密 按下述步骤进行：
*
*
* 将字符串每相邻 2 个字符划分为一个子字符串，对于每个子字符串 s ，找出满足 values[i] == s 的一个下标 i 。如果存在多个有效的 i
* ，从中选择 任意 一个。这意味着一个字符串解密可能得到多个解密字符串。
* 在字符串中，用 keys[i] 替换 s 。
*
*
* 实现 Encrypter 类：
*
*
* Encrypter(char[] keys, String[] values, String[] dictionary) 用 keys、values 和
* dictionary 初始化 Encrypter 类。
* String encrypt(String word1) 按上述加密过程完成对 word1 的加密，并返回加密后的字符串。
* int decrypt(String word2) 统计并返回可以由 word2 解密得到且出现在 dictionary 中的字符串数目。
*
*
*
*
* 示例：
*
* 输入：
* ["Encrypter", "encrypt", "decrypt"]
* [[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc",
* "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]
* 输出：
* [null, "eizfeiam", 2]
*
* 解释：
* Encrypter encrypter = new Encrypter([['a', 'b', 'c', 'd'], ["ei", "zf",
* "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda",
* "abad"]);
* encrypter.encrypt("abcd"); // 返回 "eizfeiam"。
* // 'a' 映射为 "ei"，'b' 映射为 "zf"，'c' 映射为 "ei"，'d' 映射为 "am"。
* encrypter.decrypt("eizfeiam"); // return 2.
* ⁠                             // "ei" 可以映射为 'a' 或 'c'，"zf" 映射为 'b'，"am" 映射为
* 'd'。
* ⁠                             // 因此，解密后可以得到的字符串是 "abad"，"cbad"，"abcd" 和
* "cbcd"。
* ⁠                             // 其中 2 个字符串，"abad" 和 "abcd"，在 dictionary
* 中出现，所以答案是 2 。
*
*
*
*
* 提示：
*
*
* 1 <= keys.length == values.length <= 26
* values[i].length == 2
* 1 <= dictionary.length <= 100
* 1 <= dictionary[i].length <= 100
* 所有 keys[i] 和 dictionary[i] 互不相同
* 1 <= word1.length <= 2000
* 1 <= word2.length <= 200
* 所有 word1[i] 都出现在 keys 中
* word2.length 是偶数
* keys、values[i]、dictionary[i]、word1 和 word2 只含小写英文字母
* 至多调用 encrypt 和 decrypt 总计 200 次
*
*
*/
package leetcode

import "sort"

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
type ListNode struct {
    Val int
    Next *ListNode
}
// @lc code=start

type Node struct {
	// map 实现可以用 map[rune]*TreeNode
	children [26]*Node
    score int 
    is_end bool
}

type Trie struct{
    root *Node
}

func NewTrie() *Trie{
    node := &Node{
        children: [26]*Node{},
        score: 0,
        is_end: false,
    }
    return &Trie{node}
}

// 插入一个单词
func(t *Trie) Insert(word string){
    cur := t.root
    for _, ch := range word{
        id := ch - 'a'
        if cur.children[id] == nil{
            cur.children[id] = &Node{
                children: [26]*Node{},
                score: 0,
                is_end: false,
            }
        }
        cur = cur.children[id]
        cur.score ++ 
    }
    cur.is_end = true
}

// 判断单词是否存在
func(t *Trie) Search(word string) bool {
    cur := t.root
    for _, ch := range word{
        id := ch - 'a'
        if cur.children[id] == nil{
            return false
        } 
        cur = cur.children[id]
    }
    return cur.is_end
}



type Encrypter struct {
    t *Trie
    mp map[string][]byte
    mpp map[byte]string
}


func Constructor(keys []byte, values []string, dictionary []string) Encrypter {
    t := NewTrie()
    for _, d := range dictionary{
        t.Insert(d)
    }
    mp := map[string][]byte{}
    mpp := map[byte]string{}
    for i := 0 ; i < len(keys) ; i ++ {
        mpp[keys[i]] = values[i]
        mp[values[i]] = append(mp[values[i]], keys[i])
    }
    for _, v := range mp{
        sort.Slice(v, func(i, j int) bool {return v[i] < v[j]})
    }
    return Encrypter{t: t, mp: mp, mpp: mpp}
}


func (this *Encrypter) Encrypt(word1 string) string {
    res := ""
    for i := range word1{
        res += this.mpp[word1[i]]
    }
    return res 
}


func (this *Encrypter) Decrypt(word2 string) int {
    res := 0
    p := make([]byte, 0)
    var dfs func(i int, t *Node) 
    dfs = func (i int, t *Node)  {
        if i == len(word2){
            res ++
            return
        }
        var pre byte = '#'
        val, ok := this.mp[word2[i:i + 2]]
        if ok {
            for j := 0 ; j < len(val) ; j ++ {
                if val[j] == pre{continue}
                id := int(val[i] - 'a')
                if t.children[id] == nil{ continue }
                pre = val[j]
                p = append(p, val[j])
                dfs(i + 2, t.children[id])
                p = p[:len(p) - 1]
            }
        }
    }
    dfs(0, this.t.root)
    return res 
}


/**
 * Your Encrypter object will be instantiated and called as such:
 * obj := Constructor(keys, values, dictionary);
 * param_1 := obj.Encrypt(word1);
 * param_2 := obj.Decrypt(word2);
 */
// @lc code=end



/*
// @lcpr case=start
// ["Encrypter", "encrypt", "decrypt"][[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]],["abcd"], ["eizfeiam"]]\n
// @lcpr case=end

 */

