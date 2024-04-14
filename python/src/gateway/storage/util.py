import pika, json
import logging

def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except Exception as err:
        return err, 500
    
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        channel.basic_publish(
            exchange="",
            routing_key="video", # name of the queue in rabbit mq
            body=json.dumps(message), # converts a python object into a string
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE # messages are persisted in the queue in case of a pod crash or any other issue
            )
        )
    except Exception as err:
        fs.delete(fid)
        return "Internal server error", 500