// 需要将定义的函数暴露给外界
export default function () {
    let role = localStorage.getItem('role')


    // 向外部提供所需要的东西
    return {role}
}