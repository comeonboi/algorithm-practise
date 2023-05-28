/**
<p>Given the <code>root</code> of a binary search tree (BST) with duplicates, return <em>all the <a href="https://en.wikipedia.org/wiki/Mode_(statistics)" target="_blank">mode(s)</a> (i.e., the most frequently occurred element) in it</em>.</p>

<p>If the tree has more than one mode, return them in <strong>any order</strong>.</p>

<p>Assume a BST is defined as follows:</p>

<ul> 
 <li>The left subtree of a node contains only nodes with keys <strong>less than or equal to</strong> the node's key.</li> 
 <li>The right subtree of a node contains only nodes with keys <strong>greater than or equal to</strong> the node's key.</li> 
 <li>Both the left and right subtrees must also be binary search trees.</li> 
</ul>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg" style="width: 142px; height: 222px;" /> 
<pre>
<strong>Input:</strong> root = [1,null,2,2]
<strong>Output:</strong> [2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li> 
 <li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li> 
</ul>

<p>&nbsp;</p> 
<strong>Follow up:</strong> Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>二叉搜索树</li><li>二叉树</li></div></div><br><div><li>👍 641</li><li>👎 0</li></div>
*/
#include "main.h"
//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    int count;
    int maxCount;
    TreeNode * pre;
    vector<int> result;
    void searchBST(TreeNode* cur){
        if (cur == NULL) return;
        searchBST(cur->left);
        if (pre == NULL){
            count = 1;
        }
        else if (pre->val == cur->val){
            count ++;
        }else {
            count = 1;
        }
        // update the last node
        pre = cur;
        if (count == maxCount){
            result.push_back(cur->val);
        }
        if (count > maxCount){
            maxCount = count;
            result.clear();
            result.push_back(cur->val);
        }
        searchBST(cur->right);
        return ;
     }
public:

    vector<int> findMode(TreeNode* root) {
//        int count = 0;
//        int maxCount = 0;
//        TreeNode* pre = NULL;
        result.clear();
        searchBST(root);
        return result;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
