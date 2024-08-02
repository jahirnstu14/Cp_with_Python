# nice explanation : https://takeuforward.org/Greedy/jump-game-i

                            
def can_jump(nums):
    # Initialize the maximum
    # index that can be reached
    max_index = 0

    # Iterate through each
    # index of the array
    for i in range(len(nums)):
        # If the current index is greater
        # than the maximum reachable index
        # it means we cannot move forward
        # and should return false
        if i > max_index:
            return False

        # Update the maximum index
        # that can be reached by comparing
        # the current max_index with the sum of
        # the current index and the
        # maximum jump from that index
        max_index = max(max_index, i + nums[i])

    # If we complete the loop,
    # it means we can reach the
    # last index
    return True


def main():
    nums = [4, 3, 7, 1, 2]

    print("Array representing maximum jump from each index: ", end="")
    for i in range(len(nums)):
        print(nums[i], end=" ")
    print()

    ans = can_jump(nums)

    if ans:
        print("It is possible to reach the last index.")
    else:
        print("It is not possible to reach the last index.")


if __name__ == "__main__":
    main()
                           
                        