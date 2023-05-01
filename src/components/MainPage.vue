<template>
    <div class="container">

        <div class="header">
            <img src="../assets/SplitVertical32Filled.svg" alt="" />
            <nav>
                <a>首页</a>
                <a>视频场景分割</a>
                <button class="btn">登录</button>
            </nav>
        </div>
        <div class="body">
            <div class="left" v-bind:style="{backgroundColor:bg}">
                <div class="videoContainer">
                    <div class="initContainer" v-show="!styleControl.videoShow">
                        <h1 class="headline">视频分割系统</h1>
                        <p class="description">
                            现今的信息技术水平极速发展，极大的影响了人们生活的方方面面，人工智能也逐渐走进我们的生活，本系统基于当前最新的视频场景分割算法搭建，它的目的是将视频按照场景内容的不同划分为若干个子视频，每个子视频包含一个或多个连续的镜头，这些片段可用于进行剪辑、提取视频主题，生成视频摘要，检索相关视频等工作。
                        </p>
                        <div v-show="!styleControl.videoShow" class="uploadFile" @click="openFileChose">
                            <p>选择文件</p>
                            <input class="input" type="file" accept="video/*" @change="upload" ref="input">
                        </div>
                    </div>

                    <h1 v-show="styleControl.videoShow" class="title">{{ playingVideo }}</h1>
                    <div v-show="styleControl.videoShow" id="mui-player"></div>
                </div>
                <div class="modeSelect" v-show="styleControl.videoShow">
                    <el-tag type="warning" class="modeTag">镜头分割模式：</el-tag>
                    <el-select v-model="modeSelected.shot" clearable placeholder="请选择镜头分割模式">
                        <el-option v-for="item in shotOptions" :key="item.value" :label="item.label" :value="item.value">
                        </el-option>
                    </el-select>
                    <el-tag type="warning" class="modeTag">场景分割模式：</el-tag>
                    <el-select v-model="modeSelected.scene" clearable placeholder="请选择场景分割模式">
                        <el-option v-for="item in sceneOptions" :key="item.value" :label="item.label" :value="item.value">
                        </el-option>
                    </el-select>
                </div>
                <div class="functionContainer">
                    <button class="startAnalysis" v-show="styleControl.videoShow" @click="startAnalysis">获取场景边界</button>
                    <button class="startAnalysis" v-show="styleControl.videoShow" @click="getSubVideo">分割视频</button>
                    <button class="startAnalysis" v-show="styleControl.videoShow" @click="getAnalysis">下载场景信息</button>
                    <option value=""></option>
                </div>
            </div>

            <div class="right" v-show="styleControl.videoShow" v-bind:style="{backgroundColor:bg}">
                <el-collapse class="dataShowWindow" v-model="activeName" accordion>
                    <el-collapse-item title="场景边界信息" name="1">
                        <el-card class="sceneUI">
                            <el-table :data="sceneList" height="400" style="width: 100%">
                                <el-table-column type="index" :index="indexMethod" label="边界镜头" width=100>
                                </el-table-column>
                                <el-table-column prop="start_time" label="开始时间" width=140>
                                </el-table-column>
                                <el-table-column prop="start_frame" label="开始帧" width=140>
                                </el-table-column>
                                <el-table-column prop="end_time" label="结束时间" width=140>
                                </el-table-column>
                                <el-table-column prop="end_frame" label="结束帧" width=140>
                                </el-table-column>
                            </el-table>
                        </el-card>

                    </el-collapse-item>
                    <el-collapse-item title="子视频列表" name="2">
                        <el-card clas="subVideoUI">
                            <div class="subVideoItem" v-for="item in subList" :key="item.id">
                                <div @click="playSubVideo('' + item.subVideoUrl)">{{ item.subVideoName }}</div>
                                <button class="downLoadBtn" @click="downLoad('' + item.subVideoUrl)">下载</button>
                            </div>
                        </el-card>

                    </el-collapse-item>
                </el-collapse>
            </div>
        </div>
        <div class="footer">
            <div class="socialMedia">
                <a href="https://github.com/SherlockCorleone"><img src="../assets/github.svg" alt="github" /></a>
                <img src="../assets/email.svg" title="sherlockcorleone@qq.com" alt="email"/>
                <a href="https://space.bilibili.com/511350351?spm_id_from=333.1007.0.0"><img src="../assets/bilibili.svg" alt="bilibili" /></a>
            </div>
        </div>
    </div>
