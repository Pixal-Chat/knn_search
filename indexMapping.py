indexMapping = {
    "properties":{
        "id":{
            "type": "long"
        },
        "author":{
            "type": "text"
        },
        "title":{
            "type": "text"
        },
        "content":{
            "type": "text"
        },
        "image_src":{
            "type": "text"
        },
        "TitleContent":{
            "type": "text"
        },
        "TitleContentVector":{
            "type": "dense_vector",
            "dims": 1536,
            "index": True,
            "similarity": "l2_norm"
        },
    }
}