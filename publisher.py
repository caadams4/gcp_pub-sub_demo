import os
#to import that, use pip install google-cloud-pubsub
# or, go to settings and add package google-cloud-pubsub
from google.cloud import pubsub_v1

# you need to set the location of GCP credentials json file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/squanch/gcp/woven-respect-370021-e5a62b30172e.json"

# you need to set your project id
PROJECT_ID = 'woven-respect-370021'

TOPIC_NAME = 'myTopic' # Set this to something, but be sure that it matches the topic name used in the subscriber code.

topic_full_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=PROJECT_ID,
    topic=TOPIC_NAME,
)

# Make publisher object
publisher = pubsub_v1.PublisherClient()

# Make topic. Include this line only once. After running the first time, comment this line out
#publisher.create_topic(name = topic_full_name)

# Send a message
if True:
    # this method is works on some versions of the python google.cloud package, but not on all versions
    # is this code crashes, then set change True to False, and use the other method to send messages to pubsub
    future = publisher.publish(topic_full_name, b'My first message!', spam='eggs')
    print(future.result())
    print("Sent first")
    future = publisher.publish(topic_full_name, b'My second message!', spam='eggs')
    print(future.result())
    print("Sent second")
else:
    publisher.publish(topic_full_name, b'My first message!', spam='eggs')
    print("Sent first")
    publisher.publish(topic_full_name, b'My second message!', spam='eggs')
    print("Sent second")