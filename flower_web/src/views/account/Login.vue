<template>
    <div class="container">
        <!-- 登录表单-->
        <div class="login-box">
            <h2>网上花店系统</h2>
            <el-form
                    style="max-width: 600px"
                    :model="ruleForm"
                    :rules="rules"
                    label-width="auto"
                    class="demo-ruleForm"
                    status-icon
            >
                <el-form-item prop="username">
                    <el-input v-model="ruleForm.username" type="text" placeholder="用户名">
                        <template #prefix>
                            <el-icon class="el-input__icon">
                                <User/>
                            </el-icon>
                        </template>
                    </el-input>
                </el-form-item>

                <el-form-item prop="password">
                    <el-input v-model="ruleForm.password" type="password" placeholder="密码" show-password>
                        <template #prefix>
                            <el-icon class="el-input__icon">
                                <Lock/>
                            </el-icon>
                        </template>
                    </el-input>
                </el-form-item>

                <el-form-item>
                    <el-button class="login-btn" type="success" @click="onSubmit">登 录</el-button>

                    <span style="margin-left: 167px; margin-top: 10px; color: #AAAAAA">没有账号，
                        <el-button type="text" @click="dialogFormVisible = true">立即注册</el-button>
                    </span>
                </el-form-item>
            </el-form>
        </div>

        <!-- 对话框-->
        <el-dialog v-model="dialogFormVisible" title="新用户注册" width="500" :close-on-click-modal="false">
            <el-form :model="form" :rules="registerForm" label-width="auto">

                <el-form-item label="用户名" prop="username">
                    <el-input v-model="form.username" autocomplete="off" clearable/>
                </el-form-item>


                <el-form-item label="密码" prop="password">
                    <el-input v-model="form.password" autocomplete="off" type="password" clearable show-password/>
                </el-form-item>

                <el-form-item label="确认密码" prop="password">
                    <el-input v-model="form.confirm_password" autocomplete="off" type="password" clearable show-password/>
                </el-form-item>

                <el-form-item label="姓名" prop="name">
                    <el-input v-model="form.name" autocomplete="off" clearable/>
                </el-form-item>

                <el-form-item label="手机号" prop="phone">
                    <el-input v-model="form.phone" autocomplete="off" clearable/>
                </el-form-item>

                <el-form-item label="性别">
                    <el-radio-group v-model="form.sex" class="ml-4">
                        <el-radio value="1">男</el-radio>
                        <el-radio value="0">女</el-radio>
                    </el-radio-group>
                </el-form-item>


            </el-form>
            <template #footer>
                <div class="dialog-footer">
                    <el-button @click="dialogFormVisible = false">取 消</el-button>
                    <el-button type="primary" @click="onRegister">
                        注 册
                    </el-button>
                </div>
            </template>
        </el-dialog>

    </div>

</template>

<script setup>

import {reactive, ref} from 'vue'
import {LoginRequest} from "@/apis/login.js";
import {RegisterRequest} from "@/apis/register.js";
import {ElMessage} from "element-plus";
import {useRouter} from "vue-router";
import {Lock, User} from '@element-plus/icons-vue'
import useUser from "@/hooks/useUser.js";


// hooks中的数据
const {registerForm,rules} = useUser()

// 实例化useRouter对象
const router = useRouter()

// 对话框是否显示
const dialogFormVisible = ref(false)

// 对话框数据
const form = reactive({
    password: '',
    name: '',
    phone: '',
    username: '',
    sex: "1",
    confirm_password:''
})


// 定义表单登录数据
const ruleForm = reactive({
    username: '',
    password: ''
})

// 点击登录按钮发送请求
async function onSubmit() {
    const res = await LoginRequest({username: ruleForm.username, password: ruleForm.password})
    console.log(res)
    if (res.code === 1001) {
        ElMessage({
            message: "用户名或密码错误",
            type: 'error'
        })
    } else {
        ElMessage({
            message: '登录成功',
            type: 'success'
        })
        // 登录成功保存token
        localStorage.setItem('token', res.token)
        localStorage.setItem('username', res.username)
        localStorage.setItem('role', res.role)
        // localStorage.setItem('user_id', res.data.user_id)
        // 登录成功跳转到管理员首页
        router.replace({path: '/home'})

    }

}


// 用户注册
async function onRegister() {
    try {
        const res = await RegisterRequest({
            username: form.username,
            password: form.password,
            name: form.name,
            phone: form.phone,
            sex: form.sex,
            confirm_password:form.confirm_password,
        })
        ElMessage({
            type:'success',
            message:'注册完成，请登录'
        })
        dialogFormVisible.value = false

    }catch (e) {
        if (e.response.data.name){
            ElMessage({
                type:'error',
                message:'姓名已存在'
            })
        }

        if (e.response.data.confirm_password){
            ElMessage({
                type:'error',
                message:'两次密码不一致'
            })
        }


        if (e.response.data.phone){
            ElMessage({
                type:'error',
                message:'手机号已存在'
            })
        }


        if (e.response.data.username){
            ElMessage({
                type:'error',
                message:'用户名已存在'
            })
        }

    }
}



</script>


<style scoped>


.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;

    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-image: url('@/assets/flower.png');
    background-size: cover;
    background-position: center;

}

.login-box {
    background-color: rgba(255, 255, 255, 0.1); /* 透明度为0.7的白色背景 */
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
    width: 300px;
}

.login-box h2 {
    text-align: center;
    margin-bottom: 20px;
}

.login-box input[type="text"],
.login-box input[type="password"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 15px;
    box-sizing: border-box;
}

.login-box input[type="submit"] {
    width: 100%;
    background-color: #4caf50;
    color: #fff;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

.login-box input[type="submit"]:hover {
    background-color: #45a049;

}

.login-btn {
    width: 100%;
}
</style>