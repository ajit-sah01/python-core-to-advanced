import pandas as pd
from ydata_profiling import ProfileReport
#  pip install ydata-profiling


df = pd.read_csv("data.csv")

profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("report.html")
