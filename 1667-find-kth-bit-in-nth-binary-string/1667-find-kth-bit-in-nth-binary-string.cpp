class Solution {
public:
    char findKthBit(int n, int k) {
        return sn(n)[k-1];
    }

    string sn(int n) {
        if (n == 1) return "0";
        else {
            string prev = sn(n-1);
            string flipped = "";
            for (int i = prev.size()-1; i >= 0; i--) {
                if (prev[i] == '1') flipped += '0';
                else                flipped += '1';
            }
            return prev + "1" + flipped;
        }
        return "";
    }
};