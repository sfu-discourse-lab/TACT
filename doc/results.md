# TACT: Results

## Constructiveness and Toxicity

Constructiveness and toxicity are two axes along which we can evaluate a comment.
Intuitively, we expect constructive comments to make well-reasoned arguments, while non-constructive comments do not add meaningful discussion.
Toxic comments contain insults, profanity or attacks on the authors or people mentioned in an article.
Non-toxic comments do not.
Any given comment is either constructive and toxic, constructive and non-toxic, non-constructive and toxic, or non-constructive and non-toxic.

A non-constructive and non-toxic comment does not add meaningful discussion but does not insult either.
Examples of this type of comment include polite, unjustified agreement or disagreement with the article.
In the data we considered, these comments tended to show agreement more often than disagreement. **_CHECK::ANECDOTAL CLAIM, NO PROPER ANALYSIS DONE_**

A non-constructive and toxic comment on the other hand consists of directed malice without providing good reasoning.
This type of comment often contains colourful language but this category also includes sarcasm and more subtle insults.
Despite the fact that agreement or disagreement with the article's content has nothing to do with a comment being in this category, we found a pattern in the data we considered.
Comments in this category tended to disagree with the article's content or show disapproval of the views of the author or others mentioned in the article. **_CHECK::ANECDOTAL CLAIM, NO PROPER ANALYSIS DONE_**

Comments that are constructive and non-toxic read like an essay.
They tend to be longer and their sentences are linked cohesively, providing convincing arguments for their point of view.
Nobody is insulted, regardless of whether the comment writer agrees or disagrees with the content of the article.

Finally, perhaps the most interesting category is the constructive and toxic comment.
Almost paradoxically, they contain well-reasoned arguments as well as hateful language.
They sound condescending and often follow a format where they open with a toxic insult and continue with good reasoning.
The shift is often so dramatic that if the first sentence was ignored, the comment would land squarely in the constructive and non-toxic category.
These comments are more common than one would expect and are particularly interesting because they do not follow intuition.

Below is a visual depiction of the four categories which also illustrates some examples.
The non-constructive and toxic category consists of several examples stitched together where words considered insulting are censored with red asterisks.

![](https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/Comment_taxonomy.png "Taxonomy of an online comment")

With this taxonomy of the online comment in mind, we examine some of the trends in our data, first altogether and then broken up by publication.
These graphs all show toxicity on the horizontal axis, the number of comments on the vertical axis, and one line each for constructive and non-constructive comments.

![](https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/All_comments.png "All comments - constructiveness and toxicity")

The highest point in the graph at over 200,000 comments is a blue dot, i.e., non-constructive comments.
They are low in toxicity - around 0-15% toxicity.
Non-constructive and non-toxic comments like "I agree" or "I disagree" fall into this category and make up the majority of online comments in these three publications, as we would expect.

Through most of the graph, non-constructive comments are more common than constructive comments, which also aligns with our intuitions about seeing few logical comments on the internet.
However, in the central part of the graph with middling levels of toxicity, constructive comments tend to be slightly more common.
Additionally, the peak of the constructive (orange) line is at about 15% toxicity.
Both these findings imply that constructive comments tend to contain some small proportion of toxicity.
The explanation we suggest for this is that constructive comments tend to provide qualified rather than total agreement or disagreement, unlike non-constructive comments.
This qualification gives room for some name-calling in many constructive comments.

