## Problem: 
Design a service like TinyURL, a URL shortening service, a web service that provides short aliases for redirection of long URLs.

## Solution: 
If you don't know about TinyURL, just check it. Basically we need a one to one mapping to get shorten URL which can retrieve original URL later. This will involve saving such data into database.
We should check the following things:

### Clarify before solving
What's the traffic volume / length of the shortened URL?
What's the mapping function?
Single machine or multiple machines?

## Traffic: 
Let's assume we want to serve more than 1000 billion URLs. If we can use 62 characters [A-Z, a-z, 0-9] for the short URLs having length n, then we can have total 62^n URLs. So, we should keep our URLs as short as possible given that it should fulfill the requirement. For our requirement, we should use n=7 i.e the length of short URLs will be 7 and we can serve 62^7 ~= 3500 billion URLs.

## Basic solution:
To make things easier, we can assume the alias is something like http://tinyurl.com/<alias_hash> and alias_hash is a fixed length string.
To begin with, let’s store all the mappings in a single database. A straightforward approach is using alias_hash as the ID of each mapping, which can be generated as a random string of length 7.

Therefore, we can first just store <ID, URL>. When a user inputs a long URL “http://www.google.com”, the system creates a random 7-character string like “abcd123” as ID and inserts entry <“abcd123”, “http://www.google.com”> into the database.

In the run time, when someone visits http://tinyurl.com/abcd123, we look up by ID “abcd123” and redirect to the corresponding URL “http://www.google.com”.

### Problem with this solution:
We can't generate unique hash values for the given long URL. In hashing, there may be collisions (2 long urls map to same short url) and we need a unique short url for every long url so that we can access long url back but hash is one way function.

## Better Solution:

One of the most simple but also effective one, is to have a database table set up this way:

Table Tiny_Url(
ID : int PRIMARY_KEY AUTO_INC,
Original_url : varchar,
Short_url : varchar
)
Base10: Auto_Inc -> Base62: short_url
Then the auto-incremental primary key ID is used to do the conversion: (ID, 10) <==> (short_url, BASE). Whenever you insert a new original_url, the query can return the new inserted ID, and use it to derive the short_url, save this short_url and send it to cilent.

**Con** : we can not assure that this will be 1:1 mapping. It will be 1 long: N short mapping.
However, this is a **trade off**.  If we want to use hash solution, we need a key-value store, which is also very expensive.

Code for methods (that are used to convert ID to short_url and short_url to ID):

```
string idToShortURL(long int n)
{
    // Map to store 62 possible characters
    char map[] = "abcdefghijklmnopqrstuvwxyzABCDEF"
                 "GHIJKLMNOPQRSTUVWXYZ0123456789";
  
    string shorturl;
  
    // Convert given integer id to a base 62 number
    while (n)
    {
        shorturl.push_back(map[n%62]);
        n = n/62;
    }
  
    // Reverse shortURL to complete base conversion
    reverse(shorturl.begin(), shorturl.end());
  
    return shorturl;
}
```

```
// Function to get integer ID back from a short url
long int shortURLtoID(string shortURL)
{
    long int id = 0; // initialize result
  
    // A simple base conversion logic
    for (int i=0; i < shortURL.length(); i++)
    {
        if ('a' <= shortURL[i] && shortURL[i] <= 'z')
          id = id*62 + shortURL[i] - 'a';
        if ('A' <= shortURL[i] && shortURL[i] <= 'Z')
          id = id*62 + shortURL[i] - 'A' + 26;
        if ('0' <= shortURL[i] && shortURL[i] <= '9')
          id = id*62 + shortURL[i] - '0' + 52;
    }
    return id;
}
```

## Multiple machines:

### Easy approach
Let's say we have two machines, one always give odd auto_inc, one alawys give even auto_inc.
Similiarly, if we have 100 machines, each of them can hand out XXX01, XXX02, XXX03.. etc.

### A more mature approach
If we are dealing with massive data of our service, distributed storage can increase our capacity. The idea is simple, get a hash code from original URL and go to corresponding machine then use the same process as a single machine. For routing to the correct node in cluster, **Consistent Hashing** is commonly used.

Following is the pseudo code for example,
1. Get shortened URL
2. hash original URL string to 2 digits as hashed value hash_val
3. use hash_val to locate machine on the ring
4. insert original URL into the database and use getShortURL function to get shortened URL short_url
5. Combine hash_val and short_url as our final_short_url (length=8) and return to the user
6. Retrieve original from short URL
7. get first two chars in final_short_url as hash_val
8. use hash_val to locate the machine
9. find the row in the table by rest of 6 chars in final_short_url as short_url
10. return original_url to the user


## Other factors:

### Guid?
One thing I’d like to further discuss here is that by using GUID (Globally Unique Identifier) as the entry ID, what would be pros/cons versus incremental ID in this problem?
GUIDs are big, and they index badly in MySQL.

### Random string
If you dig into the insert/query process, you will notice that using random string as IDs may sacrifice performance a little bit. More specifically, when you already have millions of records, insertion can be costly. Since IDs are not sequential, so every time a new record is inserted, the database needs to go look at the correct page for this ID. However, when using incremental IDs, insertion can be much easier – just go to the last page.

### What database?
Redis

### 301 vs 302?
301 is permanent redirect, while 302 is temp redirect.
301 is more reasonable because once we get the shorten URL, it point to a link forever. However, with 301, we can't get the click number of the URL.
Click number is an important user data, thus, if we want to analysis user behavior, 302 could be a choice even it could require more server power.

### Can we do 1:1 mapping?
So 1 long: N short is good enough. But can we make 1:1 mapping possible?
Use key-value store. Save the most recent generated long:short relation. (LRU/ 1 hour)
Pseudo code:
1. Looking for long URL in the recent key-value store
1.1. Return if we can find it. And extent the TTL 1 hour
1.2. If we can't find it, we generate a shorten URL by using the inc generator, and save it to key-value store. TTL == 1 hour

**Pro**: 
1. If an address is frequent use, it would be in the key-value store all the times.
2. Also, this could defend the attack which keep asking service to generate new ID.
**Con**: We still can't make it 100% 1:1 mapping but the implement is much cheaper. Let's say, for a rarely used URL, you will get different shorten URL every time, but is it really matter?

### Other reading
Twitter Snow Flake