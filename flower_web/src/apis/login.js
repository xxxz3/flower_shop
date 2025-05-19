import instance from "@/utils/http.js";


export function LoginRequest({username,password}){
    return instance({
        url:'login/',
        method:"POST",
        data:{
            username,
            password
        }
    })
}