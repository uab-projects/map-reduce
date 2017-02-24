# The workflow
We've split the software functionality as a several step process to be able to use divide and conquer technique and get the software architecture:
## Steps
### 1. Reading and splitting
The first step is to be able to read the file in pieces (split the file while reading) to be able to send the data to the following steps (map and reduce)
#### Splitting methods
We've seen three ways to read and split the file, according to what and how we split it:
1. **By words**:
   Choose a parameter $n_{words}$, so we read the file by groups of $n_{words}$.
2. **By lines**
   Choose a parameter $n_{lines}$ so we read the file $n_{lines}$ by $n_{lines}$
3. **By letters**
   Read $n_{letters}$ and go reading $n_{letters}$ by $n_{letters}$

#### Inputs and outputs
##### Inputs
The inputs are files
##### Outputs
Outputs are a piece of text that has been read, depends on the splitting method. The outputs are sent to a MapPool, that receives those pieces of texts and creates the map key/value pair values
### 2. The mapping
While we go reading and creating groups from the file using one of the above splitting methods, in the map pool we receive those pieces of text.

#### The map task
What the map pool must do as a task is pick these piece of text, separe the text by words or letters and create a list of key/value pairs with the word / letter and value 1 (just one word / letter) is counted.

After a map list of key/value pairs has been created, this is sent to the reduce pool

### 3. The reducing
We receive in the reduce pool a list of key / value pairs with words or letters as key and the count of words / letters as value.

#### The reduce task
The reduce task is to take a pair of received map results and join them looking for repeated keys and performing the sum of their values so it reduces a pair of received map results into the sum, returning a map reduce that is introduced as a feedback to itself until no more map entries are received from the mapping process

### 4. The result
Finally, when the reduce detects that no more map entries are being sent and no more reduce tasks are pending, a result callback has to be called presenting the only map entry resting in the work queue of the reduce process, that will be the result.
