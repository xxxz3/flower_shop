<template>
    <div>
        <el-carousel :interval="2000" type="card" height="300px">
            <el-carousel-item v-for="item in bannerList" :key="item.id">
                <el-image :src="item.image" style="width: 100%;height: 300px"></el-image>
            </el-carousel-item>
        </el-carousel>
    </div>

    <div class="box_content">
        <div class="content" v-for="item in announcementList" :key="item.id">
            <span class="title">
                最新公告: &nbsp;&nbsp;{{ item.title }}
            </span>

            <span>
                {{ item.content }}
            </span>
        </div>


    </div>
</template>

<script setup>
import {ref, onMounted} from "vue";
import {getBannerRequest} from "@/apis/banner.js";
import {getAnnouncementRequest} from "@/apis/announcement.js";


const bannerList = ref('')  // 轮播图列表
const announcementList = ref('')

// 发送请求获取轮播图列表
async function getBannerList() {
    const res = await getBannerRequest()
    bannerList.value = res
    console.log(res)
}
onMounted(() => getBannerList())


// 发送请求获取公告列表
async function getAnnouncementList() {
    const res = await getAnnouncementRequest()
    announcementList.value = res
}
onMounted(() => getAnnouncementList())


</script>

<style scoped>
.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}

.box_content {
    margin-top: 40px;
    background-color: #e2e2e2;
    height: 200px;
    border-radius: 5px;
}


.content {
    display: flex;
    flex-direction: column;
    padding: 20px;
}

.title {
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 10px;
}
</style>