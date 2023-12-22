import {GenerateApi} from "@/NeteaseSDK/util/request";

export const LoginGetQRKey = async (query: { cookie: any }) => {
    const data = {
        type: 1,
    }
    return GenerateApi(
        `https://music.163.com/weapi/login/qrcode/unikey`,
        1,
        data,
        {
            crypto: 'weapi',
            cookie: query.cookie,
        },
    )
}
