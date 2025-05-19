import instance from "@/utils/http.js";


// ######################## 轮播图 #################################
export function getBannerRequest() {
    return instance({
        url: 'banner/',
    })
}


// 新增
export function addBannerRequest({image}) {
    return instance({
        url: 'banner/',
        method: 'POST',
        data: {
            image,
        }
    })
}


// 删除
export function deleteBannerRequest(id) {
    return instance({
        url: 'banner/' + id + '/',
        method: 'delete',

    })
}

