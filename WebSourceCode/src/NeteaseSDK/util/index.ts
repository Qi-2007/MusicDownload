export const SDKUtils = {
  toBoolean(val:any) {
    if (typeof val === 'boolean') return val
    if (val === '') return val
    return val === 'true' || val == '1'
  },
  cookieToJson(cookie:string) {
    if (!cookie) return {}
    let cookieArr = cookie.split(';')
    let obj = {} as any
    cookieArr.forEach((i) => {
      let arr = i.split('=')
      obj[arr[0]] = arr[1]
    })
    return obj
  },
  getRandom(num:number) {
    var random = Math.floor(
      (Math.random() + Math.floor(Math.random() * 9 + 1)) *
        Math.pow(10, num - 1),
    )
    return random
  },
}