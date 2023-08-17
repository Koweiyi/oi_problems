package main

type TreeNode struct {
	// map 实现可以用 map[rune]*TreeNode
	children [26]*TreeNode

    score int 
    is_end bool
}

type Trie struct{
    root *TreeNode
}

func NewTrie() *Trie{
    node := &TreeNode{
        children: [26]*TreeNode{},
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
            cur.children[id] = &TreeNode{
                children: [26]*TreeNode{},
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

// LC2416 统计前缀得分板子
func (t *Trie) CountPrefix(word string) int {
    cur := t.root
    res := 0
    for _, ch := range word{
        id := ch - 'a'
        cur = cur.children[id]
        res += cur.score      
    }
    return res 
} 

// 判断是否存在前缀
func (t *Trie) StartWith(prefix string) bool{
	cur := t.root
	for _, ch := range prefix{
		id := ch - 'a'
		if cur.children[id] == nil{
			return false
		}
		cur = cur.children[id]
	}
	return true
}

