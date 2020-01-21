# Text-Summarizer
This project lets you simply summarize your long boring texts. Much to study? Say no more! With this project you can simply summarize your texts.


## **Installation:**

python >=3.7
pip install Flask
pip install flask-bootstrap
python (start python shell)
import nltk
nltk.download()
>Then an installation window appears: 
1)Go to the 'Models' tab and select 'punkt' from under the 'Identifier' column. Then click Download and it will install the necessary files.<br>
2)Go to the ‚Corpora‘ tab and select ‚stopwords‘ from under the 'Identifier' column. Then click Download and it will install the necessary files.
<br>
- then to run the program (on unix):<br>
A) export FLASK_APP=main<br>
B) flask run<br>
<br>
- on windows:<br>
A) Set FLASK_APP=main<br>
B) flask run
<br>
-----

(if nothing above works try using miniconda with a python 3.7 environment and try again)

-----
In miniconda (to run it):
move to cd miniconda3/envs/textanalyzer  => conda activate textanalyzer
then cd text_analyzer => run A) and B)
