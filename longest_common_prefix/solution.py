class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return max([strs[0][:i] for i in range(len(min(strs, key=len))+1) if all([s[:i] == strs[0][:i] for s in strs[1:]])]+[""], key=len) if len(strs) > 0 else ""