import './assets/main.css'

import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import 'element-plus/dist/index.css';
import locale from 'element-plus/es/locale/lang/zh-cn'
import ElementPlus from 'element-plus'

const app = createApp(App)

app.use(router)
app.use(ElementPlus, {locale})

app.mount('#app')
