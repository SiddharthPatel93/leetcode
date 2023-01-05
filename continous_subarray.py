def checkSubarraySum( nums, k):
        for i in range(0, len(nums)):
            sum = nums[i]
            for j in range(i+1, len(nums)):
                sum+=nums[j]
                if sum % k == 0: 
                    return bool(True);
                else: 
                    continue;
        return bool(False);
            
#print(checkSubarraySum([23,2,6,4,7],13));
#s is the sequence of words
#words is an array of words

def numMatchingSubseq(s,words):
    count=0;
    for subword in words: #each word in array
        for i in range(0,len(subword)): # each charcter in each word
            for j in range(i,len(s)):
                if subword[i] == s[j]:
                    break;
                else:
                    continue;
        count+=1;
    return count;

#print(numMatchingSubseq("abcde",["a","bb","acd","ace"]));

def performOperations(arr,operations):
    for operation in operations:
        index1= operation[0];
        index2= operation[1];
        #reverseorder(arr,index1,index2);
    for element in arr:
        print(element);

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    def addTwoNumbers(self, l1, l2):
        if l1 == None and l2 == None:
            return None;
        else:
            rnode= ListNode();
            if l1 == None:
                l1=ListNode(val=0,next=None);
                v1=0;
            else:
                v1=l1.val;
            if l2 == None:
                l2=ListNode(val=0,next=None);
                v2=0;
            else:
                v2=l2.val;
            v3=v1+v2;
            if v3 >=10:
                rem = v3%10;
                print(rem);
                rnode.val=rem;
                if l1.next != None:
                    l1.next.val=l1.next.val+1;
                    rnode.next=self.addTwoNumbers(l1.next,l2.next);
                elif l1.next == None and l2.next != None:
                    l2.next.val=l2.next.val+1;
                    rnode.next=self.addTwoNumbers(l1.next,l2.next);

                else:
                    rnode.next=ListNode(val=1,next=None);
                    print(1);   
            else:
                print(v3);
                rnode.val = v3;
                if l1.next != None or l2.next!=None:
                    rnode.next= self.addTwoNumbers(l1.next,l2.next);
            while rnode!=None:
                renode=rnode;
                rnode=rnode.next;
                return renode;
                    
        
l7= ListNode(val=9,next=None);
l6 = ListNode(val=9,next=l7);
l5 = ListNode(val=9,next=l6);
l4 = ListNode(val=9,next=l5);
l3 = ListNode(val=9,next=l4);
l2 = ListNode(val=9,next=l3);
l1 = ListNode(val=9,next=l2);


n4 = ListNode(val=9,next=None);
n3 = ListNode(val=9,next=n4);
n2 = ListNode(val=9,next=n3);
n1 = ListNode(val=9,next=n2);

t3 = ListNode(val=4,next=None);
t2 = ListNode(val=6,next=t3);
t1 = ListNode(val=5,next=t2);

r3 = ListNode(val=3,next=None);
r2 = ListNode(val=4,next=r3);
r1 = ListNode(val=2,next=r2);


newnode=t1.addTwoNumbers(t1,r1);