</template>

<script>
import 'mui-player/dist/mui-player.min.css'
import MuiPlayer from 'mui-player'
import axios from 'axios'
export default {
    name: 'HelloWorld',
    components: {
        MuiPlayer
    },
    data() {
        return {
            bg: "rgba(255, 255, 255, 0)",
            styleControl: {
                videoShow: false,
                scene: false,
                subVideo: false,
                titleClick1: false,

                titleClick2: false
            },
            file: {
                file: null,
                fileName: '',
                filePath: '',
                fileReady: false
            },
            api: {
                videoUpload: 'http://127.0.0.1:8080/video/upload',
                getScence: 'http://127.0.0.1:8080/sceneboundary/getboundary',
                getSubVideo: 'http://127.0.0.1:8080/subvideo/splitvideo'
            },
            testData: {

            },
            scence: {
                url: ''
            },
            mp: null,
            videoId: 0,
            modeSelected: {
                shot: 1,
                scene: 1
            },
            video: {
                videoId: 0,
                videoname: "",
                sceneBoundaryId: 0

            },
            sceneList: [],
            subList: [],
            playingVideo: '',
            sceneUrl: '',
            shotOptions: [{
                value: 1,
                label: '传统检测法'
            }, {
                value: 2,
                label: '深度学习检测法'
            }],
            sceneOptions: [{
                value: 1,
                label: '场景边界感知法'
            }, {
                value: 2,
                label: '场景一致性法'
            }]
        }
    },
    mounted() {

    },
    methods: {
        indexMethod(index) {
            return index + 1;
        },
        openFileChose: function () {
            this.$refs.input.click()
            this.bg="rgba(255, 255, 255, 0.9)"
        },
        playerInit: function () {
            var _this = this
            let file = this.file.file
            let url = URL.createObjectURL(file)
            this.playingVideo = this.file.fileName
            var mp = new MuiPlayer({
                container: '#mui-player',
                title: this.file.fileName,
                src: url,
                height: 480,
                width: 720,
                objectFit: 'contain',
                autoFit: false
            })
            this.mp = mp
            mp.on('back', function (event) {
                _this.styleControl.videoShow = false
                _this.file = {
                    file: null,
                    fileName: '',
                    filePath: '',
                    fileReady: false
                }
                _this.sceneList = []
                _this.subList = []
            })
        },
        upload: function (e) {
            if (e.target.files[0].name.indexOf('%') >= 0) {
                alert('文件名中含有空格，请确保文件名规范')
            } else {
                this.file.fileName = e.target.files[0].name
                this.file.filePath = e.target.value
                this.file.fileReady = true
                this.file.file = e.target.files[0]
                this.styleControl.videoShow = true
                this.playerInit()

            }
        },
        startAnalysis: function () {
            let file = this.file.file
            let url = URL.createObjectURL(file)
            console.log(url)
            const formData = new FormData()
            formData.append('video', file,)
            formData.append('filename', this.file.fileName)
            axios.post(this.api.videoUpload, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                },
                onUploadProgress: function (processEvent) {
                    var percentCompleted = Math.round((processEvent.loaded * 100) / processEvent.total)
                    console.log(percentCompleted)
                }
            })
                .then((res) => {
                    this.$message({
                        message: '视频上传成功，开始分割视频场景！',
                        type: 'success'
                    })
                    this.video.videoId = res.data.video.videoId
                    this.video.videoName = res.data.video.videoName
                    this.getScence().then(responce => {
                        this.$message({
                            message: '视频场景边界获取成功！',
                            type: 'success'
                        })
                        this.sceneUrl = responce.data.sceneBoundary.sceneBoundaryUrl.split(':')[1]
                        responce.data.data.forEach(item => {
                            if (item['bound_label'] == 1) this.sceneList.push(item)
                        })
                        this.video.sceneBoundaryId = responce.data.sceneBoundary.sceneBoundaryId
                        // this.scence.url=responce.data.sceneBoundary.sceneBoundaryUrl
                    })
                })

        },
        getScence: function () {
            var _this = this
            var url = this.api.getScence + '?' + 'extraShotType=' + this.modeSelected.shot + '&' + 'extraSceneType=' + this
                .modeSelected.scene + '&' + 'videoId=' + this.video.videoId
            return new Promise((resolve, reject) => {
                axios.get(url)
                    .then(responce => {
                        if (responce.data['code'] != 200) {
                            reject(new Error('Not Ready'))
                            setTimeout(_this.getScence, 2000)
                        }
                        return responce;
                    })
                    .then(data => {
                        resolve(data)
                    })
                    .catch(error => {
                        console.error((error))
                        this.$message.error("视频场景分割失败！\n失败原因：" + responce.data['msg']);
                        setTimeout(_this.getScence, 2000)
                    })
            })
        },
        getSubVideo: function () {
            this.subVideo().then(res => {
                this.$message({
                    message: '视频分割成功！',
                    type: 'success'
                })

                res.data.subVideoList.forEach(item => {
                    item.subVideoUrl = 'http://localhost:8080' + item.subVideoUrl
                    this.subList.push(item)
                })
            })
        },
        subVideo: function () {
            var _this = this
            var url = this.api.getSubVideo + '?' + 'videoId=' + this.video.videoId + '&' + 'sceneBoundaryId=' +
                this.video.sceneBoundaryId
            return new Promise((resolve, reject) => {
                axios.get(url)
                    .then(responce => {
                        if (responce.data['code'] != 200) {
                            reject(new Error('Not Ready'))
                            setTimeout(_this.getScence, 2000)
                        }
                        return responce;
                    })
                    .then(data => {
                        resolve(data)
                    })
                    .catch(error => {
                        console.error((error))
                        this.$message.error("视频分割失败！\n失败原因：" + responce.data['msg']);
                        setTimeout(_this.getScence, 2000)
                    })
            })
        },
        playSubVideo: function (ev) {
            const filename = ev.split('/')
            this.playingVideo = filename[filename.length - 1]
            this.mp.reloadUrl(ev)
            this.mp.on('back', function (event) {
                this.mp.reloadUrl(this.file.filePath)
                // this.playingVideo=this.file.fileName
            })
        },
        downLoad: function (url) {
            const length = url.split("/").length
            this.downloadFile(url, url.split(".")[0].split("/")[length - 1])
        },
        titleCilck: function (num) {
            if (num == 1) {
                this.styleControl.scene = !this.styleControl.scene
                this.styleControl.titleClick1 = !this.styleControl.titleClick1
            } else {

                this.styleControl.subVideo = !this.styleControl.subVideo
                this.styleControl.titleClick2 = !this.styleControl.titleClick2
            }
        },
        getAnalysis: function () {
            this.downloadFile('http://localhost:8080' + this.sceneUrl, this.video.videoName.split(".")[0] + '.json')
        },
        downloadFile: function (url, fileName) {
            // 创建 XMLHttpRequest 对象
            const xhr = new XMLHttpRequest();
            // 设置 responseType 为 "blob"，表示返回的是二进制数据
            xhr.responseType = 'blob';
            xhr.onreadystatechange = function () {
                // 当请求完成时执行
                if (xhr.readyState === xhr.DONE) {
                    if (xhr.status === 200 || xhr.status === 201) {
                        // 创建一个 a 标签
                        const a = document.createElement('a');
                        // 获取下载链接
                        const url = window.URL.createObjectURL(xhr.response);
                        // 设置 a 标签的 href 属性为下载链接
                        a.href = url;
                        // 设置 a 标签的 download 属性为文件名称
                        a.download = fileName;
                        // 模拟点击 a 标签进行下载
                        a.click();
                        // 释放 URL 对象
                        window.URL.revokeObjectURL(url);
                    } else {
                        this.$message.error("下载失败！");
                    }
                }
            };
            // 发送 GET 请求
            xhr.open('GET', url);
            xhr.send();
            this.$message({
                message: '下载成功！',
                type: 'success'
            });

        }

    }

}
</script>

