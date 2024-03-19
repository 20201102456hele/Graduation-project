/**
 * 前端路由管理
 **/

/** 路由类型 */
import type { Route } from '../index.type'

/** 引入需要权限的Modules */
import Dashboard from '../modules/dashboard'
import SystemManage from '../modules/systemManage'
import pages from "@/router/modules/pages";

/** 登录后需要动态加入的本地路由 */
const FrontRoutes: Route[] = [
    ...Dashboard,
    ...SystemManage,
    ...pages,


]

export default FrontRoutes
