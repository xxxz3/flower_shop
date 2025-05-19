import instance from "@/utils/http.js";

// 订购鲜花
export function purchaseFlowerRequest({flower,quantity}) {
    return instance({
        url: 'order/',
        method: 'post',
        data: {
            flower,quantity
        }
    })
}


// 订单列表
export function OrderListRequest() {
    return instance({
        url: 'order/',
    })
}


// 删除订单
export function deleteOrderRequest(id) {
    return instance({
        url: 'order/' + id + '/',
        method:'delete'
    })
}


