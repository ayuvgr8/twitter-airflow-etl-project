# twitter-airflow-etl-project

This is End-To-End Data Engineering Project using Airflow and Python. In this project, we will extract data using Youtube API, use python to transform data, deploy the code on Airflow/EC2 and save the final result on Amazon S3.



Through some Google searching, I discovered that I could retrieve comments from specific YouTube videos. This got me thinking about developing a simple ETL to extract data from the Google Data API and use the data to get some actionable insights that might help him to improve the content.
![image](https://github.com/ayuvgr8/youtube_comments-airflow-etl-project/assets/49532650/f1d89430-94d1-4fce-9f7b-277768da7f85)


### Data extraction

Google has simplified their API usage, providing an API explorer that lets me experiment with queries and see the returned data directly within the explorer itself.

