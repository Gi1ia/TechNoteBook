## Solution

### Clarify before solving
1. Multiple devices?
2. text? image?
3. Security?
4. User scale? 1 million
    ~10 msg/dayy
5. (serach?)
6. send to individual user first; group chat later
7. confirmation
8. error

### 
* client to server/ server to client
* Server will need a database 
    -- user-table
    -- msg-table

#### user table
It won't be updated very much, expected to be small.
so, it could be stored in sql
-------------------------
| id | username | email |
-------------------------

#### msg table
* Purpose is to deliver the msg. We keep adding new messages, but don't change the old message a lot.

* Total storage = 1M * 10 * 200B ~= 2G. Thus we may think about data retention
* content 200k; chunk it if necessary 
----------------------
| id(4 Byte) | 
----------------------
| from                    |
| to                      |
| content                 |
| time stamp              |
| status                  |
| belong to X conversation| (used to look up in coversation table)
-----------------------
* Scale msg talbe

### Message/Packets duplicate/sequence/lost
#### Handle the messages sync
1. http connection -- pull 
    * It doesnt' work. we want to 2 way communication
2. web socket -- 2 way communication
    2.1 A --> msg_to_B --> server --> forward to A
    2.2 C --> msg_to_B --> server --> forward to A

#### async 
* Using messages queue/worker
* Extra machine to handle the queue

### Confirmation

### Communication / Conversation
* An extra service (micro) to handle conversation (sequence)
* Both group and time sequence
ID: fromXXXTOXXX