#### Pair Problem

For the two strings below, given in Python syntax as `mmg` and `geb`, make a three-word phrase entirely from words five letters or longer that occur in both selections.

*If you finish early, use the time to see if you code is clear and concise. And if not, see if you can do something about that. Feel free to use [yesterday's solution](../01-regularization/pair.ipynb) as a resource.*

```Python
mmg = """I am the very model of a modern Major-General,
I've information vegetable, animal, and mineral,
I know the kings of England, and I quote the fights historical
From Marathon to Waterloo, in order categorical;
I'm very well acquainted, too, with matters mathematical,
I understand equations, both the simple and quadratical,
About binomial theorem I'm teeming with a lot o' news, (bothered for a rhyme)
With many cheerful facts about the square of the hypotenuse.
I'm very good at integral and differential calculus;
I know the scientific names of beings animalculous:
In short, in matters vegetable, animal, and mineral,
I am the very model of a modern Major-General.

I know our mythic history, King Arthur's and Sir Caradoc's;
I answer hard acrostics, I've a pretty taste for paradox,
I quote in elegiacs all the crimes of Heliogabalus,
In conics I can floor peculiarities parabolous;
I can tell undoubted Raphaels from Gerard Dows and Zoffanies,
I know the croaking chorus from The Frogs of Aristophanes!
Then I can hum a fugue of which I've heard the music's din afore, (bothered for a rhyme)
And whistle all the airs from that infernal nonsense Pinafore.
Then I can write a washing bill in Babylonic cuneiform,
And tell you ev'ry detail of Caractacus's uniform:
In short, in matters vegetable, animal, and mineral,
I am the very model of a modern Major-General.
In fact, when I know what is meant by "mamelon" and "ravelin",
When I can tell at sight a Mauser rifle from a javelin,
When such affairs as sorties and surprises I'm more wary at,
And when I know precisely what is meant by "commissariat",
When I have learnt what progress has been made in modern gunnery,
When I know more of tactics than a novice in a nunnery -
In short, when I've a smattering of elemental strategy - (bothered for a rhyme)
You'll say a better Major-General has never sat a gee.
For my military knowledge, though I'm plucky and adventury,
Has only been brought down to the beginning of the century;
But still, in matters vegetable, animal, and mineral,
I am the very model of a modern Major-General."""

geb = """Gödel, Escher, Bach: An Eternal Golden Braid, also known as
GEB, is a 1979 book by Douglas Hofstadter. The tagline "a metaphorical
fugue on minds and machines in the spirit of Lewis Carroll" was used
by the publisher to describe the book.

By exploring common themes in the lives and works of logician Kurt
Gödel, artist M. C. Escher and composer Johann Sebastian Bach, GEB
expounds concepts fundamental to mathematics, symmetry, and
intelligence. Through illustration and analysis, the book discusses
how self-reference and formal rules allow systems to acquire meaning
despite being made of "meaningless" elements. It also discusses what
it means to communicate, how knowledge can be represented and stored,
the methods and limitations of symbolic representation, and even the
fundamental notion of "meaning" itself.

In response to confusion over the book's theme, Hofstadter has
emphasized that GEB is not about mathematics, art, and music but
rather about how cognition and thinking emerge from well-hidden
neurological mechanisms. In the book, he presents an analogy about how
the individual neurons of the brain coordinate to create a unified
sense of a coherent mind by comparing it to the social organization
displayed in a colony of ants."""
```

*Text taken from Wikipdia pages [Major-General's Song](http://en.wikipedia.org/wiki/Major-General%27s_Song) and [Gödel, Escher, Bach](http://en.wikipedia.org/wiki/G%C3%B6del,_Escher,_Bach), with some characters converted to ASCII for convenience.*
