import instance from "@/utils/http.js";


// ######################## 公告 #################################
export function getAnnouncementRequest(title) {
    return instance({
        url: 'announcement/',
        params: {
            title
        }
    })
}


// 新增
export function addAnnouncementRequest({
                                           title,
                                           content,

                                       }) {
    return instance({
        url: 'announcement/',
        method: 'POST',
        data: {
            title,
            content,

        }
    })
}


// 删除
export function deleteAnnouncementRequest(id) {
    return instance({
        url: 'announcement/' + id + '/',
        method: 'delete',

    })
}

