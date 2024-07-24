def solution(N):
    base_letters = 'abcdefghijklmnopqrstuvwxyz'
    k = min(26, N)  # Number of distinct letters to use
    repeat_count = N // k  # How many times each letter should appear
    extra_count = N % k  # Extra letters to account for if N is not perfectly divisible by k

    # Create the result string
    result = []
    
    # Add letters that repeat `repeat_count` times
    for letter in base_letters[:k]:
        result.append(letter * repeat_count)
    
    # Add extra letters if there are any
    result = ''.join(result) + ''.join(base_letters[:extra_count])
    
    return result[:N]

