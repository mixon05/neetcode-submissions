from functools import partial

class Twitter:
    def __init__(self):
        self.followers_set = defaultdict(set)
        self.user_tweets = defaultdict(partial(deque, maxlen=10))
        self.tweet_inc = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followers_set[userId].add(userId)
        self.user_tweets[userId].append((self.tweet_inc, tweetId))
        self.tweet_inc += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for followee_id in self.followers_set[userId]:
            if not self.user_tweets[followee_id]:
                continue
            last_tweet_idx = len(self.user_tweets[followee_id]) - 1
            heapq.heappush_max(heap, (*self.user_tweets[followee_id][-1], followee_id, last_tweet_idx))
        feed = []
        for _ in range(10):
            if not heap:
                return feed
            _, tweet_id, user_id, last_tweet_idx = heapq.heappop_max(heap)
            feed.append(tweet_id)
            if last_tweet_idx:
                tweet_idx = last_tweet_idx - 1 
                heapq.heappush_max(heap, (*self.user_tweets[user_id][tweet_idx], user_id, tweet_idx))
        return feed
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers_set[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers_set[followerId] and followerId != followeeId:
            self.followers_set[followerId].remove(followeeId)