<style>
html,
body {
    width: 100vw;
    height: 100vh;
    margin: 0;
    padding: 0;

}

.footer {
    padding: 24px 10vw;
    display: flex;
    flex-direction: row;

}

.socialMedia {
    width: auto;
}

.socialMedia>img {
    margin-left: 2rem;
    margin-right: 2rem;
}
.socialMedia>a {
    margin-left: 2rem;
    margin-right: 2rem;
}

.header {
    width: 100vw;
    margin-bottom: 15px;
    display: grid;
    grid-template-columns: max-content 1fr;
    align-items: center;
}

.header img {
    margin-right: 50rem;
}

nav {
    display: flex;
    gap: 88px;
    align-items: center;
    justify-content: flex-end;
    font-size: 18px;
}

nav a {
    text-decoration: none;
    color: #000000;
}

.btn {
    width: 120px;
    height: 48px;
    background: #ffffff;
    border: 2px solid #261c35;
    border-radius: 0;
    box-shadow: -4px 6px #fcb671;
    font-weight: 500;
    font-size: 18px;
}

.container {
    display: flex;
    flex-direction: column;
    width: 100vw;
    height: 100vh;
    background-image: url('../assets/main.svg');
    background-position: center;
    background-size: cover;
    overflow-y: hidden;
}

