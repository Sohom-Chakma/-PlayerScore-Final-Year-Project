import streamlit as st
from sklearn.preprocessing import StandardScaler
import pandas as pd


# setting page configurations
st.set_page_config(
    page_title="Transforming Data",
    page_icon=":soccer:")

#creating sidebar with caption
st.sidebar.success("Explore my project!")

st.title("Transforming Data")

# Section 1: Data Prep
st.write("Preparing data by creating separate lists for each type of indicatores")

st.code("""
#creating separate tables with positive and negative impact columns only
positive= df.drop(columns= ['Player','Pos', 'Squad','Challenges Lost', 'Err',
        'Nation', 'Comp',  'Take-Ons Tkld', 'Take-Ons Tkld%', 'Carries Mis',
        'Carries Dis', 'Performance CrdY', 'Performance CrdR', 'Performance 2CrdY', 
        'Performance Fls', 'Performance Off', 'Performance PKcon', 'Performance OG', 
        'Aerial Duels Lost', 'Season'])

negative= df[['Challenges Lost','Err','Carries Mis','Carries Dis',
        'Take-Ons Tkld','Take-Ons Tkld%', 'Performance CrdY', 'Performance CrdR',
        'Performance 2CrdY', 'Performance Fls', 'Performance Off',
        'Performance PKcon', 'Performance OG', 'Aerial Duels Lost']]        
        """)

# Section 2: Transforming
st.write("I used the StandardScaler() method to perform the z-score transformation to the dataset.")

st.code("""
        from sklearn.preprocessing import StandardScaler

        # Initialize the StandardScaler
        scaler = StandardScaler()

        # Fit and transform the features for Positive Indicators
        scaled_features = scaler.fit_transform(positive)

        # Convert the scaled features back into a DataFrame
        scaled_positive = pd.DataFrame(scaled_features, columns=positive.columns)

        # Fit and transform Negative Indicators
        scaled_features = scaler.fit_transform(negative)

        # Convert the scaled features back into a DataFrame
        scaled_negative = pd.DataFrame(scaled_features, columns=negative.columns)
""")
# Section 3: Compiling results and categorical columns into final dataframe.
st.subheader("Adding up all scores")
st.code("""
# Fit and transform the features
scaled_features = scaler.fit_transform(negative)

# Convert the scaled features back into a DataFrame
scaled_negative = pd.DataFrame(scaled_features, columns=negative.columns)
        
seasonal_score['Player']= df['Player'] 
seasonal_score['Pos']= df['Pos'] 
seasonal_score['Squad']= df['Squad'] 
seasonal_score['Season']= df['Season'] 
seasonal_score['Comp']= df['Comp'] 

seasonal_score["Sohom's Seasonal Score"]= seasonal_score['Positive Score']-seasonal_score['Negative Score']
        """)






df= pd.read_csv("FBREF Data.csv")

# renaming a column
df.rename(columns={"03-Jan":"1/3"}, inplace= True)

# dropping index column
df.drop(df[df.columns[[0]]], axis=1, inplace= True)

#removing entries with 0 matches played as they would be irrelevent to the final outcome.

df.drop(df[df['90s'] == 0].index, inplace=True)
df.drop(df[df['Pos'] == 'GK'].index, inplace=True)

df.reset_index(drop=True, inplace=True)

#creating table with all necessary columns
features= df[
    [
        '90s',
        'Player',
        'Pos',
        'Squad',
        'Nation',
        'Comp', 
        'Season',
        'Standard Gls',
        'Standard SoT',
        'Standard SoT%',
        'Standard PK',
        'Standard G/Sh',
        'Expected npxG',
        'Expected np:G-xG',
        'Total TotDist',
        'Total PrgDist',
        'Total Cmp',
        'Total Cmp%',
        'Short Cmp',
        'Short Att',
        'Short Cmp%',
        'Medium Cmp',
        'Medium Att',
        'Medium Cmp%',
        'Long Cmp',
        'Long Att',
        'Long Cmp%',
        'Ast',
        'Expected xA',
        'KP',
        '1/3',
        'PPA',
        'CrsPA',
        'PrgP',
        'SCA SCA',
        'SCA SCA90',
        'GCA GCA',
        'GCA GCA90',
        'Tackles TklW',
        'Challenges Tkl',
        'Challenges Att',
        'Challenges Lost',
        'Blocks Blocks',
        'Blocks Sh',
        'Blocks Pass',
        'Int',
        'Clr',
        'Err',
        'Touches Def 3rd',
        'Touches Mid 3rd',
        'Touches Att 3rd',
        'Take-Ons Succ',
        'Take-Ons Succ%',
        'Take-Ons Tkld',
        'Take-Ons Tkld%',
        'Carries TotDist',
        'Carries PrgDist',
        'Carries PrgC',
        'Carries 1/3',
        'Carries CPA',
        'Carries Mis',
        'Carries Dis',
        'Receiving Rec',
        'Receiving PrgR',
        'Performance CrdY',
        'Performance CrdR',
        'Performance 2CrdY',
        'Performance Fls',
        'Performance Fld',
        'Performance Off',
        'Performance PKwon',
        'Performance PKcon',
        'Performance OG',
        'Performance Recov',
        'Aerial Duels Won',
        'Aerial Duels Lost'
        ]
    ]
#creating separate tables with positive and negative impact columns only
positive= features.drop(columns= ['Player','Pos', 'Squad','Challenges Lost', 'Err','Nation', 'Comp',  'Take-Ons Tkld', 'Take-Ons Tkld%',
'Carries Mis', 'Carries Dis',
'Performance CrdY', 'Performance CrdR',
'Performance 2CrdY', 'Performance Fls',
'Performance Off', 'Performance PKcon',
'Performance OG', 'Aerial Duels Lost', 'Season'])

negative= features[['Challenges Lost',
'Err',
'Carries Mis',
'Carries Dis',
'Take-Ons Tkld',
'Take-Ons Tkld%',
'Performance CrdY',
'Performance CrdR',
'Performance 2CrdY',
'Performance Fls',
'Performance Off',
'Performance PKcon',
'Performance OG',
'Aerial Duels Lost']]


# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the features
scaled_features = scaler.fit_transform(positive)

# Convert the scaled features back into a DataFrame
scaled_positive = pd.DataFrame(scaled_features, columns=positive.columns)

# Fit and transform the features
scaled_features = scaler.fit_transform(negative)

# Convert the scaled features back into a DataFrame
scaled_negative = pd.DataFrame(scaled_features, columns=negative.columns)

seasonal_score= pd.DataFrame()

scaled_positive['Positive Score'] = scaled_positive.sum(axis=1)
seasonal_score['Positive Score']= scaled_positive[['Positive Score']]

scaled_negative['Negative Score'] = scaled_negative.sum(axis=1)
seasonal_score['Negative Score']= scaled_negative[['Negative Score']]

seasonal_score['Player']= df['Player'] 
seasonal_score['Pos']= df['Pos'] 
seasonal_score['Squad']= df['Squad'] 
seasonal_score['Season']= df['Season'] 
seasonal_score['Comp']= df['Comp'] 


seasonal_score["PlayerScore"]= seasonal_score['Positive Score']-seasonal_score['Negative Score']

#Section 4: Results

st.subheader("Top 100")
st.write("Below are the top 100 players in the order of their Season Score")

result= seasonal_score.sort_values(by= "PlayerScore", ascending= False).head(100)

st.dataframe(result)


%store seasonal_score