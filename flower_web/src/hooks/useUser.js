import {reactive} from "vue";

// 需要将定义的函数暴露给外界
export default function () {
    // 数据
    // 注册表单校验
    // 管理员
    let registerForm = reactive({
        password: [
            {required: true, message: '密码不能为空', trigger: 'blur'},
        ],
        name: [
            {required: true, message: '姓名不能为空', trigger: 'blur'},
        ],
        phone: [
            {required: true, message: '手机号不能为空', trigger: 'blur'},
        ],
        username: [
            {required: true, message: '用户名不能为空', trigger: 'blur'},
        ],
        confirm_password: [
            {required: true, message: '确认密码不能为空', trigger: 'blur'},
        ]

    })




    // 用户
    const rules = reactive({
        username: [
            {required: true, message: '用户名不能为空', trigger: 'blur'},
        ],
        password: [
            {required: true, message: '密码不能为空', trigger: 'blur'},
            {min: 6, max: 18, message: '密码长度为6 ~ 18位', trigger: 'blur'},
        ],
    })
// 方法


    // 向外部提供所需要的东西
    return {registerForm,rules}
}