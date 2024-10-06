### 1. Marcovchain with state size 1
- very random output

### 2. Marcovchain with state 2-3
- beatiful output
- turns out just copy pasting poems
    - wrote a plagarising checker with 10-grams

### 3. went back to state size 1, no(less) copy pasting but too meaningless

### 4. Tried to add randomeness with avoiding overlps of certain size
- at first we tought that the vopy pasting issue is solvd but we managed to caught copy pasting by lovering the n-gram checker. 

### 5. When max_overlap is smaller it still gets 4-grams from different opems but chains them in a rather meaningfull way.
- only certain meet the constraints, so a bit repetitive


tries=20000,
max_overlap_ratio=0.6,  # Allow only up to 50% overlap
max_overlap_total=3   # Allow overlap of up to 10 words


# Bad Poets Society Logbook

## 1. Poem Fetching

We wanted to have an autamted system to fetch and store the poems for training the poem generator system. poetrydb.org had a web api where we can fetch all poems of a author by sending an get reguest to https://poetrydb.org/author/{poet_name}. 

We went with the following authors
- Emily Dickinson: 362 poems
- Oscar Wilde: 10 poems
- William Blake: 52 poems
- Percy Bysshe Shelley: 312 poems

### 1.1 Stats
We also record some stats per author

        self.stats = {
            'number_of_poems': num_poems,
            'mean_length_of_poems': mean_length,
            'number_of_unique_words': num_unique_words
        }

with the intention of analyzing the creativity of the system based on the characterstics of the reference data

## 2. Poem Generation With Markov Chains

We first decided to go with fine tuning a LLM to generate poems as it is the most state of the art approach. However because of its simple nature and ease of implementation, we decided to use markov chains to generate the content. 

### 2.1 Markov chains

#### 2.1.1 First-Order Markov Chains
A first-order Markov chain treats each word in the reference database as a node in a directed graph. Edges between nodes indicate the probability of transitioning from one state to another. These probabilities can be calculated from the reference text by noting each consecutive word tuple and normalizing the values to correspond to probabilities.


#### 2.1.2 Higher-Order Markov Chains
A higher-order Markov chain operates similarly to a first-order chain but considers previous transitions to the current node. For example, a second-order Markov chain takes into account the two preceding words. In this case, the probability of a transition is represented as:

$$
P(w_3 \mid (w_1, w_2))
$$

where \( n \) is the number of unique words in the database, and the chain has \( n^2 \) possible states or nodes. Each node represents the likelihood of transitioning from a word pair \( (w_1, w_2) \) to a subsequent word \( w_3 \).

This enables the modelling the more complex relationships between words and hopefully come up with meaningful sentences.

### 2.2 Implementation

We first tried to do our own implementation in python since the algorithm is fairly simple where we record the probabilities in a n*n sparse matrix in training stage and then traverse the chain by "flipping a coin" in each node and following the transition based on the transition probabilities. However we quicky decided to go with an exisiting python implementation called **markovify** since its much more efficient and supports higher order chains out of the box. Also some of its features came in handy in the later stages where we tried to avoid the model just copying existing poems.

With **markovify** implementing a markov chain is as simple as

    model = markovify.Text(text, state_size)

### 2.3 Generating Poems

At first we tried to generate a poem with a single order markov chains with Emily Dickinson poems. The majority of the experimentation is made with emily dickinson poems. We then tested the system with the rest of poets with the optimum parameters obtained from the experimentation. 
#### 2.3.1 Generation with first order chanins

We can get a sentence from the markow model like

    line= self.model.make_sentence()

We first generated 3 sentences. Markovify internally handles the termination by treating terminal punctuations as a seperate termination node. A sentence is finished once we reach the termination node. 

**Generated Poem 1.1**: *The Moon or of Thee -- By innocent Surprise Cool us -- how Nature -- No more slowly The other, as yet no more -- Its unobtrusive Mass. No Trace -- Intact -- Tell Him -- And so bolder every step For Whom I stood -- the site of a pilgrim be Adjusted -- Prosperity -- And yet it -- They said the Wall In Nature feels. The Forest of thee to scan -- Which solemnizes me. Loose the backward leaves Us homesick, who ne'er so I stepped upon my strong trust -- With God.*

The length of sentences were more than the average sentence line in the database. This is either a result of the randomness of the first order model or how the termination is treated with termination punctuation marks. Since the use of punctuation in the poems don't follow conventional use. So we tried trating end of lines as termination by 

    model = markovify.NewlineText(self.text, state_size=state_size)

This resulted in better generations that matched the reference poems

**Generated Poem 1.2**:

*Alloys our names -- adjust the fragrant Cocks --*

*Propitiation's claw -- guessed it --*

*And so, and shake your inference appalling*

**Generated Poem 1.3**:

*Thou art not -- like a Hell can see --*

*It pleased my Knitting --*

*And whatsoever is Theirs unto the House of Itself -- a cheek --*

**Generated Poem 1.4**:

*To hold my Life, My own Grave -- the fire will give him as Hours slid fast --*

*If they waded -- Her Lips of their loveliness*

*Is but One Claw --*

These poems better matched our expectations. At this point the way we assesed the creativity of these systems were solely based on our opinions. We **desperately** searched for meaning in the generated lines. The word choice and the style of these poems resembled Emily Dickinson but as if she didn't speak english. 





















