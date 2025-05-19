import axios from 'axios'

// 创建axios实例
const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/',
    timeout: 5000
})

// axios请求拦截器
instance.interceptors.request.use(config => {
    config.headers.Authorization = localStorage.getItem('token')
    return config
}, e => Promise.reject(e))

// axios响应式拦截器
instance.interceptors.response.use(res => res.data, e => {
    return Promise.reject(e)
})


export default instance