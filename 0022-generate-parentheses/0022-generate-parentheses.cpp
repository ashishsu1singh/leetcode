class Solution {
public:
    void solve(string current, int n, int open, int close,
               vector<string>& ans) {

        if (current.length() == 2 * n) {
            ans.push_back(current);
            return;
        }

        // Add '('
        if (open < n) {
            solve(current + '(', n, open + 1, close, ans);
        }

        // Add ')'
        if (close < open) {
            solve(current + ')', n, open, close + 1, ans);
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> ans;

        solve("", n, 0, 0, ans);

        return ans;
    }
};