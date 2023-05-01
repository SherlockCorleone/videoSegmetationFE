<template>
    <div class="container">
        <header>
            <img src="../assets/images/SplitVertical32Filled.svg" alt="" />
            <nav>
                <a >首页</a>
                <a>视频场景分割</a>
                <button class="btn">登录</button>
            </nav>
        </header>
        <main>
            <div class="mainLeft">
                <h1 class="headline">视频分割系统</h1>
                <p class="description">
                    现今的信息技术水平极速发展，极大的影响了人们生活的方方面面，手机似乎已经成为了人们的“伴侣”，我们用手机查看地图出行，提醒日常任务，与世界各地的人联络...
                </p>
                <button class="btn">注册</button>
            </div>
            <div class="mainRight">
                <img src="../assets/images/main.svg" alt="" />
            </div>
        </main>
        <footer>
            <div class="socialMedia">
               <a href="https://github.com/SherlockCorleone"><img src="../assets/images/github.svg" alt="github" /></a> 
                <img src="../assets/images/email.svg" alt="email" />
                <img src="../assets/images/bilibili.svg" alt="bilibili" />
            </div>
        </footer>
    </div>
</template>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: Helvetica, "PingFang SC", sans-serif;
}

.container {
    width: 100vw;
    max-width: 100%;
    height: 100vh;
    display: grid;
    grid-template-rows: 120px 1fr 120px;
}

header,
main,
footer {
    padding: 24px 10vw;
}

header {
    display: grid;
    grid-template-columns: max-content 1fr;
    align-items: center;
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

.mainLeft {
    font-family: Helvetica, "PingFang SC", sans-serif;
    
    display: grid;
    width: 36%;
    height: 100%;
    align-content: center;
    row-gap: 36px;
    transform: translateY(-10%);
}

.mainLeft h1 {
    color: #000;
    font-size: 64px;
    text-shadow: -6px 6px #fcb671;
}

.mainLeft p {
    color: #000;
    font-weight: 300;
    text-align: justify;
}

.mainLeft button {
    background: #fcb671;
    box-shadow: -4px 6px #000000;
}

.mainRight {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}

.mainRight img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: bottom;
}

footer {
    padding-top: 32px;
}

.socialMedia {
    display: flex;
    align-items: center;
    gap: 64px;
}
</style>