The tail end of the graph is towards the right, i.e., high toxicity.
This is somewhat unusual because our perception of comments online tends to be that many are nasty and hurtful.
But we propose that this impression can be attributed to the [negativity bias](https://en.wikipedia.org/wiki/Negativity_bias).

Another point to notice when looking at the leftmost part of the graph is that at a very low level of toxicity, there seem to be may more non-constructive comments than constructive comments - more than twice as many.
This means that there are more than twice as many non-toxic comments like "I agree" or "I disagree" than well-reasoned comments without insults.

Now we will consider each publication individually to see how closely their data matches the average case.

![](https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/SOCC.png "SOCC - constructiveness and toxicity")

The main difference between SOCC comments and the overall pattern is that non-constructive comments are consistently far more frequent than constructive comments at all levels of toxicity.

Additionally, the drop in the number of comments with increasing toxicity is less steep than the overall pattern, indicating that SOCC comments are more toxic on average.

### The Tyee

![](https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/The_Tyee.png "The Tyee - constructiveness and toxicity")

The Tyee has many more constructive comments with the orange line consistently above the blue one starting at about 15% toxicity.

The original pattern at a low level of toxicity of more non-constructive than constructive comments is consistent with the overall pattern.

### The Conversation

![](https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/The_Conversation.png "The Conversation - constructiveness and toxicity")

The Conversation seems to have much fewer toxic comments than the average as the drop in the lines from the left (low toxicity) to right (high toxicity) is very steep.

Most interestingly, the low level toxicity pattern is not seen in this publication, i.e., at 0-15% toxicity, there is a very small difference between the numbers of constructive and non-constructive comments.
We attribute this to the nature of the publication.
With content from academics and researchers, we imagine that the audience interested in reading these articles is self-selected to be more cautious in their comments.

## Topic Modelling

Topic modelling is a technique to discover the themes (henceforth "topics") discussed in a corpus of documents.
Having trained an LDA topic model on the large corpus of SOCC articles, 15 distinct topics were discovered. The top 10 words of each topic is displayed below.

<p align="center">
  <b>Topic 1</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Topic 2</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Topic 3</b>
</p>

<img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic1.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic2.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic3.png" width="285" height="250">

<p align="center">
  <b>Topic 4</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Topic 5</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Topic 6</b>
</p>

<img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic4.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic5.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic6.png" width="285" height="250">

<p align="center">
  <b>Topic 7</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Topic 8</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Topic 9</b>
</p>

<img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic7.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic8.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic9.png" width="285" height="250">

<p align="center">
  <b>Topic 10</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Topic 11</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Topic 12</b>
</p>

<img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic10.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic11.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic12.png" width="285" height="250">

<p align="center">
  <b>Topic 13</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Topic 14</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Topic 15</b>
</p>

<img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic13.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic14.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic15.png" width="285" height="250">

Predictions were first made on the articles. An article was counted towards a topic if the topic model predicted a probability of more than 10% for the topic in that article.

![](https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/Articles.png "Topics discussed in the articles")

We see clearly that the 3 most popular topics of SOCC articles are topics 14, 10 and 4.

<img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic14.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic10.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic4.png" width="285" height="250">

These topics appear political but are not limited to Canada.
The most common one, topic 14, contains the words "British" and "Chinese", suggesting international politics and economics.
Topic 4 is clearly about Canadian politics at the national level, with the words "government", "NDP", "Liberals", "Harper" and "party".
Topic 10 is about "people", "public" and "system[s]", suggesting local news, further emphasized by the appearance of "Vancouver".

When predictions were made on the three comment corpora with the LDA model, strikingly similar patterns emerged.
The top three topics are the same for both articles and comments and they remain the top three by a big margin.
The graph below shows the results for all comments combined, but even when split up by corpus, the results are not far from each other.

![](https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/All_comments.png "Topics discussed in the comments")

These graphs lead us to our first conclusion which is that the proportions of the topics discussed in comments seem to correlate directly with those of articles.
This suggests that what people talk about is associated with the articles that they read, as opposed to being disproportionately about other topics.

We cannot conclude from these graphs that people comment more about politics than any other topic, however.
This is because if there is a correlation between topics in articles and topics in comments, then they are not independent from each other.
To find out what people comment most about, we need to account for and normalize the number of articles in any given topic.

We do this by dividing the number of comments on a certain topic by the number of articles on that same topic.
Interesting results emerge, as shown in the graph below.

![](https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/All_comments_normalized.png "Normalized discussed in the comments")

This graphs shows the difference in the proportion of comments about a topic when compared to articles about that same topic.
What we see here is a different set of top three topics - topics 6, 7 and 2.

<img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic6.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic7.png" width="285" height="250"> <img src="https://raw.githubusercontent.com/sfu-discourse-lab/TACT/master/img/topics/topic2.png" width="285" height="250">

In these topics, we see more people mentioned - "Charest", "Redford" and "Romney".
We also see more personal, abstract concepts such as "talk", "problem", "matter", "home", "community", "life" and "death".
In contrast to these words, articles tend to be more factual and have more concrete nouns.

At the same time, judging from the words "legislation", "program", "Trade", "Commons", "candidates", "global" and "local", it seems that comments do talk considerably about politics at different levels.
This leads to our second conclusion, that people comment more about politics than other topics, but that they bring in personal experience and anecdotes when they do so.

## Topic Modelling and Constructiveness

## Topic Modelling and Toxicity

## Future Research
