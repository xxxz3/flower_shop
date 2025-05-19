<template>
    <div class="common-layout">
        <el-container>

            <!-- 左侧菜单栏-->
            <el-aside width="200px">

                <el-col :span="100" style="height: 100vh;">
                    <h5 class="mb-3" style="margin:20px 60px;">网上花店系统</h5>
                    <el-menu
                            :default-active="index"
                            class="el-menu-vertical-demo"
                            background-color="#ffb0b0"
                    >
                        <el-menu-item index="1">
                            <el-icon>
                                <HomeFilled/>
                            </el-icon>
                            <span @click="goHome">首页</span>
                        </el-menu-item>

                        <el-menu-item index="2" v-if="role == 2">
                            <el-icon>
                                <user-filled/>
                            </el-icon>
                            <span @click="goUser">用户管理</span>
                        </el-menu-item>

                        <el-menu-item index="3">
                            <el-icon>
                                <Collection/>
                            </el-icon>
                            <span @click="goFlower">鲜花管理</span>
                        </el-menu-item>


                        <el-menu-item index="4" v-if="role == 2">
                            <el-icon>
                                <Reading/>
                            </el-icon>
                            <span @click="goAnnouncement">公告管理</span>
                        </el-menu-item>

                        <el-menu-item index="5" v-if="role == 2">
                            <el-icon>
                                <Picture/>
                            </el-icon>
                            <span @click="goBanner">轮播图管理</span>
                        </el-menu-item>


                        <el-menu-item index="6">
                            <el-icon>
                                <Reading/>
                            </el-icon>
                            <span @click="goOrder">订单管理管理</span>
                        </el-menu-item>

                    </el-menu>
                </el-col>
            </el-aside>

            <el-container>
                <!-- 头部导航条-->
                <el-header>
                    <el-menu
                            :default-active="activeIndex"
                            class="el-menu-demo"
                            mode="horizontal"
                            :ellipsis="false"
                            background-color="#ffb0b0"
                    >

                        <div class="flex-grow"/>
                        <el-sub-menu index="2">
                            <template #title>{{ username }}</template>
                            <el-menu-item index="2-2" @click="logout">退出登录</el-menu-item>
                        </el-sub-menu>
                    </el-menu>
                </el-header>

                <!-- 内容区域-->
                <el-main>
                    <RouterView></RouterView>
                </el-main>




            </el-container>
        </el-container>
    </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import {useRouter} from "vue-router";
import useRole from "@/hooks/useRole.js";
import {
    HomeFilled,
    UserFilled,
    Collection,
    Reading, Picture
} from '@element-plus/icons-vue'


const router = useRouter()  // 实例化useRouter对象
const activeIndex = ref('2-2')  // 导航条菜单默认激活
const username = localStorage.getItem('username')  // 获取当前登录人的用户名
const index = ref('1')  // 左侧栏默认激活
const {role} = useRole()

// 退出登录
function logout() {
    localStorage.clear()
    router.push({path: '/login'})

}

// 页面刷新跳转回首页
onMounted(() => {
    router.push({path: "/home"})
})


// 跳转到首页
function goHome() {
    router.push({path: '/home'})
}


// 跳转到用户管理页面
function goUser() {
    router.push({path: '/user'})
}

// 跳转到鲜花管理页面
function goFlower() {
    router.push({path: '/flower'})
}


// 跳转到订单管理页面
function goOrder() {
    router.push({path: '/order'})
}

// 跳转到公告页面
function goAnnouncement() {
    router.push({path: '/announcement'})
}

// 跳转到轮播图
function goBanner() {
    router.push({path: '/banner'})
}


</script>

<style scoped>
.flex-grow {
    flex-grow: 1;
}

.el-menu {
    background-color: var(--el-menu-bg-color);
    border-right: 1px solid #dcdfe6;
    height: 87%;
    box-sizing: border-box;
    list-style: none;
    margin: 0;
    padding-left: 0;
    position: relative;
}

.footer {
    text-align: center;
    border-top: 1px solid #dcdfe6;
    height: 30px;
    line-height: 30px;
}


</style>