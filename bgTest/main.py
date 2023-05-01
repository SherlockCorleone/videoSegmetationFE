from flask import Flask, request
import json
import numpy as np
import pandas as pd
app = Flask(__name__)


@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ


@app.route('/video/upload', methods=["POST"])
def videoUpload():
    print(request.files)
    responce = {
        "msg": "操作成功",
        "code": 200,
        "video": {
            "videoId": 123,
            "videoName": 123
            }
        }
    return json.dumps(responce)


@app.route('/subvideo/splitvideo', methods=["GET"])
def subGet():
    responce = {
            "msg": "操作成功",
            "code": 200,
            "subVideoList": [
                {
                    "subVideoId": 183,
                    "subVideoName": "SC20230428133728-0.mp4",
                    "parentVideoId": 11,
                    "subVideoUrl": "/1/data/split_video/SCRL/TransNetV2/SC20230428133728/SC20230428133728-0.mp4",
                    "sceneBoundaryId": 8,
                    "sceneBoundaryType": "null",
                    "shotBoundaryType": "null"
                },
                {
                    "subVideoId": 184,
                    "subVideoName": "SC20230428133728-1.mp4",
                    "parentVideoId": 11,
                    "subVideoUrl": "/1/data/split_video/SCRL/TransNetV2/SC20230428133728/SC20230428133728-1.mp4",
                    "sceneBoundaryId": 8,
                    "sceneBoundaryType": "null",
                    "shotBoundaryType": "null"
                },
                {
                    "subVideoId": 185,
                    "subVideoName": "SC20230428133728-10.mp4",
                    "parentVideoId": 11,
                    "subVideoUrl": "/1/data/split_video/SCRL/TransNetV2/SC20230428133728/SC20230428133728-10.mp4",
                    "sceneBoundaryId": 8,
                    "sceneBoundaryType": "null",
                    "shotBoundaryType": "null"
                },
                {
                    "subVideoId": 186,
                    "subVideoName": "SC20230428133728-11.mp4",
                    "parentVideoId": 11,
                    "subVideoUrl": "/1/data/split_video/SCRL/TransNetV2/SC20230428133728/SC20230428133728-11.mp4",
                    "sceneBoundaryId": 8,
                    "sceneBoundaryType": "null",
                    "shotBoundaryType": "null"
                },
                {
                    "subVideoId": 187,
                    "subVideoName": "SC20230428133728-12.mp4",
                    "parentVideoId": 11,
                    "subVideoUrl": "/1/data/split_video/SCRL/TransNetV2/SC20230428133728/SC20230428133728-12.mp4",
                    "sceneBoundaryId": 8,
                    "sceneBoundaryType": "null",
                    "shotBoundaryType": "null"
                },
                {
                    "subVideoId": 188,
                    "subVideoName": "SC20230428133728-13.mp4",
                    "parentVideoId": 11,
                    "subVideoUrl": "/1/data/split_video/SCRL/TransNetV2/SC20230428133728/SC20230428133728-13.mp4",
                    "sceneBoundaryId": 8,
                    "sceneBoundaryType": "null",
                    "shotBoundaryType": "null"
                },
                {
                    "subVideoId": 189,
                    "subVideoName": "SC20230428133728-2.mp4",
                    "parentVideoId": 11,
                    "subVideoUrl": "/1/data/split_video/SCRL/TransNetV2/SC20230428133728/SC20230428133728-2.mp4",
                    "sceneBoundaryId": 8,
                    "sceneBoundaryType": "null",
                    "shotBoundaryType": "null"
                },
                {
                    "subVideoId": 190,
                    "subVideoName": "SC20230428133728-3.mp4",
                    "parentVideoId": 11,
                    "subVideoUrl": "/1/data/split_video/SCRL/TransNetV2/SC20230428133728/SC20230428133728-3.mp4",
                    "sceneBoundaryId": 8,
                    "sceneBoundaryType": "null",
                    "shotBoundaryType": "null"
                }
            ]
        }
    return json.dumps(responce)


