import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

def load_data(name):
    return pd.read_csv(name)


data = load_data("SpotifyFeatures.csv")

#CODE TO RUN ML

# from sklearn.ensemble import RandomForestRegressor
# from sklearn.preprocessing import scale
# import matplotlib.pyplot as plt
# from sklearn import set_config 

# df = data

# #removing the unnecessary data
# df = df.drop('genre', 1)
# df = df.drop('track_name', 1)
# df = df.drop('artist_name' , 1)


# Y = df["popularity"]  
# X = df.iloc[:, 1:]
# # define the model
# model = RandomForestRegressor()
# # fit the model
# model.fit(X, Y)
# # get importance
# importance = model.feature_importances_

# # summarize feature importance
# for i in range(len(importance)):
#     print(X.columns[i] + " : "+ str(importance[i].round(6)))
    
# # plot feature importance
# plt.xticks(rotation=90)
# plt.bar([x for x in X.columns], importance, color = 'orange')

# m.xaxis.label.set_color('yellow')        #setting up X-axis label color to yellow
# m.yaxis.label.set_color('blue') 
# plt.show()

if st.checkbox("Show Raw Data"):
    st.write(data)

#Visualization1
chart_pop_1=alt.Chart(data).mark_point(filled=True).encode(
    alt.X('liveness:Q',scale=alt.Scale(zero=False)),
    alt.Y('energy:Q',scale=alt.Scale(zero=False)),
    alt.Size('duration_ms:Q'),
    alt.Color('genre:N'),
    alt.OpacityValue(0.7),
    tooltip = [alt.Tooltip('track_name:N'),
               alt.Tooltip('artist_name:N'),
              ]

).properties(width=800,height=500)



#Visualization2
brush = alt.selection_interval()

scat= alt.Chart(data).mark_point(filled=True).encode(
    alt.X('popularity',scale=alt.Scale(zero=False)),
    alt.Y('count()',scale=alt.Scale(zero=False)),
    color= alt.condition(brush, alt.value("red"), alt.value("grey"))
    ).add_selection(brush)

hist1= alt.Chart(data).transform_filter(brush).mark_bar(filled=True).encode(
    alt.X('genre'),
    alt.Y('count()'),
    alt.Color('genre')
    )


#Visualization3

data1 = load_data("SpotifyFeatures.csv")
df = data1
#selecting only the songs with popularity greater than 90
df.drop(df[df['popularity'] < 90].index, inplace = True) 
input_dropdown = alt.binding_select(options=['Dance', 'Electronic', 'Hip-Hop', 'Rap', 'Indie', 'Pop',
       'Reggaeton', 'R&B', 'Rock'], name="Select Genre  ")
picked = alt.selection_single(encodings=["color"], bind=input_dropdown)
hist = alt.Chart(df).mark_bar().encode(
    alt.X("artist_name", scale = alt.Scale(zero=False)), 
    alt.Y("count(popularity)", scale = alt.Scale(zero=False)), 
    alt.Color("genre")
    ).properties(width=800,height=500)




st.title("Song Popularity Analysis")
st.header("Feature importance using RandomForest Regressor ")


image = Image.open('feature_importance.jpeg')
st.text("Extracting top features for song popularity")
st.image(image, caption='Feature Importance')

st.header("Visualizing Top 2 Features with respect to Genre and Duration")
st.text("Select any level of popularity to discover how songs are distributed on the basis of top two features (liveness and Energy)")

desired_pop = st.slider("Select Popularity",1,100,1)
pop_filter= chart_pop_1.transform_filter(f"datum['popularity']== {desired_pop}")
st.write(pop_filter)

st.header("Visualizing the relation between Genre and Popularity")
st.text("Brush over the scatter plot to select given range of points and see the top genre change in the histogram")
selection = alt.selection_interval(bind='scales')
st.write(scat & hist1)

st.header("Visualizing the Top Artists(based on popularity) and their Genre")
st.text("Select the genre in drop down to discover top artist in that genre")
st.write(hist.encode(
    color=alt.condition(picked, "genre:N", alt.value("lightgray"))
).add_selection(picked))

st.header("Conclusion")
'''By using the above visualizations, we can get a clear idea about the features that drive the popularity of the songs. 
The genre and the artist that have produced the most popular 
songs till date can also be discovered using the above visualizations.'''

