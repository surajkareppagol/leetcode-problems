# 🧩 20\. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

```txt
Example 1:

Input: s = "()"

Output: true
```

```txt
Example 2:

Input: s = "()[]{}"

Output: true
```

```txt
Example 3:

Input: s = "(]"

Output: false
```

```txt
Example 4:

Input: s = "([])"

Output: true
```

```txt
Constraints:

- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.
```
