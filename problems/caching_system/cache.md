# Design a Caching System

## Clarifying Questions
1. Is the cache going to store key value pairs? Example Ans: Yes
2. Is the cache going to have a set capacity? Example Ans: Yes
3. What caching mechanism are we going to be using? Example Ans: LRU
4. We should be able to get from cache and put into cache right? Ans: Yes
5. If element we're trying to get from cache is not there in the cache, what do we do? Ans: Return -1

## Requirements for Design

 - A Node class to define Double Linked List
 - An Cache class that handles all the mechanisms of the cache
 - The Cache class should be able to **get** from cache and **put** into cache with additional helper functions