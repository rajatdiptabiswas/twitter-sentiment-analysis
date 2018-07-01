# Twitter Sentiment Analysis
A Python script that analyses sentiment on a given topic from tweets data provided by Twitter

</br>

## Getting Started

The project requires authentication via the Twitter API. A new application needs to be created to get the necessary keys. A few libraries also need to be installed for the script to run properly.

### Prerequisites

* [Tweepy](http://www.tweepy.org), the official Python library for accessing the Twitter API
* [TextBlob](https://textblob.readthedocs.io/en/dev/), a Python library for processing textual data
* [NLTK](https://www.nltk.org) dataset, to help better natural language processing
* Keys from the [Twitter Developer Application Management](https://apps.twitter.com/) site
  - Consumer key
  - Consumer secret
  - Access token
  - Access token secret
  
### Installing

The **Tweepy** library can be installed by using the command
```
pip3 install tweepy
```  
</br>

The **TextBlob** library can be installed using
```
pip3 install textblob
```  
</br>

The **NLTK corpora** can be downloaded by using the following command
```
python3 -m textblob.download_corpora
```
These files will provide better natural language processing capabilites for the TextBlob library. 

> **Note:** A missing cerificate error can arise when trying to download the NLTK corpus files. To fix the issue, navigate to the Python folder `/Applications/Python 3.6` and run the `Install Certificates.command` file.

</br>

To obtain the **consumer keys** and **access tokens** from the Twitter Dev Application Management site, a new app needs to be created using a Twitter account.

* Open [apps.twitter.com](https://apps.twitter.com/) and use the `Create New App` button.
* Complete the form with the necessary application details. The application name must be unique.
* Navitgate to the `Keys and Access Tokens` tab.
* Copy `Consumer Key`, `Consumer Secret`, `Access Token` and `Access Token Secret` and update the variables `consumer_key`, `consumer_secret`, `access_token`, and `access_token_secret` in the `sentiment_analysis.py` file accordingly.

</br>

## Running the program

* Download the `sentiment_analysis.py` file from the repository
* Update the consumer keys and access token values with the appropriate data in the file
* Run the file using
```
python3 sentiment_analysis.py
```

</br>

## Sample output
```
Rajats-MacBook-Pro:Desktop rajat$ python3 sentiment_analysis.py 

Enter a topic to apply sentiment analysis on:
	Putin


Sentiment analysis results:
	Positive	14.29 %
	Negative	12.86 %
	Neutral 	72.86 %


Positive tweets:

	> The new John Bolton: Trump ally swaps fire and brimstone for a spoonful of sugar 

Trump’s national security advise… 
	Polarity = 0.136 ; Subjectivity = 0.136

	> RT  Yup. Trump and Putin are meeting in Finland next month. Which is more appropriate than you’d think, since if these two kee…
	Polarity = 0.333 ; Subjectivity = 0.333

	> RT  Trump knows. Seth Rich. HRC Server, Uranium One, AWAN, Assange, Putin Summit. Dems can't stop it. Wait for it.
	Polarity = 0.375 ; Subjectivity = 0.375

	> RT  “Why would a president so desirous of making America strong be so obsequious and accommodating when it comes to Russia? That’…
	Polarity = 0.433 ; Subjectivity = 0.433

	>  Putin "If I help you win election, you turn a blind eye to Crimea and Syria"

Trump "Oh, yeah. No problem.… 
	Polarity = 0.150 ; Subjectivity = 0.150


Negative tweets:

	> RT  Republicans were outraged when Obama couldn't deter Putin from annexing Crimea, but many now silent when Trump considers endors…
	Polarity = -0.133 ; Subjectivity = -0.133

	> RT   If Hillary were President she would not be a traitor, idolize Putin, or do any of the dumb shit that Trump do…
	Polarity = -0.287 ; Subjectivity = -0.287

	> RT  Lots of hysterical SNOWFLAKE LIBS are worried the Russians are listening in on  unsecured phone calls. Gi…
	Polarity = -1.000 ; Subjectivity = -1.000

	> RT  11/ The evil menace currently occupying the WH may not get a passing grade on removing troops from east Asia during Putin's…
	Polarity = -0.500 ; Subjectivity = -0.500

	> RT  Trying to finish up a song about Trump, can't come up with the last verse.

(need to rhyme with "can")

- An moron wit…
	Polarity = -0.400 ; Subjectivity = -0.400


Neutral tweets:

	> RT  Darth Putin 
	Polarity = 0.000 ; Subjectivity = 0.000

	> RT  I was with two Journalists at dinner last night.  They were talking about the Trump Putin summit.  I said that’s not a summit…
	Polarity = 0.000 ; Subjectivity = 0.000

	> RT  Yes, Russians installed Trump. Only took about 80,000 votes in 3 states to change the outcome of the electoral college.…
	Polarity = 0.000 ; Subjectivity = 0.000

	> RT  Looks like Trump is preparing yet another gift for Putin in advance of their July get together. 
	Polarity = 0.000 ; Subjectivity = 0.000

	> RT  A young Russian boy was suffering a form of Cancer. He wrote to President Vladimir Putin requesting the President visits him as…
	Polarity = 0.050 ; Subjectivity = 0.050
  
  
```

</br>

## Authors

* **Rajat Dipta Biswas** - *Initial work* - [rajatdiptabiswas](https://github.com/rajatdiptabiswas)

See also the list of [contributors](https://github.com/rajatdiptabiswas/twitter-sentiment-analysis/graphs/contributors) who participated in this project.

</br>

## Acknowledgments

* [NLTK documentation](https://www.nltk.org)
* [TextBlob documentations](https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis)
* [Twitter Sentiment Analysis - Learn Python for Data Science](https://www.youtube.com/watch?v=o_OZdbCzHUA)
* [Twitter Sentiment Analysis using Python](https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/)
