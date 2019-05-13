# TACT
Topic Analysis, Constructiveness and Toxicity for online articles and comments

## Project Overview

We set out to investigate trends in the toxicity, constructiveness and topics of online comments.
Online comments by themselves are interesting but it also helps to look at them in context - we do this using information about the articles on which these comments appeared.

To find these trends, we use various machine-learning-based systems and approaches.
For constructiveness, we use **_CHECK::REFERENCE_**, a constructiveness system developed at Simon Fraser University by Dr Maite Taboada and Dr Varada Kolhatkar.
For toxicity, we use Google's Perspective API.
For topic modelling, we settled on creating a Latent Dirichlet Allocation (LDA) model, the details of which are discussed in subsequent sections.

The results of this project will provide insights to online news publications that monitor the comment sections on their websites.

## Data - What and Where

We look at three publications - The Globe and Mail, The Tyee and The Conversation.
Some of this data is not publicly available and so is stored on [SFU Vault](https://vault.sfu.ca/) for use by the Discourse Processing Lab in our research.
Any subsequent mentions of Vault refer to this cloud storage service.

+ SOCC (The Globe and Mail)

The SFU Opinion and Comments Corpus (SOCC) is a corpus of preprocessed opinion articles that appeared online and comments on them.
There are no genres in this corpus and the data comes from The Globe and Mail, a Canadian daily.
There are 10,339 articles and 663,173 comments.

The SOCC data is located in __Vault -> Discourse Lab -> Data -> Globe_and_Mail__.
It can alternatively also be downloaded following the instructions on the SOCC project's [GitHub](https://github.com/sfu-discourse-lab/SOCC).
The texts of the articles are in the subfolder __CSVs__, where the two most important files are __gnm_articles.csv__ and __gnm_comments.csv__.

The constructiveness and toxicity predictions on the comments are stored in the subfolder __Globe_analysis__.
The topic modelling predictions on both the articles and the comments are stored in __Vault -> Discourse Lab -> Data -> Topic_Modelling -> results__ in the files __socc_articles_topics.txt__ and __socc_comments_topics.txt__.

+ The Tyee

The Tyee is also a Canadian daily which focuses on the province of British Columbia.
All the data we have from The Tyee is stored in __Vault -> Discourse Lab -> Data -> The_Tyee__.
We have 731,804 comments from their website.
The raw texts of these comments are in XML format, stored in the subfolder __Raw XML Data__.
After preprocessing, the data was put in CSV format and is available in the subfolder __CSVs -> the_tyee_posts_preprocessed.csv__.

The constructiveness and toxicity predictions on the comments are stored in the subfolder __Tyee analysis__.
The topic modelling predictions on the comments are stored in __Vault -> Discourse Lab -> Data -> Topic_Modelling -> results__ in the file __tyee_comments_topics.txt__.

+ The Conversation

The Conversation is a media outlet that sources articles from academics and researchers.
We use comment data from the Canadian website, all of which is stored in __Vault -> Discourse Lab -> Data -> The_Conversation__.
We have 11,283 comments from their website.
The preprocessed texts of these comments are available in the CSV file __the_conversation.csv__.

The constructiveness and toxicity predictions on the comments are stored in the subfolder __Conversation analysis__.
The topic modelling predictions on the comments are stored in __Vault -> Discourse Lab -> Data -> Topic_Modelling -> results__ in the file __conversation_comments_topics.txt__.

## Constructiveness and Toxicity Pipeline

Getting constructiveness and toxicity predictions on comments is straightforward as neither system requires special preprocessing of a comment.

For constructiveness, we use the SVM model batch predictor.
A new ConstructivenessPredictor is initialized and the predict_svm_batch() method is called on a pandas DataFrame of comments.
The notebooks were placed in the __web_interface__ level of the hierarchy in the Constructiveness system source code which is publicly available on [GitHub](https://github.com/sfu-discourse-lab/Constructiveness_public).
The constructiveness prediction is a binary value.
The results are written to a new CSV file.

The toxicity pipeline required some more set-up.
First an API key needs to be requested by going to the [Perspective API website](http://perspectiveapi.com/#/).
Filling out this form will whitelist you for an API key, after which their [quickstart documentation](https://github.com/conversationai/perspectiveapi/blob/master/quickstart.md) need to be followed to actually create an API key and try a request.
As with most APIs, there is a rate limit of 1000 AnalyzeComment requests per 100 seconds per user.
Thus, the notebooks for getting toxicity predictions for each comment include throttling, which was not necessary for the constructiveness pipeline.
The Perspective API has different models to predict different kinds of abuse and harrassment but we are most interested in the "TOXICITY" attribute. This returns a floating point value between 0 and 1.
So as to not maintain hundreds of thousands of comments in memory for hours at a time, each row of comment and toxicity prediction was written to a results file as soon as a response was received from the API.

## Stopping

Most coherent text - including articles and comments - consists of informative words about the topic, interspersed with filler or function tokens like articles (the, an, a) and punctuation that do not contribute to the meaning of the text.
These are called stopwords.

A typical step in preprocessing data before training a topic model is to remove stopwords and we have used an augmented version of the SMART stopword list.
In addition to the 570 words in the list, we added "Mr", "Mrs", "Ms", "Dr", "per", "cent", and all 7 days of the week.
We only kept tokens that were alphabetical.

Refer to the following [Basecamp document](https://3.basecamp.com/3749531/buckets/3682815/vaults/1408093034) for more information on how the stopwords were chosen.

## Topic Modelling

### Preface

As articles tend to be long and comments tend to be quite short generally, we decided to train a topic model on the SOCC articles and then apply this model to make predictions on comments from all three corpora.
Since all three publications are Canadian, we assumed that the topics discussed in the articles would have a lot of overlap.
By this logic and with the large number of SOCC articles we have (over 10,000), the fact that we did not have article data for the other two publications would not present a problem.

We had no previous knowledge of the topics that exist across the articles in SOCC.
This makes it difficult to apply a topic model such as LDA to it, where we need to specify the number of topics.
The corpus is too large to consider trying out a wide range of values and evaluating them by hand individually.
We would prefer a computational way to do this.

Let's say we have a computational parameter that measures the "goodness" of a topic model.
Then it is a lot simpler to write code to maximize the value of that computational parameter.
We would iteratively create topic models with different numbers of topics, and finally return the model that is evaluated as being the best, based on the magical computational parameter we assume that we have.
Let's call this series of steps a topic model creation pipeline.

There are a range of options for this computational parameter that can be optimized for a solution to the problem, notably, perplexity, coherence, and rate of perplexity change.
Finally, topic models are always best judged by humans, so there is always some degree of manual evaluation once the numbers are manageable.

### High-level Approach

With multiple options for the computational parameter that chooses the "best" topic model, but we don't necessarily know how well any of these metrics will perform on unlabelled data such as the SOCC articles.
For a more trustworthy model creation pipeline, we can apply it to labelled data and tweak how we use these parameters so that when it is applied to the data, it gives us almost the same number of topics and labelling as the true topics (the labels).

What we know about the SOCC data is that they are opinion articles from the Globe and Mail that are formally written.
For topic modelling, we are more interested in the content-rich parts rather than the opinionated parts of the articles.
So news articles (even hard news) would be a sensible choice for labelled data on which to train the topic model creation pipeline.

The topics are never transplanted from the labelled dataset to the SOCC articles.
All we are optimizing is our method of discovering a topic model that will then give us topics specific to the input corpus.
We used the Rubin Satire dataset to finetune our topic model creation pipeline.
This dataset consists of 240 articles across 12 topics in 4 domains, from real as well as satirical news sources.

To evaluate the performance of a given topic model on the Rubin Satire dataset, we created a cross-tabulation by document of topic predictions and true labels, and performed a chi-squared test on it.
The null hypothesis is that the predictions and the labels are independent of each other (which is not what we want).
We want a low p-value to reject this null hypothesis in favour of the alternate hypothesis, that the topic model's results correlate with the true labels.

With a range of topic models, we could look at the correlation between the p-values of their predictions on the Rubin Satire dataset (a true measure of correctness) and other heuristic measures such as coherence and perplexity, to see which metric matched up best.

### What Did Not Work

In terms of topic models, we found that the Hierarchical Dirichlet Process (HDP) topic model did not work and that LDA was better.
Regarding heuristics to evaluate a topic model, the rate of perplexity was very noisy and so would not work.
Additionally, as of the writing of this document, the [gensim](https://github.com/RaRe-Technologies/gensim/issues/701) and [scikit-learn](https://github.com/scikit-learn/scikit-learn/issues/6777) implementations have bugs that cause perplexity to increase with as the number of topics increased which should not happen.

HDP theoretically seemed like a silver bullet as it does not require a number of topics to be specified.
However, with the gensim implementation of HDP, the number of topics returned is fixed at 150.
Many of these 150 topics are not useful, but discriminating between them is a difficult problem.

One heuristic solution is to extract the LDA alpha parameter from the HDP model, the prior weight of a topic.
All the prior weights add up to a total of 1, and each weight can be understood roughly as how likely that topic is to really exist in the data.
However, picking a cutoff weight seemed almost arbitrary.
The distributions of the priors for the Rubin Satire data looked very different from that of the SOCC article data, where the model seemed to suggest classifying all the articles into just 2-3 topics, so we decided to try other approaches.

### Finalized Pipeline

We trained LDA models with different numbers of topics and used coherence scores to evaluate them.
After picking a reasonable range of values, we fine-tuned the model's parameters such as the chunk size and how often to estimate log perplexity.
There was also a lot of manual review of the topics' key words to ensure that we were not compromising on topic model quality by following what the numbers said.

## Visualizations

## Scripts - What and Where

+ The Tyee XML to CSV conversion: The [preprocessing](./preprocessing/) subfolder contains a notebook with the conversion of The Tyee raw data from XML to CSV format
+ Constructiveness pipeline: The [constructiveness](./constructiveness/) subfolder contains notebooks for each corpus
+ Toxicity pipeline: The [toxicity](./toxicity/) subfolder contains notebooks for each corpus except for SOCC, for which we had previous results
+ Stopping: The [preprocessing](./preprocessing/) subfolder contains a notebook with code for stopping, as well as a CSV file containing the list of SMART stopwords
+ Topic modelling exploration: The [topic_modelling/exploration](./topic_modelling/exploration/) subfolder, where the most important notebook is the one titled __Topic Modelling Exploration__
+ Topic modelling final pipeline: The notebook titled __Running topic modelling on everything__ in the [topic_modelling](./topic_modelling/) subfolder
+ 

## Constructiveness and Toxicity Results

## Topic Modelling Results

## Discussion

## References
