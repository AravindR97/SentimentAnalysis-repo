# Sentiment Analysis: AI Web App

Web App to perform Sentiment Analysis on given text using Watson AI libraries.

## Demo

https://github.com/AravindR97/SentimentAnalysis-repo/assets/132665408/cb10be41-e6cc-4103-a6eb-3a4abe5c38e0

## Description:
**Text Sentiment Analysis**: The practice of using computers to recognize sentiment or emotion expressed in a text. Sentiment analysis is often performed on textual data to help businesses monitor brand and product sentiment in customer feedback, and understanding customer needs. It helps attain the attitude and mood of the wider public which can then help gather insightful information about the context.

In this project, I have:

	1. Created an AI based sentiment analysis application using Watson NLP embedded libraries.
	2. Formatted the output received from the Watson NLP library function to extract relevant information from it.
	3. Packaged the application and made it importable to any python code for usage.
	4. Ran unit tests on the application and checked the validity of its outputs for different inputs.
	5. Deployed the application using Flask framework.
	6. Incorporated error handling capability in the application, such that a response code of 500 receives an appropriate response from the application.
	7. Ran static code analysis on the code files to confirm their adherence to the PEP8 guidelines.

### Dependencies
* Python
* HTML5
* JavaScript
* Watson AI NLP Library
* Flask
* Requests Library

### Installation
For this project, you need access to Watson AI Natural Language Processing Library
* Go to https://www.ibm.com/products/natural-language-processing
* Click on **Start your Free Guided Trial**
* The next 5 pages will give you many options to choose from. Choose each option as shown below:
![IBM_NLP](https://github.com/AravindR97/SentimentAnalysis-repo/assets/132665408/cb3c2eac-93f1-4e0a-bb34-6cee3122a141)
* Click Next
* Go to Step 3 and generate a container URL by logging in or signing up:
![IBM_NLP2](https://github.com/AravindR97/SentimentAnalysis-repo/assets/132665408/ce48a2d3-42f9-41c7-993c-70a5f9d0583d)
* After log-in, a pop-up showing the container URL will be shown. Copy the URL and save it for future use.

### How to run the program
* Fork this repository
* Clone it to your local PC
* In the repository, go to SentimentAnalysis & open sentiment_analysis.py in a code editor
* Inside emotion_detector function, paste the **container URL** you saved earlier to the variable 'base_url' & uncomment it.
* Save the file, open commandline, navigate to the repository and run server.py. Your app will be hosted on web.
* Go to localhost address '127.0.0.1:5000' on any browser to use the app.