@app.route('/sceneboundary/getboundary', methods=["GET"])
def scenceGet():
    responce = {
        "msg": "操作成功",
        "code": 200,
        "data": [{
            "video_id": "SC20230428133728",
            "shot_id": 0,
            "bound_label": 0,
            "start_time": "00:00:00.000",
            "start_frame": 0,
            "end_time": "00:00:01.733",
            "end_frame": 52
        },
        {
            "video_id": "SC20230428133728",
            "shot_id": 1,
            "bound_label": 0,
            "start_time": "00:00:01.767",
            "start_frame": 53,
            "end_time": "00:00:03.033",
            "end_frame": 91
        },
        {
            "video_id": "SC20230428133728",
            "shot_id": 2,
            "bound_label": 0,
            "start_time": "00:00:03.067",
            "start_frame": 92,
            "end_time": "00:00:05.833",
            "end_frame": 175
        },
        {
            "video_id": "SC20230428133728",
            "shot_id": 3,
            "bound_label": 1,
            "start_time": "00:00:05.867",
            "start_frame": 176,
            "end_time": "00:00:06.367",
            "end_frame": 191
        },
        {
            "video_id": "SC20230428133728",
            "shot_id": 4,
            "bound_label": 0,
            "start_time": "00:00:06.400",
            "start_frame": 192,
            "end_time": "00:00:18.500",
            "end_frame": 555
        },
        {
            "video_id": "SC20230428133728",
            "shot_id": 5,
            "bound_label": 0,
            "start_time": "00:00:18.533",
            "start_frame": 556,
            "end_time": "00:00:20.000",
            "end_frame": 600
        },
        {
            "video_id": "SC20230428133728",
            "shot_id": 6,
            "bound_label": 0,
            "start_time": "00:00:20.033",
            "start_frame": 601,
            "end_time": "00:00:25.667",
            "end_frame": 770
        },
        {
            "video_id": "SC20230428133728",
            "shot_id": 7,
            "bound_label": 0,
            "start_time": "00:00:25.700",
            "start_frame": 771,
            "end_time": "00:00:28.000",
            "end_frame": 840
        },
        {
            "video_id": "SC20230428133728",
            "shot_id": 8,
            "bound_label": 0,
            "start_time": "00:00:28.033",
            "start_frame": 841,
            "end_time": "00:00:30.967",
            "end_frame": 929
        },
        {
            "video_id": "SC20230428133728",
            "shot_id": 9,
            "bound_label": 1,
            "start_time": "00:00:31.000",
            "start_frame": 930,
            "end_time": "00:00:31.633",
            "end_frame": 949
        },
        {
            "video_id": "SC20230428133728",
            "shot_id": 10,
            "bound_label": 0,
            "start_time": "00:00:31.667",
            "start_frame": 950,
            "end_time": "00:00:37.333",
            "end_frame": 1120
        },
        {
            "video_id": "SC20230428133728",
            "shot_id": 11,
            "bound_label": 0,
            "start_time": "00:00:37.367",
            "start_frame": 1121,
            "end_time": "00:00:38.133",
            "end_frame": 1144
        },
        {
            "video_id": "SC20230428133728",
            "shot_id": 12,
            "bound_label": 0,
            "start_time": "00:00:38.167",
            "start_frame": 1145,
            "end_time": "00:00:39.600",
            "end_frame": 1188
        }
    ],
        "sceneBoundary": {
            "sceneBoundaryId": 7,
            "sceneBoundaryUrl":
            "F:/Work/CODE/Web/bacgroundClip/bgTest/SC20230422174818.ndjson",
            "sceneBoundaryType": 2,
            "shotBoundaryType": 2,
            "videoId": 4,
            "createDate": "2023-04-23T09:02:43.000+00:00"
            }
    }

    return json.dumps(responce)
if __name__ == '__main__':
   app.run(host="127.0.0.1", port=8080, debug=True)
