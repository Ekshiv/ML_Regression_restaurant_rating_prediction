from nturl2path import url2pathname
import requests

url="https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants/download"

r=requests.get(url)
print(r)
