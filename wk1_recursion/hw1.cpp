class Solution {
public:
    // Leetcode 21 Merge Two sorted List
    /**
     * Definition for singly-linked list.
     * struct ListNode {
     *     int val;
     *     ListNode *next;
     *     ListNode() : val(0), next(nullptr) {}
     *     ListNode(int x) : val(x), next(nullptr) {}
     *     ListNode(int x, ListNode *next) : val(x), next(next) {}
     * };
     */
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == nullptr || list2 == nullptr)
            return list1 == nullptr ? list2 : list1;
        if(list1 -> val < list2 -> val)
        {
            list1 -> next = mergeTwoLists(list1 -> next, list2);
            return list1;            
        }
        else
        {
            list2 -> next = mergeTwoLists(list1, list2 -> next);
            return list2;
        }
    }

    // Leetcode 231 Power of Two
    bool isPowerOfTwo(int n) {
        if (n <= 2)
            return n > 0 ? true: false;
        else
        {
            if (n % 2 != 0)
                return false;
            else
                return isPowerOfTwo( n / 2);
        }
    }
    // Leetcode 203 Remove Linked List Elements
    /**
     * Definition for singly-linked list.
     * struct ListNode {
     *     int val;
     *     ListNode *next;
     *     ListNode() : val(0), next(nullptr) {}
     *     ListNode(int x) : val(x), next(nullptr) {}
     *     ListNode(int x, ListNode *next) : val(x), next(next) {}
     * };
    */
    ListNode* removeElements(ListNode* head, int val) {
        if(head == nullptr)
            return head;
        ListNode tmp = ListNode(0);
        tmp.next = head;
        ListNode* current = &tmp;
        while(current->next != nullptr)
        {
            if(current->next->val == val)
            {
                current->next = current->next->next;
            }
            else
            {
                current = current->next;
            }
        }
        return tmp.next;


        // if (head == null) return null;
        // head.next = removeElements(head.next, val);
        // return head.val == val ? head.next : head;
        if(head == nullptr)
            return head;
        if(head->val == val)
            return removeElements(head->next, val);
        else
        {
            head->next = removeElements(head->next, val);
            return head;
        }
    }
    // Leetcode 794 Valid Tic-Tac-Toe State
    bool isWin(vector<string>& board, char player)
    {
        for(int i = 0; i < 3; ++i)
        {
            if(board[i][0] == player && board[i][1] == player && board[i][2] == player)
                return true;
        }
        for(int i = 0; i < 3; ++i)
        {
            if(board[0][i] == player && board[1][i] == player && board[2][i] == player)
                return true;
        }
        if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
            return true;
        if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
            return true;
        return false;
    }

    bool validTicTacToe(vector<string>& board) {
        int n = int(board.size());
        int count_x = 0, count_o = 0;
        for(auto row:board)
        {
            for(auto c:row)
            {
                if(c == 'X')
                    ++count_x;
                else if(c == 'O')
                    ++count_o;
            }
        }
        if(count_o > count_x || count_x - count_o > 1) 
            return false;
        bool is_x_win = isWin(board, 'X');
        bool is_o_win = isWin(board, 'O');
        if(is_x_win && is_o_win) return false;
        if(is_x_win && (count_x - count_o) != 1) return false;
        if(is_o_win && (count_x != count_o)) return false;
        return true;
    }

};
