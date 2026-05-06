class Twitter:

    def __init__(self):
        from collections import defaultdict, deque
        self.followingList = defaultdict(set)
        self.userTweet = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        import time
        self.userTweet[userId].append((-time.time(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # fetch all following (which includes himself)
        self.followingList[userId].add(userId)
        following = self.followingList[userId]
        total, res = [], []
        for f in following:
            total.extend(self.userTweet[f])
        heapq.heapify(total) # min heap
        while total:
            if len(res) == 10:
                return res
            res.append(heapq.heappop(total)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingList[followerId]:
            self.followingList[followerId].remove(followeeId)
