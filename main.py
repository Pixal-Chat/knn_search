# %%
import pandas as pd # type: ignore

# %%
df = pd.read_csv("news_1.csv")
df.head()

# %%
df.dropna(inplace=True)
df.shape

# %%
df["TitleContent"] = df['title'] + df["content"]
df.head()

# %%
from openai import OpenAI
client = OpenAI(api_key="")

def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input = [text], model=model).data[0].embedding

# %%
df["TitleContentVector"] = df["TitleContent"].apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))
df.to_csv("embedded_1.csv")

# %%
from elasticsearch import Elasticsearch
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", ""),
    ca_certs=""
)
es.ping()

# %%
from indexMapping import indexMapping
import numpy as np

# %%
es.indices.create(index="news_content_14", mappings=indexMapping)

# %%
embedding_df = pd.read_csv("embedded_1.csv", index_col=0)
embedding_df["TitleContentVector"] = embedding_df.TitleContentVector.apply(eval).apply(np.array)

# %%
docs = embedding_df.to_dict("records")
docs[:6]

# %%
for doc in docs:
    try:
        es.index(index="news_content_14", document=doc, id=doc["id"])
    except Exception as e:
        print(e)

# %%
es.count(index="news_content_14")

# %%
input_keyword = "facebook attributes certain filtering problems on human judges rather than artificial intelligence."
vector_of_input_keyword = get_embedding(input_keyword)

# %%
query = {
    "field" : "TitleContentVector",
    "query_vector" : vector_of_input_keyword,
    "k" : 10,
    "num_candidates" : 500, 
}

res = es.knn_search(index="news_content_14", knn=query , source=["title","author","content","image_src"])
res["hits"]["hits"]


