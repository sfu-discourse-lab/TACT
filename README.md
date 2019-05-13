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
After pre-processing, the data was put in CSV format and is available in the subfolder __CSVs -> the_tyee_posts_preprocessed.csv__.

The constructiveness and toxicity predictions on the comments are stored in the subfolder __Tyee analysis__.
The topic modelling predictions on the comments are stored in __Vault -> Discourse Lab -> Data -> Topic_Modelling -> results__ in the file __tyee_comments_topics.txt__.

+ The Conversation

The Conversation is a media outlet that sources articles from academics and researchers.
We use comment data from the Canadian website, all of which is stored in __Vault -> Discourse Lab -> Data -> The_Conversation__.
We have 11,283 comments from their website.
The pre-processed texts of these comments are available in the CSV file __the_conversation.csv__.

The constructiveness and toxicity predictions on the comments are stored in the subfolder __Conversation analysis__.
The topic modelling predictions on the comments are stored in __Vault -> Discourse Lab -> Data -> Topic_Modelling -> results__ in the file __conversation_comments_topics.txt__.

## Constructiveness and Toxicity Pipeline

Getting constructiveness and toxicity predictions on comments is straightforward as neither system requires special pre-processing of a comment.

For constructiveness, we use the SVM model batch predictor.
A new ConstructivenessPredictor is initialized and the predict_svm_batch() method is called on a pandas DataFrame of comments.
The notebooks were placed in the __web_interface__ level of the hierarchy in the Constructiveness system source code which is publicly available on [GitHub](https://github.com/sfu-discourse-lab/Constructiveness_public).
The results are written to a new CSV file.

The toxicity pipeline required some more set-up.
First an API key needs to be requested by going to the [Perspective API website](http://perspectiveapi.com/#/).
Filling out this form will whitelist you for an API key, after which their [quickstart documentation](https://github.com/conversationai/perspectiveapi/blob/master/quickstart.md) need to be followed to actually create an API key and try a request.
As with most APIs, there is a rate limit of 1000 AnalyzeComment requests per 100 seconds per user.
Thus, the notebooks for getting toxicity predictions for each comment include throttling, which was not necessary for the constructiveness pipeline.
So as to not maintain hundreds of thousands of comments in memory for hours at a time, each row of comment and toxicity prediction was written to a results file as soon as a response was received from the API.

## Topic Modelling Pipeline

## Visualizations

## Scripts - What and Where

+ Constructiveness pipeline: The __constructiveness__ subfolder contains notebooks for each corpus
+ Toxicity pipeline: The __toxicity__ subfolder contains notebooks for each corpus except for SOCC, for which we had previous results

## Constructiveness and Toxicity Results

## Topic Modelling Results

## Discussion

## References
