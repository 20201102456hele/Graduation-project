import request from "@/utils/system/request";

export function timestampApi(params: string) {
    return request({
        url: `/timestamp?timestamp=${params}`,
        method: 'get'
    })
}


export function timestampDateApi(params: string) {
    return request({
        url: `/timestamp/date?timestamp=${params}`,
        method: 'get'
    })
}


export function dateComputeApi(one: string, two: string) {
    return request({
        url: `/date/compute?one=${one}&two=${two}`,
        method: 'get'
    })
}



export function unicodeRightApi(keyword: string) {
    return request({
        url: `/unicode/right?keyword=${keyword}`,
        method: 'get'
    })
}


export function unicodeLeftApi(keyword: string) {
    return request({
        url: `/unicode/left?keyword=${keyword}`,
        method: 'get'
    })
}

// json解析
export function jsonAnalysisApi(data: object) {
    return request({
        url: `/json/analysis`,
        method: 'post',
        data
    })
}




// jsonPath在线测试
export function jsonPathApi(data: Object) {
    return request({
        url: `/json/path`,
        method: 'post',
        data
    })
}

// 正则表达式在线测试
export function reTestApi(data: Object) {
    return request({
        url: `/re/test`,
        method: 'post',
        data
    })
}

// 二维码生成
export function orCodeApi(url: String) {
    return request({
        url: `/or/code?url=${url}`,
        method: 'get',
    })
}



// md5加密
export function md5Api(data: String) {
    return request({
        url: `/md5?data=${data}`,
        method: 'get',
    })
}


// http接口测试
export function httpApi(data: Object) {
    return request({
        url: `/http/test`,
        method: 'post',
        data
    })
}






// 收藏
export function collectApi(userId: string, toolId: string) {
    return request({
        url: `/collect?userId=${userId}&toolId=${toolId}`,
        method: 'get'
    })
}


export function unCollectApi(userId: string, toolId: string) {
    return request({
        url: `/unCollect?userId=${userId}&toolId=${toolId}`,
        method: 'get'
    })
}




export function getToolApi(userId: string) {
    return request({
        url: `/get/tool?userId=${userId}`,
        method: 'get'
    })
}



