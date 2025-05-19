import instance from "@/utils/http.js";


// 搜索鲜花
export function FlowerRequest(name) {
    return instance({
        url: 'flower/',
        params: {
            name
        }
    })
}

// 删除鲜花
export function DelFlowerRequest(id) {
    return instance({
        url: 'flower/' + id + '/',
        method: 'delete'
    })
}

// 新增鲜花
export function addFlowerRequest({name, price, image, flower_language,stock}) {
    return instance({
        url: 'flower/',
        method: 'post',
        data: {
            name, price, image, flower_language,stock
        }
    })
}