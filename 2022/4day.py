with open('4inp.txt') as f:
    lines = f.readlines()

total = 0
for idx, line in enumerate(lines):
    x = line.strip("\n")
    x = line.split(",")
    first = x[0]
    # if idx != len(lines) - 1:
    #     second = x[1][:-1]
    # else:
    second = x[1]

    nums1 = first.split("-")
    nums2 = second.split("-")
    nums1[0] = int(nums1[0])
    nums1[1] = int(nums1[1])
    nums2[0] = int(nums2[0])
    nums2[1] = int(nums2[1])
    if nums1[0] <= nums2[0] and nums1[1] >= nums2[1]:
        total += 1
    elif nums2[0] <= nums1[0] and nums2[1] >= nums1[1]:
        total += 1
print(f"Part One: {total}")

# Part Two
# How many overlap at all 
count = 0
for idx, line in enumerate(lines):
    x = line.split(",")
    first = x[0]
    if idx != len(lines) - 1:
        second = x[1][:-1]
    else:
        second = x[1]

    nums1 = first.split("-")
    nums2 = second.split("-")
    nums1[0] = int(nums1[0])
    nums1[1] = int(nums1[1])
    nums2[0] = int(nums2[0])
    nums2[1] = int(nums2[1])
    if nums1[0] <= nums2[0] and nums1[1] >= nums2[0]:
        count += 1 
    elif nums2[0] <= nums1[0] and nums2[1] >= nums1[0]:
        count += 1
print(f"Part Two: {count}")

