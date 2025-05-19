import instance from "@/utils/http.js";


export function RegisterRequest({
                                    username,
                                    password,
                                    confirm_password,
                                    name,
                                    phone,
                                    sex
                                }) {
    return instance({
        url: 'register/',
        method: "POST",
        data: {
            username,
            password,
            confirm_password,
            name,
            phone,
            sex,
        }
    })
}