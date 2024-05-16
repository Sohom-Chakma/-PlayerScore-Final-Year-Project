import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import numpy as np
import seaborn as sns
import altair as alt

# Setting page configurations
st.set_page_config(
    page_title="'PlayerScore'",
    page_icon=":soccer:",
    layout='wide'
)

#######################################################################################################################################################################################################################
# Title as shown at the top of the page
st.title("Enhancing Football Awards with 'PlayerScore':soccer:")

#######################################################################################################################################################################################################################
#creating sidebar with caption
st.sidebar.success("Explore my project!")

#######################################################################################################################################################################################################################

st.header("Hello!")
st.markdown(
    """
    This is my first Data Analytics personal project, marking the beginning of my journey into coding and analytics. 

    Throughout this project I use Python and Tableau for data manipulation. I am eager to keep learning and uncover new insights! 

    I hope you enjoy my project!
    """
)

#######################################################################################################################################################################################################################
st.subheader    ("Problem Statement")

st.write("""
    Traditional football metrics often carry biases, influencing player evaluation and impacting their career prospects. My project, "PlayerScore," aims to provide a fair and comprehensive assessment of a player’s season by using advanced statistics. This system will support fair decision-making by sports journalists, analysts, and coaches, challenging outdated evaluation methods and promoting merit-based recognition in the industry. Drawing inspiration from Michael Lewis's critique of MLB scouting, "PlayerScore" seeks to transform football analytics for greater equity and accuracy in player valuation.         
""")
#######################################################################################################################################################################################################################

st.subheader("Methodology")

st.write("""
The dataset tracks individual player statistics in separate columns as numerical data. To compare a player’s individual impact, I will use the z-score value for each player. This measures how far the individual’s score deviates from the population mean. A higher z-score indicates better performance for that metric.

""")

# zscore formula
st.image(
    'z_score.svg',
    width=150
)

st.write("""
The z-score value is calculated using data from the 2017 to 2024 seasons, allowing for cross-season comparisons of player performance.

The final score for each player will be the sum of all metrics' z-scores, providing a performance rating for a given season. The player with the higher score is deemed to be the most impactful. 

The formula for the final score is as follows:
""")

# PlayerScore formula
st.image(
    'PlayerScore.svg',
    width=500
)

st.write("It should be noted that, since I am trying to final the player impact, there are stats that can negatively impact the player’s score. Metrics such as aerial duels lost and unsuccessful tackles should detract from the final so the z-score sum of these ‘negative’ metrics will be subtracted from the final score.")

resources = pd.DataFrame(
    {
        "Data": [
            "FBREF Database",
            "Ballon D'Or Shortlist (1956-2023)"
        ],
        "Links": [
            'Challenges Lost',
            'Err'
            ],
    }
)


st.dataframe(data=resources,
    hide_index=True
)

#######################################################################################################################################################################################################################

# Paragraph 1, describing the data. 
st.subheader("About data")
st.write("""
         
         The dataset was scraped from a database hosted by FBREF, the most comprehensive publicly available stats tracker for football.
         
         In addition to statistical metrics (Goals, Assists, Tackles, Saves, etc.) it also contains categorical data about the player (Nationality, Club, Position, etc.). 

        It should be noted that, although FBREF has data that goes back to the 1800s, it only in the 2017 seasons when deeper statistics were being tracked making for more numerous and varied stats tracking. In a sport with such a differs array of skill sets and roles it would help to paint a better picture of a player’s impact by taking into a variety of stats. Because of this I will only be scraping data from the 2017 season and onwards.

         The following steps were taken to collect and organize the data:
         1. Scrape each desired webpage
         2. Append to a list for individual seasons for merging
         3. Further append to a list contain merged data for each season
         4. Concatinate vertically to create the final dataset.
         """)

#######################################################################################################################################################################################################################
st.header("EDA")

st.subheader("Some analytical questions:")

st.write("- Is there a correlation among the numerical data ?")
st.write("The heatmap shows that the columns are generally unrelated to one another. However, the 'Order' and 'Points' columns appear to have a moderately negative correlation. This is because the more poinst a player has, the higher their rankings in the polls.  ")

st.image(
    'numeric_corr.png',
    width=500
)

#######################################################################################################################################################################################################################

st.write("- Is there a correlation between the different Positions (GK, DF, MF, FW) and the Points column?")
st.write("Although it shows that the 'Points' column is unrelated to the position, the positive relation with the FW position shows that they are likely to score higher than the other positions, and win the Ballon D'Or.")
st.image(
    'pos_corr.png',
    width=500
)
#######################################################################################################################################################################################################################

st.subheader("Analytical Results")
st.write("""
         1. Due to the strong correlation between the FW position and the 'Points' column we can conclude that specific positions are more likely to score higher.
         2. The positive relationship between points and FW position is further supported by this scatterplot which shows how many points players of each position scored throughout the years. We can see that FWs tend to be nominated more often and score higher and in higher volume. 
         3. From the dashboard we can see that, historically, the most Ballon D'Or candidates come from European countries, with the top 3 being Germany, Italy and France. The highest concentration of nominees comes from South America, most notably Argentina and Brazil.  
         """)

#######################################################################################################################################################################################################################

st.subheader("My Dashboard")

# Embed code as a string
embed_code = '''<div class='tableauPlaceholder' id='viz1715610356051' style='position: relative'><noscript><a href='#'><img alt='Ballon D&#39;Or Insights Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1_17155351460450&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Book1_17155351460450&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1_17155351460450&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1715610356051');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1200px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1200px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='1577px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''

# Use the HTML component to embed your Tableau dashboard
components.html(embed_code, height=800)

st.divider()

#######################################################################################################################################################################################################################

st.subheader("Resources")

resources = pd.DataFrame(
    {
        "Data": [
            "FBREF Database",
            "Ballon D'Or Shortlist (1956-2023)"
        ],
        "Links": [
            "https://fbref.com/en/comps/Big5/Big-5-European-Leagues-Stats",
            "https://www.kaggle.com/datasets/davidantonioteixeira/ballon-dor"
        ],
    }
)


st.data_editor(
    resources,
    column_config={
        "Links": st.column_config.LinkColumn(
        ),
    },
    hide_index=True,
)