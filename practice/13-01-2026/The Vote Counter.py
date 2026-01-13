def count_votes(votes_list):
    result = {}
    for name in votes_list:
        if name not in result:
            result[name] = 1
        else:
            result[name] += 1
    return result

votes = ["alice", "bob", "alice", "alice", "bob", "charlie"]
print(count_votes(votes))