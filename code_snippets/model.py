model = transformers.pipeline("text-generation", model='gpt-j-125M')
collection.create_model('my-gpt', model)
collection.create_watcher('my_gpt', filter_={'text': {'$exists': 1}}, key='text')