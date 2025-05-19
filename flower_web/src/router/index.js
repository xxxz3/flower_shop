import {createRouter, createWebHistory} from 'vue-router'
import Login from "@/views/account/Login.vue";
import Layout from "@/views/Layout.vue";
import Home from "@/views/home/Home.vue";
import User from '@/views/user/User.vue'
import Announcement from "@/views/announcement/Announcement.vue";
import Banner from "@/views/banner/Banner.vue";
import Order from "@/views/order/Order.vue";
import Flower from "@/views/flower/Flower.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '',
            name: 'layout',
            component: Layout,
            children:[
                {
                    path: '/home',
                    name: 'home',
                    component: Home
                },
                {
                    path: '/user',
                    name: 'user',
                    component: User
                },
                {
                    path: '/announcement',
                    name: 'announcement',
                    component: Announcement
                },
                {
                    path: '/banner',
                    name: 'banner',
                    component: Banner
                },
                {
                    path: '/order',
                    name: 'order',
                    component: Order
                },
                {
                    path: '/flower',
                    name: 'flower',
                    component: Flower
                },
            ]
        },

    ]
})



// 登录拦截（全局）
router.beforeEach((to, from, next) => {
    // 如果登录继续访问
    if (localStorage.getItem('token')) {
        next();
        return;
    }

    // 未登录，访问登录页面
    if (to.name === 'login') {
        next();
        return;
    }

    // 未登录，跳转登录页面
    next({name: 'login'})
})


export default router
