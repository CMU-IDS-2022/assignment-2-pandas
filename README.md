# CMU Interactive Data Science Assigment 2

* **Team members**: ruhihemp@andrew.cmu.edu and swapnilk@andrew.cmu.edu (Update XXXX with your team's emails)
* **Online URL**: https://share.streamlit.io/cmu-ids-2022/YYYY/master/streamlit_app.py (Update YYYY with your repo name)

## Instructions

### Run Locally

Check out the Streamlit [getting started](https://docs.streamlit.io/en/stable/getting_started.html) guide and setup your Python environment.

To run the application locally, install the dependencies with `pip install -r requirements.txt` (or another preferred method to install the dependencies listed in `requirements.txt`). Then run `streamlit run streamlit_app.py`.

### Deploy to Streamlit Sharing

Before you can view your application online, you need to have it set up with Streamlit Cloud. 
Sign up for a [free Starter Streamlit Cloud account](https://streamlit.io/cloud). 

Then, go to [share.streamlit.io](https://share.streamlit.io) to deploy your Streamlit app by creating a new app and pointing it to your github repo.

Once the repo is set up, please update the URL as the top of this readme and add the URL as the website for this GitHub repository.

### Deliverables

A clear description of the goals of your project. Describe the question that you are enabling a user to answer. The question should be compelling and the solution should be focused on helping users achieve their goals. 
What factors should a person consider while producing popular music?
In this project , we are using the SpotifyFeatures dataset that has 18 columns and 232726 rows.  The columns include artist name, genre and different  music features like acousticness, speechiness, loudness, duration_ms etc  and the popularity (between 1 and 100)for 232726 different tracks. The goal of our project is to find out ultimately what features drive the popularity of music and what kind of music is liked the most by the spotify users so as to give the music producers a better idea.
We have used three different interactive visualizations to help users gain insights of popularity with respect to all the different columns. 
A rationale for your design decisions. How did you choose your particular visual encodings and interaction techniques? What alternatives did you consider and how did you arrive at your ultimate choices?
 We wanted to start by selecting two top most features related to popularity from the 11 features available for each track. This step is important because one track cannot have all 11 features, thus it is important for a user to know that popularity is the most dependent on which two top features . We have used Random Forest Regressor to find out the feature importance of our model. We have converted our entire data to numerical format to run the model. The code for this has been commented on in the python file as it takes a lot of time to run the model on around 250,000 rows.
Our first visualization focuses on plotting a scatter plot using the top features - liveness and energy as predicted by the model. The genre of the track has been used to add color and duration_ms has been used to determine the size of the points in the scatter plot. The user can select the popularity by using the selection slider and can get a fair idea about what is the liveness, energy , genre and duration of the track belonging to that popularity score. A user will generally be interested in finding out the liveness, energy , genre and duration of tracks with a higher popularity so if he/she wants to produce music, they know what features it should have to gain popularity from spotify users.
For producing music, the first step is deciding the genre that is the most popular among spotify users. Thus, for our second visualization we decided to display scatter and histogram charts paired with brush feature plot to show what genre has the maximum count for a range of popularity. The alternative we considered here was to include the time period of each track in this visualization to get a better understanding. Because every time period is famous for its own genre of music. The 90s was famous for Jazz music and the 2020s are more famous for Rap music. But unfortunately this data wasn't available in the dataset and we couldn't integrate it from any other source.
Artist_name  plays an important role in the popularity of a track. It is useful to know what genre sung by that artist has gained more popularity. These insights can help a music producer take inspiration from the tracks of a specific genre produced by the top artists. In this case it is only beneficial to know the genres of only those artists who have gained a high popularity ( > 95) . Thus we have sliced the data accordingly. The Histogram in the third visualization shows the popularity of the songs sung by an artist based on the genre input given by the user. 
An overview of your development process. Describe how the work was split among the team members. Include a commentary on the development process, including answers to the following questions: Roughly how much time did you spend developing your application (in people-hours)? What aspects took the most time?
Both the team members worked closely in developing the interactive visualizations. We spent a considerable amount of time selecting a dataset and understanding that data before we started working with it. We referred to the altair code done in the lecture alongside the Professor. We started by  cleaning the data to perform ML algorithms and gaining insights from it. Then we started with coding the interactive  visualization graphs using altair and ended with deploying it to streamlit. We spent around 15 hours per person in developing the overall application along with the documentation. 
We wanted the visualizations to be useful and support our problem statement. Thus we spent the maximum time on  choosing which columns to include in our visualization and include only those that have an impact on our output.
A success story of your project. Describe an insight or discovery you gain with your application that relates to the goals of your project.
From the first visualization you can see that less popular songs (Score: 3) have low liveness (0.05 - 0.02) and low energy rating (0.02 - 0.04). More popular songs (Score: 76) have high liveness(0.5 - 0.15) and low energy rating (0.4 - 0.85).
In visualization 2 we can see that popularity between 90 and 100 , “POP” genre has the highest count , followed by “DANCE”. Thus tracks with these genres are gaining the maximum popularity.
From the visualization three, you can see that Ariana Grande has a higher number of popular songs that belong to the dance genre than the pop genre. Also in the pop category, Post Malone and XXXTENTACION have the highest number of popular records. Thus, if you want to listen to good rap music or produce rap music, these artists should be your inspiration.
 

