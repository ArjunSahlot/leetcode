// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        for (auto i = n; i > 0; i--) if (!isBadVersion(i)) return i+1;
        return 1;
    }
};