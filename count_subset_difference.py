from count_subset_difference import subset_sum
def count_subset_difference(arr, diff):
    # Here in this we wanted to find a no of subsets whoes length difference is diff
    # Means Lets say we have a array arr whoes subsets are s1, s2 so, sum(s1)-sum(s2)=diff
    # To achive this we already know that ssum(s1) + sum(s2) = sum(arr) by equating both the equations we got the sum(s1) = diff+sum(arr)/2
    # and by putting same sum(s1) value we will get the sum(s2) whcih means its broken down into count subset sum problem

    s1_sum = (diff + sum(arr))/2
    return subset_sum(arr, s1_sum)