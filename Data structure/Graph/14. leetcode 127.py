
# nice solution with explanation : https://takeuforward.org/graph/word-ladder-i-g-29/

# the problem solved using bfs using shortest path concept 

from typing import List
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Creating a queue of type {word, transitions to reach 'word'}.
        q = deque([(beginWord, 1)])

        # Push all values of wordList into a set to make deletion easier and in less time complexity.
        st = set(wordList)
        st.discard(beginWord)

        while q:
            word, steps = q.popleft()

            # We return the steps as soon as the first occurrence of endWord is found.
            if word == endWord:
                return steps

            for i in range(len(word)):
                # Now, replace each character of 'word' with char from a-z
                # then check if 'word' exists in wordList.
                original = word[i]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    word = word[:i] + ch + word[i+1:]
                    # Check if it exists in the set and push it in the queue.
                    if word in st:
                        st.remove(word)
                        q.append((word, steps + 1))
                word = word[:i] + original + word[i+1:]
        
        # If there is no transformation sequence possible
        return 0

# Example usage
if __name__ == "__main__":
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    startWord = "hit"
    targetWord = "cog"

    obj = Solution()
    ans = obj.ladderLength(startWord, targetWord, wordList)

    print(ans)  # This line is for testing the code locally and should be removed when submitting to LeetCode