.header {
    height: 5vh;
    width: 100vw;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-self: center;
}

.body {
    height: 88vh;
    width: 100vw;
    display: flex;
    flex-direction: row;
    display: flex;
    flex-direction: row;
}

.left {
    flex: 3;
    height: 80vh;
    margin-top: -1vh;
    /* background-color: rgba(255, 255, 255, 0.9); */
}

.right {
    flex: 2;
    height: 80vh;
    overflow-y: auto;
    margin-top: -1vh;
    display: flex;
    flex-direction: column;
    /* background-color: rgba(255, 255, 255, 0.9); */
}

.initContainer {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-left: -300px;
    margin-right: 600px;
}

.headline {
    color: #000;
    font-size: 64px;
    text-shadow: -6px 6px #fcb671;
}

.description {
    color: #000;
    font-weight: 450;
    width: 500px;
    text-align: justify;
    margin-bottom: 2rem;
}

.videoContainer {
    width: 100%;
    height: 80%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.videoContainer>.title {
    margin-left: 0;
    width: auto;
}

.uploadFile {
    width: 6rem;
    height: 3rem;
    box-shadow: -0.35rem 0.35rem;
    border: 1px solid black;
    border-radius: 0.5rem;
    background-color: #fcb671;

}

.uploadFile:hover {
    background-color: #9efffc;
}

#mui-player {
    width: 100%;
    height: 100%;
}

.input {
    display: none;
}

.functionContainer {
    width: 100%;
    height: 20%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.functionContainer>button {
    margin-left: 2rem;
    margin-right: 2rem;
}

.startAnalysis {
    width: 6rem;
    height: 3rem;
    border: 1px solid black;
    box-shadow: -0.35rem 0.35rem;
    border-radius: 0.5rem;
    background-color: #fcb671;
}

.startAnalysis:hover {
    background-color: #9efffc;
}

.title {
    font-size: 1.3rem;
    display: flex;
    flex-direction: row;
    width: 90px;

}

.sceneContainer {
    width: 95%;
    height: auto;
    margin-top: 1rem;
    margin-left: 1rem;


}

.subVideoContainer {
    margin-left: 1rem;
    width: 95%;
    height: auto;
    display: flex;
    flex-direction: column;
}

::-webkit-scrollbar {
    width: 0rem;
}

.subVideoItem {
    width: auto;
    height: 3rem;
    line-height: 5rem;
    margin-left: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid gray;
}

.subVideoItem>p {
    font-weight: 550;
    font-size: 1.3rem;
    margin-left: 0rem;
}

.downLoadBtn {
    height: 2rem;
    width: 3rem;
    border: 1px solid black;
    border-radius: 0.5rem;
    background-color: rgba(255, 255, 255, 0.9);
    margin-right: 6rem;
}



.sceneItem {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    width: auto;
    height: 5rem;
    margin-bottom: 1rem;
    border-top: 1px solid black;
}

.titleBox {
    height: 2rem;
    font-weight: 800;
    display: flex;
    width: auto;
    margin-left: 2rem;
}

.titleBox::before {
    content: '〉';
    transform: translateX(-1rem);

}

.titleBoxClick {
    height: 2rem;
    font-weight: 800;
    display: flex;
    width: auto;
    margin-left: 0;
    margin-left: 2rem;
}

.titleBoxClick::before {
    content: '〉';
    transform: translateX(-1rem) rotate(90deg);
}

.dataShowWindow {
    margin-right: 100px;
    margin-top: 80px;
    font-size: 18px;
}

.modeTag {
    width: 96px;
    margin-right: 6px;
    margin-left: 50px;
    padding: 0 10px;
}

.modeSelect {
    margin-top: 20px
}

.functionContainer {
    margin-top: -30px;
}
</style>
