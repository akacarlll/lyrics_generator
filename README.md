# 🎤 Lyrics Generation Project

## 📋 Overview
This project focuses on generating song lyrics inspired by French rappers. Using data science and natural language processing (NLP) techniques, the project analyzes lyrics, extracts key patterns, and generates new verses mimicking the style of specific artists.

## 🎯 Objectives
- Retrieve and preprocess song lyrics from **Genius**.
- Analyze lyrics to uncover stylistic elements, including common words and themes.
- Generate new lyrics using advanced machine learning models.
- Provide tools for sentiment analysis and visualization of lyrics data.

## 🛠️ Tools and Technologies
- **Python 3.12.4**: Programming language.
- **Kedro**: For project pipeline management and reproducibility.
- **Pandas**: For data manipulation.
- **NLP Libraries**: Spacy, NLTK, or Transformers for text processing and generation.
- **Visualization**: Matplotlib and WordCloud for graphical analysis.
- **Genius API**: To retrieve song lyrics.

## 📂 Project Structure
The project follows a structured pipeline to ensure clean and efficient workflows:
```
├── data
│   ├── raw                # Raw data retrieved from Genius
│   ├── 02_intermediate    # Preprocessed data ready for analysis
|   ├── 03_advanced        # Preprocessed data with new information added
|   ├── 04_feature         # Wordcloud
├── notebooks              # Jupyter notebooks for analysis and testing
├── src
│   ├── preprocessing      # Scripts for data cleaning and preprocessing
│   ├── add_features       # Scripts for adding new informations to the datasets
│   ├── data_analysis      # Scripts for word cloud, sentiment analysis and summarization
│   ├── concatenate        # Code to merge all the datasets
├── tests                  # Unit tests for the project
├── README.md              # Project overview
└── requirements.txt       # Dependencies
```

## 📊 Features
1. **Lyrics Retrieval**: 
   - Automates the retrieval of lyrics for specific artists and songs using the Genius API.
2. **Data Analysis**:
   - Word clouds to visualize the most cited words by artists.
   - Sentiment analysis of lyrics.
3. **Lyrics Generation**:
   - Leverages deep learning models (e.g., GPT2, CamemBert) to generate new lyrics mimicking the artist's style, or to classify these lyrics.
4. **Visualization**:
   - Provides graphical representations of word frequencies and thematic elements.

## 🚀 Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.12 or later
- pip (Python package manager)
- conda 

### Installation
1. Clone this repository:
   ```powershell
   git clone https://github.com/akacarlll/lyrics_generator.git
   ```
2. Navigate to the project directory:
   ```powershell
   cd lyrics_generator
   ```
3. Install the dependencies:
   ```powershell
    pip install -r requirements.txt
            or
    conda env create -f environment.yml
   ```

### Usage
1. Retrieve and preprocess data:
   ```
    Use :
        python get_lyrics.py
            or
    Use :
        the scrape.ipynb
   
   ```
2. Analyze lyrics:
   ```powershell
    kedro run --pipeline thrid_pipeline
   ```
3. Train and generate lyrics:
   ```
   Use the notebook finetune_GPT2.ipynb
   ```


## 📚 Future Work
- Expand the dataset to include more artists and genres.
- Improve the lyric generation model using transformer-based architectures like GPT3.
- Implement more advanced analyses, such as rhyme schemes or thematic clustering.


## 📜 License
This project is licensed under the [MIT License](LICENSE).
