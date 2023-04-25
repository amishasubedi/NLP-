{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e6fe5783",
   "metadata": {},
   "source": [
    "## MS Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "7fc33452",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Windows-1252\n"
     ]
    }
   ],
   "source": [
    "import chardet\n",
    "\n",
    "with open('Chat.csv', 'rb') as f:\n",
    "    result = chardet.detect(f.read())\n",
    "\n",
    "print(result['encoding'])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dd01251b",
   "metadata": {},
   "source": [
    "## Data Preprocessing  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "4cf16130",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\subed\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import re\n",
    "import nltk\n",
    "import nltk\n",
    "nltk.download('punkt')\n",
    "from nltk.tokenize import word_tokenize, sent_tokenize\n",
    "from nltk.corpus import stopwords\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "from sumy.parsers.plaintext import PlaintextParser\n",
    "from sumy.summarizers.luhn import LuhnSummarizer\n",
    "from sumy.summarizers.lsa import LsaSummarizer\n",
    "from sumy.nlp.tokenizers import Tokenizer\n",
    "import spacy\n",
    "from spacy.lang.en.stop_words import STOP_WORDS\n",
    "from string import punctuation\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "a725aa53",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import pandas as pd\n",
    "df = pd.read_csv('Chat.csv', encoding='Windows-1252')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f2bceb1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "cd7c6f5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Question</th>\n",
       "      <th>Answer</th>\n",
       "      <th>Unnamed: 2</th>\n",
       "      <th>Unnamed: 3</th>\n",
       "      <th>Unnamed: 4</th>\n",
       "      <th>Unnamed: 5</th>\n",
       "      <th>Unnamed: 6</th>\n",
       "      <th>Unnamed: 7</th>\n",
       "      <th>Unnamed: 8</th>\n",
       "      <th>Unnamed: 9</th>\n",
       "      <th>...</th>\n",
       "      <th>Unnamed: 86</th>\n",
       "      <th>Unnamed: 87</th>\n",
       "      <th>Unnamed: 88</th>\n",
       "      <th>Unnamed: 89</th>\n",
       "      <th>Unnamed: 90</th>\n",
       "      <th>Unnamed: 91</th>\n",
       "      <th>Unnamed: 92</th>\n",
       "      <th>Unnamed: 93</th>\n",
       "      <th>Unnamed: 94</th>\n",
       "      <th>Answers(411)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>What are the requirements for voting by absent...</td>\n",
       "      <td>Voters unable to vote in person on Election Da...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Absentee voting is available if you meet any o...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>What is the voter registration deadline?</td>\n",
       "      <td>Primary Election Date is June 7, 2022 (Registe...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>n person registration at the county clerk's of...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Where can I cast my vote?</td>\n",
       "      <td>After registering to vote, your Voter Registra...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>What are the registration qualifications to vote?</td>\n",
       "      <td>Every U.S. citizen who possesses the following...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>How to register by mail to vote?</td>\n",
       "      <td>1. Complete a Mail-In Voter Registration Appli...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 96 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                            Question  \\\n",
       "0  What are the requirements for voting by absent...   \n",
       "1           What is the voter registration deadline?   \n",
       "2                          Where can I cast my vote?   \n",
       "3  What are the registration qualifications to vote?   \n",
       "4                   How to register by mail to vote?   \n",
       "\n",
       "                                              Answer  Unnamed: 2  Unnamed: 3  \\\n",
       "0  Voters unable to vote in person on Election Da...         NaN         NaN   \n",
       "1  Primary Election Date is June 7, 2022 (Registe...         NaN         NaN   \n",
       "2  After registering to vote, your Voter Registra...         NaN         NaN   \n",
       "3  Every U.S. citizen who possesses the following...         NaN         NaN   \n",
       "4  1. Complete a Mail-In Voter Registration Appli...         NaN         NaN   \n",
       "\n",
       "   Unnamed: 4  Unnamed: 5  Unnamed: 6  Unnamed: 7  Unnamed: 8  Unnamed: 9  \\\n",
       "0         NaN         NaN         NaN         NaN         NaN         NaN   \n",
       "1         NaN         NaN         NaN         NaN         NaN         NaN   \n",
       "2         NaN         NaN         NaN         NaN         NaN         NaN   \n",
       "3         NaN         NaN         NaN         NaN         NaN         NaN   \n",
       "4         NaN         NaN         NaN         NaN         NaN         NaN   \n",
       "\n",
       "   ...  Unnamed: 86  Unnamed: 87  Unnamed: 88  Unnamed: 89  Unnamed: 90  \\\n",
       "0  ...          NaN          NaN          NaN          NaN          NaN   \n",
       "1  ...          NaN          NaN          NaN          NaN          NaN   \n",
       "2  ...          NaN          NaN          NaN          NaN          NaN   \n",
       "3  ...          NaN          NaN          NaN          NaN          NaN   \n",
       "4  ...          NaN          NaN          NaN          NaN          NaN   \n",
       "\n",
       "   Unnamed: 91  Unnamed: 92  Unnamed: 93  Unnamed: 94  \\\n",
       "0          NaN          NaN          NaN          NaN   \n",
       "1          NaN          NaN          NaN          NaN   \n",
       "2          NaN          NaN          NaN          NaN   \n",
       "3          NaN          NaN          NaN          NaN   \n",
       "4          NaN          NaN          NaN          NaN   \n",
       "\n",
       "                                        Answers(411)  \n",
       "0  Absentee voting is available if you meet any o...  \n",
       "1  n person registration at the county clerk's of...  \n",
       "2                                                NaN  \n",
       "3                                                NaN  \n",
       "4                                                NaN  \n",
       "\n",
       "[5 rows x 96 columns]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "8825df56",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Select columns that have a name\n",
    "df = df.loc[:, ~df.columns.str.contains('^Unnamed')]\n",
    "\n",
    "# Remove columns that have only NaN values\n",
    "df = df.dropna(axis=1, how='all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "2541deb6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Question</th>\n",
       "      <th>Answer</th>\n",
       "      <th>Answers(411)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>What are the requirements for voting by absent...</td>\n",
       "      <td>Voters unable to vote in person on Election Da...</td>\n",
       "      <td>Absentee voting is available if you meet any o...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>What is the voter registration deadline?</td>\n",
       "      <td>Primary Election Date is June 7, 2022 (Registe...</td>\n",
       "      <td>n person registration at the county clerk's of...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Where can I cast my vote?</td>\n",
       "      <td>After registering to vote, your Voter Registra...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>What are the registration qualifications to vote?</td>\n",
       "      <td>Every U.S. citizen who possesses the following...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>How to register by mail to vote?</td>\n",
       "      <td>1. Complete a Mail-In Voter Registration Appli...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                            Question  \\\n",
       "0  What are the requirements for voting by absent...   \n",
       "1           What is the voter registration deadline?   \n",
       "2                          Where can I cast my vote?   \n",
       "3  What are the registration qualifications to vote?   \n",
       "4                   How to register by mail to vote?   \n",
       "\n",
       "                                              Answer  \\\n",
       "0  Voters unable to vote in person on Election Da...   \n",
       "1  Primary Election Date is June 7, 2022 (Registe...   \n",
       "2  After registering to vote, your Voter Registra...   \n",
       "3  Every U.S. citizen who possesses the following...   \n",
       "4  1. Complete a Mail-In Voter Registration Appli...   \n",
       "\n",
       "                                        Answers(411)  \n",
       "0  Absentee voting is available if you meet any o...  \n",
       "1  n person registration at the county clerk's of...  \n",
       "2                                                NaN  \n",
       "3                                                NaN  \n",
       "4                                                NaN  "
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "d4ac830b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def preprocess_text(text):\n",
    "    # Loading spaCy model\n",
    "    nlp = spacy.load('en_core_web_sm')\n",
    "\n",
    "    # Check if text is a string\n",
    "    if isinstance(text, str):\n",
    "        # Converting text to lowercase\n",
    "        text = text.lower()\n",
    "\n",
    "        # Removing extra whitespaces\n",
    "        text = ' '.join(text.split())\n",
    "\n",
    "        # Removing punctuation\n",
    "        text = re.sub(r'[^\\w\\s]', '', text)\n",
    "\n",
    "        # Lemmatization\n",
    "        doc = nlp(text)\n",
    "        text = ' '.join([token.lemma_ for token in doc])\n",
    "\n",
    "    return text\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "7ddf06f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Preprocessing text data\n",
    "df['preprocessed_text'] = df['Answer'].apply(preprocess_text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2ba79b44",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['preprocessed_text'] = df['preprocessed_text'].astype(str)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "1da99840",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Saving preprocessed data as a new CSV file\n",
    "df.to_csv('preprocessed_file.csv', index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f7daa4ee",
   "metadata": {},
   "source": [
    "## NLP Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "fc88d518",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Question</th>\n",
       "      <th>Answer</th>\n",
       "      <th>Answers(411)</th>\n",
       "      <th>preprocessed_text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>What are the requirements for voting by absent...</td>\n",
       "      <td>Voters unable to vote in person on Election Da...</td>\n",
       "      <td>Absentee voting is available if you meet any o...</td>\n",
       "      <td>voter unable to vote in person on election day...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>What is the voter registration deadline?</td>\n",
       "      <td>Primary Election Date is June 7, 2022 (Registe...</td>\n",
       "      <td>n person registration at the county clerk's of...</td>\n",
       "      <td>primary election date be june 7 2022 register ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Where can I cast my vote?</td>\n",
       "      <td>After registering to vote, your Voter Registra...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>after register to vote your voter registration...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>What are the registration qualifications to vote?</td>\n",
       "      <td>Every U.S. citizen who possesses the following...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>every us citizen who possess the follow qualif...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>How to register by mail to vote?</td>\n",
       "      <td>1. Complete a Mail-In Voter Registration Appli...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1 complete a mailin voter registration applica...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                            Question  \\\n",
       "0  What are the requirements for voting by absent...   \n",
       "1           What is the voter registration deadline?   \n",
       "2                          Where can I cast my vote?   \n",
       "3  What are the registration qualifications to vote?   \n",
       "4                   How to register by mail to vote?   \n",
       "\n",
       "                                              Answer  \\\n",
       "0  Voters unable to vote in person on Election Da...   \n",
       "1  Primary Election Date is June 7, 2022 (Registe...   \n",
       "2  After registering to vote, your Voter Registra...   \n",
       "3  Every U.S. citizen who possesses the following...   \n",
       "4  1. Complete a Mail-In Voter Registration Appli...   \n",
       "\n",
       "                                        Answers(411)  \\\n",
       "0  Absentee voting is available if you meet any o...   \n",
       "1  n person registration at the county clerk's of...   \n",
       "2                                                NaN   \n",
       "3                                                NaN   \n",
       "4                                                NaN   \n",
       "\n",
       "                                   preprocessed_text  \n",
       "0  voter unable to vote in person on election day...  \n",
       "1  primary election date be june 7 2022 register ...  \n",
       "2  after register to vote your voter registration...  \n",
       "3  every us citizen who possess the follow qualif...  \n",
       "4  1 complete a mailin voter registration applica...  "
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "ba37bbaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sumy.summarizers.lex_rank import LexRankSummarizer\n",
    "\n",
    "summarizer = LexRankSummarizer()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "9a7f69ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sumy.parsers.plaintext import PlaintextParser\n",
    "\n",
    "document = PlaintextParser.from_string(df['preprocessed_text'], Tokenizer(\"english\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "08ff960a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_summary(text, length=3):\n",
    "    parser = PlaintextParser.from_string(text, Tokenizer(\"english\"))\n",
    "    summary = summarizer(parser.document, length)\n",
    "    summary_text = \"\\n\".join([str(sentence) for sentence in summary])\n",
    "    return summary_text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "4ad98ed8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['SummaryOfficial'] = df['Answer'].apply(get_summary)\n",
    "\n",
    "df['Summary(411)'] = df['Answers(411)'].apply(get_summary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "a59afcf2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Question</th>\n",
       "      <th>Answer</th>\n",
       "      <th>Answers(411)</th>\n",
       "      <th>preprocessed_text</th>\n",
       "      <th>SummaryOfficial</th>\n",
       "      <th>Summary(411)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>What are the requirements for voting by absent...</td>\n",
       "      <td>Voters unable to vote in person on Election Da...</td>\n",
       "      <td>Absentee voting is available if you meet any o...</td>\n",
       "      <td>voter unable to vote in person on election day...</td>\n",
       "      <td>Voters, who are required to be at work while t...</td>\n",
       "      <td>The last day to request an absentee ballot is ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>What is the voter registration deadline?</td>\n",
       "      <td>Primary Election Date is June 7, 2022 (Registe...</td>\n",
       "      <td>n person registration at the county clerk's of...</td>\n",
       "      <td>primary election date be june 7 2022 register ...</td>\n",
       "      <td>Primary Election Date is June 7, 2022 (Registe...</td>\n",
       "      <td>n person registration at the county clerk's of...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Where can I cast my vote?</td>\n",
       "      <td>After registering to vote, your Voter Registra...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>after register to vote your voter registration...</td>\n",
       "      <td>After registering to vote, your Voter Registra...</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>What are the registration qualifications to vote?</td>\n",
       "      <td>Every U.S. citizen who possesses the following...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>every us citizen who possess the follow qualif...</td>\n",
       "      <td>Every U.S. citizen who possesses the following...</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>How to register by mail to vote?</td>\n",
       "      <td>1. Complete a Mail-In Voter Registration Appli...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1 complete a mailin voter registration applica...</td>\n",
       "      <td>If you do not provide your driverâ€™s license ...</td>\n",
       "      <td>nan</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                            Question  \\\n",
       "0  What are the requirements for voting by absent...   \n",
       "1           What is the voter registration deadline?   \n",
       "2                          Where can I cast my vote?   \n",
       "3  What are the registration qualifications to vote?   \n",
       "4                   How to register by mail to vote?   \n",
       "\n",
       "                                              Answer  \\\n",
       "0  Voters unable to vote in person on Election Da...   \n",
       "1  Primary Election Date is June 7, 2022 (Registe...   \n",
       "2  After registering to vote, your Voter Registra...   \n",
       "3  Every U.S. citizen who possesses the following...   \n",
       "4  1. Complete a Mail-In Voter Registration Appli...   \n",
       "\n",
       "                                        Answers(411)  \\\n",
       "0  Absentee voting is available if you meet any o...   \n",
       "1  n person registration at the county clerk's of...   \n",
       "2                                                NaN   \n",
       "3                                                NaN   \n",
       "4                                                NaN   \n",
       "\n",
       "                                   preprocessed_text  \\\n",
       "0  voter unable to vote in person on election day...   \n",
       "1  primary election date be june 7 2022 register ...   \n",
       "2  after register to vote your voter registration...   \n",
       "3  every us citizen who possess the follow qualif...   \n",
       "4  1 complete a mailin voter registration applica...   \n",
       "\n",
       "                                     SummaryOfficial  \\\n",
       "0  Voters, who are required to be at work while t...   \n",
       "1  Primary Election Date is June 7, 2022 (Registe...   \n",
       "2  After registering to vote, your Voter Registra...   \n",
       "3  Every U.S. citizen who possesses the following...   \n",
       "4  If you do not provide your driverâ€™s license ...   \n",
       "\n",
       "                                        Summary(411)  \n",
       "0  The last day to request an absentee ballot is ...  \n",
       "1  n person registration at the county clerk's of...  \n",
       "2                                                nan  \n",
       "3                                                nan  \n",
       "4                                                nan  "
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "8bc16f95",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Voters, who are required to be at work while the polling places are open on Election Day or will be out of town, must absentee vote in person.\\nPlease check with your Circuit or Municipal Clerk to determine if you are entitled to vote by an absentee ballot and to learn the procedures for doing so.\\nUOCAVA voters may register to vote using the FPCA until ten days before an election and may receive and return an absentee ballot by mail, email, or fax.'"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['SummaryOfficial'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "d296d4a5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'voter unable to vote in person on election day may be eligible to vote by absentee ballot most absentee voter must appear before the circuit clerk or municipal clerk and absentee vote in person a few category of absentee voter may request a mail ballot voter who be require to be at work while the polling place be open on election day or will be out of town must absentee vote in person absentee voter who be 65 or old have a permanent or temporary physical disability or be temporarily reside outside their county of residence may absentee vote by mail please check with your circuit or municipal clerk to determine if you be entitle to vote by an absentee ballot and to learn the procedure for do so if you know you will vote by absentee ballot you may visit or contact your circuit or municipal clerkâs office within 45 day of the election voter include within the uniform and overseas citizen absentee voting act uocava such as member of the military and overseas citizen may register to vote and request an absentee ballot by federal post card application fpca uocava voter may register to vote use the fpca until ten day before an election and may receive and return an absentee ballot by mail email or fax absentee ballot be now final vote if you cast an absentee ballot you may no long cast a regular ballot on election day but you may cast an affidavit ballot if you know you will vote by absentee ballot you may visit or contact your circuit or municipal clerkâs office within 45 day of the election for more information call the secretary of stateâs election hotline at 18008296786 or visit our website at wwwyallvotem'"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['preprocessed_text'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "e8eedb76",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Absentee voting is available if you meet any of the criteria below. The last day to request an absentee ballot is 5 days before the election.\\xa0 You can return your absentee ballot request form through the mail or in person. Voted ballots must be postmarked by Election Day and received up to 5 days after the election in order to be counted. Contact your local elections office for more information. You are eligible to vote absentee if you are a qualified and registered voter who will be absent from your county of residence on Election Day, or are: A disabled war veteran who is a patient in any hospital and a citizen of Mississippi A citizen of Mississippi temporarily residing outside the territorial limits of the United States and the District of Columbia An employee engaged in interstate transportation A student, teacher or administrator An employee engaged in offshore employment, or as an employee on a vessel or other watercraft An employee, businessperson, professional, tradesman or worker required to be over 50 miles away from the county of residence on election day due to employment A person with a temporary or permanent physical disability 65 years of age or older A parent, spouse or dependent of a person with a temporary or permanent disability hospitalized more than 50 miles from home county and with such person Election Day A member of a congressional delegation Please check with your voter registrar to determine if you are entitled to vote absentee and to learn the procedures for doing so. You can fill out an absentee ballot request form here. Those who requested an absentee ballot but end up voting in person: You may only do so by a provisional ballot. Do not mail a ballot and vote in person. For specifics, you can find your local county clerk contact info here. U.S. military personnel and overseas citizens can find information on how to register to vote and request an absentee ballot at the Overseas Vote Foundation. Request your Ballot (https://absentee.vote411.org/vote/VoterInformation.htm) (https://absentee.vote411.org/vote/eoddomestic.htm) (https://www.overseasvotefoundation.org/vote/election-official-directory) (https://absentee.vote411.org/vote/VoterInformation.htm) (https://www.usvotefoundation.org/vote/RavaLogin.htm?redirect=/w/domestic_absentee/1.htm) (https://absentee.vote411.org/vote/eoddomestic.htm) (https://www.overseasvotefoundation.org/vote/home.htm) (https://absentee.vote411.org/vote/VoterInformation.htm)'"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Answers(411)'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "03d6abe6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The last day to request an absentee ballot is 5 days before the election.\\nYou are eligible to vote absentee if you are a qualified and registered voter who will be absent from your county of residence on Election Day, or are: A disabled war veteran who is a patient in any hospital and a citizen of Mississippi A citizen of Mississippi temporarily residing outside the territorial limits of the United States and the District of Columbia An employee engaged in interstate transportation A student, teacher or administrator An employee engaged in offshore employment, or as an employee on a vessel or other watercraft An employee, businessperson, professional, tradesman or worker required to be over 50 miles away from the county of residence on election day due to employment A person with a temporary or permanent physical disability 65 years of age or older A parent, spouse or dependent of a person with a temporary or permanent disability hospitalized more than 50 miles from home county and with such person Election Day A member of a congressional delegation Please check with your voter registrar to determine if you are entitled to vote absentee and to learn the procedures for doing so.\\nDo not mail a ballot and vote in person.'"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Summary(411)'][0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72549c57",
   "metadata": {},
   "source": [
    "## SC Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "74f0fa92",
   "metadata": {},
   "outputs": [],
   "source": [
    "df1 = pd.read_csv('sc_voter_faq.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "3c660251",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Question</th>\n",
       "      <th>Answer</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>It is past the voter registration deadline and...</td>\n",
       "      <td>If you\\n\\n\\n\\nmoved to another residence withi...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>What offices, candidates and questions are on ...</td>\n",
       "      <td>The offices, candidates and questions on a par...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>How and where can I vote early in person?</td>\n",
       "      <td>Visit an early voting center in your county du...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Who can vote absentee?</td>\n",
       "      <td>State law allows voters with qualifying reason...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>How can I vote absentee?</td>\n",
       "      <td>Step 1:  Get your application\\n\\nCall, visit o...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                            Question  \\\n",
       "0  It is past the voter registration deadline and...   \n",
       "1  What offices, candidates and questions are on ...   \n",
       "2          How and where can I vote early in person?   \n",
       "3                             Who can vote absentee?   \n",
       "4                           How can I vote absentee?   \n",
       "\n",
       "                                              Answer  \n",
       "0  If you\\n\\n\\n\\nmoved to another residence withi...  \n",
       "1  The offices, candidates and questions on a par...  \n",
       "2  Visit an early voting center in your county du...  \n",
       "3  State law allows voters with qualifying reason...  \n",
       "4  Step 1:  Get your application\\n\\nCall, visit o...  "
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "8629d825",
   "metadata": {},
   "outputs": [],
   "source": [
    "df1['Summary'] = df1['Answer'].apply(get_summary)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "33931848",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Question</th>\n",
       "      <th>Answer</th>\n",
       "      <th>Summary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>It is past the voter registration deadline and...</td>\n",
       "      <td>If you\\n\\n\\n\\nmoved to another residence withi...</td>\n",
       "      <td>moved to another residence in another county p...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>What offices, candidates and questions are on ...</td>\n",
       "      <td>The offices, candidates and questions on a par...</td>\n",
       "      <td>The offices, candidates and questions on a par...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>How and where can I vote early in person?</td>\n",
       "      <td>Visit an early voting center in your county du...</td>\n",
       "      <td>Visit an early voting center in your county du...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Who can vote absentee?</td>\n",
       "      <td>State law allows voters with qualifying reason...</td>\n",
       "      <td>State law allows voters with qualifying reason...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>How can I vote absentee?</td>\n",
       "      <td>Step 1:  Get your application\\n\\nCall, visit o...</td>\n",
       "      <td>Call, visit or send your request for an absent...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                            Question  \\\n",
       "0  It is past the voter registration deadline and...   \n",
       "1  What offices, candidates and questions are on ...   \n",
       "2          How and where can I vote early in person?   \n",
       "3                             Who can vote absentee?   \n",
       "4                           How can I vote absentee?   \n",
       "\n",
       "                                              Answer  \\\n",
       "0  If you\\n\\n\\n\\nmoved to another residence withi...   \n",
       "1  The offices, candidates and questions on a par...   \n",
       "2  Visit an early voting center in your county du...   \n",
       "3  State law allows voters with qualifying reason...   \n",
       "4  Step 1:  Get your application\\n\\nCall, visit o...   \n",
       "\n",
       "                                             Summary  \n",
       "0  moved to another residence in another county p...  \n",
       "1  The offices, candidates and questions on a par...  \n",
       "2  Visit an early voting center in your county du...  \n",
       "3  State law allows voters with qualifying reason...  \n",
       "4  Call, visit or send your request for an absent...  "
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "b69750e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'moved to another residence in another county prior to the October 9 registration deadline, you are not eligible to vote.\\nmoved to South Carolina after the October 9 registration deadline, you are not eligible to vote.\\nVote at the polling place in your previous precinct using a failsafe provisional ballot.'"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1['Summary'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "388cd29c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'If you\\n\\n\\n\\nmoved to another residence within your precinct, you can update your address at your polling place and vote a regular ballot.\\nmoved to a different precinct within your county, you are eligible vote Failsafe (see below).\\nmoved to another residence in another county within 30 days of the election, you are eligible to vote Failsafe (see below).\\nmoved to another residence in another county prior to the October 9 registration deadline, you are not eligible to vote. State law requires you to be registered prior to the deadline to be eligible to vote.\\nmoved to South Carolina after the October 9 registration deadline, you are not eligible to vote. State law requires you to be registered prior to the deadline to be eligible to vote.\\n\\n\\n\\nTwo Options for Voting Failsafe:\\n\\nVote at the polling place in your previous precinct using a failsafe provisional ballot. A failsafe provisional ballot contains only federal, statewide, countywide, and municipality-wide offices.\\nGo to the voter registration office in the county in which you currently reside, change your address, and vote a regular ballot there.'"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1['Answer'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bee42ef4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
