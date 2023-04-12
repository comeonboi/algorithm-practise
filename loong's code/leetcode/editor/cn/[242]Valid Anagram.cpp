/**
<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if</em> <code>t</code> <em>is an anagram of</em> <code>s</code><em>, and</em> <code>false</code> <em>otherwise</em>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<pre><strong>Input:</strong> s = "anagram", t = "nagaram"
<strong>Output:</strong> true
</pre>
<p><strong class="example">Example 2:</strong></p> 
<pre><strong>Input:</strong> s = "rat", t = "car"
<strong>Output:</strong> false
</pre> 
<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li> 
 <li><code>s</code> and <code>t</code> consist of lowercase English letters.</li> 
</ul>

<p>&nbsp;</p> 
<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>

<div><div>Related Topics</div><div><li>哈希表</li><li>字符串</li><li>排序</li></div></div><br><div><li>👍 759</li><li>👎 0</li></div>
*/
#include "main.h"
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        int count[26] = {0};
        for (int i = 0; i < s.length(); i++){
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++){
            if (count[i] != 0) return false;
        }
        return true;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
