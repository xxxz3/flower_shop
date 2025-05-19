import instance from "@/utils/http.js";


// ######################## 用户 #################################
// 获取用户列表
export function getUserRequest() {
    return instance({
        url: 'user/',
    })
}


export function getUserNameRequest(name) {
    return instance({
        url: 'user/',
        params:{
            name
        }
    })
}





// 删除
export function deleteUserRequest(id) {
    return instance({
        url: 'user/' + id + '/',
        method: 'delete',

    })
}